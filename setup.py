import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bidoo-model-interpreter",
    version="0.0.1",
    author="Lucas Deleforge",
    description="Package to interpret ML models",
    url="https://github.com/lucasDeleforge/bidoo-model-interpreter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU LESSER GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ]
)
