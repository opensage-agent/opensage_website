# Project Structure

## Directory Overview

```
OpenSage/
├── src/opensage/            # Public Python namespace
│   ├── agents/              # Agent implementations
│   ├── cli/                 # Command-line interface
│   ├── config/              # Configuration system
│   ├── session/             # Session management
│   ├── sandbox/             # Sandbox implementations
│   ├── toolbox/             # Security analysis tools
│   ├── evaluations/         # Benchmark evaluations
│   ├── features/            # Framework features
│   ├── plugins/             # ADK plugins
│   ├── patches/             # ADK patches
│   └── templates/           # Configuration templates
├── examples/                # Example agents and usage
├── tests/                   # Test suite
├── docs/                    # Documentation
└── README.md               # Quick start guide
```

## Key Directories Explained

### `src/opensage/agents/`
- Extended ADK agent class
- Tool loading and dynamic tool injection

### `src/opensage/session/`
- Session manager
- Sandbox lifecycle management
- Agent creation and caching
- Multi-agent coordination

### `src/opensage/sandbox/`
- Abstract sandbox interface
- Docker-based sandbox
- Kubernetes-based sandbox
- `initializers/`: Sandbox initialization logic

### `src/opensage/toolbox/`
- `static_analysis/`: Joern, CodeQL integration
- `fuzzing/`: Fuzzing tools
- `debugger/`: GDB integration
- `coverage/`: Coverage analysis
- `retrieval/`: Code search tools

### `src/opensage/evaluations/`
- `cybergym/`: CyberGym benchmark
- `patchagent/`: PatchAgent benchmark
- `secodeplt/`: SecCodePLT benchmark

## See Also

- [Core Components](Core-Components.md) - Component details
- [Development Guides](Development-Guides.md) - How to add to the codebase
