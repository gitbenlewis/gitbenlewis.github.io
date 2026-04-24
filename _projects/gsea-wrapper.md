---
layout: page
title: GSEApy Wrapper
description: Reproducible preranked gene set enrichment analysis across human and mouse with FDR-controlled scoring and multi-collection support.
img: assets/img/projects/gsea_enrichment_plot.png
importance: 3
category: work
github: https://github.com/gitbenlewis/run_GSEApy_wrapper
---

{% include figure.liquid loading="eager" path="assets/img/projects/gsea_enrichment_plot.png" title="Preranked GSEA enrichment plot — Glioma (hsa05214, Homo sapiens). NES: 1.907, FDR: 0.000" class="img-fluid rounded z-depth-1" %}

## Overview

A Python wrapper around [GSEApy's](https://gseapy.readthedocs.io/) preranked GSEA method, built for reproducible gene set enrichment analysis with FDR-controlled scoring. The library exposes a single primary function — `run_gseapy_prerank_multiple_term_collections()` — that accepts ranked gene lists and runs GSEA simultaneously against multiple GMT collections in one call. Supports both human and mouse gene spaces with precomputed ortholog conversion tables.

## Tech Stack

- Python 3.11
- GSEApy 1.1.11
- NumPy, SciPy, Pandas, Scikit-learn
- AnnData, Matplotlib, Seaborn
- Conda environment management

## Key Features

- **Multi-collection GSEA** -- run against multiple GMT libraries (Enrichr, MSigDB) in a single function call
- **Reproducible FDR** -- consistent permutation-based false discovery rate scoring across runs
- **Multi-species support** -- human and mouse gene lists with precomputed ortholog conversion tables (`h2m_agg.csv`, `m2h_agg.csv`)
- **Curated GMT collections** -- Enrichr and MSigDB gene sets for both species, including ortholog-converted versions, downloaded and organized on setup
- **Modular design** -- core wrapper (`_gseapy_pre_rank_wrap.py`), visualization (`_gseapy_dot_plots.py`), and post-processing helpers (`_gseapy_post_process_helpers.py`) as separate modules
- **Example workflow** -- end-to-end demo using GSE68719 with organized result directories and expected outputs

## Repository Structure

```
run_GSEApy_wrapper/
├── _gseapy_pre_rank_wrap.py        # primary GSEA wrapper
├── _gseapy_dot_plots.py            # enrichment dot plot visualizations
├── _gseapy_post_process_helpers.py # result filtering and formatting
├── config/
│   ├── env_GSEApy.yaml             # conda environment spec
│   └── download_gseapy_gmt_files.py
├── data/ref/
│   ├── h2m_agg.csv                 # human → mouse ortholog table
│   ├── m2h_agg.csv                 # mouse → human ortholog table
│   └── gmt/                        # enrichr/ and msigdb/ by species
└── examples/GSE68719/              # example workflow
```

## Setup

```bash
git clone https://github.com/gitbenlewis/run_GSEApy_wrapper.git
cd run_GSEApy_wrapper

# Create environment
conda env create -f ./config/env_GSEApy.yaml
conda activate env_GSEApy

# Download GMT annotation files and build ortholog tables
python config/download_gseapy_gmt_files.py
```

## Usage

```python
from _gseapy_pre_rank_wrap import run_gseapy_prerank_multiple_term_collections

run_gseapy_prerank_multiple_term_collections(
    data_csv_path="examples/GSE68719/data/ranked_genes.csv",
    list_of_term_collections=["h.all.v2023.2.Hs.symbols", "c2.cp.kegg"],
    rank_metric_calc_flavor="signal_to_noise",
    outdir="examples/GSE68719/results/"
)
```

## Repository

Source code and documentation:
[gitbenlewis/run_GSEApy_wrapper](https://github.com/gitbenlewis/run_GSEApy_wrapper)
