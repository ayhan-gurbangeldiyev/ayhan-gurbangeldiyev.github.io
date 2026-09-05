---
layout: post
title: "Before Adding a Second Agent: What the Evidence Actually Shows"
date: 2026-09-05 13:50:00 +0300
author: Ayhan Gurbangeldiyev
categories: [ai-engineering, agents]
excerpt: "What recent research says about coordination, task dependencies, and the evidence needed before adding another agent."
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

Before choosing an architecture, I would ask:

- Can useful subtasks run independently?
- How much context must every agent share?
- Who resolves conflicting findings or duplicated work?
- Can success be verified outside the model’s final response?

## Make the comparison measurable

A practical starting point is a single-agent baseline on representative tasks. Compare an additional-agent configuration using the same model versions, tools, inputs, and clearly specified resource budgets. Report successful completion, errors, latency, and actual cost, including retries and coordination. Repeat trials to expose variability.

Evaluation should inspect the resulting state: a claimed account update must correspond to the intended change. Anthropic’s evaluation guidance distinguishes this outcome from the conversation transcript. [Agent evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents).

The decision is whether coordination improves the outcome enough for the application’s constraints. The evidence supports testing that proposition for a specific task before treating agent count as a measure of system capability.

---

[About the author and projects](https://ayhangurbangeldiyev.com/)
