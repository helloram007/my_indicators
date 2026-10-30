# Phase 1: HTF structure and bias

Status: reusable HTF library and standalone Pine v6 consumer; TradingView compilation and replay validation pending. See README.md for library setup, timing, and timeframe settings.

## Use

Open `src/htf_structure.pine` in TradingView Pine Editor and select Structure HTF. Use standard candles with chart timeframe equal to or below the selected HTF. Default pivot lengths are 2 left / 2 right source candles. See README.md for the monthly, weekly, daily, 4H and 1H configuration and shared-library API.

## Deterministic rules

- Only completed candles can update state or emit events. A pivot becomes available after its configured right-side bars complete.
- Compare each confirmed pivot high with the previous confirmed pivot high: higher is HH, lower is LH, equal is EH. Compare lows similarly: HL, LL, or EL. The first high/low is H/L.
- Swing labels are anchored to the original pivot candle timestamp and price, but are created only after confirmation. BOS/CHoCH labels identify the source break candle. Bias and step lines update on completed-snapshot delivery and are not backdated. See README.md for the intentional delivery delay.
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

## Acceptance checks and validation

Use the current checklist in README.md. The previous 4H-only restriction and confirmation-candle label placement have been superseded. Replay must distinguish the candle an annotation identifies from the later time it becomes available.

Source-contract tests verify generated consumer consistency, source timestamp placement, completed-snapshot offsets, and event deduplication wiring. They do not compile Pine or prove market behavior. TradingView compilation, replay, import parity, and cross-timeframe comparison remain pending.

## Next increment

Validate this HTF module in TradingView, then add Phase 2 supply/demand zone detection as a separate consumer of the shared structure core.
