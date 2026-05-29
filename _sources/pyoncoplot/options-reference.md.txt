# Options Reference

`OncoplotOptions` controls layout and visual details. Pass it through the
`options` argument:

```python
from pyoncoplot import OncoplotOptions, oncoplot

result = oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    backend="matplotlib",
    options=OncoplotOptions(width=1200, height=700),
)
```

## Size and Layout

| Option | Default | Meaning |
| --- | --- | --- |
| `width` | `1200` | intended output width in pixels |
| `height` | `650` | intended output height in pixels |
| `selection_type` | `"none"` | Plotly selection mode: `"none"`, `"multiple"`, or `"single"` |
| `tmb_height_ratio` | `0.14` | relative height of the TMB bar area |
| `gene_bar_width_ratio` | `0.18` | relative width of the right gene bar |
| `metadata_height_ratio` | `0.18` | relative height of metadata tracks |
| `metadata_position` | `"bottom"` | `"bottom"` or `"top"` |
| `buffer_metadata` | `0.08` | spacing around metadata tracks |
| `buffer_tmb` | `0.08` | spacing around the TMB bar |
| `buffer_gene_bar` | `0.02` | spacing between the matrix and gene bar |

## Labels and Axes

| Option | Default | Meaning |
| --- | --- | --- |
| `x_label` | `"Sample"` | x-axis label |
| `y_label` | `"Gene"` | y-axis label |
| `show_sample_ids` | `False` | show sample labels |
| `sample_id_position` | `"bottom"` | sample label placement |
| `sample_id_angle` | `90` | sample label rotation |
| `show_x_label` | `False` | show x-axis label |
| `show_y_label` | `False` | show y-axis label |
| `show_tmb_y_label` | `False` | show TMB y-axis label |
| `show_tmb_axis` | `True` | show TMB tick labels |
| `show_gene_bar_axis` | `True` | show gene bar axis |

## Legends

| Option | Default | Meaning |
| --- | --- | --- |
| `show_legend` | `True` | draw mutation legend |
| `show_legend_titles` | `True` | draw legend titles |
| `mutation_legend_position` | `"bottom"` | `"bottom"`, `"right"`, or `"none"` |
| `show_metadata_legends` | `True` | draw categorical metadata legends and numeric metadata colorbars |
| `metadata_legend_position` | `"right"` | `"right"` or `"bottom"` |
| `legend_key_size` | `1.0` | mutation legend key size multiplier |
| `legend_offsets` | `{}` | per-legend `{"x": ..., "y": ...}` offsets in figure/paper coordinates |
| `metadata_legend_nrow` | `None` | optional metadata legend row limit |
| `metadata_legend_ncol` | `None` | optional metadata legend column count |
| `metadata_legend_key_size` | `1.0` | metadata legend key size multiplier |
| `legend_label_max_chars` | `None` | optional maximum displayed legend label length |
| `legend_title_max_chars` | `None` | optional maximum displayed legend title length |

Plotly uses one shared interactive legend. `mutation_legend_position="none"`
hides mutation traces while categorical metadata legends can remain visible. A
bottom request creates a horizontal Plotly legend; otherwise visible legends are
placed vertically on the right. Expanded main-grid variant-value colorbars are
an exception: Plotly and Matplotlib place them horizontally below the plot area so
they do not compete with right-side metadata legends. Matplotlib keeps separate
static legend layout controls, including `metadata_legend_nrow` and
`metadata_legend_ncol`.

`legend_offsets` targets individual legends by stable keys. Use source columns
where available, such as `mutation:type`, `tmb:tmb_type`, `metadata:clinical_group`,
or `variant:vaf`. Use stable fallback keys for legends without one source column:
`mutation`, `tmb`, `variant:shared`, and `gene_bar`. Positive `x` moves right and
positive `y` moves up. Plotly splits only targeted categorical legend groups into
separate legend containers; untargeted legends keep the default shared position.

## Tile Styling

| Option | Default | Meaning |
| --- | --- | --- |
| `background_color` | `"#E5E5E5"` | empty tile background |
| `tile_height` | `1.0` | mutated and empty tile height |
| `tile_width` | `1.0` | mutated and empty tile width |
| `tile_linewidth` | `0.25` | tile border width |
| `row_separator_linewidth` | `0.8` | row separator width |
| `unspecified_mutation_color` | `"#1A1A1A"` | fallback mutation color |
| `multi_hit_color` | `"black"` | multi-hit color |

`tile_width` and `tile_height` are Matplotlib/static-layout controls. Plotly
uses fixed interactive square markers; `tile_linewidth` applies to marker
outlines in both renderers.

## Fonts

