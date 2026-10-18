# RareGuard — project rules

## Always
- Type hints on public functions
- Module docstring: Purpose / Invariants / Why / References
- Every model metric logged to `runs` (Supabase or local `runs.csv`)
- Chronological splits with embargo, manifest committed
- Scalers/encoders fit inside Pipeline, train fold only
- Report recall@FPR, never bare accuracy
- Parameterise every threshold, window size, hyperparameter

## Never
- Commit data, `.env`, or model binaries
- Fit any transform on validation or test
- Add dependencies without asking
- Narrating comments (`# import pandas`)
- Em dashes in prose; buzzwords ("delve", "leverage", "robust", "seamless")
- Silently choose a threshold or window size

## Project facts
- MetroPT-3: 0.1 Hz sampling, 4 failures, regime = COMP==0
- BAF: 8 months (month 0–7), month-based splits, 5 categoricals, -1 sentinels
- Core frozen at v0.3.0 after Gate G2
- MVP cutoff: W12. Ship the small version, extend later.
- **Python:** CI runs 3.11, Colab runs 3.13 — check both when adding dependencies

## Commands
- `pip install -e ".[dev]"` — install
- `python scripts/fetch_data.py` — download datasets
- `pytest -v` — run tests
- `ruff check src tests` — lint
