import streamlit as st
import segno
import io


@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    # Dynamically read the actual deployed URL — works on any domain
    try:
        host = st.context.headers.get("host", "snapclass-main.streamlit.app")
    except Exception:
        host = "snapclass-main.streamlit.app"

    # Local dev runs over plain http; a https:// link to localhost is dead.
    scheme = "http" if host.startswith(("localhost", "127.0.0.1")) else "https"
    join_url = f"{scheme}://{host}/?join-code={subject_code}"

    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(out, kind='png', scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('### Copy Link')
        st.code(join_url, language="text")
        st.code(subject_code, language="text")
        st.info('Copy this link to share on WhatsApp or Email')

    with col2:
        st.markdown('### Scan to Join')
        st.image(out.getvalue(), caption='QR Code for class joining')