from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambda-packaging",
    version="0.0.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nuage-studio/lambda-packaging",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=["pathspec>=0.8.0"],
    test_requires=[],
    test_suite="test",
)
