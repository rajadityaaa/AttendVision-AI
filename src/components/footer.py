import streamlit as st

# Change this to whatever you want shown at the bottom of every screen.
CREDIT = "AttendVision AI • Built & maintained by Aditya"


def footer_home():
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:white;"> {CREDIT} </p>
        </div>
                """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:#5865F2;"> {CREDIT} </p>
        </div>
                """, unsafe_allow_html=True)
