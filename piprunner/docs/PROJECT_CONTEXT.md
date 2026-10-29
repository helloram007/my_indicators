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

Latest display is **UI 0.9**. Protected 4H labels explain `breached, await 4H close` when current chart price is beyond protection; toggle defaults on. Display-only: no change to bias, protected price or event rules. Swing notation remains 4SH/HH etc. All three independent proposed structure layers exist, colored by timeframe, with large BOS/CHoCH and horizontal levels. 1H is available only on 1H/15m, and 15m only on 15m. See ANNOTATION_STYLE and timeframe documents.

User explicitly confirmed protection updated after the 4H candle closed in their example. This is a successful observed single transition, not full replay acceptance. Next actual strategy feature is 4H location and 1H P2/SPA qualification. User clarified SPA = Strong Price Action and confirmed end of P2, either S/R OR S/D plus any one directional pin/engulfing/piercing pattern. S/D invalidates on ANY far-edge wick breach, independent of the close-confirmed structural bias. The supplied course was reviewed; `LOCATION_SPA_SPEC.md` records confirmed intent and proposed mechanical detectors. Exact zone automation, pattern thresholds/contact, S/R invalidation and bearish piercing counterpart remain open. Do not treat proposed thresholds as user-approved rules.

Source stays `src/piprunner_4h_bias.pine`. Run `python -m unittest discover -s piprunner/tests -v`: 21 reference tests pass. Source comparison confirms shared snapshot, existing 4H/1H request/render blocks and 11 audit outputs unchanged. These checks do not execute Pine. UI 0.5 is visible in the latest user screenshot and user reports a clear view; record partial runtime/presentation acceptance only. UI 0.9 compilation and full three-layer replay/visual checks remain pending; source comparisons verify snapshot and 16 numeric audit outputs unchanged. No orders, retest, signal-candle entry, P2/SPA qualification or empirical backtests exist. Existing strategy scripts have not been supplied.

Presentation preferences are in ANNOTATION_STYLE: horizontal lines, distinct timeframe colors, Large BOS/CHoCH text by default. UI_02/UI_03 preserve earlier presentation history; DECISIONS records rule ownership.

The Word copy could not be visually rendered because the renderer was unavailable. `requirements.md` is the reviewable design text. Later platform confirmation and progress are recorded here and in DECISIONS; the older requirements section D02 asking to choose a platform is superseded by decision D-001. Its other feed/session questions remain open. Do not treat the Word copy as a current progress ledger.

## First implementation to build

The Pine v6 source and reference fixtures have now been written. Next: review LOCATION_SPA_SPEC, settle the zone detector and pattern mechanics, then implement causal zone lifecycle and candle detectors before connecting setup gates. UI 0.9 can be loaded to review provisional-breach text; outstanding broader replay checks remain open. Keep candidate B4H v0 explicitly labelled PROPOSED. Do not enable orders or claim the user has approved its structural behavior.

Candidate summary: strict confirmed L/R pivots (proposed default 2/2), independent high/low lists, two highs and two lows for classification, HH+HL bullish and LH+LL bearish, mixed structure neutral, insufficient data unknown. Close-based protected-level invalidation wins over same-update pivot classification; rearming needs fresh evidence. Verify full details in the requirements before coding.

Include AN01–AN04 and a checklist shell for later stages, plus Training/Guided/Minimal/Off visibility. Distinguish origin/confirmation/publication time. Pending features cannot show PASS. Reference tests B01–B14 and annotation tests A02–A06; B15 needs chart review. Pine compilation and replay are separate verification gates.

Known implementation limits: chart support restricted to standard 15m/1H/4H; native feed sessions; malformed OHLC latches UNKNOWN until corrected-data reload; missing-session detection and automatic recovery not implemented. Initial annotation controls are a subset of the full future design. See `4H_BIAS.md` for precise supported controls and outstanding acceptance tests. Complete event export remains pending; numeric audit plots are present.

## Still open

User chart review 001 is recorded in `CHART_REVIEW_001.md` (snapshot https://www.tradingview.com/x/JPaT4zMi/). Indicator output is visible on 4H/1H/15m, with matching current bearish state, evidence pairs, 13:00 UTC confirmation and 1.33386 protection. Treat this as user-provided execution/partial visual evidence, not independent exact-revision compilation or replay validation. Current 4H is open above protection; waiting for its close is consistent with the rule. Readability issues: checklist covers candles, confirmation labels overlap, pivot-side colors can confuse trend interpretation. UI 0.3 resolved the main clutter concern according to later user feedback; UI 0.4 enlarges event text. Closed-bar/replay checks remain open; do not change model rules based on one image.

Approval of the 4H candidate and feed/session boundaries; automated zone formation and S/R invalidation, FVG status, numeric SPA/contact definitions and bearish piercing counterpart; precise 15m structure, retest and candle predicates; expiry inclusivity; stop buffer; meaning of minimum 2R; target and runner policy; sizing, costs and test datasets. Read the complete decision register D01–D11 in requirements.

## Continuation routine

1. Read repository/project instructions and these context documents.
2. Inspect current branch, status, recent commits and actual source/tests. Repository state can be newer than this handover.
3. Continue the first incomplete roadmap item. Platform is already confirmed; do not ask again.
4. Record verification honestly and update this handover plus the roadmap and decisions as appropriate.

## Source provenance

User requests in this development chat establish the confirmed scope above. The earlier discussion was titled `Analyse Strategy Integration`, conversation ID `6ae359fc-2d4c-83eb-a580-3d277ef48ff1`. Its assistant recommendations were proposals, not user approvals. The repository documents are intended to be self-contained; access to that chat is not required to continue.
