# Pathways and Sorting

Gene and sample ordering are central to making an oncoplot readable.

## Default Gene Ranking

By default, genes are ranked by the number of distinct samples with a mutation.

```python
oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    top_n=15,
)
```

## Explicit Gene Order

Use `include_genes` when a gene panel should be fixed:

```python
oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    include_genes=["TP53", "PIK3CA", "PTEN", "EGFR"],
)
```

## Pathway Input

Pathway input has exactly two columns: one gene column and one pathway column.

```python
pathway = pd.DataFrame(
    {
        "gene": ["TP53", "RB1", "PIK3CA", "PTEN"],
        "pathway": ["Cell cycle", "Cell cycle", "PI3K", "PI3K"],
    }
)

oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    pathway=pathway,
    pathway_gene_col="gene",
)
```

Validation rules:

- pathway input must have exactly two columns.
- pathway genes cannot be missing.
- pathway names cannot be missing.
- pathway gene values must be unique.
- `"Other"` is reserved for unmapped genes.

## Sample Ordering

By default, samples are ordered to emphasize mutations in high-ranked genes.

Use `sample_order` for exact control:

```python
oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    sample_order=["S3", "S2", "S1"],
)
```

## Metadata Sorting

Use metadata sorting to group samples by clinical categories.

```python
oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    metadata=metadata,
    metadata_cols=["Subtype", "Response"],
    metadata_sort_cols=["Subtype", "Response"],
    metadata_sort_by=["alphabetical", "frequency"],
    metadata_sort_desc=[False, True],
)
```

Common values for `metadata_sort_by`:

| Value | Meaning |
| --- | --- |
| `"alphabetical"` | sort category labels alphabetically |
| `"frequency"` | sort category labels by frequency |

## Showing All Samples

Use `show_all_samples=True` when metadata or custom TMB inputs should define
the cohort, even if some samples have no mutations in the selected gene panel.

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
