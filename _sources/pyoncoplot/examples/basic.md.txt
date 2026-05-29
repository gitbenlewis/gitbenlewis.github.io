# Basic Example

This example makes a small static and interactive oncoplot.

```python
import pandas as pd
from pyoncoplot import OncoplotOptions, oncoplot

mutations = pd.DataFrame(
    {
        "sample": ["A", "A", "B", "C", "C", "D"],
        "gene": ["TP53", "EGFR", "TP53", "PTEN", "EGFR", "PTEN"],
        "mutation_type": [
            "Missense_Mutation",
            "Frame_Shift_Del",
            "Nonsense_Mutation",
            "Splice_Site",
            "In_Frame_Del",
            "Missense_Mutation",
        ],
    }
)

interactive = oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    draw_gene_bar=True,
    draw_tmb_bar=True,
)
interactive.save("basic.html")

static = oncoplot(
    mutations,
    gene_col="gene",
    sample_col="sample",
    mutation_type_col="mutation_type",
    draw_gene_bar=True,
    draw_tmb_bar=True,
    backend="matplotlib",
    options=OncoplotOptions(width=900, height=500),
)
static.save("basic.png", dpi=120)
```

Key ideas:

- one row is one mutation event.
- repeated sample/gene rows collapse into one tile.
- `draw_gene_bar=True` adds recurrence counts.
- `draw_tmb_bar=True` adds per-sample mutation burden.

