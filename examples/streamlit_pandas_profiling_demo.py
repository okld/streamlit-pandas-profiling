import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

df = pd.DataFrame(
    np.random.rand(100, 5),
    columns=['a', 'b', 'c', 'd', 'e']
)

pr = ProfileReport(df, explorative=True)

st.title("Pandas Profiling in Streamlit")
st.write(df)
st_profile_report(pr)
