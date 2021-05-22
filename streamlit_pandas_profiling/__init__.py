import streamlit as st

from pathlib import Path
from streamlit.components.v1.components import declare_component
from streamlit_pandas_profiling.version import __release__, __version__

if __release__:
    _source = {"path": (Path(__file__).parent/"frontend"/"build").resolve()}
else:
    _source = {"url": "http://localhost:3001"}

_render_component = declare_component("streamlit_pandas_profiling", **_source)


def st_profile_report(report, height=None, navbar=True, key=None):
    """Display a profile report.

    Parameters
    ----------
    report : pandas_profiling.ProfileReport
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
    config = {
        "inline": True,
        "minify_html": True,
        "use_local_assets": True,
        "navbar_show": navbar if height is not None else False,
        "style": {
            "full_width": True
        }
    }

    with st.spinner("Generating profile report..."):
        try:
            report.set_variable("html", config)
        except AttributeError:
            # Since Pandas Profiling 3.0.0
            report.config.html.inline = config["inline"]
            report.config.html.minify_html = config["minify_html"]
            report.config.html.use_local_assets = config["use_local_assets"]
            report.config.html.navbar_show = config["navbar_show"]
            report.config.html.full_width = config["style"]["full_width"]

        _render_component(html=report.to_html(), height=height, key=key, default=None)
