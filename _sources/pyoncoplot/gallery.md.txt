# Example Gallery

The gallery recreates reference-style plots from deterministic local inputs.
Generated images are written outside the reference image paths so originals stay
untouched.

Runtime choices live in `python_refactor_goal_sources/config.yaml` under the
`gallery_params` block. `recreate_gallery.py` loads that YAML once and dispatches
clean runs to `make_oncoplots.py` for direct public `oncoplot()` presets or to
`make_other_gallery_plots.py` for custom plots. Oncoplot-style presets use
`renderer: oncoplot` and keep public `oncoplot()` params under `params.oncoplot`,
including table sources, sample or mutation filters, titles, subplot labels,
legends, and layout options.
Input filenames are also declared there under `gallery_params.input_files`;
custom renderers read the TSV/JSON files from those configured names.
Deterministic non-fuc input-generation settings live in
`gallery_params.synthetic_inputs`.

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

This regenerates the non-fuc synthetic fixtures. The Python/fuc AML and SV
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
```

Comparison sheets contain two panels: the original source image and the clean
generated image.

Outputs are written to:

```text
python_refactor_goal_sources/generated_plots/comparison/
```

## Accepted Clean Baselines

The generated AML metadata plots are treated as approved clean baselines:

- `python_refactor_goal_sources/generated_plots/clean/gen.goal_plot_18.png`
- `python_refactor_goal_sources/generated_plots/clean/gen.goal_plot_19.png`
- `python_refactor_goal_sources/generated_plots/clean/gen.goal_plot_21.png`

Do not tune these toward the originals if it makes the generated versions worse.

## Presets

Goal plots are numbered by source family: ggoncoplot/R examples first, other
R-based paper examples next, and Python/fuc examples last.

| Preset | Output | Size | Notes |
| --- | --- | --- | --- |
| `brca_large` | `gen.goal_plot_01.png` | `3600 x 1800` | ggoncoplot/R large BRCA plot |
| `ggoncoplot_readme_small` | `gen.goal_plot_02.png` | `672 x 480` | ggoncoplot/R small README oncoplot |
| `ggoncoplot_readme_basic` | `gen.goal_plot_03.png` | `7200 x 3000` | ggoncoplot/R README basic oncoplot |
| `ggoncoplot_readme_marginal` | `gen.goal_plot_04.png` | `7200 x 3600` | ggoncoplot/R README oncoplot with marginal bars |
| `ggoncoplot_readme_metadata` | `gen.goal_plot_05.png` | `7200 x 3600` | ggoncoplot/R README oncoplot with clinical metadata |
| `ggoncoplot_package_mark` | `gen.goal_plot_06.png` | `125 x 144` | ggoncoplot/R package mark recreation |
| `ggoncoplot_interactive_snapshot` | `gen.goal_plot_07.png` | `1566 x 1036` | ggoncoplot/R static interactive snapshot |
| `ggoncoplot_comparison_table_jats` | `gen.goal_plot_08.png` | `800 x 513` | ggoncoplot/R compact comparison table |
| `lasso_select` | `gen.goal_plot_09.png` | `1408 x 922` | ggoncoplot/R lasso-selection scatterplot |
| `multimodal_selection_old` | `gen.goal_plot_10.png` | `7620 x 5204` | ggoncoplot/R multimodal linked panel |
| `multimodal_selection` | `gen.goal_plot_11.png` | `7620 x 5204` | ggoncoplot/R multimodal linked panel |
| `multimodal_selection_with_lasso` | `gen.goal_plot_12.png` | `2281 x 1520` | ggoncoplot/R multimodal panel with lasso |
| `paper_gbm_oncoplot` | `gen.goal_plot_13.png` | `864 x 432` | ggoncoplot/R compact paper-style GBM oncoplot |
| `brca_compact_complex` | `gen.goal_plot_14.png` | `850 x 683` | other R-based paper compact BRCA plot |
| `cssc_compact` | `gen.goal_plot_15.png` | `1400 x 700` | other R-based paper alteration matrix |
| `gbm_clinical_molecular` | `gen.goal_plot_16.png` | `1080 x 436` | other R-based paper GBM clinical/molecular heatmap |
| `aml_basic` | `gen.goal_plot_17.png` | `1080 x 720` | Python/fuc basic AML oncoplot |
| `aml_metadata_unsorted` | `gen.goal_plot_18.png` | `1080 x 720` | Python/fuc accepted clean baseline |
| `aml_metadata_sorted` | `gen.goal_plot_19.png` | `1080 x 720` | Python/fuc accepted clean baseline |
| `sv_panel` | `gen.goal_plot_20.png` | `1296 x 864` | Python/fuc structural-variation panel |
| `aml_metadata_survival` | `gen.goal_plot_21.png` | `1080 x 720` | Python/fuc survival-filtered AML baseline |

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
| SV/fuc | `sv_depth.tsv`, `sv_allele_fraction.tsv`, `sv_gene_models.tsv` |
| ggoncoplot README | `ggoncoplot_readme_mutations.tsv`, `ggoncoplot_readme_metadata.tsv`, `ggoncoplot_readme_tmb.tsv`, `ggoncoplot_readme_palette.json` |
| Multimodal paper | `paper_multimodal_samples.tsv`, `paper_multimodal_points.tsv`, `paper_multimodal_events.tsv`, `paper_multimodal_clinical.tsv`, `paper_multimodal_selection.tsv`, `paper_multimodal_palette.json` |
| Comparison table | `ggoncoplot_comparison_table.tsv` |

## Related Examples

- [Metadata Example](examples/metadata.md)
- [BRCA Gallery Example](examples/brca-gallery.md)
- [Structural Variation Panel](examples/structural-variation-panel.md)
