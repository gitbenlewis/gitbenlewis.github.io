# Example Gallery

The gallery recreates reference-style oncoplot figures from deterministic local
inputs. Active goal plots are limited to figures that can be rendered directly
through the public `oncoplot()` API with `renderer: oncoplot`.

Runtime choices live in `python_refactor_goal_sources/config.yaml` under the
`gallery_params` block. `recreate_gallery.py` loads that YAML and renders clean
runs by passing `params.oncoplot` to public `oncoplot()`, including table
sources, gene choices, sample or mutation filters, metadata tracks, legends,
and layout options.

## Render The Clean Gallery

```bash
python3 python_refactor_goal_sources/recreate_gallery.py
```

Outputs are written to:

```text
python_refactor_goal_sources/generated_plots/clean/
```

## Regenerate Gallery Inputs

```bash
python3 python_refactor_goal_sources/generate_synthetic_inputs.py
```

This regenerates the deterministic non-fuc fixtures. The Python/fuc AML
fixtures are derived from upstream `sbslee/fuc-data` files with:

```bash
python3 python_refactor_goal_sources/fuc_sources/rebuild_fuc_fixtures.py --source-dir /path/to/fuc-data
```

Gallery inputs are checked in under:

```text
python_refactor_goal_sources/syntheitic_goal_data/
```

## BRCA Comparison Sheets

```bash
python3 python_refactor_goal_sources/recreate_gallery.py --style comparison --preset brca_large
python3 python_refactor_goal_sources/recreate_gallery.py --style comparison --preset brca_compact_complex
```

Comparison sheets contain two panels: the original source image and the clean
generated image.

Outputs are written to:

```text
python_refactor_goal_sources/generated_plots/comparison/
```

## Accepted Clean Baselines

The generated AML metadata plots are treated as approved clean baselines:

```text
python_refactor_goal_sources/generated_plots/clean/gen.goal_plot_11.png
python_refactor_goal_sources/generated_plots/clean/gen.goal_plot_12.png
python_refactor_goal_sources/generated_plots/clean/gen.goal_plot_13.png
```

Do not tune these toward the originals if it makes the generated versions worse.

## Presets

Goal plots are compactly numbered by source family: ggoncoplot/R oncoplot
examples first, other R-based oncoplot-style examples next, and Python/fuc AML
examples last.

| Preset | Output | Size | Notes |
| --- | --- | --- | --- |
| `brca_large` | `gen.goal_plot_01.png` | `3600 x 1800` | ggoncoplot/R large BRCA oncoplot |
| `ggoncoplot_readme_small` | `gen.goal_plot_02.png` | `672 x 480` | ggoncoplot/R small README oncoplot |
| `ggoncoplot_readme_basic` | `gen.goal_plot_03.png` | `7200 x 3000` | ggoncoplot/R README basic oncoplot |
| `ggoncoplot_readme_marginal` | `gen.goal_plot_04.png` | `7200 x 3600` | ggoncoplot/R oncoplot with marginal bars |
| `ggoncoplot_readme_metadata` | `gen.goal_plot_05.png` | `7200 x 3600` | ggoncoplot/R oncoplot with clinical metadata |
| `paper_gbm_oncoplot` | `gen.goal_plot_06.png` | `864 x 432` | ggoncoplot/R compact paper-style GBM oncoplot |
| `brca_compact_complex` | `gen.goal_plot_07.png` | `850 x 683` | other R-based paper compact BRCA oncoplot |
| `cssc_compact` | `gen.goal_plot_08.png` | `1400 x 700` | other R-based paper alteration matrix |
| `gbm_clinical_molecular` | `gen.goal_plot_09.png` | `1080 x 436` | other R-based paper GBM clinical/molecular heatmap |
| `aml_basic` | `gen.goal_plot_10.png` | `1080 x 720` | Python/fuc basic AML oncoplot |
| `aml_metadata_unsorted` | `gen.goal_plot_11.png` | `1080 x 720` | Python/fuc accepted clean baseline |
| `aml_metadata_sorted` | `gen.goal_plot_12.png` | `1080 x 720` | Python/fuc accepted clean baseline |
| `aml_metadata_survival` | `gen.goal_plot_13.png` | `1080 x 720` | Python/fuc survival-filtered AML baseline |

## Config-Driven Runs

Each `plot_runs` entry declares its renderer, output file, source goal plot,
expected size, run toggle, and renderer params:

```yaml
gallery_params:
  plot_runs:
    brca_large:
      run: true
      renderer: oncoplot
      style: clean
      output_name: gen.goal_plot_01.png
      goal_plot: goal_plot_01.png
      expected_size: [3600, 1800]
      params:
        oncoplot:
          data: {path: syntheitic_goal_data/brca_mutations.tsv, sep: "\t"}
          gene_col: gene
          sample_col: sample
          mutation_type_col: mutation_type
          include_genes: [PIK3CA, TP53, CDH1]
          options:
            width: 3600
            height: 1800
```

Generated outputs keep the zero-padded numbered naming convention:
`gen.goal_plot_NN.png` for generated plots and `compare.goal_plot_NN.png` for
comparison sheets.

## Input Families

| Family | Files |
| --- | --- |
| AML/fuc | `aml_mutations.tsv`, `aml_metadata.tsv`, `aml_tmb.tsv`, `aml_palette.json`, `aml_gallery_params.json` |
| BRCA | `brca_mutations.tsv`, `brca_metadata.tsv`, `brca_tmb.tsv`, `brca_palette.json` |
| CSSC | `cssc_mutations.tsv`, `cssc_tmb.tsv`, `cssc_palette.json` |
| GBM | `gbm_clinical_tracks.tsv`, `gbm_events.tsv`, `gbm_palette.json` |
| ggoncoplot README | `ggoncoplot_readme_mutations.tsv`, `ggoncoplot_readme_metadata.tsv`, `ggoncoplot_readme_tmb.tsv`, `ggoncoplot_readme_palette.json` |

## Related Examples

- [Metadata Example](examples/metadata.md)
- [BRCA Gallery Example](examples/brca-gallery.md)
