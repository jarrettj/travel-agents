# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A multi-agent travel booking platform configuration and tooling repo. The agents run inside **Hermes Workspace** (an external application at `~/hermes-workspace`), not as standalone processes from this repo. This repo contains:

- Agent configuration files (`*-soul.md` files defining each agent's persona, tools, and workflow)
- The swarm definition (`travel-agents-swarm.yaml`)
- A Python workflow runner for dispatching agents via the Hermes API
- A FastAPI web interface (`web/`) for submitting travel requests
- Skills and documentation

## Key Commands

### Run the Hermes Workspace (required before anything else)
```bash
cd ~/hermes-workspace
pnpm install
pnpm dev
# Accessible at http://localhost:3000
```

### Run the web interface
```bash
cd web
pip install -r requirements.txt
python app.py
# Accessible at http://127.0.0.1:9999
```

### Trigger the sequential agent workflow
```bash
# Run all agents starting from the first
python workflow/runners/workflow-runner.py 0

# Start from a specific agent (index into workflow/config.json agents array)
python workflow/runners/workflow-runner.py 1
```

### Check Hermes agent/swarm status
```bash
curl http://localhost:3000/api/health
curl http://localhost:3000/api/swarm/status
curl "http://localhost:3000/api/swarm/checkpoint?workerId=researcher-travel"
```

### Web API health check
```bash
curl http://localhost:9999/api/health
```

## Architecture

### Agent Execution Model

Agents are **Hermes Workspace workers** defined in `travel-agents-swarm.yaml`. They run inside tmux sessions managed by Hermes and communicate via the Hermes REST API at `http://localhost:3000`. The repo interacts with them through:

1. **Hermes Workspace UI** — dispatch tasks via the Swarm Mode Kanban board
2. **Direct API calls** to `POST /api/swarm-dispatch`
3. **`workflow/runners/workflow-runner.py`** — orchestrates sequential dispatch, polls for checkpoints, and passes output as `inputContext` to the next agent

### Sequential Pipeline

The deliberate design choice (see `docs/decisions.md`) is **sequential execution**:

```
Researcher (swarm14) → Designer (swarm15) → Reviewer (swarm17) → Developer (swarm16)
```

Each agent completes and returns a **checkpoint** before the next agent starts. The workflow runner polls `GET /api/swarm/checkpoint?workerId=<id>` until `status == "checkpointed"`, then passes the `deliverable` as `inputContext` to the next dispatch.

### Checkpoint Format

All agents must return this standardized JSON structure:
```json
{
  "agentId": "researcher",
  "status": "completed",
  "deliverable": {
    "type": "research_findings",
    "version": 1,
    "data": { "..." }
  },
  "confidence": 0.92,
  "nextAgent": "designer",
  "summary": "Brief summary for context"
}
```

### Agent Identities

Travel-specific agents are defined in `travel-agents-swarm.yaml` with swarm IDs **swarm13–swarm17**. The general-purpose swarm agents (swarm1–swarm12) handle non-travel tasks (PR review, ops, research, etc.).

| Swarm ID | Name | Role |
|----------|------|------|
| swarm13 | Travel Orchestrator | Coordinates workflow, routes tasks |
| swarm14 | Travel Researcher | Researches flights, hotels, activities |
| swarm15 | Travel Designer | Designs itineraries and booking flows |
| swarm16 | Travel Developer | Builds booking integrations, executes bookings |
| swarm17 | Travel Reviewer | Validates bookings, checks feasibility |

### Agent Configuration Files

Each agent's behavior is defined by a `*-soul.md` file:
- `researcher-agent/researcher-soul.md` — research workflow, output format, handoff protocol
- `designer-agent/designer-soul.md` — itinerary design template, packing lists, handoff protocol

The soul files are loaded into the agent's Hermes profile. When modifying agent behavior, edit the soul file and reload the agent in the Hermes dashboard.

### Web Interface (`web/`)

A FastAPI app providing a REST interface for travel requests. State is held **in-memory** (`requests_history`, `active_requests` dicts) — there is no database. The frontend is a static `index.html` file. The API does not yet trigger real agent dispatch; the `/api/requests/{id}/agent/{name}/handoff` endpoint simulates agent processing.

Key environment variables for `web/app.py`:
- `PORT` — defaults to `9999`
- `HOST` — defaults to `127.0.0.1`
- `API_KEY` — defaults to `demo-key`

### Skills

`skills/travel-agent-assistant/SKILL.md` is a domain knowledge document (travel APIs, booking patterns, common errors, budget estimators) loaded into an agent's context when it needs travel-specific expertise. Load it by referencing it in the agent's soul file or appending it to a dispatch task's context.

### Workflow Configuration

`workflow/config.json` defines the agent sequence for the Python runner. The `agents` array is ordered; the runner dispatches them in sequence. The `id` field must match a `workerId` registered in Hermes.

## Key Conventions

- **Soul files live in this repo** but are also copied to `~/hermes-workspace/profiles/travel-agents/` for Hermes to load them. Keep both in sync when editing.
- **No actual booking APIs are integrated yet** — the Developer agent's booking calls and the web API's search results are mocked/simulated.
- **Model**: `apple/omlx/qwen` (local model), 120 iterations per agent, sequential mode — configured in `travel-agents-swarm.yaml` under `global`.
- **New documentation** goes in `docs/`; meeting notes in `docs/meeting-notes/YYYY-MM-DD.md`; decisions in `docs/decisions.md`.
- **Skills** are Markdown files under `skills/<skill-name>/SKILL.md` and are loaded manually into agent contexts.
