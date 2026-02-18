# Core Concepts

## Session Management

Every operation in OpenSage is scoped to a session. Sessions provide:
- Resource isolation
- Configuration management
- Lifecycle management

```python
import opensage

session = opensage.get_session("my_session_id", config_path="config.toml")
```

## Agent Creation

Agents are created through `mk_agent` functions:

```python
def mk_agent(session_id: str):
    session = opensage.get_session(session_id)
    # ... configure agent ...
    return Agent(...)
```

## Sandbox Lifecycle

Sandboxes are managed through the session:

```python
session = opensage.get_session("my_session_id")
sandbox = session.sandboxes.get_sandbox("main")
result = sandbox.run_command_in_container("ls /shared")
```

## Tool Development

In OpenSage, tools are implemented as **Agent Skills** (bash scripts) or **MCP toolsets**, rather than Python functions. This design provides better isolation and allows tools to run directly in sandbox containers.

### Agent Skills (Bash Scripts)

Agent Skills are bash scripts organized in a structured directory format:

```
src/<package>/bash_tools/
└── category/
    └── tool-name/
        ├── SKILL.md          # Metadata and documentation
        └── scripts/
            └── tool_script.sh # Bash implementation
```

The `SKILL.md` file contains:
- YAML frontmatter with `name` and `description`
- Parameter definitions
- Sandbox requirements
- Usage examples
- Return value format

### MCP Toolsets

MCP (Model Context Protocol) toolsets provide integration with external services:

```python
@safe_tool_execution
@requires_sandbox("gdb_mcp")
def get_toolset(session_id: str) -> MCPToolset:
    url = get_mcp_url_from_session_id("gdb_mcp", session_id)
    return MCPToolset(connection_params=SseConnectionParams(url=url))
```

### Automatic Discovery

Tools are automatically discovered from:
- `src/opensage/bash_tools/` (built-in tools)
- `~/.local/plugins/opensage/tools/` (user plugins)

No manual registration is required.

## Configuration

Configuration is TOML-based with template variables:

```toml
src_dir_in_sandbox = "/shared/code"
[sandbox.sandboxes.main]
image = "ubuntu:20.04"
```

## See Also

- [Development Guides](Development-Guides.md) - Practical development examples
- [Common Patterns](Common-Patterns.md) - Common code patterns
- [Best Practices](Best-Practices.md) - Best practices
