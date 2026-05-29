# API Reference

This is a human-written reference for the public API. It focuses on stable
behavior and examples rather than generated internals.

## `oncoplot`

```python
oncoplot(
    data=None,
    *,
    params=None,
    params_key=None,
    **kwargs,
)
```

Create an oncoplot from mutation-level data and return an `OncoplotResult`.
The function accepts normal explicit keyword arguments, a `params` dictionary,
the path to a YAML params file, or both. Explicit keywords override values in
`params`. Pass `save={"path": ..., ...}` to save the returned result during the
same call; keys other than `path` are forwarded to `OncoplotResult.save()`.

Common call:

```python
from pyoncoplot import oncoplot

result = oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    draw_gene_bar=True,
    draw_tmb_bar=True,
    backend="matplotlib",
)
```

Config-driven or reusable calls can pass the same arguments as a dictionary.
Table inputs can be DataFrames or paths to CSV/TSV-style files:

```python
params = {
    "data": "data/mutations.csv",
    "metadata": "data/metadata.csv",
    "gene_col": "gene",
    "sample_col": "sample",
    "mutation_type_col": "mutation_type",
    "metadata_cols": ["Subtype"],
    "backend": "matplotlib",
    "options": {"width": 900, "height": 520},
}

result = oncoplot(params=params, top_n=20)
```

Here `top_n=20` overrides any `params["top_n"]` value.

If you need to keep the unpacked `**params` call style while overriding a key
that may already be in the dictionary, merge first:

```python
from pyoncoplot import merge_oncoplot_params, oncoplot

merged = merge_oncoplot_params(params, options={"width": 1000, "height": 600})
result = oncoplot(**merged)
```

`collections.ChainMap` also works for lightweight one-off calls. Put overrides
first because the first mapping wins:

```python
from collections import ChainMap

result = oncoplot(**ChainMap({"options": {"width": 1000, "height": 600}}, params))
```

Avoid `oncoplot(options=..., **params)` when `params` may contain `"options"`;
Python raises a duplicate keyword error before `oncoplot()` can merge values.

YAML configs can be loaded directly:

```python
result = oncoplot(params="config.yaml", params_key="datasets.m15.plot1_params")
```

or read first:

```python
from pyoncoplot import load_oncoplot_params

params = load_oncoplot_params("config.yaml", key="datasets.m15.plot1_params")
result = oncoplot(params=params)
```

Relative table paths inside YAML are resolved relative to the config file. Use
`params_key`/`key` for dot-separated nested mappings. Table read specs pass
extra options to `pandas.read_csv`:

```yaml
datasets:
  m15:
    plot1_params:
      data:
        path: files/mutations.txt
        sep: "\t"
      metadata: files/metadata.csv
      gene_col: gene
      sample_col: sample
      mutation_type_col: mutation_type
```

### Core Arguments

| Argument | Purpose |
| --- | --- |
| `data` | mutation-level `pandas.DataFrame` or CSV/TSV path |
| `gene_col`, `sample_col` | required column names for gene and sample identifiers |
| `mutation_type_col` | optional mutation category column used for tile colors and legends unless a continuous-only main grid is requested |
| `tooltip_col` | optional tooltip text column; generated from sample, gene, mutation type, and expanded-grid variant summaries when omitted |
| `include_genes`, `ignore_genes`, `top_n` | choose the displayed gene panel |
| `draw_gene_bar`, `draw_tmb_bar` | add recurrence and mutation burden side panels |
| `palette`, `tmb_palette`, `metadata_palette`, `variant_value_palette` | color mappings for mutation tiles, typed TMB bars, metadata, and continuous variant heatmaps |
| `metadata`, `metadata_cols`, `metadata_sample_col` | clinical annotation input and selected tracks |
| `metadata_require_mutations`, `show_all_samples` | sample inclusion controls |
| `filter_samples_by_isin_lists`, `filter_samples_by_greater_than`, `filter_samples_by_less_than` | pre-ranking sample-cohort filters from metadata first, then mutation data |
| `filter_mutations_by_isin_lists`, `filter_mutations_by_greater_than`, `filter_mutations_by_less_than` | pre-ranking row filters for the mutation table |
| `pathway`, `pathway_gene_col` | pathway grouping input |
| `sample_order`, `metadata_sort_cols` | explicit or metadata-driven sample sorting |
| `mutation_type_order`, `metadata_category_orders`, `tmb_type_order` | categorical level order for colors, stacks, and legends |
| `tmb_data` | optional 2- or 3-column custom TMB table |
| `variant_value_col`, `variant_value_cols`, `variant_value_agg`, `variant_value_missing` | optional numeric variant column or columns, collapse rule, and missing-value policy for continuous main-grid coloring |
| `main_grid_rows`, `variant_value_scale` | expanded main-grid row specifications and per-column/shared continuous color scaling |
| `gene_name_x_offset` | extra leftward padding for expanded-grid gene labels |
| `main_grid_rows_label_x_offset` | extra leftward padding for expanded-grid row labels |
| `backend`, `interactive` | choose Plotly or Matplotlib rendering |
| `copy_on_click` | Plotly clipboard payload behavior |
| `options` | `OncoplotOptions` instance or mapping for visual controls |
| `save` | optional mapping with `path` plus save keyword arguments |

