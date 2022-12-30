import setuptools

with open("README.md","r",encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"    # update as per your need

REPO_NAME = "<your Repository Name>"
AUTHOR_USER_NAME = "<your user name>"
SRC_REPO = "<your Repository Name>"
AUTHOR_EMAIL = "<your email id>"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    )


