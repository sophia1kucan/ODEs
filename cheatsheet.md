## most things are self-documenting. type <command> --help may give clues or <commad> <partial params> --help 

---
### terminal commands
A bunch of useful commands for the terminal usage.

- ls - list files
- htop - show activity
- cd - change directory
- pwd - path to the working directory (where you are)
- tree - show contents
- cat - dump file to screen
- wc - word count
- | - 'pipe' channel output from one program to another eg. ```cat filename | wc -list```
- 'cd -' - change directory to previous directory
- pushd directory - change directory to new directory and push current directory on the stack
- popd - go to the last pushed directory on the stack
- mv a b - move object a to object b but really this is a rename
- rm \<object\>- remove object
- grep - search in files for patterns. e.g.
    ```cat somefile.txt | grep -E "sophia kucan"``` matches all lines in the file that contain "sophia kucan". important concept here is regular expressions. so you can do something like this too: ```cat somefile.txt | grep -E "(sophia)|(lev) kucan"``` which will match all the lines contaning "sophia kucan" or "lev kucan"
- kill -9  \<pid\> - kill a program identified by the process id (pid)


---
### conda/mamba commands
mamba is a newer and better conda, almost 100% compatible. it is much faster so use mamba where possible. if a mamba command doesnt work, it may be worth trying conda
- mamba is just the new conda
- an environment is a python installation with a set of target packages
- you can have multiple independent environments with different possibly conflicting packages
- mamba env list - list all environments
- mamba create -n newenv - creates a new mamba/conda/python environment called 'newenv'
- mamba activate newenv - activates (makes current) the newenv environment
- mamba install \<package\>[=version] - installs a package into the active environment. You can target a different environment by specifying -n'env'
- mamba list - lists packages in active environment 


---
### git commands
git is used to managa source code. makes sure you dont lose code. you can use versions, and also branches for developing with others.
- git init . - initialises/creates a brand new git repository in the current folder
- git add ./\<some path\> - adds changes for submission
- git commit . - commits changes locally
- git push - push changes to remote repository
- git pull - pull changes from remote repository
