---
layout: page
title: Blood Collection Dashboard
description: Interactive Plotly Dash app for monitoring biomarker collection progress in clinical trials.
img: assets/img/projects/blood_collection_dashboard.png
importance: 1
category: work
github: https://github.com/gitbenlewis/blood_collection_dashboard
---

{% include figure.liquid loading="eager" path="assets/img/projects/blood_collection_dashboard.png" title="Blood Collection Dashboard" class="img-fluid rounded z-depth-1" %}

## Overview

A config-driven Plotly Dash web application for monitoring clinical trial biomarker collection progress. The dashboard visualizes collection rates across multiple derived biomarker types (plasma, serum, PBMC) constrained to visits where the primary blood sample was collected, with interactive charts and per-visit metrics across a simulated 100-participant cohort.

## Tech Stack

- Dash 4.1.0 (interactive web framework)
- Dash Bootstrap Components 2.0.4 (responsive layout)
- Plotly 6.6.0 (interactive charts)
- Pandas 2.3.3 (data manipulation)
- PyYAML 6.0.3 (config parsing)

## Key Features

- **Multi-tab interface** for tracking blood, plasma, serum, and PBMC collection independently
- **KPI metric cards** showing overall collection rate, samples collected, samples not collected, and total participants
- **Per-visit bar charts** with collection percentage overlays and 50% threshold reference line
- **Participant distribution histogram** revealing collection rate spread across the cohort
- **Participant-by-visit heatmap** displaying collection status for every participant across all timepoints

## Config-Driven Architecture

The entire application is driven by a single `config.yaml` file that defines:

- **Datasets** -- CSV file paths, column mappings, collected/not-collected value labels, and random seeds
- **Source constraints** -- one dataset marked `is_source: true` (blood collection); derived datasets (plasma, serum, PBMC) are constrained so collection is only possible at visits where the source sample was collected
- **UI settings** -- color schemes, chart dimensions, heatmap row heights, typography, and font sizes

This design allows non-programmers to add new datasets, adjust colors, or modify cohort parameters by editing YAML alone with no code changes required.

## Data Simulation

The `generate_data.py` script creates reproducible test datasets using seeded randomness:

1. Generates the source blood collection CSV across 100 participants and visits
2. Creates a source mask recording which participant-visit combinations have blood collected
3. Generates three derived CSVs (plasma, serum, PBMC) where collection is only possible where the source mask is `True`

## Repository

Source code and documentation:
[gitbenlewis/blood_collection_dashboard](https://github.com/gitbenlewis/blood_collection_dashboard)
