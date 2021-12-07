from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)
@task
def test(ctx):
    ctx.run("pytest src")


@task
def lint(ctx):
    ctx.run("pylint src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")