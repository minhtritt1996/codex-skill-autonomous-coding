#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 --target <project-dir>"
}

TARGET=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      TARGET="${2:-}"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [[ -z "$TARGET" ]]; then
  echo "Error: --target is required" >&2
  usage >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
UPSTREAM_DIR="$SKILL_ROOT/assets/upstream"

if [[ ! -d "$UPSTREAM_DIR" ]]; then
  echo "Error: Upstream template not found at $UPSTREAM_DIR" >&2
  exit 1
fi

if [[ -e "$TARGET" && -n "$(ls -A "$TARGET" 2>/dev/null || true)" ]]; then
  echo "Error: target directory exists and is not empty: $TARGET" >&2
  exit 1
fi

mkdir -p "$TARGET"
cp -a "$UPSTREAM_DIR/." "$TARGET/"

echo "Bootstrapped autonomous-coding quickstart into: $TARGET"
echo "Next steps:"
echo "  cd $TARGET"
echo "  codex --help    # verify Codex CLI is available"
echo "  python codex_autonomous_demo.py --project-dir ./my_project --max-iterations 1"
echo "  # remove --max-iterations to keep auto-continuing"
