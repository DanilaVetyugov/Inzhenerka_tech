from setuptools import find_packages, setup

setup(
    name="inzhenerka_dagstr",
    packages=find_packages(exclude=["inzhenerka_dagstr_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
