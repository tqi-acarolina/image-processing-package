from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="carolsrd",
    author_email="anacarolinadosreissilva@gmail.com",
    description="Desafio DIO Unimed",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="git@github.com:tqi-acarolina/image-processing-package.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5'
)