# Example Plot Source Citations

Reviewed on 2026-05-28.

This note maps the example/reference plots in
`python_refactor_goal_sources/goal_plots/` to the primary papers, data sources,
or documentation pages that produced or motivated them. The clean gallery images
in `python_refactor_goal_sources/generated_plots/clean/` use deterministic local
TSV/JSON fixtures to recreate the visual structure of those sources; the
Python/fuc fixtures are compact derivatives of upstream `sbslee/fuc-data`.

Local source files reviewed:

- `python_refactor_goal_sources/source_info_for_training.md`
- `python_refactor_goal_sources/config.yaml`
- `python_refactor_goal_sources/fuc_sources/manifest.json`
- `python_refactor_goal_sources/ggoncoplot/paper/paper.md`
- `python_refactor_goal_sources/ggoncoplot/paper/paper.bib`
- `python_refactor_goal_sources/ggoncoplot/inst/CITATION`

## Plot-To-Source Map

| Goal plots | Example family | Read/cite first | Source URL |
| --- | --- | --- | --- |
| `goal_plot_01.png` | ggoncoplot paper Figure 1, TCGA BRCA | El-Kamand et al. 2025; Goldman et al. 2020; Ellrott et al. 2018; TCGA Research Network | https://doi.org/10.21105/joss.07390 |
| `goal_plot_02.png` - `goal_plot_07.png` | ggoncoplot README/pkgdown examples and package assets | El-Kamand et al. 2025; ggoncoplot documentation | https://selkamand.github.io/ggoncoplot/ |
| `goal_plot_08.png` | ggoncoplot package comparison table | El-Kamand et al. 2025; Gu 2022; Mayakonda et al. 2018; Skidmore et al. 2016 | https://doi.org/10.21105/joss.07390 |
| `goal_plot_09.png` - `goal_plot_12.png` | ggoncoplot multimodal linked-selection figures | El-Kamand et al. 2025; Goldman et al. 2020; Ellrott et al. 2018; TCGA Research Network | https://www.theoj.org/joss-papers/joss.07390/10.21105.joss.07390.pdf |
| `goal_plot_13.png` | ggoncoplot GBM paper asset | El-Kamand et al. 2025; TCGA/MC3-derived GBM test data | https://github.com/selkamand/ggoncoplot/tree/main/paper |
| `goal_plot_14.png` | Chinese breast tumor oncoplot | Zhang et al. 2019 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6526269/ |
| `goal_plot_15.png` | Metastatic cutaneous squamous cell carcinoma alteration matrix | Thind et al. 2022 | https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2022.919118/full |
| `goal_plot_16.png` | Glioblastoma clinical/molecular panel | Hoogstrate et al. 2023 | https://www.sciencedirect.com/science/article/pii/S1535610823000478 |
| `goal_plot_17.png` - `goal_plot_19.png`, `goal_plot_21.png` | AML/fuc oncoplot tutorial examples | Lee, fuc tutorials and fuc-data TCGA-LAML fixtures | https://sbslee-fuc.readthedocs.io/en/latest/tutorials.html |
| `goal_plot_20.png` | fuc structural-variation VCF tutorial example | Lee, fuc tutorials; Biostars post linked in the source map | https://www.biostars.org/p/9493544/ |

## Directly Used Papers

These are the main papers behind source figures used as reference/example plots.

1. El-Kamand S, Quinn JMW, Cowley MJ. ggoncoplot: an R package for interactive visualisation of somatic mutation data from cancer patient cohorts. Journal of Open Source Software. 2025;10(115):7390. doi:10.21105/joss.07390. https://doi.org/10.21105/joss.07390

2. Zhang G, Wang Y, Chen B, et al. Characterization of frequently mutated cancer genes in Chinese breast tumors: a comparison of Chinese and TCGA cohorts. Annals of Translational Medicine. 2019;7(8):179. doi:10.21037/atm.2019.04.23. https://pmc.ncbi.nlm.nih.gov/articles/PMC6526269/

3. Thind AS, Ashford B, Strbenac D, Mitchell J, Lee J, Mueller SA, Minaei E, Perry JR, Ch'ng S, Iyer NG, Clark JR, Gupta R, Ranson M. Whole genome analysis reveals the genomic complexity in metastatic cutaneous squamous cell carcinoma. Frontiers in Oncology. 2022;12:919118. doi:10.3389/fonc.2022.919118. https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2022.919118/full

4. Hoogstrate Y, Draaisma K, Ghisai SA, et al. Transcriptome analysis reveals tumor microenvironment changes in glioblastoma. Cancer Cell. 2023;41(4):678-692.e7. doi:10.1016/j.ccell.2023.02.019. https://www.sciencedirect.com/science/article/pii/S1535610823000478

