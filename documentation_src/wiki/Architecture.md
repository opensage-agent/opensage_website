# Architecture Overview

## Design Principles

1. **Session Isolation**: Each session has its own resources (sandboxes, configs, agents)
2. **Minimal Global State**: Resources are session-bound (except the session registry)
3. **Composability**: Build complex agents from simple components
4. **Tool Integration**: Seamless integration with security analysis tools
5. **Extensibility**: Easy to add new tools, sandboxes, and agents

## Component Relationships

- **OpenSageSession** is the central manager that coordinates all resources
- **OpenSageAgent** extends ADK agents with self-programming capabilities
- **Sandboxes** provide isolated execution environments
- **Configuration** is TOML-based with template variables
- **Tools** are dynamically loaded and session-aware

## See Also

- [Core Components](Core-Components.md) - Detailed component descriptions
- [Core Concepts](Core-Concepts.md) - Core concepts explained
- [Project Structure](Project-Structure.md) - Code organization
