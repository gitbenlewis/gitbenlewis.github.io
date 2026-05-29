# Structural Variation Panel

The structural-variation panel recreates `gen.goal_plot_20.png` from compact
depth, allele-fraction, and exon-model inputs derived from the fuc
`pyvcf/getrm-cyp2d6-vdr.vcf` example.

It is gallery-specific and is not rendered through `oncoplot()`, because it is a
depth and allele-fraction panel rather than a mutation oncoplot.

## Render It

```bash
python3 python_refactor_goal_sources/recreate_gallery.py --preset sv_panel
```

Output:

```text
python_refactor_goal_sources/generated_plots/clean/gen.goal_plot_20.png
```

## Inputs

```text
python_refactor_goal_sources/syntheitic_goal_data/sv_depth.tsv
python_refactor_goal_sources/syntheitic_goal_data/sv_allele_fraction.tsv
python_refactor_goal_sources/syntheitic_goal_data/sv_gene_models.tsv
```

## Input Shapes

`sv_depth.tsv`:

| Column | Meaning |
| --- | --- |
| `sample` | sample identifier |
| `source_sample` | upstream VCF sample used for the displayed sample |
| `title` | panel title |
| `position` | genomic position |
| `depth` | read depth |

`sv_allele_fraction.tsv`:

| Column | Meaning |
| --- | --- |
| `sample` | sample identifier |
| `source_sample` | upstream VCF sample used for the displayed sample |
| `position` | genomic position |
| `allele` | `REF` or `ALT` |
| `allele_fraction` | observed allele fraction |

`sv_gene_models.tsv`:

| Column | Meaning |
| --- | --- |
| `gene` | gene label |
| `exon` | exon number from the fuc example script |
| `start` | interval start |
| `end` | interval end |
| `strand` | gene strand |
