# Installation

## Development Install

From the repository root:

```bash
python3 -m pip install -e ".[test,export]"
```

The package requires Python `>=3.9`.

## Runtime Dependencies

`pyoncoplot` depends on:

- `numpy`
- `pandas`
- `plotly`
- `matplotlib`

The `test` extra installs `pytest`.

The `export` extra installs `kaleido`, which is needed when writing Plotly
figures directly to image formats such as PNG. Plotly HTML export does not need
Kaleido.

Installing only `pytest` is not enough to run the local suite: the test modules
also import the runtime dependencies above. Use the development install command
so `pandas`, `numpy`, Plotly, Matplotlib, and the test tools are available in the
same environment.

## Verify The Install

```bash
python3 - <<'PY'
import pyoncoplot
print(pyoncoplot.__all__)
PY
```

Run the test suite:

```bash
.venv/bin/python -m pytest -q
```

## Next Step

Continue with the [Quickstart](quickstart.md).
