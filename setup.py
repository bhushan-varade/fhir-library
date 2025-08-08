from setuptools import setup, find_packages

setup(
    name="fhir_flex",
    version="0.0.1",
    author="Bhushan Varade",
    author_email="bvarade02@gmail.com",
    description="A flexible library to simplify and map FHIR Patient objects to custom JSON schemas.",
    packages=["fhir_flex"],
    license="MIT",
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="fhir patient json healthcare flexible",
)


