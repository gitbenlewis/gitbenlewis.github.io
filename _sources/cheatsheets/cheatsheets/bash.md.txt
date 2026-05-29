# Bash Cheatsheet

## Navigation

```bash
# show the current directory
pwd

# list files in the current directory
ls

# list files with details and hidden files
ls -lah

# move to the home directory
cd

# move into a directory
cd path/to/project

# move up one directory
cd ..

# return to the previous directory
cd -
```

## Files and Directories

```bash
# create a directory
mkdir new_folder

# create nested directories
mkdir -p data/raw

# create an empty file
touch notes.txt

# copy a file
cp source.txt destination.txt

# copy a directory
cp -r source_folder destination_folder

# move or rename a file
mv old_name.txt new_name.txt

# remove a file
rm file.txt

# remove an empty directory
rmdir empty_folder

# remove a directory and its contents
rm -r folder_name
```

## View Files

```bash
# print a whole file
cat file.txt

# page through a file
less file.txt

# show the first lines
head file.txt

# show the last lines
tail file.txt

# follow a growing log file
tail -f log.txt

# count lines, words, and bytes
wc file.txt
```

## Search

```bash
# search a file for text
grep "pattern" file.txt

# search all files below the current directory
grep -R "pattern" .

# find files by name
find . -name "*.py"

# find directories by name
find . -type d -name "data"

# locate commands on the PATH
which python
```

## Pipes and Redirects

```bash
# send command output into another command
ls -lah | less

# save command output to a file
ls -lah > files.txt

# append command output to a file
date >> log.txt

# send errors to a file
python script.py 2> errors.txt

# send output and errors to one file
python script.py > run.log 2>&1
```

## Permissions

```bash
# show file permissions
ls -l script.sh

# make a script executable
chmod +x script.sh

# remove write permission for group and others
chmod go-w file.txt

# change file owner
chown user:group file.txt
```

## Environment and History

```bash
# print an environment variable
echo "$PATH"

# set an environment variable for the current shell
export PROJECT_DIR="$HOME/projects/my_project"

# run one command with a temporary variable
PROJECT_DIR=data python script.py

# show command history
history

# search command history interactively
ctrl-r
```

## Processes

```bash
# show running processes
ps aux

# show live system activity
top

# stop a process by process ID
kill PID

# force stop a process by process ID
kill -9 PID

# run a command in the background
python script.py &

# show background jobs
jobs
```