Filtering runs before gene ranking, TMB preparation, sample ordering, and
recurrence denominators. Mutation filters are row-wise and operate only on the
main mutation table. Sample filters choose a cohort; each column is resolved from
metadata first when available, otherwise from the mutation table. All filters
combine with AND semantics, and numeric filters use strict `>` and `<`
comparisons.

```python
oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    metadata=metadata,
    filter_samples_by_isin_lists={"Subtype": ["Basal", "HER2"]},
    filter_samples_by_greater_than={"Age_years": 45},
    filter_mutations_by_isin_lists={"mutation_type": ["Missense_Mutation"]},
    filter_mutations_by_less_than={"VAF": 0.80},
)
```

Categorical order controls apply to both Plotly and Matplotlib. If an explicit
order is not supplied, pandas categorical dtype order is used when present;
otherwise palette mapping order and then observed data order are used.

```python
oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    metadata=metadata,
    metadata_cols=["clinical_group"],
    mutation_type_order=["Nonsense", "Missense", "Silent"],
    metadata_category_orders={"clinical_group": ["low", "intermediate", "high"]},
    tmb_type_order=["clonal", "subclonal"],
)
```

Continuous variant coloring replaces categorical mutation-type coloring in the
main grid when `variant_value_col` is supplied. The mutation type column is
still retained for stacked gene bars and TMB fallbacks:

```python
oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    variant_value_col="VAF",
    variant_value_agg="max",
    variant_value_palette="viridis",
    draw_gene_bar=True,
    options={"gene_bar_mode": "percent"},
)
```

`variant_value_agg` controls how multiple rows for the same sample/gene tile are
collapsed and can be `"max"`, `"mean"`, `"median"`, or `"min"`.
`variant_value_missing="blank"` is the default: missing values are ignored for
aggregation, and an all-missing tile is left blank. Use
`variant_value_missing="zero"` to fill missing values with zero before
aggregation.

Use `main_grid_rows` when the main heatmap should show mutation type and one or
more continuous variant tracks as separate subrows for each gene:

```python
oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    main_grid_rows=[
        {"kind": "mutation_type", "label": "Variant type"},
        {"kind": "variant_value", "column": "VAF_pct", "label": "VAF %", "agg": "max"},
        {"kind": "variant_value", "column": "VAF_abs", "label": "VAF abs", "palette": "magma", "missing": "zero"},
    ],
    gene_name_x_offset=12,
    draw_gene_bar=True,
)
```

For the common case, `variant_value_cols=["VAF_pct", "VAF_abs"]` expands to a
mutation-type row followed by one row per numeric value column. Set
`variant_value_scale="shared"` to use one shared min/max and colorbar across all
continuous rows; the default `"per_column"` gives each continuous row its own
range and bottom horizontal colorbar. A `main_grid_rows` variant-value row can set
`missing="blank"` or `missing="zero"` to override `variant_value_missing` for
that row. `gene_name_x_offset` and `main_grid_rows_label_x_offset` are also
available in `OncoplotOptions`; top-level arguments win when supplied.

## `merge_oncoplot_params`

```python
merge_oncoplot_params(params=None, *, params_key=None, **overrides)
```

Return a plain dictionary of oncoplot parameters with explicit overrides taking
precedence. It accepts the same mapping or YAML config path forms as
`oncoplot(params=...)`, including `params_key` for nested YAML mappings.

## `OncoplotResult`

Returned by `oncoplot()`.

