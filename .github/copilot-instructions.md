Project: adivina_el_numero — notes for AI coding agents

Short goal
- This repository appears to be a very small Python CLI game named "adivina_el_numero" (guess the number). The only source file at the root is `app.py`, which currently contains author comments.

Why this guidance exists
- The project is minimal and single-file. Keep changes small, clear, and self-contained. When adding behavior prefer creating small modules under the repository root (for example `game.py`, `cli.py`) and keep `app.py` as the entrypoint that wires them together.

How to run (discovered from workspace)
- Use the project's root Python to run the program. On Windows (PowerShell):

  python app.py

Key file(s)
- `app.py` — current entrypoint. It contains only header comments now; treat it as the main CLI bootstrap.

Conventions & patterns to follow (repo-specific)
- Single-file CLI: use a main guard in `app.py`:

  if __name__ == "__main__":
      main()

- Prefer clear separation: put game logic in a `game.py` module and CLI / I/O in `cli.py`. This keeps automated tests easy and the entrypoint minimal.
- Use Spanish-language docstrings or comments if adding user-facing text in Spanish (the repository authors use Spanish names). Internal identifiers may be English or Spanish — be consistent with surrounding code.

Testing and development workflow (inferred)
- No tests are present. If you add tests, place them under a top-level `tests/` directory and use `pytest`.
- Recommended quick dev cycle on Windows PowerShell:

  python -m pip install --user pytest
  pytest -q

Integration and external dependencies
- No external dependencies are detected. If you add a dependency, add a `requirements.txt` with pinned versions and update README with install steps.

Editing and commit guidance for AI
- Make minimal, self-contained commits with descriptive messages (e.g., "Add game logic module and wire in app.py").
- When refactoring move logic out of `app.py` into new modules and update imports. Avoid changing global behavior unless adding tests that require it.

Examples from this repo to reference
- `app.py` — use as the canonical entrypoint. If you add a `game.py`, reference it in `app.py` with a simple import and call:

  from game import jugar
  
  def main():
      jugar()

Edge cases and things NOT to assume
- Do not assume there is a web server or packaging (this is a CLI script). Do not add frameworks (Flask, Django) unless the user asks.
- Don't assume tests, CI, or linters are configured — if you add them, include config files (`pyproject.toml`, `.github/workflows/...`) and document the change.

What to ask the maintainer if uncertain
- Preferred language for user prompts (Spanish vs English).
- Whether `app.py` should remain the single-file entrypoint or be converted into a package layout.

If you update this file
- Preserve the top-level intent: keep guidance short, actionable, and tied to the actual files in the repository. Avoid generic, non-actionable suggestions.

End of guidance
