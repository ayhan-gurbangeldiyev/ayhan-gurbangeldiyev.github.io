---
layout: post
title: "Before Adding a Second Agent: What the Evidence Actually Shows"
date: 2026-09-05 13:50:00 +0300
author: Ayhan Gurbangeldiyev
categories: [ai-engineering, agents]
excerpt: "What recent research says about coordination, task dependencies, and the evidence needed before adding another agent."
description: "What recent research says about coordination, task dependencies, and the evidence needed before adding another agent."
permalink: /writing/before-adding-a-second-agent/
featured: true
article_type: Research note
topics: [agentic-systems, ai-evaluation]
cover: /assets/images/agent-coordination-cover.svg
image:
  path: /assets/images/agent-coordination-social.png
  width: 1200
  height: 630
  alt: "Before Adding a Second Agent: single-agent and coordinated multi-agent paths."
---

Adding a second agent creates an architectural question: can the task benefit from independent work, and will the improvement justify the coordination required? Recent research offers useful evidence, provided its results stay attached to the conditions under which they were measured.

*This article was drafted with AI assistance. It is a commentary on published research, not a report of experiments conducted by the author.*

## What the evidence says

In January 2026, Google Research described an evaluation of 180 agent configurations across four benchmarks. Its reported results varied substantially by task: centralized coordination improved performance by 80.9% on Finance-Agent, while the multi-agent variants tested on PlanCraft reduced performance by 39–70%. These are relative changes against the study’s single-agent baselines, not percentage-point changes or forecasts for other applications. [Google Research](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/).

Anthropic reported a different, compatible finding in June 2025. On its internal research evaluation, a system using Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2%. It also reported that multi-agent systems used roughly 15 times the tokens of ordinary chat interactions. That token comparison was against chats, not the single-agent evaluation baseline, and it is not a dollar-cost multiplier. [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system).

These studies examine different systems and tasks. Their numbers should not be combined into a universal estimate of what another agent will deliver.

## Look at the dependencies

Consider two illustrative tasks. Comparing several vendors could allow separate agents to inspect each vendor’s documentation before combining findings. Resolving an account issue may require checking identity, retrieving the correct record, and applying an authorized change in sequence.

The first example offers opportunities for independent investigation. In the second, later steps depend on earlier results and a consistent account state. Splitting responsibility introduces handoffs that need an explicit reason to exist. These examples suggest questions to test; they are not measured results.

{% include figure.html src="/assets/images/single-vs-multi.svg" fallback="/assets/images/single-vs-multi.png" width=960 height=600 alt="Single-agent flow: task to agent and tools to verified outcome. Multi-agent flow: task to coordinator, independent agent A and agent B, synthesis, and verified outcome. Shared context, handoffs, and conflict resolution add coordination work." caption="Figure 1. Two illustrative architectures. Parallel work is useful only when the task allows it; delegation also adds shared context, handoffs, and synthesis. This is a conceptual comparison, not a measured performance result." %}

Before choosing an architecture, I would ask:

- Can useful subtasks run independently?
- How much context must every agent share?
- Who resolves conflicting findings or duplicated work?
- Can success be verified outside the model’s final response?

## Make the comparison measurable

A practical starting point is a single-agent baseline on representative tasks. Compare an additional-agent configuration using the same model versions, tools, inputs, and clearly specified resource budgets. Report successful completion, errors, latency, and actual cost, including retries and coordination. Repeat trials to expose variability.

Evaluation should inspect the resulting state: a claimed account update must correspond to the intended change. Anthropic’s evaluation guidance distinguishes this outcome from the conversation transcript. [Agent evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).

The decision is whether coordination improves the outcome enough for the application’s constraints. The evidence supports testing that proposition for a specific task before treating agent count as a measure of system capability.

{% include figure.html src="/assets/images/evaluation-decision.svg" fallback="/assets/images/evaluation-decision.png" width=960 height=680 alt="Decision process: define representative tasks and a single-agent baseline. If subtasks cannot run independently, retain the baseline. Otherwise compare architectures with fixed models, tools, inputs, and budgets; repeat trials and inspect outcomes, failures, latency, and actual cost. Adopt coordination only if its benefit justifies the overhead under the application's constraints." caption="Figure 2. An evaluation decision process derived from the questions in this note. Success means a verified outcome within the application’s constraints. No numerical thresholds or new experimental results are implied." %}

## References

- [Google Research: Towards a science of scaling agent systems](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/) — task-specific comparisons across agent configurations.
- [Anthropic: How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) — an internal research evaluation and its resource trade-offs.
- [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — distinguishing transcripts from outcomes.

---

[About the author and projects](https://ayhangurbangeldiyev.com/)
