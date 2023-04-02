"""
Author:         Alexandre Desfosses
Creation date:  2023-03-30
Documentation:
References:
"""

import os


AVOID:      list = ["__pycache__", "build", "dist", ".egg-info", ".git", ".idea", "venv"]
DIRECTORY:  str = os.getcwd().split("\\")[-1]


def walk_directory() -> list:
    """
    Description...

    Returns:
    """

    all_paths: list = []
    for (path, directories, files) in os.walk(os.path.join(os.getcwd())):
        for file in files:
            all_paths.append(os.path.join(path, file))
    return all_paths


def trim_paths(all_paths: list) -> list:
    """
    Description...

    Args:
        all_paths:

    Returns:
    """

    for i in range(len(all_paths)):
        all_paths[i] = all_paths[i].split("\\".join(os.getcwd().split("\\")[-2:]))
        all_paths[i] = all_paths[i][-1]
        all_paths[i] = all_paths[i].lstrip("\\")
        all_paths[i] = all_paths[i].split("\\")
    return all_paths


def filter_subdirectories(all_paths: list) -> list:
    """
    Description...

    Args:
        all_paths:

    Returns:
    """

    to_remove = set()
    for index in range(len(all_paths)):
        for element in AVOID:
            if element in all_paths[index]:
                to_remove.add(index)

    to_remove = sorted(to_remove, reverse=True)
    for index in to_remove:
        all_paths.remove(all_paths[index])
    return all_paths


def group_by_subdirectories(all_paths: list, parsed_path: dict) -> list:
    """
    Description...

    Args:
        all_paths:
        parsed_path:

    Returns:
    """

    for line in all_paths:
        if line[0] not in parsed_path.keys():
            parsed_path[line[0]] = line[1:]
        else:
            parsed_path[line[0]].append(line[1:])
    return all_paths


def print_directory_tree() -> None:
    """
    Description...

    Returns:
    """

    print()
    print(DIRECTORY + "/")

    all_paths: list = walk_directory()

    all_paths = trim_paths(all_paths)

    all_paths = filter_subdirectories(all_paths)

    # Here build a dictionary by parsing lines before printing (need to aggregate lines for subdirs)
    parsed_paths = {}
    all_paths = group_by_subdirectories(all_paths, parsed_paths)

    for line in sorted(all_paths, key=lambda x: x[0]):
        if len(line) == 1:
            print("   - " + line[0])
        else:
            index = 0
            while index != len(line) - 1:
                subdir = line[index]
                print("   " * (index + 1) + "- " + subdir + "/")
                index += 1
            print("   " * (index + 1) + "- " + line[-1])


if __name__ == '__main__':
    print_directory_tree()
