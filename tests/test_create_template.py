def test_run_cookiecutter_default(cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "python_project"
    assert result.project_path.is_dir()

    assert result.project_path.joinpath("README.md").is_file()
    assert result.project_path.joinpath("LICENSE").is_file()
    assert result.project_path.joinpath("pyproject.toml").is_file()
    assert result.project_path.joinpath(".pre-commit-config.yaml").is_file()
    assert result.project_path.joinpath(".editorconfig").is_file()
    assert result.project_path.joinpath(".tool-versions").is_file()

    assert result.project_path.joinpath(".github").is_dir()
    assert result.project_path.joinpath(".github", "PULL_REQUEST_TEMPLATE.md").is_file()
    assert (
        result.project_path.joinpath(".github")
        .joinpath("workflows", "ci.yml")
        .is_file()
    )

    assert result.project_path.joinpath("src").is_dir()
    assert result.project_path.joinpath("src", "main.py").is_file()
    assert result.project_path.joinpath("src", "__init__.py").is_file()

    assert result.project_path.joinpath("tests").is_dir()
    assert result.project_path.joinpath("tests", "__init__.py").is_file()
    assert result.project_path.joinpath("tests", "test_main.py").is_file()


def test_run_cookiecutter_without_tool_version(cookies):
    result = cookies.bake(extra_context={"use_tool_versions": False})

    assert result.project_path.joinpath(".tool-versions").is_file() is False

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "python_project"
    assert result.project_path.is_dir()

    assert result.project_path.joinpath("README.md").is_file()
    assert result.project_path.joinpath("LICENSE").is_file()
    assert result.project_path.joinpath("pyproject.toml").is_file()
    assert result.project_path.joinpath(".pre-commit-config.yaml").is_file()
    assert result.project_path.joinpath(".editorconfig").is_file()

    assert result.project_path.joinpath(".github").is_dir()
    assert result.project_path.joinpath(".github", "PULL_REQUEST_TEMPLATE.md").is_file()
    assert (
        result.project_path.joinpath(".github")
        .joinpath("workflows", "ci.yml")
        .is_file()
    )

    assert result.project_path.joinpath("src").is_dir()
    assert result.project_path.joinpath("src", "main.py").is_file()
    assert result.project_path.joinpath("src", "__init__.py").is_file()

    assert result.project_path.joinpath("tests").is_dir()
    assert result.project_path.joinpath("tests", "__init__.py").is_file()
    assert result.project_path.joinpath("tests", "test_main.py").is_file()


def test_run_cookiecutter_without_github(cookies):
    result = cookies.bake(extra_context={"use_github_actions": False})

    assert result.project_path.joinpath(".github").is_dir() is False

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "python_project"
    assert result.project_path.is_dir()

    assert result.project_path.joinpath("README.md").is_file()
    assert result.project_path.joinpath("LICENSE").is_file()
    assert result.project_path.joinpath("pyproject.toml").is_file()
    assert result.project_path.joinpath(".pre-commit-config.yaml").is_file()
    assert result.project_path.joinpath(".editorconfig").is_file()

    assert result.project_path.joinpath("src").is_dir()
    assert result.project_path.joinpath("src", "main.py").is_file()
    assert result.project_path.joinpath("src", "__init__.py").is_file()

    assert result.project_path.joinpath("tests").is_dir()
    assert result.project_path.joinpath("tests", "__init__.py").is_file()
    assert result.project_path.joinpath("tests", "test_main.py").is_file()