## TCGA And Xena Data Sources

The ggoncoplot paper states that its TCGA breast carcinoma and multimodal
examples use TCGA Research Network data, with methylation, expression, and
somatic mutation data obtained from the Xena TCGA Pan-Cancer Atlas Hub.

1. The Cancer Genome Atlas Research Network. The Cancer Genome Atlas Program. National Cancer Institute. https://www.cancer.gov/tcga

2. Goldman MJ, Craft B, Hastie M, Repecka K, McDade F, Kamath A, Banerjee A, Luo Y, Rogers D, Brooks AN, Zhu J, Haussler D. Visualizing and interpreting cancer genomics data via the Xena platform. Nature Biotechnology. 2020;38(6):675-678. doi:10.1038/s41587-020-0546-8. https://doi.org/10.1038/s41587-020-0546-8

3. Ellrott K, Bailey MH, Saksena G, Covington KR, Kandoth C, Stewart C, Hess J, Ma S, Chiotti KE, McLellan M, Sofia HJ, Hutter C, Getz G, Wheeler D, Ding L, MC3 Working Group, The Cancer Genome Atlas Research Network. Scalable open science approach for mutation calling of tumor exomes using multiple genomic pipelines. Cell Systems. 2018;6(3):271-281.e7. doi:10.1016/j.cels.2018.03.002. https://doi.org/10.1016/j.cels.2018.03.002

## Documentation And Source Image Pages

These are not all primary research papers, but they are the direct public source
locations for several imported reference images.

1. Lee S. fuc documentation: Tutorials. Read the Docs. Revision 7b0fbfbd. Accessed 2026-05-26. https://sbslee-fuc.readthedocs.io/en/latest/tutorials.html

2. Lee S. fuc-data image assets. GitHub. Accessed 2026-05-26. https://github.com/sbslee/fuc-data/tree/main/images

3. Lee S. fuc-data TCGA-LAML and pyvcf example datasets. GitHub. Accessed 2026-05-26. https://github.com/sbslee/fuc-data

4. El-Kamand S, Quinn JMW, Cowley MJ. ggoncoplot source repository, paper assets, and README figures. GitHub. Accessed 2026-05-26. https://github.com/selkamand/ggoncoplot

5. El-Kamand S, Quinn JMW, Cowley MJ. Easily Create Interactive Oncoplots: ggoncoplot package site. Accessed 2026-05-26. https://selkamand.github.io/ggoncoplot/

6. Biostars post referenced by the local source map for the structural-variation example. https://www.biostars.org/p/9493544/

## Supporting Visualization References

These papers are cited by the ggoncoplot paper and are useful background for the
comparison-table example (`goal_plot_08.png`), but they
are not themselves the source images.

1. Gu Z. Complex heatmap visualization. iMeta. 2022;1(3):e43. doi:10.1002/imt2.43. https://doi.org/10.1002/imt2.43

2. Mayakonda A, Lin DC, Assenov Y, Plass C, Koeffler HP. Maftools: efficient and comprehensive analysis of somatic variants in cancer. Genome Research. 2018;28:1747-1756. doi:10.1101/gr.239244.118. https://doi.org/10.1101/gr.239244.118

3. Skidmore ZL, Wagner AH, Lesurf R, Campbell KM, Kunisaki J, Griffith OL, Griffith M. GenVisR: Genomic Visualizations in R. Bioinformatics. 2016;32:3012-3014. doi:10.1093/bioinformatics/btw325. https://doi.org/10.1093/bioinformatics/btw325

4. Cerami E, Gao J, Dogrusoz U, Gross BE, Sumer SO, Aksoy BA, Jacobsen A, Byrne CJ, Heuer ML, Larsson E, Antipin Y, Reva B, Goldberg AP, Sander C, Schultz N. The cBio Cancer Genomics Portal: an open platform for exploring multidimensional cancer genomics data. Cancer Discovery. 2012;2(5):401-404. doi:10.1158/2159-8290.CD-12-0095. https://doi.org/10.1158/2159-8290.CD-12-0095

## Notes

- The generated PyOncoplot gallery uses fixture data in
  `python_refactor_goal_sources/syntheitic_goal_data/`; most files are
  deterministic stand-ins, while the Python/fuc AML and SV files are compact
  derivatives of upstream fuc-data examples.
- The original numbered goal plots are source/reference images and should stay
  immutable.
- The spelling `syntheitic_goal_data` matches the existing repository path.
