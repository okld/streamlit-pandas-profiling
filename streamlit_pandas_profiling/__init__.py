import os
import streamlit as st
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _pandas_profiling = components.declare_component("pandas_profiling", url="http://localhost:3001")
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _pandas_profiling = components.declare_component("pandas_profiling", path=build_dir)


def st_profile_report(profile_report, key=None):
    """Display a profile report.

    Parameters
    ----------
    profile_report: pandas_profiling.ProfileReport
        The profile report instance to display.
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    """
    with st.spinner("Generating profile report..."):
        _pandas_profiling(html=profile_report.to_html(), key=key)


if not _RELEASE:
    import numpy as np
    import pandas as pd
    from pandas_profiling import ProfileReport

    df = pd.DataFrame(
        np.random.rand(100, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )

    pr = ProfileReport(df, explorative=True)
    st.title("Pandas Profiling in Streamlit")
    st.write(df)
    st_profile_report(pr)
