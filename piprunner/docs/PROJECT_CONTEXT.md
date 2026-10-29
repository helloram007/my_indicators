# Project context and handover

Last updated: 29 October 2026.

## User goal

Build a TradingView hybrid trading indicator/strategy feature by feature. End-of-P2 governs the multi-timeframe process; selected Piprunner components are optional A/B experiments. The user wants chart annotations that explain every required checklist item and train visual recognition, with controls to reduce or disable annotations later.

## Confirmed scope

- Platform: TradingView, explicitly confirmed by the user on 29 October 2026.
- Repository: `https://github.com/helloram007/my_indicators`; project directory: `piprunner/`.
- Architecture: 4H bias, 1H setup, 15m structure and entry.
- Preserve 15m CHoCH → separate swing break → retest → signal candle → entry one tick beyond the signal candle.
- Preserve three-bar expiry, stop beyond retest extreme, minimum 2R opportunity, 50% TP1 and runner. Exact unresolved interpretations remain OPEN.
- EMA36/100 and Williams Fractals are optional; hiding annotations never changes decisions.
- Start with 4H Bias in depth, with non-repainting structural rules and tests.
- Store durable context in GitHub so future assistants can continue without asking for the entire conversation again.

## Current implementation status

Documentation foundation is present: requirements, editable Word copy, feature roadmap and AI handover files. No executable indicator, order engine or strategy has been implemented. No Pine compilation, TradingView chart replay or empirical backtest has been performed. Existing Piprunner/End-of-P2 source scripts have not been supplied.

The Word copy could not be visually rendered because the renderer was unavailable. `requirements.md` is the reviewable design text. Later platform confirmation and progress are recorded here and in DECISIONS; the older requirements section D02 asking to choose a platform is superseded by decision D-001. Its other feed/session questions remain open. Do not treat the Word copy as a current progress ledger.

## First implementation to build

Create a Pine v6 4H Bias indicator in `src/`, with tests/reference fixtures in `tests/`. Implement candidate B4H v0 from requirements Sections 3–5, explicitly labelled PROPOSED. Do not enable orders or claim the user has approved its structural behavior.

Candidate summary: strict confirmed L/R pivots (proposed default 2/2), independent high/low lists, two highs and two lows for classification, HH+HL bullish and LH+LL bearish, mixed structure neutral, insufficient data unknown. Close-based protected-level invalidation wins over same-update pivot classification; rearming needs fresh evidence. Verify full details in the requirements before coding.

Include AN01–AN04 and a checklist shell for later stages, plus Training/Guided/Minimal/Off visibility. Distinguish origin/confirmation/publication time. Pending features cannot show PASS. Reference tests B01–B14 and annotation tests A02–A06; B15 needs chart review. Pine compilation and replay are separate verification gates.

## Still open

Approval of the 4H candidate and feed/session boundaries; SPA/P2/zone/FVG definitions and mandatory status; precise 15m structure, retest and candle predicates; expiry inclusivity; stop buffer; meaning of minimum 2R; target and runner policy; sizing, costs and test datasets. Read the complete decision register D01–D11 in requirements.

## Continuation routine

1. Read repository/project instructions and these context documents.
2. Inspect current branch, status, recent commits and actual source/tests. Repository state can be newer than this handover.
3. Continue the first incomplete roadmap item. Platform is already confirmed; do not ask again.
4. Record verification honestly and update this handover plus the roadmap and decisions as appropriate.

## Source provenance

User requests in this development chat establish the confirmed scope above. The earlier discussion was titled `Analyse Strategy Integration`, conversation ID `6ae359fc-2d4c-83eb-a580-3d277ef48ff1`. Its assistant recommendations were proposals, not user approvals. The repository documents are intended to be self-contained; access to that chat is not required to continue.
