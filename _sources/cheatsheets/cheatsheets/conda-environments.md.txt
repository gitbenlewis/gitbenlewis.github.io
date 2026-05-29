# Conda Environments Cheatsheet

## Setup

```bash
# show conda version
conda --version

# update conda in the base environment
conda update -n base conda

# add conda-forge as a package channel
conda config --add channels conda-forge

# add bioconda as a package channel
conda config --add channels bioconda

# use strict channel priority
conda config --set channel_priority strict
```

## Create and Activate

```bash
# create an environment with a Python version
conda create -n project-env python=3.11

# create an environment with starter packages
conda create -n project-env python=3.11 pandas numpy

# activate an environment
conda activate project-env

# deactivate the active environment
conda deactivate

# list all environments
conda env list
```

## Install and Update Packages

```bash
# install packages into the active environment
conda install pandas numpy matplotlib

# install packages from conda-forge
conda install -c conda-forge seaborn scikit-learn

# install packages from bioconda
conda install -c bioconda samtools

# update one package
conda update pandas

# update all packages in the active environment
conda update --all

# list installed packages
conda list
```

## Environment Files

```bash
# export the active environment with exact package builds
conda env export > environment.yml

# export only manually requested packages
conda env export --from-history > environment.yml

# create an environment from a file
conda env create -f environment.yml

# update an environment from a file
conda env update -f environment.yml --prune

# remove an environment
conda env remove -n project-env
```

## Jupyter Kernels

```bash
# install Jupyter kernel support in the active environment
conda install ipykernel

# register the active environment as a Jupyter kernel
python -m ipykernel install --user --name project-env --display-name "Python (project-env)"

# list Jupyter kernels
jupyter kernelspec list

# remove a Jupyter kernel
jupyter kernelspec uninstall project-env
```

## Clean Up

```bash
# remove unused package tarballs and caches
conda clean --all

# remove one package from the active environment
conda remove package-name

# show environment details
conda info

# search for a package
conda search package-name
```
