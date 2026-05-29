# Quickstart

Most workflows import the package as `sctl` and then call the public namespaces:

```python
import single_cell_python_tools as sctl
```

## Notebook Path Setup

For notebook work outside an installed environment, add the parent directory
that contains this repository to `sys.path`:

```python
repo_parent_dir = "../../"

import sys
if repo_parent_dir not in sys.path:
    sys.path.append(repo_parent_dir)

import single_cell_python_tools as sctl
```

Editable installation with `pip install -e .` is usually simpler once the
environment is stable.

## Function-Based Workflow

Function-based workflows operate directly on an `AnnData` object:

```python
import scanpy as sc
import single_cell_python_tools as sctl

adata = sc.read_10x_mtx(data_directory_path)
adata.uns["parameters"] = pbmc3k_parameters

sctl.pp.basic_filitering(adata, **adata.uns["parameters"])
sctl.pp.annotate_n_view_adata_raw_counts(adata, **adata.uns["parameters"])
sctl.pp.filter_cells_by_anotated_QC_gene(adata, **adata.uns["parameters"])
sctl.pp.remove_genes(adata, **adata.uns["parameters"])
sctl.pp.process2scaledPCA(adata, **adata.uns["parameters"])
sctl.pp.leiden_clustering(adata, **adata.uns["parameters"])
sctl.pl.silhouette_score_n_plot(adata, **adata.uns["parameters"])
```

## DATASET_class Workflow

The high-level class stores parameters and `AnnData` state on the instance, then
returns `self` from many methods so calls can be chained:

```python
import single_cell_python_tools as sctl

pbmc3k_sctl_DATASET = sctl.DATASET_class(parameters=pbmc3k_parameters)

(
    pbmc3k_sctl_DATASET
    .download_data()
    .unpack_tar()
    .load_data()
    .basic_filitering()
    .annotate_n_view_adata_raw_counts()
    .filter_cells_by_anotated_QC_gene()
    .remove_genes()
    .process2scaledPCA()
    .leiden_clustering()
    .rename_leiden_clusters()
    .silhouette_score_n_plot()
    .marker_gene_umaps()
)
```

See [DATASET_class](DATASET_class.md) for the full method inventory.

