from setuptools import setup, find_packages

version = {}
with open("plater/version.py") as fp:
    exec(fp.read(), version)

setup(
    name="plater",
    version=version["__version__"],
    author="Peter Vegh",
    description="Generating picklist files from transfer lists.",
    license="MIT",
    url="https://github.com/Edinburgh-Genome-Foundry/Plater",
    keywords="biology",
    packages=find_packages(exclude="docs"),
    install_requires=["dioscuri", "pandas", "plateo"],
    include_package_data=True,
)
