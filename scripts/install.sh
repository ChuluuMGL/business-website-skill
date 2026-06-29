#!/usr/bin/env bash
set -euo pipefail

SKILL_NAME="business-website-skill"
REPO_URL="${BUSINESS_WEBSITE_SKILL_REPO:-https://github.com/ChuluuMGL/business-website-skill.git}"

usage() {
  cat <<'EOF'
Install business-website-skill into a local agent skills directory.

Usage:
  scripts/install.sh <target>
  scripts/install.sh custom <skills-root>

Targets:
  codex        ~/.codex/skills/business-website-skill
  claude       ./.claude/skills/business-website-skill
  cursor       ./.cursor/skills/business-website-skill
  trae         ./.trae/skills/business-website-skill
  antigravity  ./.agent/skills/business-website-skill
  gemini       ./.gemini/skills/business-website-skill
  kimi         ./.kimi/skills/business-website-skill
  hermes       ~/.hermes/skills/business-website-skill
  agents       ./.agents/skills/business-website-skill
  custom PATH  PATH/business-website-skill

Examples:
  scripts/install.sh codex
  scripts/install.sh claude
  scripts/install.sh custom "$HOME/.config/agents/skills"
EOF
}

target="${1:-}"
if [[ -z "$target" || "$target" == "-h" || "$target" == "--help" ]]; then
  usage
  exit 0
fi

case "$target" in
  codex) root="${CODEX_HOME:-$HOME/.codex}/skills" ;;
  claude) root="$PWD/.claude/skills" ;;
  cursor) root="$PWD/.cursor/skills" ;;
  trae) root="$PWD/.trae/skills" ;;
  antigravity) root="$PWD/.agent/skills" ;;
  gemini) root="$PWD/.gemini/skills" ;;
  kimi) root="$PWD/.kimi/skills" ;;
  hermes) root="$HOME/.hermes/skills" ;;
  agents) root="$PWD/.agents/skills" ;;
  custom)
    root="${2:-}"
    if [[ -z "$root" ]]; then
      echo "custom target requires a skills root path" >&2
      exit 2
    fi
    ;;
  *)
    echo "unknown target: $target" >&2
    usage >&2
    exit 2
    ;;
esac

dest="$root/$SKILL_NAME"
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source_root="$(cd "$script_dir/.." && pwd)"

mkdir -p "$root"

if [[ "$source_root" == "$dest" ]]; then
  echo "Already installed at $dest"
  exit 0
fi

if [[ -f "$source_root/SKILL.md" && -f "$source_root/skill.json" ]]; then
  mkdir -p "$dest"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a \
      --exclude ".git" \
      --exclude ".github" \
      --exclude ".vercel" \
      --exclude ".DS_Store" \
      --exclude "__pycache__" \
      --exclude "*.pyc" \
      --exclude "dist" \
      --exclude "public" \
      --exclude "site" \
      --exclude "package.json" \
      --exclude "vercel.json" \
      --exclude "assets/previews/*.png" \
      --exclude "assets/previews/*.jpg" \
      --exclude "assets/previews/interactions/*.gif" \
      --exclude "assets/previews/styles/*.png" \
      "$source_root/" "$dest/"
  else
    (cd "$source_root" && tar \
      --exclude ".git" \
      --exclude ".github" \
      --exclude ".vercel" \
      --exclude ".DS_Store" \
      --exclude "__pycache__" \
      --exclude "*.pyc" \
      --exclude "dist" \
      --exclude "public" \
      --exclude "site" \
      --exclude "package.json" \
      --exclude "vercel.json" \
      -cf - .) | (cd "$dest" && tar -xf -)
  fi
else
  if [[ -e "$dest" ]]; then
    echo "destination already exists: $dest" >&2
    echo "remove it first or run this script from a local checkout to update in place" >&2
    exit 1
  fi
  git clone "$REPO_URL" "$dest"
fi

echo "Installed $SKILL_NAME to $dest"