| Attribute or method | Purpose |
| --- | --- |
| `figure` | backend-specific Plotly or Matplotlib figure |
| `backend` | `"plotly"` or `"matplotlib"` |
| `prepared_data` | transformed data shared by renderers |
| `show()` | call the backend's display method |
| `save(path, **kwargs)` | save HTML or image output |
| `to_html(...)` | Plotly-only HTML string export |

### Save Behavior

`OncoplotResult.save()` chooses behavior from the file suffix. Plotly results
save `.html` directly, while Plotly image suffixes such as `.png`, `.svg`, and
`.pdf` require the export extra. Matplotlib results save through
`figure.savefig()` and support the image/vector formats available in the local
Matplotlib installation. Matplotlib saves default to `bbox_inches="tight"`;
pass `bbox_inches=None` when exact configured figure dimensions should be
preserved.

## `prepare_oncoplot_data`

Prepares mutation, metadata, pathway, and TMB inputs without rendering.

Use it when you want to inspect selected genes, sample order, collapsed tiles, or
metadata filtering:

```python
from pyoncoplot import prepare_oncoplot_data

prepared = prepare_oncoplot_data(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    top_n=10,
)

print(prepared.genes)
print(prepared.samples)
print(prepared.tiles.head())
```

### `PreparedOncoplotData` Fields

| Field | Summary |
| --- | --- |
| `tiles` | one displayed row per sample/gene tile, with collapsed `MutationType` and tooltip text |
| `samples`, `genes` | final display order used by both renderers |
| `total_samples` | denominator used for recurrence percentages |
| `mutation_type_col` | original mutation type column name, when supplied |
| `metadata`, `metadata_cols`, `metadata_tracks` | filtered metadata table and renderer-neutral track summaries |
| `pathway`, `pathway_by_gene`, `pathway_groups` | pathway input and contiguous display groups |
| `tmb` | filtered TMB input or inferred mutation burden table |
| `tmb_sample_col`, `tmb_value_col`, `tmb_type_col` | resolved TMB sample, numeric value, and optional subtype columns |
| `tmb_render_stacked`, `tmb_is_custom` | flags used by renderers to decide stacked TMB behavior |
| `mutation_counts`, `tmb_totals`, `tmb_type_counts` | summary tables for testing, debugging, and downstream inspection |
| `mutation_type_levels`, `tmb_type_levels` | resolved categorical order used by renderers |
| `variant_value_col`, `variant_value_agg`, `variant_value_missing`, `variant_value_min`, `variant_value_max` | continuous tile-coloring metadata when `variant_value_col` is supplied |
| `variant_value_cols`, `variant_value_scale` | multi-row continuous variant track inputs and scale mode |
| `main_grid_rows`, `main_grid_tiles`, `main_grid_mode` | renderer-neutral expanded main-grid row and tile tables |

## `identify_top_genes`

Rank genes by the number of distinct mutated samples.

```python
from pyoncoplot import identify_top_genes

genes = identify_top_genes(
    mutations,
    gene_col="gene",
    sample_col="sample",
    top_n=20,
)
```

## `score_sample_by_gene_rank`

Assign one sample a score based on mutations in higher-ranked genes. This is the
low-level helper used to produce a useful default sample ordering.

```python
from pyoncoplot import score_sample_by_gene_rank

score = score_sample_by_gene_rank(
    mutated_genes=["TP53", "PTEN"],
    genes_informing_score=["TP53", "PIK3CA", "PTEN"],
    gene_rank=[1, 2, 3],
)
```

## `rank_genes_by_pathway`

Rank genes while respecting pathway order.

```python
from pyoncoplot import rank_genes_by_pathway

gene_pathway_map = pd.DataFrame(
    {
        "gene": ["TP53", "RB1", "PIK3CA", "PTEN"],
        "pathway": ["Cell cycle", "Cell cycle", "PI3K", "PI3K"],
    }
)

ranked = rank_genes_by_pathway(
    gene_pathway_map,
    gene_ranks=["PIK3CA", "TP53", "PTEN", "RB1"],
    pathway_ranks=["Cell cycle", "PI3K"],
)
```

## `prettify`

Convert machine-style labels into display labels.

```python
from pyoncoplot import prettify

prettify("Missense_Mutation")
# "Missense Mutation"
```

## Palette Helpers

```python
from pyoncoplot import assert_palette_is_sensible, get_sensible_default_palette

palette = get_sensible_default_palette(mutations["mutation_type"])
assert_palette_is_sensible(palette, mutations["mutation_type"])
```
