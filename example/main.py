import numpy as np
import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport

from streamlit_ydata_profiling import st_profile_report

df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])
pr = ProfileReport(df, minimal=True, orange_mode=True, explorative=True)

st.markdown(
    """
# 📈 Streamlit ydata Profiling

## Installation

```sh
pip install streamlit-ydata-profiling
```

## Getting started

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

"""
)
st_profile_report(pr, navbar=True)
