import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clinicaltrials",
    version="0.1.0",
    author="Leo Sternlicht",
    author_email="lsternlicht@gmail.com",
    description="exploration tools for clinicaltrials.gov (forked from @sylvaingchassang)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lsternlicht/trial-explorer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

