# Travel Agents — Multi-Agent Platform

A multi-agent workspace for building and managing a travel agency platform using Hermes Workspace agents.

## Project Overview

This repository tracks the development of a **travel agency platform** that uses multiple specialized agents working in sequence to:
- Research travel markets and destinations
- Design the user interface and experience
- Develop the full-stack platform
- Review and deploy the final product

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   Orchestration Layer                      │
│  ┌────────────────┐  ┌──────────────┐  ┌───────────────┐ │
│  │   Orchestrator │→ │  Travel      │→ │  Deployer     │ │
│  │   (Herme Agent)│  │   Planner    │  │  (Herme Agent)│ │
│  └────────────────┘  └──────────────┘  └───────────────┘ │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Agent Workflows                          │
│  ┌──────────────┐  ┌───────────────┐  ┌───────────────┐   │
│  │  Researcher  │  │   Designer     │  │  Developer    │   │
│  │ (Herme Agent)│→ │ (Herme Agent)  │→ │ (Herme Agent)│   │
│  └──────────────┘  └───────────────┘  └───────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  Review & QA                               │
│  ┌──────────────┐  ┌───────────────┐  ┌───────────────┐   │
│  │   Reviewer   │← │   QA Checker   │← │  Test Runner  │   │
│  │ (Herme Agent)│  │ (Herme Agent)  │  │ (Herme Agent)│   │
│  └──────────────┘  └───────────────┘  └───────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Hermes Workspace                        │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌───────────┐  │ │
│  │  │ Chat   │ │Terminal │ │ Memory  │ │ Skills    │  │ │
│  │  └─────────┘ └─────────┘ └─────────┘ └───────────┘  │ │
│  └───────────────────────────────────────────────────────┘ │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────────┐  │ │
│  │  │ Kanban     │ │Reports      │ │Inbox            │  │ │
│  │  │  Board     │ │+ Checkpoints│ │+ Escalations    │  │ │
│  │  └─────────────┘ └─────────────┘ └─────────────────┘  │ │
│  └───────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Agent Setup

### Planned Agents

| Agent | Role | Specialty | Mission |
|-------|------|-----------|---------|
| `agent-researcher` | Researcher | Travel Market Analysis | Investigate destinations, competition, pricing trends |
| `agent-designer` | Designer | UI/UX Design | Create wireframes, mockups, user flows |
| `agent-developer` | Developer | Full-stack Development | Build platform features, integrate APIs |
| `agent-reviewer` | Reviewer | QA/Testing | Review checkpoints, approve PRs, ensure quality |

### Sequential Execution

Agents run sequentially with automatic handoffs:
```bash
1. Researcher → Checkpoint → 2. Designer → Checkpoint →
3. Developer → Checkpoint → 4. Reviewer → Deploy
```

## Workspace Setup

```bash
# Start the Hermes Workspace
cd ~/hermes-workspace
pnpm install
pnpm dev

# Access at http://localhost:3000
```

## How to Use This Repo

1. **Meeting Notes**: Add to `docs/meeting-notes/YYYY-MM-DD.md`
2. **Agent Specs**: Check `docs/agents/` for role configurations
3. **Workflow Plans**: See `docs/workflows/` for task sequences
4. **Progress Tracking**: Check `notes/` for work logs
5. **Decisions**: See `docs/decisions.md` for major decisions
6. **Skills**: Created under `skills/` for loading in Hermes Agent

## Repository Updates (May 2026)

### ✅ Cleanup Completed

- **Removed duplicate README.md files** from each agent folder (`agent*/README.md`)
- **Created proper .gitignore** to prevent future duplicates
- **Consolidated documentation** in `docs/` directory

**Why this matters:**
- Agent-specific READMEs were identical duplicates (same 761 words)
- Documentation should live in centralized `docs/agents/` folder
- Cleaner repo structure for maintenance

### ✅ New Skills Added

- **`travel-agent-assistant`** - Domain-specific travel knowledge for LLM agents
- Located: `skills/travel-agent-assistant/SKILL.md`
- Loads automatically when agents need travel domain expertise

## Quick Links

- [Project README](./README.md)
- [Architecture Guide](./docs/architecture/README.md)
- [Agent Specifications](./docs/agents/)
- [Meeting Notes](./docs/meeting-notes/)
- [Recent Notes](./notes/)

## License

MIT License — See [LICENSE](./LICENSE)

---

**Built with Hermes Agent & Hermes Workspace**
