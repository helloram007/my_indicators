---
name: piprunner-end-of-p2
description: Develop, review, or explain the user's TradingView Piprunner and End-of-P2 hybrid strategy, preserving multi-timeframe rules and distinguishing optional Williams Fractal signals from existing structure annotations.
---

# Piprunner + End of P2

Use this skill for this user's strategy implementation, chart teaching, requirements and testing. It carries strategy constraints, not live market data or an executable indicator.

## Load current project context

Locate the user's checkout of https://github.com/helloram007/my_indicators. Work within `piprunner/`. Do not assume a branch or machine-specific path. Read root/project AGENTS.md, then `piprunner/docs/PROJECT_CONTEXT.md`, `DECISIONS.md`, `roadmap.md`, and the relevant requirements. Inspect actual source and tests before stating implementation status. Read [references/strategy-contract.md](references/strategy-contract.md) for the portable rule baseline and original Piprunner signal.

If the checkout is unavailable, use the reference to explain rules, but mark implementation status unverified and request the relevant source for code-specific work. New explicit user corrections supersede older records; update the project decision log. Preserve CONFIRMED, PROPOSED and OPEN distinctions. Never turn an implementation default or a successful compile into trading-rule approval.

## Keep the three strategy roles distinct

- End-of-P2 baseline: 4H direction → 1H pullback completion → 15m CHoCH, separate swing break, retest and signal candle. Preserve its entries and risk/management rules.
- Optional hybrid experiments: EMA filtering, fractal-assisted structure and an additional fractal signal gate are independently specified and tested. A visible EMA is not an active filter.
- Original Piprunner comparator: Williams Fractal continuation signal with one-pip entry, opposite-fractal stop and 1R target. These rules do not replace the baseline's one-tick signal-candle entry, retest stop or minimum 2R.

**Critical status correction (5 November 2026): the original Piprunner 15m Williams Fractal signal has NOT been implemented.** The existing generic 15m pivots and research BOS/CHoCH are not that signal, even with 2/2 settings. Verify future code before changing this status. The user's correction identifies missing work; it does not itself select a hybrid entry replacement or approve unresolved signal mechanics.

## When developing a feature

Identify its timeframe, rule owner, dependencies and whether it affects logic or drawings. Implement the requested feature without silently filling unresolved trading predicates. Ask only for decisions needed by the feature; offer labelled proposals for exact mechanics.

Use finalized source-timeframe evidence. Distinguish pivot origin, confirmation and publication time. A retrospectively drawn pivot is not a signal available on the pivot bar. Configuration must separate calculation gates from display switches.

For fractal work, read the reference's pending decisions and tests first. Require the full continuation pattern, not every confirmed fractal. Preserve the HTF/setup gates in the hybrid. Publish confirmed candidate and waiting/blocked reasons; never label an unqualified candidate as an entry.

Preserve configurable horizontal levels, timeframe prefixes, swing classifications and larger BOS/CHoCH text. Keep 4H teal/red, 1H blue/orange and 15m fuchsia/yellow independently configurable. Provide confirmation-aware fractal annotations and a separate visibility switch when implementing that module.

Validate causal/state behavior with meaningful tests. Report local/reference tests separately from actual Pine compilation, chart rendering and replay. Maintain source completeness/end-marker checks when delivering scripts; a prior truncated editor copy compiled only EMAs and hid all annotations.

Update context, decisions and roadmap after meaningful work. Report what changed, what is still proposed/open, checks actually run and the next incomplete feature. This skill grants no standing permission to publish, place trades or change accounts.

## When explaining a chart

Walk from 4H to 1H to 15m. Explain each evidenced condition as met, waiting, blocked, unknown or unimplemented. State which candles are still open. Do not infer close-confirmed breaks, hidden patterns, exact timestamps or executable signals from an insufficient screenshot. Explain why a lower-timeframe move cannot override 4H direction, and why an open wick cannot invalidate a close-based zone.
