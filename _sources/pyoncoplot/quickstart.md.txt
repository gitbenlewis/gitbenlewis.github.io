# Quickstart

This page builds a small oncoplot from an inline `pandas` DataFrame.

## Input Data

Mutation input is one row per mutation event. At minimum, you need a sample
column and a gene column. A mutation type column is strongly recommended.

```python
import pandas as pd

mutations = pd.DataFrame(
    {
        "sample": ["S1", "S1", "S2", "S2", "S3", "S4"],
        "gene": ["TP53", "EGFR", "TP53", "PTEN", "PTEN", "EGFR"],
        "mutation_type": [
            "Missense_Mutation",
            "Frame_Shift_Del",
            "Nonsense_Mutation",
            "Splice_Site",
            "Missense_Mutation",
            "In_Frame_Del",
        ],
        "tooltip": [
            "S1 TP53 missense",
            "S1 EGFR frameshift deletion",
            "S2 TP53 nonsense",
            "S2 PTEN splice",
            "S3 PTEN missense",
            "S4 EGFR in-frame deletion",
        ],
    }
)
```

## Interactive Plotly Plot

```python
from pyoncoplot import oncoplot

result = oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    tooltip_col="tooltip",
    top_n=10,
    draw_gene_bar=True,
    draw_tmb_bar=True,
    backend="plotly",
)

result.show()
result.save("quickstart.html")
```

Plotly output includes hover labels. Exported HTML also includes click-to-copy
behavior unless `copy_on_click="nothing"` is used.

## Static Matplotlib Plot

```python
from pyoncoplot import OncoplotOptions, oncoplot

result = oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    tooltip_col="tooltip",
    draw_gene_bar=True,
    draw_tmb_bar=True,
    backend="matplotlib",
    options=OncoplotOptions(width=900, height=520),
)

result.save("quickstart.png", dpi=120)
```

## Result Object

`oncoplot()` returns an `OncoplotResult` with:

- `.figure`: the backend figure object.
- `.prepared_data`: the transformed data used by the renderer.
- `.show()`: display interactive figures when the backend supports it.
- `.save(path, **kwargs)`: save HTML, PNG, SVG, PDF, or other backend-supported formats.
- `.to_html(...)`: Plotly-only HTML export.

## Where To Go Next

- [Data Inputs](data-inputs.md)
- [Metadata and TMB](metadata-and-tmb.md)
- [Options Reference](options-reference.md)

