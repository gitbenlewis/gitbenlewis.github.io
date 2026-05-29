# R Cheatsheet

## Run R

```bash
# start an interactive R session
R

# run an R script
Rscript analysis.R

# run one expression from the shell
Rscript -e "print('hello')"
```

## Packages

```r
# install a package from CRAN
install.packages("tidyverse")

# load a package
library(tidyverse)

# show installed packages
installed.packages()

# update installed packages
update.packages()

# remove a package
remove.packages("package_name")
```

## Working Directory and Files

```r
# show the current working directory
getwd()

# set the working directory
setwd("path/to/project")

# list files in the working directory
list.files()

# read a CSV file
df <- read.csv("data.csv")

# write a CSV file
write.csv(df, "output.csv", row.names = FALSE)

# save an R object
saveRDS(df, "data.rds")

# read an R object
df <- readRDS("data.rds")
```

## Vectors, Lists, and Factors

```r
# create a vector
values <- c(1, 2, 3)

# create a named list
sample <- list(name = "A", count = 10)

# get a list value by name
sample$count

# create a factor
group <- factor(c("control", "treated", "control"))

# show factor levels
levels(group)
```

## Data Frames

```r
# create a data frame
df <- data.frame(sample = c("A", "B"), count = c(10, 20))

# show the first rows
head(df)

# show column names
names(df)

# summarize columns
summary(df)

# select one column
df$count

# filter rows with base R
df[df$count > 10, ]
```

## dplyr

```r
# load dplyr from tidyverse
library(dplyr)

# filter rows
df_filtered <- df %>%
  filter(count > 10)

# select columns
df_selected <- df %>%
  select(sample, count)

# add a new column
df_mutated <- df %>%
  mutate(double_count = count * 2)

# summarize by group
df_summary <- df %>%
  group_by(sample) %>%
  summarize(total = sum(count), .groups = "drop")
```

## Plotting

```r
# make a base R scatter plot
plot(df$count, df$count)

# load ggplot2 from tidyverse
library(ggplot2)

# make a ggplot scatter plot
ggplot(df, aes(x = sample, y = count)) +
  geom_col()

# save the last ggplot
ggsave("plot.png", width = 6, height = 4, dpi = 300)
```

## Jupyter and RStudio

```r
# install the R Jupyter kernel
install.packages("IRkernel")

# register the R kernel for Jupyter
IRkernel::installspec(user = TRUE)
```

```bash
# open RStudio from a project directory when available
rstudio .
```
