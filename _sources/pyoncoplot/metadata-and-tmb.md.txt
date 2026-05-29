# Metadata and TMB

Clinical metadata and mutation burden bars are optional, but they are often what
turns an oncoplot from a mutation grid into an interpretable cohort summary.

## Metadata Table Schema

Metadata input needs one unique row per sample.

```python
metadata = pd.DataFrame(
    {
        "sample": ["S1", "S2", "S3"],
        "Subtype": ["A", "B", "A"],
        "Age_years": [62, 47, 71],
    }
)
```

Use `metadata_cols` to choose displayed tracks:

```python
oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    metadata=metadata,
    metadata_cols=["Subtype", "Age_years"],
)
```

If the metadata sample column is not named the same as `sample_col`, pass
`metadata_sample_col`.

```python
oncoplot(
    mutations,
    gene_col="gene",
    sample_col="Tumor_Sample_Barcode",
    mutation_type_col="Variant_Classification",
    metadata=metadata,
    metadata_sample_col="patient_id",
    metadata_cols=["Subtype"],
)
```

## Metadata Columns in Mutation Data

If sample-level metadata columns already live in the mutation table, you can omit
`metadata` and pass `metadata_cols` directly:

```python
oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    metadata_cols=["Subtype", "Age_years"],
)
```

`pyoncoplot` derives the metadata table from the mutation data by keeping the
sample identifier plus the requested metadata columns, then dropping exact
duplicate rows. Each sample still needs one consistent metadata value per
requested column; conflicting values for the same sample raise the usual
duplicate metadata identifier error.

## Metadata Filtering

By default, `metadata_require_mutations=True`, so metadata rows whose samples do
not appear in the mutation table are filtered before sample selection. After
gene selection, `show_all_samples=True` keeps mutation-table samples even when
they do not have mutations in the selected genes.

Use:

```python
oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    metadata=metadata,
    metadata_cols=["Subtype"],
    show_all_samples=True,
)
```

to show mutation-table samples even when they do not have selected-gene
mutations.

To keep samples that exist only in metadata, use both controls:

```python
oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    metadata=metadata,
    metadata_cols=["Subtype"],
    metadata_require_mutations=False,
    show_all_samples=True,
)
```

`filter_samples_by_isin_lists`, `filter_samples_by_greater_than`, and
`filter_samples_by_less_than` run before these inclusion controls. They use
metadata columns first when available, then fall back to mutation-table columns.
Mutation-table fallback filters identify samples with a matching retained
mutation row; custom TMB-only samples do not re-enter a filtered cohort unless
they also exist in the filtered metadata or mutation data.

## Numeric Metadata

Numeric metadata can be shown as a heatmap or as mini bars.

```python
from pyoncoplot import OncoplotOptions

options = OncoplotOptions(metadata_numeric_plot_type="bar")
```

Use `"bar"` for continuous values where relative magnitude matters, such as age
or follow-up days. Use `"heatmap"` for compact display.

## Categorical Metadata Order

Categorical metadata order controls fallback color assignment and legend order
in both Plotly and Matplotlib. PyOncoplot respects pandas categorical dtype
order, or you can pass `metadata_category_orders` directly:

```python
metadata["Subtype"] = pd.Categorical(
    metadata["Subtype"],
    categories=["Luminal", "Basal", "HER2"],
    ordered=True,
)

oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    metadata=metadata,
    metadata_cols=["Subtype"],
    metadata_category_orders={"Subtype": ["Basal", "HER2", "Luminal"]},
)
```

Explicit order wins over dtype order. Unused levels are ignored, and observed
levels missing from the explicit list are appended in observed order.

## TMB Inference

When `draw_tmb_bar=True` and no `tmb_data` is supplied, TMB is inferred from the
mutation table.

```python
oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    draw_tmb_bar=True,
)
```

## Custom TMB Data

Custom TMB input should include sample identifiers and count values. When it also
includes mutation types, the renderers can draw stacked mutation-type bars when
`log10_transform_tmb=False`.

```python
tmb = pd.DataFrame(
    {
        "sample": ["S1", "S1", "S2"],
        "mutation_type": ["Missense_Mutation", "Splice_Site", "Missense_Mutation"],
        "mutations": [12, 3, 7],
    }
)

oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    draw_tmb_bar=True,
    tmb_data=tmb,
    tmb_palette=palette,
    backend="matplotlib",
    options=OncoplotOptions(log10_transform_tmb=False),
)
```

If `log10_transform_tmb=True` with typed TMB data, both renderers collapse the
bars to sample totals and emit a `UserWarning`. Custom TMB categories need
`tmb_palette` coverage only when stacked subtype bars are
rendered with `log10_transform_tmb=False`, unless they are already present in
the mutation palette fallback.

Use `tmb_type_order` to control typed TMB stack and legend order:

```python
oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    draw_tmb_bar=True,
    tmb_data=tmb,
    tmb_palette={"clonal": "#222222", "subclonal": "#999999"},
    tmb_type_order=["clonal", "subclonal"],
    options=OncoplotOptions(log10_transform_tmb=False),
)
```
