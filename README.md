# DirectoryTree
A simplified representation of a file system written in python

A coding challenge completed by Nathan Foote for the Endpoint interview process.

## Quick Start ##
In order to run the application, run the `directory_app.py` file in the `Endpoint_Coding_Test` directory.

```
python Endpoint_Coding_Test/directory_app.py
```

## User Guide
### List of commands
#### CREATE
This command is used to create a new directory in the file system. Directories can be created at any level of the file system and within already existing directories. When creating a nested directory, parent directories will be created if they do not currently exist. 

Cannot be used to create a directory that already exists in the file system.
##### Arguments: [new_directory_name]
##### Usage:
```
CREATE food/fruits/apples/fuji
```
#### LIST
This command is used to display a heirarchical visualization of all directories that currently exist inside the file system. Directories that are children of another directory will be displayed beneith the parent and indented.
##### Usage:
```
LIST
```
#### MOVE
This command is used to move a source directory into a target directory. The source directory will be nested beneith the target directory and will be removed from its original location.

Cannot be used to move a directory that does not already exist in the file system.
##### Arguments: [source_directory] [target_directory]
##### Usage:
```
MOVE grains/squash vegetables
```
#### DELETE
This command is used to remove a given directory and all of its children directories from the file system.

Cannot be used to delete a directory that does not already exist in the file system.
##### Arguments: [directory_name]
##### Usage:
```
DELETE foods/fruits/apples
```
#### EXIT
This command will terminate the program execution.
