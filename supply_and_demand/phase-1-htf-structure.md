# Phase 1: 4H structure and bias

Status: initial Pine Script v6 implementation; TradingView compilation and replay validation pending.

## Use

Open `src/htf_structure.pine` in TradingView Pine Editor, save it, and add it to a standard 4-hour candle chart. Other timeframes and synthetic charts are rejected. Default pivot settings are two left bars and two right bars. This first increment runs directly on 4H; projecting its confirmed state onto 1H/15m is a later integration step.

## Deterministic rules

- Only completed candles can update state or emit events. A pivot becomes available after its configured right-side bars complete.
- Compare each confirmed pivot high with the previous confirmed pivot high: higher is HH, lower is LH, equal is EH. Compare lows similarly: HL, LL, or EL. The first high/low is H/L.
- Labels are drawn on the confirmation candle, at that candle's high/low. They are not drawn back on the earlier pivot candle. Step lines show the actual confirmed pivot prices.
- Initial bias is neutral. HH plus HL establishes bullish bias; LH plus LL establishes bearish bias. Equal or mixed comparisons do not establish a direction. Once established, bias persists until an opposing close breaks structure.
- A strict close above the latest unbroken confirmed swing high is an upward break. A strict close below the latest unbroken confirmed swing low is a downward break. Wick penetrations and closes exactly on the level do not qualify.
- A break in the current bias direction emits BOS. A break against it emits CHoCH and sets transitional bias. Breaks while neutral or transitional do not emit either classification.
- A level is consumed on its first qualifying close; subsequent closes beyond it cannot repeat the event. Each newly confirmed pivot installs a new level. If that level is already beyond the current close in its break direction, mark it consumed immediately without a retroactive event.
- Process breaks against previously available levels before installing newly confirmed pivots on the same candle.
- After CHoCH, require both a high and low newly confirmed after the transition candle before resolving direction. HH/HL can resolve bullish; LH/LL can resolve bearish. The relevant opposing level must remain unbroken. This is a conservative initial design choice.
- If stale/inverted high and low levels both break on one close, consume both and set transitional bias without a directional event.

These are local confirmed pivot rules, not a full protected-swing or external/internal structure model. They are an initial interpretation of the requirements and require chart review. A bullish/bearish background reports structure only; zone alignment and trade permission remain unimplemented.

## Display

Green background: bullish. Red: bearish. Orange: transitional. Gray: neutral. The Data Window exposes numeric bias (1, -1, 2, 0). Configure TradingView alerts once per bar close. Only the latest 500 swing labels are retained by TradingView; this display limit does not reset state.

## Acceptance checks in TradingView

1. Compile under Pine v6 and confirm a standard 4H chart loads; 1H and Heikin Ashi must show the chart restriction error.
2. In Bar Replay, stop before a candidate pivot has two right candles: no pivot label or level change should appear yet. Advance through confirmation and verify the label appears on the confirmation candle.
3. Observe HH/HL and LH/LL sequences establishing bullish and bearish bias respectively. First pivots and equal pivots must not establish direction alone.
4. With bullish bias, wick below a confirmed low then recover: no CHoCH. A completed close below that low must emit exactly one bearish CHoCH and set orange background. Check the bearish mirror case.
5. Continue closing beyond the same broken level: no repeated event. A new confirmed level can support a new event.
6. Verify a same-direction close break emits BOS. Confirm that CHoCH does not immediately reverse the bias and that both new high/low confirmations are required to resolve transition.
7. Reload the same symbol/session/history and compare closed-bar events with replay. Record symbol, session, pivot inputs, event times, and any mismatch.

## Validation record

- Repository whitespace check: passed before commit.
- Static inspection: state mutations are inside `barstate.isconfirmed`; no security requests, negative plot offsets, or historical label placement are used.
- No Pine compiler is installed in this workspace. No TradingView compilation, live/replay test, or profitability backtest has been performed. Acceptance checks above are pending, not passed.

## Next increment

Validate Phase 1 in TradingView, then add Phase 2 zone detection using the existing requirements. Add HTF projection for lower-timeframe use after the native 4H output is accepted.

Technical reference: [TradingView bar states](https://www.tradingview.com/pine-script-docs/concepts/bar-states/).
