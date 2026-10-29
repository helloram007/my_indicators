# Multi timeframe annotation style

## UI 0.8 combined swing and structure codes

User requested slash notation, for example **4SH/HH**. Temporary swing names now include actual classification: 4SH/HH or 4SH/LH, 4SL/HL or 4SL/LL, and the corresponding 1SH/1SL and 15SH/15SL forms. Initial/equal references display H/L or EH/EL truthfully (for example 1SH/H or 15SL/EL). Do not invent a higher/lower relationship without evidence. Prices, status, colors and logic stay unchanged. The existing toggle still restores the previous timeframe/structure text when off. This supersedes UI 0.7's code-only display. TradingView checks for UI 0.8 remain pending.

## UI 0.7 temporary swing names

CONFIRMED user request: label the current confirmed swing-high and swing-low levels **4SH / 4SL**, **1SH / 1SL**, **15SH / 15SL**. The new `Temporary swing names` input defaults on; disable it to restore HH/HL/LH/LL text. Actual structural comparisons remain available in level tooltips. Prices, protection/broken status, colors and large BOS/CHoCH labels remain unchanged. In these codes SL means Swing Low, not an order stop-loss.

These names apply to the existing current reference levels; no unconfirmed swings or extra historical bubble labels are introduced. The 4H legacy origin labels also use 4SH/4SL when enabled. Display availability is unchanged: 4H levels on all supported charts, 1H on 1H/15m, and 15m on 15m only. Structure calculations and audit plots are unchanged. Source checks pass; TradingView visual/compilation checks for UI 0.7 remain pending.

## Confirmed user preferences

29 October 2026: user reviewed UI 0.3 as a clear/promising view, requested different colors when 1H and 15m structure annotations are added, and larger BOS/CHoCH text everywhere those events appear. This is presentation feedback, not approval of the proposed structural model or unresolved entry predicates.

- Keep the horizontal-level presentation as the default.
- Distinguish 4H, 1H and 15m structure layers by color, not just their chart interval.
- Retain explicit timeframe prefixes so color is never the only distinction.
- Use a separate event-text size control for every future BOS/CHoCH renderer, default Large. General panel/swing text stays independently configurable.
- Expose per-timeframe colors. Do not reuse an indistinguishable palette across overlaid layers.

## Current delivery UI 0.4

Current 4H BOS/CHoCH and unclassified break labels use the new `BOS / CHoCH text size` input: Normal, Large (default), Huge. This only changes label presentation. Source title identifies UI 0.4. Replace source and save/update the TradingView chart to apply it.

The current 4H directional colors remain configurable teal/red. There is no 1H/15m structure engine yet and no inactive controls implying one exists. Current labels on all chart intervals still describe **4H** structure only.

## Proposed future palette

Before adding 1H/15m layers, use distinct configurable color families: 4H teal/red (existing), 1H blue/orange, 15m violet/yellow. These exact colors are proposed defaults, not user-selected colors. Maintain timeframe prefixes, direction arrows and BOS/CHoCH text independently of color. Check contrast on light and dark backgrounds and simultaneous layer readability. If colors are changed, ensure directional and timeframe meanings remain clear.

## Verification

UI 0.4 source comparison must preserve the entire structural calculation/snapshot and all six numeric audit plots. Local reference suite has 15 passing tests. Revised Pine compilation, larger-text overlap and multi-chart visual review remain pending. Do not change a break event's time or price just to accommodate its larger text.
