import os

PATH_SRC = os.path.join(os.getcwd(), "src")
PATH_OUT = os.path.join(os.getcwd(), "out")

# Compare files


def compare_files():
    missing_files = []
    extra_files = []
