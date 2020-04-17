import os


def relative_path(filename, file=__file__):
    base_path = os.path.dirname(file)
    return os.path.join(base_path, filename)
