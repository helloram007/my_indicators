# Pine compiler reports

## 30 October 2026 CE10213

User reported “The script must have at least one output function call”. Exact TradingView editor content was not supplied. The delivered UI 1.0 .pine and Git source had identical SHA256 and 20 top-level plot calls, including a chart protection plot and Data Window outputs. The missing-output cause is not established; incomplete paste or compiling different editor content is a possibility, not a verified diagnosis.

UI 1.0.1 adds an explicit `plot(close, title="Source diagnostic close", display=display.data_window)` immediately after the indicator declaration. Existing outputs, structural logic, zone detection and SPA logic remain unchanged. This is a diagnostic delivery improvement, not proof the reported error has been fixed in TradingView. The added output appears only in Data Window. Source ends with `// END OF COMPLETE PIPRUNNER SCRIPT UI 1.0.1`.

Load a NEW indicator in Pine Editor, select all existing text, replace with the full source, and verify the version header, indicator title, near-header plot and final marker. Do not copy a GitHub webpage including line numbers or only a source excerpt. Save and Add to chart. If the error persists with these markers present, obtain the complete editor source and all compiler errors before guessing at unrelated logic changes. Platform compilation remains pending until observed.
