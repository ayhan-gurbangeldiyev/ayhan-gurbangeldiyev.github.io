# Editorial strategy — 2026

**Reliable and observable AI systems in practice.** Help engineers decide what to build, how to evaluate it, and when extra complexity is justified. Prefer a question with evidence over a broad introduction to AI. Future technical writing should originate here; legacy portfolio writing follows the separate migration plan.

## Formats and evidence

- **Engineering deep dive:** constraints, baseline, alternatives, architecture and evaluated trade-offs. Distinguish synthesis from measured work.
- **Build note:** actual implemented change, inspectable code/commit, reproduction steps, limitations. Publish only after the build exists.
- **Research note:** primary-source synthesis, task/model/budget context, compatible comparisons and limits on transfer.
- **Decision record:** problem, constraints, options, selected approach, rejected alternatives and conditions for revisiting it.
- **Failure note:** reproduced failure, root-cause evidence, correction and regression check. Never invent a production incident.
- **Short note:** one useful, bounded finding with a source or reproduction.

## Prioritized backlog — ideas, not published articles

Impact and originality use qualitative High/Medium labels. Priority accounts for usefulness, differentiation and the amount of evidence still needed. No proposed experiment below has been run as part of this redesign.

| Priority | Proposed article | Format | Impact / originality | Evidence needed before publication |
| --- | --- | --- | --- | --- |
| P1 | Measuring What an Agent Actually Completed | Deep dive | High / High | Small inspectable task fixture, state-based grader, transcript/outcome counterexamples |
| P1 | Building an Evaluation Harness for AI Agents | Build note | High / High | Working repository, pinned models/tools, repeatable dataset, grader tests, repeat trials |
| P1 | Before Adding a Second Agent: What Should We Measure? | Decision record / follow-up | High / Medium | Baseline and candidate protocol; results only after controlled experiments |
| P1 | Designing Safer Tool Calls with Human Approval | Build note | High / High | Threat model, permission boundaries, denial/replay tests and approval UI behavior |
| P2 | Why Retrieval Fails Before Generation Begins | Deep dive | High / High | Labeled relevance set, chunking/retrieval trace examples, recall/error analysis |
| P2 | Tracing Agent Workflows Without Losing Context | Build note | High / Medium | Instrumented example, trace propagation, redaction and failure cases |
| P2 | Cost per Completed Task in Multi-Agent Systems | Experiment | High / High | Actual bills/usage, retries and handoffs, completion checks, fixed budgets, variability |
| P2 | A Practical Checklist for Production RAG | Decision record | High / Medium | Worked example, retrieval and answer evaluation, access controls, refresh tests |
| P2 | Failure Modes in Agentic Workflows | Failure note | High / High | Reproduced failures and traces; clearly label simulated cases |
| P3 | When a Workflow Graph Earns Its Complexity | Decision record | Medium / High | One explicit state machine versus loop, checkpoint/recovery tests, maintenance trade-offs |
| P3 | MCP Trust Boundaries: What the Tool Description Cannot Authorize | Research / build note | High / High | Current primary protocol/spec sources, concrete threat model, isolated adversarial fixtures |
| P3 | Retry Budgets and Stopping Rules for Agent Loops | Short / build note | Medium / High | Convergence and repeated-failure examples, bounded retries, recorded latency and token use |

Build evidence gradually: a task fixture and independent grader can support subsequent evaluation, tracing and cost articles. Publish a methodology or open question if results are unavailable. No target cadence requires filler or serial AI-generated articles.

## Writing and review standard

Use clear technical English. Start with the engineering problem and include only the context needed to understand the decision. Use the sequence problem → constraints → baseline → alternatives → implementation → evaluation → observations → failures → trade-offs → references when it suits the format; it is not a mandatory heading template.

Keep original measurements, external results, opinions and illustrative examples distinct. Give study conditions with any external number; never turn relative changes into percentage points or token usage into cost without justification. Cite primary sources adjacent to claims. Explain uncertainty and sample limitations. Disclose meaningful AI help. Do not invent personal experience, experiments, incidents or performance claims.

Use `templates/post.md` and the [publishing checklist](publishing-checklist.md). Proposals remain in this document until their evidence exists and the owner elects to publish.
