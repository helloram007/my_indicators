# Repository instructions

## Branch and folder for each workstream

- Before starting a new feature, indicator, strategy, or other workstream, create a dedicated Git branch and a dedicated top-level folder.
- Use the branch and folder names provided by the user. Otherwise choose concise, descriptive names based on the workstream.
- Create the branch from the repository's default branch unless the user specifies another starting point.
- When continuing an existing workstream, reuse its branch and folder instead of creating duplicates.
- Keep all workstream code, documentation, tests, examples, research, and supporting assets inside its dedicated folder. Subfolders are allowed.
- Keep repository-wide instructions such as this `AGENTS.md` at the repository root. Change shared root configuration only when necessary for the workstream.
- Do not move or overwrite unrelated existing work to enforce this convention.
- Example: a new momentum indicator uses branch `momentum` and folder `momentum/`, with code in `momentum/src/` and documentation in `momentum/docs/`.

## Supply and demand workstream

- Use branch `snd` and folder `supply_and_demand/` for the Supply & Demand Trading strategy.
- Store all code and documentation for this workstream inside `supply_and_demand/`, including requirements, design notes, trading rules, research, tests, reports, examples, and supporting assets.
- Update existing files where appropriate; create new files or subfolders there when needed.
- Example: place a market-structure design at `supply_and_demand/market-structure-design.md`.
- Apply these conventions even when a request does not repeat the branch or folder name.
