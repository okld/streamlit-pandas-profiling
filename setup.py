import setuptools
from pathlib import Path


README = (Path(__file__).parent/"README.md").read_text()

setuptools.setup(
    name="streamlit-pandas-profiling",
    version="0.1.1",
    author="Synode",
    author_email="",
    description="Pandas profiling component for Streamlit",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/okld/streamlit-pandas-profiling",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit>=0.63",
        "pandas-profiling",
    ],
)
