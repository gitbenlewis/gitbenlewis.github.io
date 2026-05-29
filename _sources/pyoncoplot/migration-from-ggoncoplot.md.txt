# Migration From ggoncoplot

`pyoncoplot` uses Pythonic argument names rather than preserving R argument
names. This keeps the API natural for `pandas`, Plotly, and Matplotlib users.

## Argument Mapping

| R `ggoncoplot` argument | Python `pyoncoplot` argument |
| --- | --- |
| `col_genes` | `gene_col` |
| `col_samples` | `sample_col` |
| `col_mutation_type` | `mutation_type_col` |
| `col_tooltip` | `tooltip_col` |
| `genes_to_include` | `include_genes` |
| `genes_to_ignore` | `ignore_genes` |
| `topn` | `top_n` |
| `draw_gene_barplot` | `draw_gene_bar` |
| `draw_tmb_barplot` | `draw_tmb_bar` |
| `copy` | `copy_on_click` |
| `cols_to_plot_metadata` | `metadata_cols` |
| `col_samples_metadata` | `metadata_sample_col` |
| `col_genes_pathway` | `pathway_gene_col` |

## Options Mapping

`ggoncoplot_options()` is represented by `OncoplotOptions`. R argument names are
not accepted directly, but the same concepts are available with Python names.

| R option concept | Python option |
| --- | --- |
| pathway strip text angle | `pathway_text_angle` |
| gene bar percentage label padding/nudge | `gene_bar_label_padding`, `gene_bar_label_nudge` |
| gene bar axis breaks | `gene_bar_scale_breaks`, `gene_bar_scale_n_breaks` |
| layout buffers | `buffer_metadata`, `buffer_tmb`, `buffer_gene_bar` |
| mutation legend key size | `legend_key_size` |
| metadata legend layout/key size | `metadata_legend_nrow`, `metadata_legend_ncol`, `metadata_legend_key_size` |
| metadata NA marker size | `metadata_na_marker_size` |
| metadata label style | `font_style_metadata` |
| numeric metadata label size | `font_size_metadata_bar_numbers` |
| metadata heatmap legend orientation | `metadata_legend_orientation_heatmap` |

## R-Style Concept

```r
ggoncoplot(
  data = mutations,
  col_genes = "gene",
  col_samples = "sample",
  col_mutation_type = "mutation_type",
  topn = 10
)
```

## Python Version

```python
from pyoncoplot import oncoplot

result = oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    top_n=10,
)
```

## Important Differences

- Python output can be Plotly or Matplotlib.
- Plotly output is interactive and can export standalone HTML.
- Matplotlib output is better for deterministic PNG/SVG/PDF figures.
- The goal is feature parity, not pixel-identical ggplot output.
- Synthetic gallery examples are checked in as TSV/JSON inputs rather than real
  patient data.

## ggoncoplot Parity Status

| Area | Status | Notes |
| --- | --- | --- |
| mutation validation, top genes, ties, multi-hit collapse | supported | behavior follows ggoncoplot semantics with Python errors |
| sample sorting, metadata sorting, pathways, TMB inference | supported | custom TMB sample columns may appear in any position |
| Matplotlib pathway strips, gene bars, metadata tracks, legends | supported with renderer differences | static output targets equivalent information, not ggplot pixel parity |
| Plotly hover, click-to-copy, and linked selection | supported with HTML hooks | hover and clipboard behavior are provided in exported HTML; linked selection uses Plotly selection events |
| R argument names and ggplot/ggiraph return objects | intentionally different | use Pythonic names and Plotly/Matplotlib objects |

## Recommended Migration Path

1. Rename input columns explicitly through `gene_col`, `sample_col`, and
   `mutation_type_col`.
2. Start with `backend="matplotlib"` if you are replacing static R figures.
3. Add metadata and TMB inputs after the basic mutation matrix is correct.
4. Add palettes last, once all displayed mutation and metadata levels are known.
5. Compare against the synthetic gallery examples for layout patterns.
