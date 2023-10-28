import pathlib

REMOVE_PATHS = [
    "{% if cookiecutter.use_github_actions == false %}.github{% endif %}",
    "{% if cookiecutter.use_tool_versions == false %}.tool-versions{% endif %}",
]


def main():
    rm_unused_files_and_dirs(REMOVE_PATHS)


def rm_unused_files_and_dirs(paths: list[str]) -> None:
    project_path = pathlib.Path(".")
    for path_str in paths:
        path_str = path_str.strip()
        if not path_str:
            continue

        path = project_path / pathlib.Path(path_str)
        remove_dir_recursively(path)


def remove_dir_recursively(path: pathlib.Path) -> None:
    if path.is_dir():
        for child in path.iterdir():
            remove_dir_recursively(child)
        path.rmdir()
    else:
        path.unlink()


if __name__ == "__main__":
    main()
