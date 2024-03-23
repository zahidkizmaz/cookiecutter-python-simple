alias i := install
alias c := compile
alias ci := compile-install

install:
	uv pip install -r requirements-dev.txt

compile:
	uv pip compile --extra=dev -o requirements-dev.txt pyproject.toml

compile-install: compile install
