# 📈 Streamlit ydata Profiling

[![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link]

## Installation

```sh
pip install streamlit-ydata-profiling
```

## Getting started

Checkout this [example/main.py](example/main.py) code.

```python
import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport
import streamlit as st

from streamlit_ydata_profiling import st_profile_report

df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])
pr = ProfileReport(df, minimal=True, orange_mode=True, explorative=True)

st_profile_report(pr, navbar=True)
```

To view dashboard execute following command:

```bash
streamlit run example/main.py
```

## Demo

[![Open in Streamlit][share_badge]][share_link]

[![Preview](https://raw.githubusercontent.com/pejmans21/streamlit-ydata-profiling/main/demo.png)][share_link]

[share_badge]: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[share_link]: https://share.streamlit.io/okld/streamlit-gallery/main?p=ydata-profiling
[share_img]: https://raw.githubusercontent.com/okld/streamlit-ydata-profiling/main/preview.png

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/okld/streamlit-ydata-profiling

[pypi_badge]: https://badgen.net/pypi/v/streamlit-ydata-profiling?icon=pypi&color=black&label
[pypi_link]: https://pypi.org/project/streamlit-ydata-profiling
