from setuptools import setup, find_packages

setup(
    name="lumi-mail",
    version="1.0.2",
    description="Official Python SDK for Lumi Email Infrastructure",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Lumi",
    author_email="team@lumi.com",
    url="https://github.com/deveterim/lumi-python",
    packages=find_packages(),
    package_data={"mailifica": ["py.typed"]},
    install_requires=[
        "requests>=2.28.0",
        "typing-extensions>=4.0.0;python_version<'3.10'",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
