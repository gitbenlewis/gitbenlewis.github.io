---
layout: page
title: Single-Cell Python Tools
description: Scanpy wrappers and utility functions for end-to-end single-cell RNA-seq analysis on AnnData objects.
img: assets/img/projects/sctl_umap_clusters.png
importance: 4
category: work
github: https://github.com/gitbenlewis/single_cell_python_tools
---

{% include figure.liquid loading="eager" path="assets/img/projects/sctl_umap_clusters.png" title="PBMC3K — Leiden cluster silhouette scores, UMAP by cluster, UMAP silhouette colormap, and PCA. Generated via sctl preprocessing pipeline." class="img-fluid rounded z-depth-1" %}

## Overview

A Python package of [Scanpy](https://scanpy.readthedocs.io/) wrappers and utility functions for streamlined single-cell RNA-seq analysis. Designed to operate natively on AnnData objects, the package supports both a function-based API for modular step-by-step control and an object-oriented `DATASET_class` interface for method-chained pipelines from raw counts through clustering, differential expression, and cell type annotation.

## Tech Stack

- Python 3.10
- Scanpy ≥ 1.11, AnnData ≥ 0.10
- Leiden clustering (leidenalg ≥ 0.10)
- UMAP (umap-learn ≥ 0.5)
- BBKNN batch correction (bbknn ≥ 1.6)
- GSEApy ≥ 1.1.9
- NumPy, Pandas, SciPy, Scikit-learn, Matplotlib, Seaborn, Numba
- Conda or pip (editable install)

## Key Features

- **Preprocessing** -- QC filtering with mitochondrial, ribosomal, hemoglobin, and MALAT1 gene annotation; normalization, scaling, and highly variable gene selection
- **Dimensionality reduction** -- PCA with configurable components feeding into UMAP projections
- **Clustering** -- Leiden algorithm with silhouette score analysis for objective cluster resolution selection
- **Cell biology** -- cell cycle scoring and regression to remove confounding variation
- **Batch correction** -- BBKNN integration for multi-sample and multi-batch datasets
- **Visualization** -- QC scatter and violin plots, UMAP projections with marker gene overlays, silhouette score plots, batch effect charts
- **Downstream analysis** -- differential expression gene (DEG) analysis, Gene Set Enrichment Analysis (GSEA), cell type annotation
- **Two usage modes** -- function-based (`sctl.pp`, `sctl.pl`, `sctl.tl`) for modular workflows; `DATASET_class` for chainable end-to-end pipelines

## Example Workflows

The repository includes PBMC3K example notebooks demonstrating complete workflows:

1. QC and preprocessing
2. Normalization, HVG selection, and PCA
3. Leiden clustering and UMAP visualization
4. Differential expression gene analysis
5. Gene set enrichment analysis (GSEA)

The figures above and below are generated from [`00_sctl_functions_preprocessing_PBMC3K.ipynb`](https://github.com/gitbenlewis/single_cell_python_tools/blob/main/Example_notebooks/01_PBMC3k/00_sctl_functions_preprocessing_PBMC3K.ipynb), which walks through the full sctl preprocessing pipeline on the canonical PBMC3K dataset. Leiden clustering recovers 8 cell populations with all expected marker genes:

| Cluster | Markers | Cell Type |
|---------|---------|-----------|
| 0 | IL7R | CD4 T cells |
| 1 | CD14, LYZ | CD14+ Monocytes |
| 2 | MS4A1 | B cells |
| 3 | CD8A | CD8 T cells |
| 4 | GNLY, NKG7 | NK cells |
| 5 | FCGR3A, MS4A7 | FCGR3A+ Monocytes |
| 6 | FCER1A, CST3 | Dendritic Cells |
| 7 | PPBP | Megakaryocytes |

{% include figure.liquid loading="eager" path="assets/img/projects/sctl_umap_markers.png" title="PBMC3K — UMAP marker gene expression across 8 Leiden clusters. All canonical PBMC marker genes recovered." class="img-fluid rounded z-depth-1" %}

## Setup

```bash
git clone https://github.com/gitbenlewis/single_cell_python_tools.git
cd single_cell_python_tools

# Create environment and install package
conda env create -f sctl.yaml
conda activate sctl

# Or install in editable mode
pip install -e .
```

## Usage

**Function-based (modular):**
```python
import sctl.pp as pp
import sctl.pl as pl

# QC and preprocessing
pp.calculate_qc_metrics(adata)
pp.filter_cells(adata, min_genes=200, max_pct_mito=20)
pp.normalize_and_scale(adata)
pp.run_pca(adata)
pp.leiden_clustering(adata, resolution=0.5)

# Visualize
pl.plot_umap(adata, color=["leiden", "CD3D", "CD14"])
pl.plot_silhouette(adata)
```

**Class-based (pipeline):**
```python
from sctl import DATASET_class

ds = DATASET_class(adata)
ds.run_qc().normalize().find_hvgs().run_pca().cluster().plot_umap()
```

## Repository

Source code, example notebooks, and documentation:
[gitbenlewis/single_cell_python_tools](https://github.com/gitbenlewis/single_cell_python_tools)
