# Rendering Backends

`pyoncoplot` has two rendering backends:

- Plotly for interactive output.
- Matplotlib for deterministic static output.

## Plotly

Use Plotly when you want hover labels, interactive inspection, and HTML export.

```python
result = oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    tooltip_col="tooltip",
    backend="plotly",
)

result.save("oncoplot.html")
```

Plotly output supports `copy_on_click`:

| Value | Copied value |
| --- | --- |
| `"sample"` | clicked sample identifier |
| `"gene"` | clicked gene identifier |
| `"tooltip"` | clicked tooltip text |
| `"mutation_type"` | clicked mutation type |
| `"nothing"` | disables clipboard behavior |

Clipboard behavior is inserted into exported HTML via
`navigator.clipboard.writeText`.

## Matplotlib

Use Matplotlib when you need PNG, SVG, PDF, deterministic gallery images, or
static figures for manuscripts.

```python
result = oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    backend="matplotlib",
)

result.save("oncoplot.svg")
```

Matplotlib currently has the richest static layout support for:

- stacked TMB bars.
- right-side gene bars with percentage labels.
- numeric metadata bars.
- separate metadata legends.
- compact tile borders and row separators.

## Choosing A Backend

| Need | Recommended backend |
| --- | --- |
| exploratory browser plot | Plotly |
| hover and click-to-copy | Plotly |
| standalone HTML | Plotly |
| PNG/SVG/PDF figure | Matplotlib |
| deterministic gallery recreation | Matplotlib |
| manuscript-style static output | Matplotlib |

## Backend Support Matrix

| Feature | Plotly | Matplotlib |
| --- | --- | --- |
| mutation grid | interactive markers with hover and linked selection | static tile grid |
| TMB totals | bar trace; log and scientific tick formatting supported | bar axis; log labels and scientific tick formatting supported |
| TMB subtype legends | `TMB: <subtype>` entries when custom stacked TMB is rendered | separate `TMB Type` legend when custom stacked TMB is rendered |
| metadata display | heatmap strip with prettified hover labels and shared interactive legend | heatmap or mini-bar strip with separate metadata legends |
| image export | HTML built in; image export needs the `export` extra | PNG, SVG, PDF, and other `savefig` formats |
| copy-on-click | supported in exported HTML | not applicable to static figures |
| static layout controls | useful font, legend, marker, and axis controls | richest support for tile dimensions, metadata bars, font faces, and separate legend layout |

The `interactive` argument is a convenience alias:

```python
oncoplot(..., interactive=True)   # backend="plotly"
oncoplot(..., interactive=False)  # backend="matplotlib"
```