| Option | Default | Meaning |
| --- | --- | --- |
| `font_size_x_label` | `26` | x-axis label size |
| `font_size_y_label` | `26` | y-axis label size |
| `font_size_genes` | `12` | gene label size |
| `font_size_samples` | `9` | sample label size |
| `font_size_metadata` | `10` | metadata row label size |
| `font_size_metadata_bar_numbers` | `8` | numeric metadata min/max label size |
| `font_size_tmb_axis` | `10` | TMB axis text size |
| `font_size_gene_bar_axis` | `10` | gene bar text size |
| `font_size_legend_text` | `None` | explicit mutation/TMB/Plotly legend label size |
| `font_size_legend_title` | `None` | explicit mutation/TMB/colorbar legend title size |
| `font_size_metadata_legend_text` | `None` | explicit metadata legend label size |
| `font_size_metadata_legend_title` | `None` | explicit metadata legend title size |
| `font_size_title` | `14` | top-level figure title size |
| `font_size_subplot_title` | `12` | named subplot title size |
| `font_size_pathway` | `None` | explicit pathway strip label size |
| `gene_name_x_offset` | `0.0` | extra leftward padding for expanded-grid gene labels |
| `main_grid_rows_label_x_offset` | `10.0` | extra leftward padding for expanded-grid row labels |
| `font_family` | `"Arial"` | renderer font family |
| `gene_font_style` | `"normal"` | gene label style |
| `sample_font_style` | `"normal"` | sample label style |
| `font_style_metadata` | `"normal"` | metadata row label style |

Plotly applies practical font sizes for sample ticks, gene ticks, axis labels,
TMB axes, gene-bar axes, and metadata row labels. Font face style controls such
as `gene_font_style`, `sample_font_style`, and `font_style_metadata` are
Matplotlib/static-layout oriented.

## Titles

| Option | Default | Meaning |
| --- | --- | --- |
| `title_text` | `None` | optional top-level figure title |
| `main_subplot_title` | `None` | optional main mutation matrix title |
| `tmb_subplot_title` | `None` | optional TMB subplot title |
| `gene_bar_subplot_title` | `None` | optional gene-bar subplot title |
| `metadata_subplot_title` | `None` | optional metadata subplot title |

## TMB and Gene Bar

| Option | Default | Meaning |
| --- | --- | --- |
| `log10_transform_tmb` | `True` | log-transform TMB values |
| `scientific_tmb` | `False` | use scientific TMB labels where supported |
| `gene_bar_mode` | `"counts"` | `"counts"` for recurrence-width bars or `"percent"` for 100% mutation-type composition bars |
| `show_gene_bar_labels` | `False` | show recurrence percentage labels |
| `gene_bar_label_round` | `0` | rounding for recurrence labels |
| `gene_bar_label_padding` | `0.24` | extra x-axis room for gene-bar percentage labels |
| `gene_bar_label_nudge` | `0.0` | additional x-axis nudge for gene-bar labels |
| `gene_bar_scale_breaks` | `None` | explicit gene-bar axis tick positions |
| `gene_bar_scale_n_breaks` | `None` | requested number of gene-bar axis breaks |

In Plotly, `gene_bar_scale_n_breaks` is passed through as an `nticks` request
when `gene_bar_scale_breaks` is not supplied.
`gene_bar_mode="percent"` keeps the same mutation-type colors but normalizes
each gene's stacked bar to 100%.

## Pathways

| Option | Default | Meaning |
| --- | --- | --- |
| `pathway_text_color` | `"white"` | pathway strip label color |
| `pathway_background_color` | `"#1A1A1A"` | pathway strip fill color |
| `pathway_outline_color` | `"black"` | pathway strip border color |
| `pathway_text_angle` | `0` | pathway strip label rotation |

## Metadata

| Option | Default | Meaning |
| --- | --- | --- |
| `metadata_na_marker` | `"!"` | legend label for missing metadata |
| `metadata_na_marker_size` | `7` | visible NA marker text size |
| `metadata_max_levels` | `40` | maximum categorical levels allowed per metadata track |
| `metadata_numeric_plot_type` | `"heatmap"` | `"heatmap"` or `"bar"` |
| `metadata_legend_orientation_heatmap` | `"vertical"` | orientation hint for numeric heatmap legends |
| `metadata_default_colors` | color sequence | fallback metadata colors |

Categorical metadata tracks reuse `metadata_default_colors` from the beginning
when there are more levels than fallback colors. `metadata_numeric_plot_type="bar"`
and metadata legend row/column controls are Matplotlib/static metadata controls.
`metadata_legend_orientation_heatmap` controls numeric metadata colorbar
orientation in both backends.
Plotly renders compact metadata heatmaps and categorical metadata legend entries
that fit its interactive model.

## Text Prettification

| Option | Default | Meaning |
| --- | --- | --- |
| `prettify_legend_titles` | `True` | prettify legend titles |
| `prettify_legend_values` | `True` | prettify legend values |
| `prettify_function` | `prettify` | function used for display labels |

## Common Bundles

Compact static plot:

```python
OncoplotOptions(
    width=900,
    height=520,
    font_size_genes=8,
    tile_linewidth=0.1,
    row_separator_linewidth=0.2,
)
```

Gallery-style static plot:

```python
OncoplotOptions(
    width=1800,
    height=900,
    log10_transform_tmb=False,
    show_gene_bar_labels=True,
    mutation_legend_position="right",
    metadata_legend_position="right",
    metadata_numeric_plot_type="bar",
)
```
