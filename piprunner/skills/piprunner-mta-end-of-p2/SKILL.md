---
name: piprunner-mta-end-of-p2
description: Develop, review or explain Piprunner + MTA-End-of-P2, adding a confirmed 15m Williams Fractal continuation gate while preserving the full End-of-P2 entry and risk rules.
---

# Piprunner + MTA-End-of-P2

Use this skill for this named indicator's requirements, implementation, chart teaching and tests. This is an instruction skill, not executable Pine code or a market feed.

## Establish scope

Locate the user's checkout of https://github.com/helloram007/my_indicators. Read root/project AGENTS.md, then piprunner/docs/INDICATOR_SPLIT.md, PROJECT_CONTEXT.md, DECISIONS.md, roadmap.md and PIPRUNNER_MTA_END_OF_P2_REQUIREMENTS.md. Read DASHBOARD_WORKFLOW.md for panel work. Inspect actual source/tests before declaring features implemented. Current branch and path must be verified, not hardcoded.

Read [references/contract.md](references/contract.md) for the portable shared and product-specific contract. It is a 5 November 2026 snapshot; newer explicit user corrections and repository decisions supersede it. If the checkout is unavailable, explain using the reference but mark code status unverified. Do not require the other product's skill to understand this one.

## Preserve rule ownership

Treat CONFIRMED, PROPOSED and OPEN separately. A successful test or chart display is not approval of a proposed trading model. Preserve 4H priority, 1H S/R OR S/D plus directional SPA, and the distinct 15m CHoCH → swing break → retest → signal candle sequence. Entry is one tick beyond that signal candle; stop beyond retest extreme; three-bar expiry; minimum 2R; 50% TP1 and runner. Undefined mechanics must remain visibly undefined rather than guessed.

Use each zone's own finalized timeframe close beyond the 30% full-base-range buffered invalidation level. Wick-only/equality do not invalidate. This buffer never replaces retest-based trade stops. Do not substitute original Piprunner's one-pip entry, opposite-fractal stop or 1R target.

## Combined boundary

The user CONFIRMED an additional 15m Williams Fractal confirmation gate, preserving every baseline entry stage and risk rule. This gate is not implemented: existing generic 15m pivots and research BOS/CHoCH do not satisfy it. Require full continuation structure: original long precursor HH/HL then confirmed LH high fractal; short precursor LH/LL then confirmed HL low fractal. Default 2/2 comes from the supplied description; exact equality, ordering, candidate lifecycle and same-setup timing remain OPEN.

The proposed final gate check before ARMED is not yet approved. Do not invent whether late fractal confirmation extends/restarts the three-bar clock or whether price must additionally break the fractal. Resolve only decisions needed by the requested feature. With the gate off, label baseline comparison and reproduce baseline decisions. EMA36/100 filtering is independent and optional; visible EMA plots do not activate it.

## Build, explain and verify

Develop the requested feature within piprunner/, preserving the other product's decisions. Keep shared algorithm versions aligned and instance state isolated. Existing src/piprunner_4h_bias.pine is a legacy research prototype, not two finished indicators. Changes to skills/docs alone do not implement trading features.

Never backdate actionable pivots: distinguish origin, right-bar confirmation and publication. Use finalized HTF snapshots and reject stale parent setup evidence. Record reason, source timeframe, evidence IDs and setup linkage. Do not infer same-bar order fills or post-fill exits from unresolved policy.

Provide configurable horizontal and vertical dashboards over the same snapshot with every step, timeframe, status, reason and evidence. Keep implementation readiness separate from live PASS/WAIT/BLOCKED/UNKNOWN/UNDEFINED. Display toggles/layouts never alter calculations. Preserve horizontal levels, SH/SL slash classifications, larger BOS/CHoCH and configurable 4H teal/red, 1H blue/orange, 15m fuchsia/yellow colors.

Test causal publication, invalidation timing, missed/reordered stages, mirrored directions, optional-gate isolation, layout/display parity and replay/reload. Report local reference tests separately from actual Pine compilation/rendering/replay and empirical backtests. Update product requirements, context, decisions and roadmap after meaningful work. The skill grants no standing authorization to publish, route trades or change accounts.

For chart teaching, walk 4H → 1H → 15m, explaining each evidenced gate and open candle. Distinguish current structure annotations from qualified setup/entry signals; insufficient images cannot establish unseen confirmations.
