# Getting Started with Travel Agents

Welcome to the Travel Agents project! This guide will help you get started with setting up and running the multi-agent workflow.

## Quick Start

### 1. Prerequisites

Make sure you have the following installed:

```bash
# Node.js 22+
# pnpm
# git
# tmux (for persistent agent sessions)
# Hermes Agent installed
```

### 2. Start Hermes Workspace

```bash
cd ~/hermes-workspace
pnpm install
pnpm dev
```

Open your browser to: `http://localhost:3000`

### 3. Add Agents to Swarm Mode

In the Hermes Workspace UI:

1. Navigate to **Swarm Mode**
2. Click **"Add Swarm"**
3. Add each agent with the configuration below:

#### Agent 1: Researcher
- **Worker ID**: `researcher`
- **Role**: `researcher`
- **Specialty**: Travel Market Analysis
- **Mission**: Research destinations, competition, pricing
- **Model**: `anthropic/claude-sonnet-4`
- **Skills**: `web_search, curl, data_analysis`

#### Agent 2: Designer
- **Worker ID**: `designer`
- **Role**: `designer`
- **Specialty**: UI/UX Design
- **Mission**: Create wireframes and user flows
- **Model**: `anthropic/claude-sonnet-4`
- **Skills**: `sketch, design-md`

#### Agent 3: Developer
- **Worker ID**: `developer`
- **Role**: `developer`
- **Specialty**: Full-stack Development
- **Mission**: Build the travel platform
- **Model**: `anthropic/claude-sonnet-4`
- **Skills**: `code_generation, api_integration, database_design`

#### Agent 4: Reviewer
- **Worker ID**: `reviewer`
- **Role**: `reviewer`
- **Specialty**: QA and Testing
- **Mission**: Review and approve the platform
- **Model**: `anthropic/claude-sonnet-4`
- **Skills**: `testing, code_review, api_testing`

### 4. Set Sequential Execution

In each agent's configuration:

```yaml
execution_order: 1  # for researcher
execution_order: 2  # for designer
execution_order: 3  # for developer
execution_order: 4  # for reviewer
```

### 5. Dispatch the First Task

Open **Terminal** in the workspace and run:

```bash
# Dispatch to Researcher
curl -X POST http://localhost:3000/api/swarm-dispatch \
  -H 'Content-Type: application/json' \
  -d '{
    "workerIds": ["researcher"],
    "prompt": "Research top 10 emerging travel destinations for 2026, including market size, key attractions, and competitor presence"
  }'
```

### 6. Monitor Progress

- **Swarm Mode UI**: View agent cards, status, and current tasks
- **Kanban Board**: Track tasks moving through lanes
- **Reports**: Review checkpoints from each agent

## Next Steps

Once you've verified the setup works:

1. **Create meeting notes**: Add to `docs/meeting-notes/`
2. **Document agent interactions**: Add to `notes/`
3. **Update architecture docs**: As you refine the approach
4. **Extend agent capabilities**: Add custom skills as needed

## Common Issues

### Issue: Agent not responding

**Solution**:
```bash
# Check worker session
tmux ls | grep "swarm-"

# Restart agent
curl -X POST http://localhost:3000/api/swarm/rotate?workerId=researcher
```

### Issue: Checkpoint timeout

**Solution**:
```bash
# Increase timeout in config.json
"timeoutSeconds": 900  # 15 minutes
```

### Issue: Permission denied on file operations

**Solution**:
```bash
# Grant permissions
chmod 755 ~/.hermes/profiles/researcher
```

## References

- **Project README**: See `README.md`
- **Agent Specifications**: See `docs/agents/README.md`
- **Workflow Guide**: See `docs/workflows/sequential-execution.md`
- **Architecture Decisions**: See `docs/decisions.md`

## Support

If you run into issues:

1. Check the logs in the workspace
2. Review the Kanban board for stuck tasks
3. Check agent session with `tmux ls`
4. Review error messages in the Terminal

---

**Happy building! 🚀**
