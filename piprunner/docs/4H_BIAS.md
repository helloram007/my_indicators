# First feature 4H Bias

Status: source implemented; local reference tests pass. Pine compilation, TradingView replay and visual acceptance remain pending. This is an indicator, not an order-generating strategy. Model B4H v0 remains PROPOSED.

## Load in TradingView

1. Open `piprunner/src/piprunner_4h_bias.pine` on the development branch and copy its full contents.
2. In TradingView, open a standard candlestick chart and its Pine Editor. Create a new indicator, replace its content and save.
3. Select **Add to chart** on a 15m, 1H or 4H chart. Other chart intervals and synthetic charts are deliberately rejected in this first version.
4. Start in Settings → Learning → **Training**. Keep left/right swing strengths at 2/2 for the initial review.
5. Record any compiler errors exactly. Successful local Python tests do not establish that TradingView accepts this Pine source.

## What to look for

- Confirmed 4H highs/lows appear as H/L initially, then HH/LH or HL/LL; equal same-side prices are EH/EL. Strict local ties disqualify pivot candidates.
- Two rising high/low pairs give BULLISH; two falling pairs give BEARISH; mixed pairs give NEUTRAL. Insufficient structure is UNKNOWN.
- Protection is the latest confirmed low in a bullish classification, or high in a bearish classification. A closed 4H break invalidates it. A wick or equal close does not.
- After invalidation, a rebound alone does not rearm bias. A new confirmed pivot is required. A newly confirmed pivot cannot override same-update invalidation.
- Independent swing lists can turn bias neutral during a pullback. This is the proposed model's behavior, not a claim that the user's discretionary trend has ended.
- The panel identifies later setup/entry modules as undefined or waiting. None can display a valid entry in this version.

## Timing and audit

The structural function runs in the 4H context. Each returned value is offset one 4H bar and requested with `lookahead_on`, so the developing 4H bar is never an input to the displayed snapshot. A pivot needs its configured right bars to close before confirmation.

The new snapshot is visible from the next available chart bar at the start of the next 4H period. After a market closure, actual chart publication can be later than source confirmation. On 4H charts this also uses the prior closed 4H bar. A future close-only execution module must log when it consumes the snapshot; it must not claim a fill earlier in that chart bar.

Origin labels are drawn on the historical pivot candle only after confirmation. Hover their tooltips for origin, confirmation and chart-publication times in UTC. Confirmation and state-event labels are anchored to the publication bar using the closed 4H price, not a moving live price. The Data Window exposes bias, version, confirmed time, protected price and latest high/low independently of visual settings. TradingView chart-data export can capture these numeric plots where that feature is available; a complete standalone event exporter is not implemented yet.

## Configuration

Current display is **UI 0.3**: horizontal structure levels and updating timeframe labels replace bubble history by default. See `UI_03.md` for proposed 4H BOS/CHoCH definitions, controls and current validation status. UI 0.2 below describes the retained Legacy labels option.

UI 0.2 adds a compact/opaque default panel, optional expansion of future checklist rows, structure-aware colors, deterministic label spacing and a developing-price explanation. See `UI_02.md` for settings and review steps. The descriptions below concern the available modes; Training no longer expands every future row by default.

Structure inputs change the research model and trigger recomputation. Learning inputs only change the presentation:

- Training: available checklist, swings, confirmation and state events; expand future rows separately.
- Guided: compact context rows, confirmation and state events; no origin labels.
- Minimal: state/next step panel and protected level.
- Off: no educational chart drawings or panel; numeric Data Window diagnostics remain available.

Additional switches hide the 4H layer, panel, origins, confirmations, bias labels, protection and invalidations. Text detail, size, colors, panel corner and retained labels are configurable. Presets set an upper visibility level; switches can hide items within that level. There is no automatic custom-preset storage, last-N-setup filter or per-row checklist visibility yet. Later modules will extend these controls. TradingView stores normal indicator input settings; use its reset controls to restore defaults.

Old labels are pruned at the selected limit, with a count in the panel. Only retained chart labels are bounded; historical numeric plots remain. AN01–AN04 are the implemented layer; AN05–AN18 are honest placeholders. No tentative pivot preview, EMA or 15m fractal module is implemented.

## Tests and remaining gates

Run `python -m unittest discover -s piprunner/tests -v` from repository root. Tests use only Python's standard library. The oracle is independent of Pine and does not execute the Pine source.

Ten tests cover B01/B02 pivot timing and failed candidates; B03 strict ties/equality; B04/B05 directional/mixed classification and raw-bar integration; B06/B07 invalidation/rearming; B08 priority; portions of B09/B10 deduplication, dual pivots and warm-up; and local B11/B12 prefix/reload parity. They also test a non-2/2 extractor setting. They do not close the complete B01–B14 platform acceptance gate.

Pending checks:

- Compile in TradingView and test max-history/input extremes.
- Replay identical feed history on 15m, 1H and 4H, checking publication alignment, no early origins, stable closed snapshots and no duplicated events.
- Verify market reopening, DST and missing-child-bar behavior (B13).
- Compare exported numeric ledgers with Training, Guided, Minimal and Off (A02/B14 visual independence). No EMA/fractal logic switches exist in this version.
- Inspect label/panel overlap, colors, pruning and all controls (A01/A03–A07).
- Review B15 annotated chart examples with the user and record disagreements before calling this an approved bias model.

## Explicit data limitations

Feed-native 4H sessions are used. Missing market bars cannot reliably be distinguished from scheduled closures in this version; no automatic gap inference or session-calendar recovery is claimed. Malformed OHLC latches UNKNOWN with DATA_ERROR_RELOAD_REQUIRED. Correct the source data and reload to rebuild from the available boundary; automatic repaired-history replay is not implemented. Starting history length and feed revisions can affect the reconstructed state and must be held fixed for parity comparisons.

These limitations keep the data-quality acceptance gate open. No financial performance, live-readiness or non-repainting platform validation is claimed until the relevant checks are performed.

## Official implementation references

- Confirmed higher-timeframe request pattern: https://www.tradingview.com/pine-script-docs/concepts/other-timeframes-and-data/
- Pine tables: https://www.tradingview.com/pine-script-docs/visuals/tables/
