import sys
import shlex
import os
import bulkrename
import secrets

from bulkrename import argpar, question


def renamer(exclude=[], logs=None, char=8):
    for file in os.listdir():
        name = file.split(".")
        randomname = secrets.token_urlsafe(char)

        if exclude:
            if name[-1] in exclude or f".{name[-1]}" in exclude:
                if logs:
                    print(f"Skipped {file}")
                continue

        if logs:
            print(f"Renamed {file} to {randomname}.{name[-1]}")

        os.rename(file, f"{randomname}.{name[-1]}")


def shell():
    arguments = argpar.getarg()
    parser = argpar.Arguments(description="Rename multiple files in a folder to random characters")
    parser.add_argument('-v', '--version', action='store_true', help='Show the version number and exit')
    parser.add_argument('-l', '--logs', action='store_true', help='Shows which files it renames')
    parser.add_argument('-e', '--exclude', nargs='+', help='Exclude file extensions')
    parser.add_argument('-c', '--characters', nargs='?', type=int, metavar="NUM", default=8, help='Amount inserteded to Python token_urlsafe (Rename length)')

    try:
        args = parser.parse_args(shlex.split(arguments))
    except Exception as e:
        print(e)
        sys.exit(0)

    if args.characters:
        if not 1 <= args.characters <= 25:
            print("You can only have a value between 1 to 25, stopped script...")
            sys.exit(0)

        if not args.characters == 8:
            print(f"Character length: {args.characters}")

    if args.version:
        print(bulkrename.__version__)
        sys.exit(0)

    if args.exclude:
        toexclude = ", ".join(args.exclude)
        print(f"Excluding file types: {toexclude}")

    if args.logs:
        print("Rename logs: Enabled")
    else:
        print("Rename logs: Disabled")

    print(f"Current target: {os.getcwd()}\n")

    if question.query_yes_no("Are you sure you want to rename all files inside here?"):
        renamer(
            exclude=args.exclude,
            logs=args.logs,
            char=args.characters
        )
    else:
        print("Stopped...")


def main():
    try:
        shell()
    except KeyboardInterrupt:
        print('\nCancelling...')


if __name__ == '__main__':
    main()
