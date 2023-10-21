import pathlib

REMOVE_PATHS = [
    "{% if cookiecutter.use_tool_versions == false %}.tool-versions{% endif %}",
]


def main():
    rm()


def rm():
    project_path = pathlib.Path(".")
    for path_str in REMOVE_PATHS:
        path_str = path_str.strip()
        path = project_path / pathlib.Path(path_str)

        if path_str and path.exists():
            if path.is_dir():
                path.rmdir()
            else:
                path.unlink()


if __name__ == "__main__":
    main()
