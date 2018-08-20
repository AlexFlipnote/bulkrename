# bulkrename
Rename multiple files in a folder to random characters

## Install
```
pip install bulkrename
```

## Usage
```
$ bulkrename -h
usage: [-h] [-v] [-l] [-r] [-nb] [-e EXCLUDE [EXCLUDE ...]] [-c [NUM]]

Rename multiple files in a folder to random characters

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Show the version number and exit
  -l, --logs            Shows which files it renames
  -r, --revert          Revert the renames with a backup file inside the
                        target
  -nb, --nobackup       Prevent the script to dump a JSON backup
  -e EXCLUDE [EXCLUDE ...], --exclude EXCLUDE [EXCLUDE ...]
                        Exclude file extensions
  -c [NUM], --characters [NUM]
                        Amount inserteded to Python token_urlsafe (Rename
                        length)
```
