# Development

## Local Setup

```bash
python3 -m pip install -e ".[test,export]"
```

Run tests:

```bash
.venv/bin/python -m pytest -q
```

## Repository Layout

```text
src/pyoncoplot/                         package code
tests/                                   pytest suite
docs/                                    Markdown documentation
plans/                                   implementation plans
python_refactor_goal_sources/            gallery scripts and training source tree
python_refactor_goal_sources/config.yaml config-driven gallery run definitions
python_refactor_goal_sources/make_oncoplots.py direct oncoplot() gallery renderer
python_refactor_goal_sources/make_other_gallery_plots.py custom gallery renderers
python_refactor_goal_sources/goal_plots/ numbered source/reference plots
python_refactor_goal_sources/fuc_sources/ fuc source scripts and fixture rebuild helper
python_refactor_goal_sources/syntheitic_goal_data/ deterministic TSV/JSON gallery inputs
```

## Regenerate Gallery Inputs

```bash
python3 python_refactor_goal_sources/generate_synthetic_inputs.py
```

This rewrites deterministic non-fuc TSV/JSON files under:

```text
python_refactor_goal_sources/syntheitic_goal_data/
```

The generator reads output filenames and deterministic non-fuc generation
settings from `gallery_params.input_files` and
`gallery_params.synthetic_inputs` in `python_refactor_goal_sources/config.yaml`.

The AML and structural-variation fuc fixtures are rebuilt separately after
downloading the upstream `fuc-data` source files listed in
`python_refactor_goal_sources/fuc_sources/manifest.json`:

```bash
python3 python_refactor_goal_sources/fuc_sources/rebuild_fuc_fixtures.py --source-dir /path/to/fuc-data
```

## Regenerate Gallery Images

```bash
python3 python_refactor_goal_sources/recreate_gallery.py
python3 python_refactor_goal_sources/recreate_gallery.py --style comparison --preset brca_large
```

Generated gallery images are tracked when intentionally updated.

## Adding A Gallery Preset

1. Add or extend synthetic input settings in `python_refactor_goal_sources/config.yaml`, or fuc-derived inputs in `python_refactor_goal_sources/fuc_sources/rebuild_fuc_fixtures.py`.
2. Commit the generated TSV/JSON inputs.
3. Use `renderer: oncoplot` when public `oncoplot()` params can express the plot.
4. Add the named run to `python_refactor_goal_sources/config.yaml` under `gallery_params.plot_runs`.
5. Add a renderer function in `python_refactor_goal_sources/make_other_gallery_plots.py` only when `oncoplot()` and the existing custom renderers cannot express the plot.
6. Add or update tests in `tests/test_gallery.py`.
7. Document the preset in [Gallery](gallery.md).

The generic oncoplot renderer reads `params.oncoplot` from config and passes it
to the public API. Keep runtime choices such as genes, metadata tracks, legend
controls, expected dimensions, output names, and save DPI in YAML.

## Documentation Changes

Docs are Markdown-first. Keep examples runnable from the repository root unless
the page says otherwise.

After editing docs:

```bash
.venv/bin/python -m pytest -q
```

The docs test checks that required pages exist and that local Markdown links
resolve.
