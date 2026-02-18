# Introduction

## What is OpenSage?

OpenSage (Open Self-programming Agent Generation Engine) is an AI agent framework built on top of Google ADK (Agent Development Kit). It represents a paradigm shift from "Agent Development 1.0" to "Agent Development 2.0" — transitioning from agents that execute predefined structures to agents that can dynamically build and manage their own systems at runtime.

## Core Value Proposition

### From "Agent Using System" to "Agent Building System"

**Agent Development 1.0** (Traditional Frameworks):
- System structure pre-defined by humans (agent topology, workflows, tool sets)
- Agents can only choose actions within given structures
- Extending to new tasks requires significant manual refactoring
- Essentially human-centered agent building

**Agent Development 2.0** (OpenSage):
- Agents upgrade from "executing predefined structures" to "autonomously building and managing structures"
- Humans provide minimal, stable system-level scaffolding
- Everything else is generated, composed, and scheduled by AI at runtime
- Agents can "invent new capabilities" rather than just calling existing ones

## Key Advantages

### 1. AI-Written Tools as First-Class System Entities

**Redefining Tools in Agent Development 2.0:**

In traditional frameworks, tools are:
- Fixed API lists
- Pre-registered function interfaces defined by humans
- Static capabilities that agents can only call

In OpenSage (Agent Development 2.0), tools are:
- **Programmatic entities** that agents can write, modify, and evolve
- **Runtime-generated capabilities** that adapt to current tasks
- **First-class system entities** with lifecycle management

**Supported Capabilities:**

OpenSage natively supports:
- **Agent-generated tools**: Agents can create new tools (bash scripts, analysis scripts, debugging tools)
- **Tool modification**: Agents can modify existing tools to adapt to current tasks
- **Runtime tool management**:
  - Multiple bash sessions for parallel execution
  - Tool-specific sandboxes (especially for long-running tools like fuzzers)
  - Tool state persistence and restoration, enabling cross-task reuse

**Design Value:**

This design enables:
- Agents can "invent new capabilities" rather than just calling existing ones
- Tool sets evolve with tasks, not statically bound
- System has continuous self-expansion potential

**Implementation:**
- `ToolLoader` dynamically discovers tools from `src/aigise/bash_tools/`
- Tools structured as "Skills" with metadata (`SKILL.md`)
- `bash_tool` enables execution of arbitrary commands, allowing agents to create new tools

### 2. Runtime-Generated Sub-Agents & Dynamic Agent Topology

**Sub-Agent Positioning:**

Sub-agents are functionally specialized agents temporarily created for specific sub-tasks, such as:
- Debugger Agent
- Retrieval Agent
- Fuzzer Agent
- Memory Agent

**Supported Capabilities:**

OpenSage supports:
- **Runtime creation/destruction** of sub-agents
- Each sub-agent has:
  - Independent identity
  - Independent tool set
  - Independent short-term memory
- **Recursive sub-agent creation**: Sub-agents can create their own sub-agents

**Agent Topology:**

All agents and sub-agents form:
- A **task-specific agent graph** (agent graph)
- The graph can **dynamically change** during execution
- Different tasks have **different agent topology structures**

**Agent Ensemble:**

System supports:
- **Parallel exploration**: Multiple agents explore in parallel
- **Result merging**: Results from multiple agents are merged
- **Dynamic trade-off**: Balance between efficiency and stability
- Thread-safe agent execution support

**Implementation:**
- `DynamicAgentManager` manages agent lifecycle
- `AigiseEnsembleManager` coordinates multi-agent execution
- Agents can discover and call other agents dynamically

### 3. Memory as Manageable System Resource

**Layered Memory Model:**

OpenSage adopts:
- **Persistent long-term memory**: Cross-session knowledge retention
- **Sub-agent specific short-term memory**: Task-specific context

**Graph-Structured Memory:**

Memory is organized as a graph structure:
- **Nodes** represent facts, events, summaries
- **Edges** represent dependencies, causal relationships, or semantic relationships
- Supports **graph queries and retrieval**

**Memory Agent:**

A dedicated memory agent (planned):
- Decides **when to store** information
- Determines **when to compress or discard** old information
- Manages **when to retrieve** historical experience

