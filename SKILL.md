---
name: autonomous-coding
description: Use this skill when the user wants to scaffold, run, or customize an autonomous coding quickstart in Codex CLI. It provides a deterministic bootstrap script and a Codex-compatible session loop runner.
---

# Autonomous Coding

## Overview

Use this skill when requests mention autonomous long-running coding loops, initializer plus coding-agent iterations, or porting Anthropic quickstart patterns to Codex CLI.

Primary goal: bootstrap a working local copy quickly, then help iterate safely.

## Quick Start Workflow

1. Bootstrap project from bundled upstream files:
   `bash scripts/bootstrap.sh --target <project-dir>`
2. Run Codex-compatible loop:
   `python codex_autonomous_demo.py --project-dir ./my_project --max-iterations 1`
3. Remove `--max-iterations` to continue autonomous iterations.

## Implementation Rules

- Keep upstream source of truth in `assets/upstream/`.
- If user asks for feature or policy changes, edit copied project files in the target directory, not `assets/upstream/`.
- For faster demos, reduce feature count in `prompts/initializer_prompt.md` after bootstrap.
- If commands are blocked, adjust allowlist in `security.py` with minimum necessary changes.
- Preserve resume behavior: stop with `Ctrl+C` and rerun the same command to continue.
- Prefer `codex_autonomous_demo.py` over `autonomous_agent_demo.py` for Codex environments.

## Troubleshooting Checklist

- Missing Codex CLI: verify `codex --help` works.
- Slow first run: initializer may take several minutes while generating `feature_list.json`.
- Security blocks: inspect command, then extend `ALLOWED_COMMANDS` conservatively.
- No progress: check project files (`feature_list.json`, git history, progress logs) in the target project directory.

## Resources

- Upstream template source: `assets/upstream/`
- Bootstrap helper: `scripts/bootstrap.sh`
- Upstream notes: `references/upstream-notes.md`
