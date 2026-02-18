"""MkDocs hook: generate CLI reference pages for AIgiSE.

This keeps the docs site in sync with the actual CLI help text without manual
copy/paste.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


_LOG_PREFIX_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\s+\|")


def _extract_help_text(raw: str) -> str:
  """Extract the CLI help text, removing runtime log lines."""
  lines = []
  started = False
  for line in raw.splitlines():
    if not started:
      if line.startswith("Usage:"):
        started = True
      else:
        continue
    if _LOG_PREFIX_RE.match(line):
      continue
    lines.append(line.rstrip())
  return "\n".join(lines).strip() + "\n"


def _run_help(repo_root: Path, *args: str) -> str:
  """Run `opensage ... --help` via uv in the AIgiSE project."""
  cmd = [
    "uv",
    "run",
    "opensage",
    *args,
    "--help",
  ]
  proc = subprocess.run(
    cmd,
    cwd=str(repo_root / "AIgiSE"),
    text=True,
    capture_output=True,
    check=False,
  )
  # Some commands may emit logs to stdout/stderr; keep stdout as primary.
  raw = proc.stdout or ""
  return _extract_help_text(raw)


def _write_page(path: Path, title: str, help_text: str) -> None:
  path.parent.mkdir(parents=True, exist_ok=True)
  content = (
    f"# {title}\n\n"
    "```text\n"
    f"{help_text}"
    "```\n"
  )
  path.write_text(content, encoding="utf-8")


def on_startup(command: str, dirty: bool) -> None:
  del dirty  # unused

  # This file lives at: opensage_website/mkdocs_hooks/...
  opensage_website_dir = Path(__file__).resolve().parent.parent
  repo_root = opensage_website_dir.parent

  docs_dir = opensage_website_dir / "documentation_src" / "wiki"
  out_dir = docs_dir / "generated" / "cli"

  # Only generate for build/serve to avoid surprising behavior.
  if command not in {"build", "serve", "gh-deploy"}:
    return

  _write_page(out_dir / "opensage.md", "opensage", _run_help(repo_root))
  _write_page(
    out_dir / "opensage-web.md",
    "opensage web",
    _run_help(repo_root, "web"),
  )
  _write_page(
    out_dir / "opensage-dependency-check.md",
    "opensage dependency-check",
    _run_help(repo_root, "dependency-check"),
  )

