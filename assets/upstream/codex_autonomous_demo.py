#!/usr/bin/env python3
"""
Codex-compatible Autonomous Coding Runner
========================================

A lightweight port of the autonomous coding loop that runs sessions via
`codex exec` instead of Claude Agent SDK.
"""

import argparse
import shlex
import shutil
import subprocess
import time
from pathlib import Path
from typing import Optional

from progress import print_progress_summary, print_session_header
from prompts import copy_spec_to_project, get_coding_prompt, get_initializer_prompt

DEFAULT_MODEL = "gpt-5-codex"
AUTO_CONTINUE_DELAY_SECONDS = 3


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Codex-compatible autonomous coding loop",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python codex_autonomous_demo.py --project-dir ./my_project --max-iterations 1
  python codex_autonomous_demo.py --project-dir ./my_project --model gpt-5-codex
  python codex_autonomous_demo.py --project-dir ./my_project --dry-run
        """,
    )

    parser.add_argument(
        "--project-dir",
        type=Path,
        default=Path("./autonomous_demo_project"),
        help="Project directory (relative paths are created under generations/)",
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=None,
        help="Maximum session iterations (default: unlimited)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=DEFAULT_MODEL,
        help=f"Codex model to use (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned codex commands without executing them",
    )

    return parser.parse_args()


def resolve_project_dir(project_dir: Path) -> Path:
    if project_dir.is_absolute() or str(project_dir).startswith("generations/"):
        return project_dir
    return Path("generations") / project_dir


def ensure_codex_available() -> None:
    if shutil.which("codex") is None:
        raise RuntimeError(
            "codex CLI not found. Install/configure Codex CLI first, then rerun."
        )


def build_prompt(is_first_run: bool) -> str:
    base = get_initializer_prompt() if is_first_run else get_coding_prompt()
    codex_notes = """

## CODEX RUNTIME NOTES

- You are running through `codex exec` in this project directory.
- Work only with files in the current project directory.
- Before ending the session, commit coherent progress and update progress notes.
"""
    return base + "\n" + codex_notes


def run_codex_session(project_dir: Path, prompt: str, model: str, dry_run: bool) -> int:
    cmd = [
        "codex",
        "exec",
        "--skip-git-repo-check",
        "--full-auto",
        "--sandbox",
        "workspace-write",
        "--cd",
        str(project_dir.resolve()),
        "--model",
        model,
        prompt,
    ]

    print("Command:")
    print("  " + shlex.join(cmd))

    if dry_run:
        return 0

    completed = subprocess.run(cmd)
    return completed.returncode


def run_loop(project_dir: Path, model: str, max_iterations: Optional[int], dry_run: bool) -> None:
    project_dir.mkdir(parents=True, exist_ok=True)

    tests_file = project_dir / "feature_list.json"
    is_first_run = not tests_file.exists()

    if is_first_run:
        copy_spec_to_project(project_dir)

    iteration = 0
    while True:
        iteration += 1
        if max_iterations and iteration > max_iterations:
            print(f"Reached max iterations ({max_iterations}).")
            break

        print_session_header(iteration, is_first_run)
        prompt = build_prompt(is_first_run)
        is_first_run = False

        rc = run_codex_session(project_dir, prompt, model, dry_run)
        if rc != 0:
            print(f"Session failed with exit code {rc}. Retrying in {AUTO_CONTINUE_DELAY_SECONDS}s...")
            if dry_run:
                break
            time.sleep(AUTO_CONTINUE_DELAY_SECONDS)
            continue

        print_progress_summary(project_dir)
        if max_iterations and iteration >= max_iterations:
            break

        print(f"Auto-continue in {AUTO_CONTINUE_DELAY_SECONDS}s... (Ctrl+C to stop)")
        if dry_run:
            break
        time.sleep(AUTO_CONTINUE_DELAY_SECONDS)


def main() -> None:
    args = parse_args()
    project_dir = resolve_project_dir(args.project_dir)

    ensure_codex_available()

    print("=" * 70)
    print("  CODEX AUTONOMOUS CODING DEMO")
    print("=" * 70)
    print(f"Project directory: {project_dir}")
    print(f"Model: {args.model}")
    print(f"Dry run: {'yes' if args.dry_run else 'no'}")

    try:
        run_loop(
            project_dir=project_dir,
            model=args.model,
            max_iterations=args.max_iterations,
            dry_run=args.dry_run,
        )
    except KeyboardInterrupt:
        print("\nInterrupted by user. Re-run the same command to resume.")


if __name__ == "__main__":
    main()
