# Pine compiler reports

## 30 October 2026 only diagnostic plot visible

User screenshot of UI 1.0.2 Style tab contains only Source diagnostic close, with no audit plots or graphic-object controls. This is inconsistent with the full delivered source, which has 21 top-level plots and object drawings. Local .pine, .txt and repository copies were checked as complete and identical. Incomplete pasted/compiled source or a stale/different chart instance is strongly suspected but not proven without the exact editor contents. Do not tell the user to keep changing visibility settings as the primary remedy.

The header diagnostic plot allowed a header-only excerpt to compile, masking incomplete source. UI 1.0.3 removes that near-header output and places the diagnostic output at the end (`Complete source loaded`). Full source still contains all 21 outputs and unchanged calculations. New full .pine/.txt copies have 667 physical lines (verify delivered file if regenerated). Use the complete text file opened locally, Select All/Copy, then Select All/Paste in a new Pine Editor indicator, save and Add to chart. Remove old instances only after identifying them. Confirm final marker and UI 1.0.3 title. If the problem persists with full source present, obtain the editor export and all errors; do not claim a confirmed fix or full Pine compilation from source checks.

## 30 October 2026 CE10213

User reported “The script must have at least one output function call”. Exact TradingView editor content was not supplied. The delivered UI 1.0 .pine and Git source had identical SHA256 and 20 top-level plot calls, including a chart protection plot and Data Window outputs. The missing-output cause is not established; incomplete paste or compiling different editor content is a possibility, not a verified diagnosis.

UI 1.0.1 adds an explicit `plot(close, title="Source diagnostic close", display=display.data_window)` immediately after the indicator declaration. Existing outputs, structural logic, zone detection and SPA logic remain unchanged. This is a diagnostic delivery improvement, not proof the reported error has been fixed in TradingView. The added output appears only in Data Window. Source ends with `// END OF COMPLETE PIPRUNNER SCRIPT UI 1.0.1`.

Load a NEW indicator in Pine Editor, select all existing text, replace with the full source, and verify the version header, indicator title, near-header plot and final marker. Do not copy a GitHub webpage including line numbers or only a source excerpt. Save and Add to chart. If the error persists with these markers present, obtain the complete editor source and all compiler errors before guessing at unrelated logic changes. Platform compilation remains pending until observed.
