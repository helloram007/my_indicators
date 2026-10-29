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

Latest revision is now **UI 0.3**, superseding the UI 0.2 presentation below. User rejected bubble clutter and requested horizontal levels plus BOS/CHoCH/timeframe labels. `UI_03.md` defines the new proposed educational overlay: default two live 4H reference levels, small updating right-edge labels, three retained confirmed break segments, summary panel and configurable history/lines. Against prior bias is CHoCH, with prior bias is BOS, neutral/unknown is unclassified Break; closed crossing and one event per pivot only. This overlay does not change bias or implement 15m entry structure. All timeframe prefixes remain 4H. Fifteen local reference tests pass. Source isolation comparison confirms bias core and six audit plots unchanged. Revised Pine compilation and visual/replay verification remain pending. Next: load UI 0.3 with Horizontal lines + Summary and inspect on all three supported chart intervals.

Latest source display revision: UI 0.2. Read `UI_02.md` before chart review. Compact/opaque panel is default; future module rows expand separately; pivot colors reflect structure; label spacing uses fixed closed-4H ranges with deterministic lanes; live-price explanation never affects structural state. Structural calculation and six audit plots are unchanged from the initial source. Ten local reference tests pass; this revised Pine source has not been compiled or visually checked in TradingView. Next action: load UI 0.2 and validate readability plus audit parity on 4H/1H/15m, then replay invalidation/rearming. No next strategy module is implemented yet.

First feature source exists in `src/piprunner_4h_bias.pine`: proposed B4H v0, strict confirmed pivots, protection, learning presets and checklist shell. Ten independent Python reference tests pass via `python -m unittest discover -s piprunner/tests -v`. They do not compile or execute Pine. No Pine compilation, TradingView chart replay or empirical backtest has been performed. Existing Piprunner/End-of-P2 source scripts have not been supplied. No orders or later strategy modules are implemented.

The Word copy could not be visually rendered because the renderer was unavailable. `requirements.md` is the reviewable design text. Later platform confirmation and progress are recorded here and in DECISIONS; the older requirements section D02 asking to choose a platform is superseded by decision D-001. Its other feed/session questions remain open. Do not treat the Word copy as a current progress ledger.

## First implementation to build

The Pine v6 source and reference fixtures have now been written. Next: compile and add to a TradingView standard 15m/1H/4H chart, fix any compiler/runtime issues, then perform replay and annotation checks in `docs/4H_BIAS.md`. Keep candidate B4H v0 explicitly labelled PROPOSED. Do not enable orders or claim the user has approved its structural behavior.

Candidate summary: strict confirmed L/R pivots (proposed default 2/2), independent high/low lists, two highs and two lows for classification, HH+HL bullish and LH+LL bearish, mixed structure neutral, insufficient data unknown. Close-based protected-level invalidation wins over same-update pivot classification; rearming needs fresh evidence. Verify full details in the requirements before coding.

Include AN01–AN04 and a checklist shell for later stages, plus Training/Guided/Minimal/Off visibility. Distinguish origin/confirmation/publication time. Pending features cannot show PASS. Reference tests B01–B14 and annotation tests A02–A06; B15 needs chart review. Pine compilation and replay are separate verification gates.

Known implementation limits: chart support restricted to standard 15m/1H/4H; native feed sessions; malformed OHLC latches UNKNOWN until corrected-data reload; missing-session detection and automatic recovery not implemented. Initial annotation controls are a subset of the full future design. See `4H_BIAS.md` for precise supported controls and outstanding acceptance tests. Complete event export remains pending; numeric audit plots are present.

## Still open

User chart review 001 is recorded in `CHART_REVIEW_001.md` (snapshot https://www.tradingview.com/x/JPaT4zMi/). Indicator output is visible on 4H/1H/15m, with matching current bearish state, evidence pairs, 13:00 UTC confirmation and 1.33386 protection. Treat this as user-provided execution/partial visual evidence, not independent exact-revision compilation or replay validation. Current 4H is open above protection; waiting for its close is consistent with the rule. Readability issues: checklist covers candles, confirmation labels overlap, pivot-side colors can confuse trend interpretation. Next practical work is presentation improvements followed by closed-bar/replay checks; do not change model rules based on one image.

Approval of the 4H candidate and feed/session boundaries; SPA/P2/zone/FVG definitions and mandatory status; precise 15m structure, retest and candle predicates; expiry inclusivity; stop buffer; meaning of minimum 2R; target and runner policy; sizing, costs and test datasets. Read the complete decision register D01–D11 in requirements.

## Continuation routine

1. Read repository/project instructions and these context documents.
2. Inspect current branch, status, recent commits and actual source/tests. Repository state can be newer than this handover.
3. Continue the first incomplete roadmap item. Platform is already confirmed; do not ask again.
4. Record verification honestly and update this handover plus the roadmap and decisions as appropriate.

## Source provenance

User requests in this development chat establish the confirmed scope above. The earlier discussion was titled `Analyse Strategy Integration`, conversation ID `6ae359fc-2d4c-83eb-a580-3d277ef48ff1`. Its assistant recommendations were proposals, not user approvals. The repository documents are intended to be self-contained; access to that chat is not required to continue.
