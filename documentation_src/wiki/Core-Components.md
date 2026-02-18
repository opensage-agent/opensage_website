# Core Components

OpenSage core components.

## 1. Session

The central manager for all session-specific resources.

**Key Responsibilities:**
- Configuration management (TOML loading, env overrides)
- Agent lifecycle (creation, persistence, cleanup)
- Sandbox management (Docker containers, resource isolation)
- Neo4j client management
- Agent ensemble coordination

**Key Files:**
- `opensage.session.session`
- `opensage.session.dynamic_agent_manager`
- `opensage.session.sandbox_manager`

## 2. Agent

Extended ADK agent with security-focused features.

**Key Features:**
- Dynamic tool loading from filesystem
- Integration with sandbox environments
- Tool combo support
- Session-aware tool execution

**Key Files:**
- Agent implementation lives under the `opensage.agents` namespace.

## 3. Sandbox System

Isolated execution environments for security analysis.

**Sandbox Types:**
- `main`: Primary analysis sandbox
- `joern`: Static analysis (CPG generation)
- `codeql`: CodeQL analysis
- `neo4j`: Graph database for CPG storage
- `gdb_mcp`: Debugger integration
- `fuzz`: Fuzzing environment

**Key Files:**
- `opensage.sandbox.base_sandbox`
- `opensage.sandbox.native_docker_sandbox`
- `opensage.sandbox.k8s_sandbox`
- `opensage.sandbox.initializers`

## 4. Configuration System

TOML-based configuration with template variable expansion.

**Key Files:**
- `opensage.config.config_dataclass`
- `opensage.templates.configs.default_config`

## 5. Toolbox

Collection of security analysis tools.

**Tool Categories:**
- Static Analysis: Joern, CodeQL queries
- Dynamic Analysis: Fuzzing, debugging
- Coverage: LLVM coverage tools
- Retrieval: Code search and symbol lookup
- Evaluation: PoC submission and validation

**Key Files:**
- `opensage.toolbox`

## Related Topics

- [Core Concepts](Core-Concepts.md) - Understanding how components work together
- [Architecture](Architecture.md) - System architecture overview
- [Development Guides](Development-Guides.md) - How to extend components
