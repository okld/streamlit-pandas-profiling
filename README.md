# 📈 Streamlit Pandas Profiling

[![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link] 

## Installation

```sh
pip install streamlit-pandas-profiling
```

## Getting started

```python
import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)
```

## Demo

[![Open in Streamlit][share_badge]][share_link] 

[![Preview][share_img]][share_link]

[share_badge]: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[share_link]: https://share.streamlit.io/okld/streamlit-gallery/main?p=pandas-profiling
[share_img]: https://raw.githubusercontent.com/okld/streamlit-pandas-profiling/main/preview.png

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/okld/streamlit-pandas-profiling

[pypi_badge]: https://badgen.net/pypi/v/streamlit-pandas-profiling?icon=pypi&color=black&label
[pypi_link]: https://pypi.org/project/streamlit-pandas-profiling
