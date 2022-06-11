#!/usr/bin/env python3
import argparse
import os


current_directory = os.path.abspath(".")


# ext and here command
file_map = {
    "py": "python {0}",
    "rs": "cargo run",
    "cpp": "g++ {0} -o {1} && ./{1}",
    "c": "gcc {0} -o {1} && ./{1}",
}


# make parser argument
parser = argparse.ArgumentParser()
parser.add_argument(
        "-f",
        help="put file name here",
        nargs="?"
        )
args = parser.parse_args()


def main():
    if args.f is not None:
        file_name = args.f
        file = file_name.split(".")
        if len(file) == 2 and os.path.exists(os.path.join(current_directory, file_name)):
            name, ext = file 
            command = file_map[ext]
            if ext == "py":
                print(command.format(file_name))
                os.system(command.format(file_name))
            elif ext == "rs":
                print(command)
                os.system(command)
            elif ext == "cpp" or ext == "c":
                print(command.format(file_name, name))
                os.system(command.format(file_name, name))
            else:
                print("this programme can't compile or run this file")
        else:
            print("file not found")
    else:
        print("verify your parameter")


if __name__ == "__main__":
    main()
