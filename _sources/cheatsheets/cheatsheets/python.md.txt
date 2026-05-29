# Python Cheatsheet

## Run Python

```bash
# show Python version
python --version

# start an interactive Python shell
python

# run a Python script
python script.py

# run a module as a script
python -m module_name

# run one line of Python
python -c "print('hello')"
```

## Virtual Environments and Packages

```bash
# create a virtual environment
python -m venv .venv

# activate a virtual environment on macOS or Linux
source .venv/bin/activate

# deactivate the active virtual environment
deactivate

# upgrade pip
python -m pip install --upgrade pip

# install packages
python -m pip install pandas numpy

# save installed packages
python -m pip freeze > requirements.txt

# install packages from a requirements file
python -m pip install -r requirements.txt
```

## Basic Script Pattern

```python
# define the script entrypoint
def main():
    print("hello")


# run main only when this file is executed directly
if __name__ == "__main__":
    main()
```

## Imports and Paths

```python
# import a standard library module
from pathlib import Path

# build a path safely
data_path = Path("data") / "input.csv"

# check whether a file exists
if data_path.exists():
    print(data_path)

# list files matching a pattern
for path in Path("data").glob("*.csv"):
    print(path)
```

## File I/O

```python
# read a whole text file
with open("input.txt", "r") as file:
    text = file.read()

# write text to a file
with open("output.txt", "w") as file:
    file.write("hello\n")

# read a CSV file with pandas
import pandas as pd

df = pd.read_csv("data.csv")

# write a CSV file with pandas
df.to_csv("output.csv", index=False)
```

## Lists and Dictionaries

```python
# create a list
values = [1, 2, 3]

# add an item to a list
values.append(4)

# loop over a list
for value in values:
    print(value)

# create a dictionary
sample = {"name": "A", "count": 10}

# get a dictionary value
count = sample["count"]
```

## Functions and Errors

```python
# define a function
def add_one(value):
    return value + 1

# call a function
result = add_one(10)

# raise an error when input is invalid
if result < 0:
    raise ValueError("result must be nonnegative")
```

## Command Line Arguments

```python
# parse command line arguments
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
args = parser.parse_args()

print(args.input)
```

## Debugging

```bash
# run a script with the Python debugger
python -m pdb script.py

# run tests with pytest
python -m pytest
```

```python
# stop execution at a breakpoint
breakpoint()

# print a quick debug value
print(f"value={value!r}")
```
