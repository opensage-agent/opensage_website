"""MkDocs hook: generate API reference pages for AIgiSE (aigise).

We generate a small set of stable, high-signal pages (by package area) rather
than one page per module. Each page uses mkdocstrings directives, so the API
reference stays in sync with the source automatically.
"""

from __future__ import annotations

from pathlib import Path


_PAGES: list[tuple[str, str, list[str] | None]] = [
  (
    "session.md",
    "Session",
    [
      "aigise.session.aigise_session",
      "aigise.session.aigise_sandbox_manager",
      "aigise.session.aigise_dynamic_agent_manager",
    ],
  ),
  (
    "sandbox.md",
    "Sandbox",
    [
      "aigise.sandbox.base_sandbox",
      "aigise.sandbox.factory",
      "aigise.sandbox.native_docker_sandbox",
      "aigise.sandbox.remote_docker_sandbox",
      "aigise.sandbox.k8s_sandbox",
    ],
  ),
  (
    "memory.md",
    "Memory",
    [
      "aigise.memory.search.search_controller",
      "aigise.memory.tools.memory_search_tools",
      "aigise.memory.tools.memory_update_tools",
    ],
  ),
  (
    "toolbox.md",
    "Toolbox",
    [
      "aigise.toolbox.decorators",
      "aigise.toolbox.general.agent_tools",
      "aigise.toolbox.general.dynamic_subagent",
    ],
  ),
  ("cli.md", "CLI", ["aigise.cli.aigise_cli", "aigise.cli.aigise_web_app"]),
  (
    "plugins.md",
    "Plugins",
    [
      "aigise.plugins.build_verifier_plugin",
      "aigise.plugins.validator_plugin",
      "aigise.plugins.memory_observer_plugin",
    ],
  ),
]


def _mkdocstrings_block(ident: str) -> str:
  return (
    f"::: {ident}\n"
    "    options:\n"
    "      members: true\n"
    "      inherited_members: true\n"
    "      show_root_heading: true\n"
    "      show_root_toc_entry: true\n"
    "      show_source: false\n"
  )


def _write_page(path: Path, title: str, idents: list[str] | None) -> None:
  path.parent.mkdir(parents=True, exist_ok=True)
  if idents is None:
    content = (
      f"# {title}\n\n"
      "This section is automatically generated from the `AIgiSE/src/aigise/`\n"
      "source tree using `mkdocstrings`.\n"
    )
  else:
    blocks = "\n\n".join(_mkdocstrings_block(ident) for ident in idents)
    content = f"# {title}\n\n{blocks}\n"
  path.write_text(content, encoding="utf-8")


def on_startup(command: str, dirty: bool) -> None:
  del dirty  # unused

  if command not in {"build", "serve", "gh-deploy"}:
    return

  opensage_website_dir = Path(__file__).resolve().parent.parent
  docs_dir = opensage_website_dir / "documentation_src" / "wiki"
  out_dir = docs_dir / "generated" / "api"

  for filename, title, idents in _PAGES:
    _write_page(out_dir / filename, title, idents)

