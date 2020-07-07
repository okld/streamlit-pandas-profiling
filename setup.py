from os.path import dirname
from os.path import join
import setuptools


def readme() -> str:
    """Utility function to read the README file.
    Used for the long_description.  It's nice, because now 1) we have a top
    level README file and 2) it's easier to type in the README file than to put
    a raw string in below.
    :return: content of README.md
    """
    return open(join(dirname(__file__), "README.md")).read()


setuptools.setup(
    name="streamlit-pandas-profiling",
    version="0.0.4",
    author="Synode",
    author_email="",
    description="Pandas profiling component for Streamlit",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Ghasel/streamlit-pandas-profiling",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit>=0.63",
        "pandas-profiling",
    ],
)
