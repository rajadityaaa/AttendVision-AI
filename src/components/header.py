import base64
from functools import lru_cache
from pathlib import Path

import streamlit as st

# The logo used to be hot-linked from the original author's i.ibb.co account,
# which meant this app's branding depended on someone else's image host. It is
# now read from img/logo.png in this repo and inlined as a data URI, because
# these headers are rendered as raw HTML and cannot point at a local file path.
LOGO_PATH = Path(__file__).resolve().parents[2] / "img" / "logo.png"


@lru_cache(maxsize=1)
def _logo_src() -> str:
    try:
        encoded = base64.b64encode(LOGO_PATH.read_bytes()).decode()
        return f"data:image/png;base64,{encoded}"
    except OSError:
        return ""


def header_home():

    logo_url = _logo_src()

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' alt='AttendVision AI logo' style='height:100px;' />
            <h1 style='text-align:center; color:#E0E3FF'>ATTEND<br/>VISION</h1>
        </div>
                """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = _logo_src()

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' alt='AttendVision AI logo' style='height:85px;' />
            <h2 style='text-align:left; color:#5865F2'>ATTEND<br/>VISION</h2>
        </div>
                """, unsafe_allow_html=True)
