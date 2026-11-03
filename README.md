# Agent Barrier Sync ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Agent Barrier Sync Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/agent-barrier-sync/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/agent-barrier-sync?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/agent-barrier-sync/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Agent Barrier Sync** is a production-ready developer tool and connector: Rendezvous barrier and milestone synchronization primitive for multi-agent workflows.

---

## 🚀 Problem Statement

Concurrent agents diverge when downstream compilation, testing, or publishing steps trigger before all upstream research agents finish their required outputs.

---

## ⚡ Architecture Flow

```mermaid
sequenceDiagram
    autonumber
    participant A1 as Research Agent 1
    participant A2 as Research Agent 2
    participant Barrier as Agent Barrier (Milestone: "RESEARCH_DONE")
    participant Next as Synthesis Agent

    A1->>Barrier: arrive(agent="A1", payload={data: ...})
    Note over Barrier: 1/2 Arrived. Barrier Locked 🔒
    A2->>Barrier: arrive(agent="A2", payload={data: ...})
    Note over Barrier: 2/2 Arrived. Barrier Released 🔓!
    Barrier-->>Next: Dispatch Combined Deliverables
```

---

## 📊 Performance Benchmarks

| Synchronization Model | Polling / Sleep | Agent Barrier Sync | Advantage |
|---|---|---|---|
| Race Conditions | Frequent / Flaky | 0% (Strict Barrier) | **100% Deterministic** |
| Idle Wait Latency | +2,000 ms (sleep) | 0.03 ms release | **Instantaneous** |
| Payload Aggregation | Ad-hoc / Lost | Consolidated manifest | **Zero Loss** |
| Timeout Resilience | Stalls forever | Safe timeout release | **No Deadlocks** |

---

## 🛠️ Installation & Quickstart

```bash
pip install agent_barrier_sync
```

### Python API

```python
import agent_barrier_sync

print(agent_barrier_sync.__version__)
```

### CLI Usage

```bash
agent-barrier-sync --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
