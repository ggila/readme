# README: utils, comment models and policy

## utils

Goal:
* easy to get with
* won't mess with previous existing readme
* avoid out-dated comment

### command makeREADME

    > makeREADME -h --help
    Update 'README.md' in cwd
    * -r --recursive: called recursively bottom to top and update all 'README.md'. If a new 'README.md' is to be created, user should confirm creation
    * -m --manual-merge: create a new README.md copy 'README.md'
    * -c --clear: clear 'README.md.backup'
    * -i --info:

    
    Gathers info from
    * 'README.md' in cwd
    * 'README.md' found in direct subdir
    * commentis found in each code file (python, playbook and script shell for now)

    Merge all infos and write result in 'README.md'
    
## comment policy in code file

* english
* each file should contain a description
* each class should contain at least a one-line description comment
* each point d'entre contain at least a one-line description comment
* more than one-line comment should be avoid

## models

Three kinds of Readme
* some with info about models
* some with info about snippets and files
* some are mix of both

info about snippets and files should be written in source code.
Ideally:
* each new file should contain at least a one-line description
* each class should contain at least a one-line description
* each point d'entre contain at least a one-line description


info about model 
