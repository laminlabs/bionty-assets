import nox
from laminci.nox import build_docs, login_testuser1, run_pre_commit, run_pytest

nox.options.default_venv_backend = "none"


@nox.session
def lint(session: nox.Session) -> None:
    run_pre_commit(session)


@nox.session()
def build(session):
    session.run(*"pip install -e .[dev]".split())
    login_testuser1(session)
    run_pytest(session)
    build_docs(session, strict=True)
