---
name: autonomous-coding
description: Use this skill when the user wants to scaffold, run, or customize Anthropic's autonomous-coding quickstart. It provides a deterministic bootstrap script plus a workflow for setup, execution, security tuning, and resume cycles.
---

# Autonomous Coding

## Overview

Use this skill when requests mention Anthropic `claude-quickstarts/autonomous-coding`, long-running autonomous coding loops, or two-agent initializer plus coding execution.

Primary goal: bootstrap a working local copy quickly, then help iterate safely.

## Quick Start Workflow

1. Bootstrap project from bundled upstream files:
   `bash scripts/bootstrap.sh --target <project-dir>`
2. Create and activate Python environment in the target directory.
3. Install dependencies from `requirements.txt`.
4. Export `ANTHROPIC_API_KEY`.
5. Run:
   `python autonomous_agent_demo.py --project-dir ./my_project`

## Implementation Rules

- Keep upstream source of truth in `assets/upstream/`.
- If user asks for feature or policy changes, edit copied project files in the target directory, not `assets/upstream/`.
- For faster demos, reduce feature count in `prompts/initializer_prompt.md` after bootstrap.
- If commands are blocked, adjust allowlist in `security.py` with minimum necessary changes.
- Preserve resume behavior: stop with `Ctrl+C` and rerun the same command to continue.

## Troubleshooting Checklist

- Missing API key: verify `ANTHROPIC_API_KEY` is set in current shell.
- Slow first run: initializer may take several minutes while generating `feature_list.json`.
- Security blocks: inspect command, then extend `ALLOWED_COMMANDS` conservatively.
- No progress: check project files (`feature_list.json`, git history, progress logs) in the target project directory.

## Resources

- Upstream template source: `assets/upstream/`
- Bootstrap helper: `scripts/bootstrap.sh`
- Upstream notes: `references/upstream-notes.md`
