---
layout: page
title: adata_science_tools
description: Python data science toolkit for differential analysis and visualization on AnnData objects.
img: assets/img/projects/baseline.png
importance: 2
category: work
github: https://github.com/gitbenlewis/adata_science_tools
---

{% include figure.liquid loading="eager" path="assets/img/projects/baseline.png" title="Simulated correlation dotplot with marginal distributions" class="img-fluid rounded z-depth-1" %}

## Overview

A Python data science toolkit that operates on AnnData objects, providing config-driven workflows for differential analysis, custom plotting, and simulated data generation. The library includes column plots, volcano plots, correlation dotplots with marginal histograms, and a simulation framework for generating reproducible test datasets with configurable covariates.

## Key Features

- **Differential analysis plotting** -- bar/dotplot combinations showing log2 fold-change with FDR-corrected p-values and per-feature data distributions
- **Volcano plots** -- configurable significance thresholds with multi-level alpha shading and gene labeling
- **Correlation dotplots** -- scatter plots with per-group regression fits, Pearson correlations, and marginal histograms/KDEs
- **Data simulation** -- config-driven AnnData generation with tunable betas, covariates (e.g. age, case/control), and residual variance
- **AnnData-native** -- all tools operate directly on AnnData objects for seamless integration with scanpy workflows

## Example Plots

### Correlation Dotplot (Simulated Data)

{% include figure.liquid loading="eager" path="assets/img/projects/baseline.png" title="Simulated feature vs Age with case/control group fits" class="img-fluid rounded z-depth-1" %}

Scatter plot with per-group linear regression fits, Pearson correlation statistics, and marginal histograms. Generated from the simulated data workflow in `example_simulated_data/`.

### Differential Log2FC Dotplot (OLINK Proteomics)

{% include figure.liquid loading="eager" path="assets/img/projects/COVID_over_NOT_D0_barh_l2fc_dotplot_FDR.png" title="Top 15 differential features - COVID over NOT at D0" class="img-fluid rounded z-depth-1" %}

Combined bar and dotplot showing per-feature OLINK distributions alongside log2 fold-change with FDR-scaled dot sizes. Data from PMID 33969320.

### Volcano Plot (OLINK Proteomics)

{% include figure.liquid loading="eager" path="assets/img/projects/COVID_over_NOT_D0_volcano_FDR.png" title="Volcano plot - COVID over NOT at D0" class="img-fluid rounded z-depth-1" %}

Volcano plot with multi-level significance coloring (alpha 0.2, 0.1, 0.05) and log2FC threshold lines. FDR-corrected t-test p-values.

## Setup

```bash
git clone https://github.com/gitbenlewis/adata_science_tools.git
conda env create -f config/env_not_base.yaml -n not_base
conda activate not_base
```

## Running the Examples

```bash
# OLINK proteomics differential analysis (PMID 33969320)
bash example_PMID_33969320/scripts/000_run_everything.bash

# Simulated data with configurable covariates
python example_simulated_data/scripts/simulate_1_var_covar_age.py
python example_simulated_data/scripts/plot_dotplot_simulate_1_var_covar_age.py
```

## Repository

Source code and documentation:
[gitbenlewis/adata_science_tools](https://github.com/gitbenlewis/adata_science_tools)
