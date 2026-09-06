import streamlit as st
from html import escape

def subject_card(name, code, section, stats=None, footer_callback=None):
    with st.container(border=True):
        html = f"""
        <div style="min-height:110px; font-family:'Poppins', sans-serif;">
            <p style="margin:0 0 4px 0; color:#1e293b; font-size:1.1rem;
                      font-weight:700; font-family:'Poppins', sans-serif;
                      text-transform:uppercase; letter-spacing:0.03em;">
                {escape(str(name))}
            </p>
            <p style="color:#64748b; margin:8px 0 10px 0; font-size:0.88rem;
                      font-family:'Poppins', sans-serif;">
                Code :&nbsp;<span style="background:#E0E3FF; color:#5865F2;
                    padding:2px 8px; border-radius:5px; font-weight:600;">
                    {escape(str(code))}</span>
                &nbsp;|&nbsp;Section :&nbsp;<span style="font-weight:500;
                    color:#1e293b;">{escape(str(section))}</span>
            </p>"""

        if stats:
            html += '<div style="display:flex; gap:8px; flex-wrap:wrap;">'
            for icon, label, value in stats:
                html += (
                    f'<div style="background:#EB459E18; padding:4px 12px;'
                    f' border-radius:12px; font-size:0.82rem;'
                    f' font-family:\'Poppins\', sans-serif; color:#1e293b;">'
                    f'{icon}&nbsp;<b style="font-weight:600;">{escape(str(value))}</b>'
                    f'&nbsp;<span style="color:#64748b;">{label}</span></div>'
                )
            html += "</div>"

        html += "</div>"
        st.markdown(html, unsafe_allow_html=True)

        st.divider()

        if footer_callback:
            footer_callback()