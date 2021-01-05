import os
import streamlit as st
from streamlit.components.v1.components import declare_component
from pathlib import Path

_RELEASE = True

if not _RELEASE:
    _component_func = declare_component("streamlit_pandas_profiling", url="http://localhost:3001")
else:
    _component_path = (Path(__file__).parent/"frontend"/"build").resolve()
    _component_func = declare_component("streamlit_pandas_profiling", path=_component_path)


def st_profile_report(profile_report, height=None, navbar=True, key=None):
    """Display a profile report.

    Parameters
    ----------
    profile_report : pandas_profiling.ProfileReport
        The profile report instance to display.
    height : int or None
        Report height. If set to None, report will take full height, but
        navbar will be disabled. Defaults to None.
    navbar : boolean
        Show navbar if height is fixed.
    key : str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will
        be re-mounted in the Streamlit frontend and lose its current state.

    """
    with st.spinner("Displaying profile report..."):
        profile_report.set_variable("html", {
            "inline": True,
            "minify_html": True,
            "use_local_assets": True,
            "navbar_show": navbar if height is not None else False,
            "style": {
                "full_width": True
            }
        })

        _component_func(html=profile_report.to_html(), height=height, key=key)