Memory is not passive context, but:
- **Runtime resource** actively scheduled by agents
- **First-class entity** in the system architecture

> **Note**: Graph-structured memory and Memory Agent are planned features and
> documentation will be added as these features are implemented.

### 4. Session-Based Resource Isolation

**Architecture:**
- Each session has completely isolated resources (sandboxes, configs, agents)
- No global singletons — all resources are session-bound
- Prevents interference between different agent runs
- Clean resource management and cleanup

### 5. Multi-Sandbox Support with Flexible Backends

**Sandbox Types:**
- `main`: Primary analysis sandbox
- `joern`: Static analysis (CPG generation)
- `codeql`: CodeQL analysis
- `neo4j`: Graph database for CPG storage
- `gdb_mcp`: Debugger integration
- `fuzz`: Fuzzing environment

**Backend Support:**
- **Docker (Native)**: Local development and testing
- **Kubernetes**: Production deployment with automatic scaling
- Easy switching between backends via configuration

**Implementation:**
- `K8sSandbox` provides Kubernetes backend
- `NativeDockerSandbox` for local Docker execution
- Sandbox factory pattern for backend abstraction

### 6. Security-Focused System-Level Customization

OpenSage is **not a generic agent demo**, but deeply customized for software security and software engineering.

**Native Integration:**
- **Static analysis tools**: CPG generation, program slicing, call graphs (via Joern/CodeQL)
- **Dynamic analysis tools**: Debuggers (GDB), fuzzing, coverage analysis (via sandbox tools)
- **LSP and code understanding tools**: Language server protocol integration

**Agent Capabilities:**
Agents can:
- **Self-diagnose** failure causes
- **Create specialized debugging sub-agents** on demand
- **Adjust workflows** based on runtime signals
- **Generate security-focused tools** for specific vulnerability types

This system-level customization makes OpenSage a powerful platform for security research and software engineering automation.

## Design Philosophy

### Agent Development 2.0 Principles

1. **First-Class Evolvable Entities**: Tool / Agent / Workflow / Memory are all first-class, evolvable entities, not static configurations
2. **Minimal Scaffolding**: Humans provide only stable system-level infrastructure
3. **Runtime Generation**: Agents build structures at runtime, not design time
4. **Continuous Self-Extension**: System has the potential for continuous self-expansion

### The Fundamental Innovation

Agent Development 2.0's innovation is not about:
- Larger models
- More complex prompts

Instead, it's about:
- Treating agents as entities that can build systems
- Elevating Tool / Agent / Workflow / Memory to first-class, evolvable entities
- Building infrastructure that enables agents to autonomously design, execute, and improve complex task systems

## Key Features

- **AI-written tools** as first-class system entities
- **Runtime sub-agent creation** and dynamic agent topology
- **Memory as manageable resource** (graph-structured, memory agent) - *planned*
- **Session-based resource management** with complete isolation
- **Multi-sandbox support** (Docker, Kubernetes)
- **Dynamic tool loading** and runtime tool generation
- **Agent ensemble** for parallel exploration
- **Integration with security tools** (Joern, CodeQL, GDB, Neo4j)
- **Evaluation framework** for security benchmarks

## Why OpenSage?

OpenSage was designed to make self-programming agent development feel more like software development. It provides:

1. **Isolation**: Each agent session has its own resources, preventing interference
2. **Flexibility**: Easy to add new tools, sandboxes, and agents
3. **Evolution**: Tools and agents can be created and modified at runtime
4. **Integration**: Seamless integration with existing security analysis tools
5. **Composability**: Build complex agents from simple components
6. **Scalability**: Kubernetes support for production deployment

## Use Cases

- Self-programming agent development
- Code generation and analysis
- Vulnerability detection and analysis
- Fuzzing campaign management
- Code coverage analysis
- Static code analysis (CPG generation)
- Multi-agent workflows
- Agent training and evaluation

## Next Steps

- [Getting Started](Getting-Started.md) - Set up your development environment
- [Architecture](Architecture.md) - Understand the system architecture
- [Core Concepts](Core-Concepts.md) - Learn the core concepts
- [Entry Points](Entry-Points.md) - Understand how to use OpenSage
