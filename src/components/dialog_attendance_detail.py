import streamlit as st
from src.database.db import get_attendance_detail
from datetime import datetime


@st.dialog("📋 Attendance Detail")
def attendance_detail_dialog(teacher_id, ts_group, subject_name, subject_code, subject_id):
    rows = get_attendance_detail(teacher_id, ts_group, subject_id)

    if not rows:
        st.warning("No detail records found for this session.")
        return

    # Parse timestamp for display
    try:
        display_time = datetime.fromisoformat(ts_group).strftime("%d %B %Y, %I:%M %p")
    except Exception:
        display_time = ts_group

    present = [r for r in rows if r.get('is_present')]
    absent  = [r for r in rows if not r.get('is_present')]

    st.markdown(f"**Course:** {subject_name} &nbsp;(`{subject_code}`)")
    st.markdown(f"**Date / Session:** {display_time}")
    st.markdown(
        f"**Attendance:** ✅ {len(present)} present &nbsp;|&nbsp; "
        f"❌ {len(absent)} absent &nbsp;|&nbsp; "
        f"👥 {len(rows)} total enrolled"
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ✅ Present")
        if present:
            for r in present:
                name = r['students']['name'] if r.get('students') else f"ID {r['student_id']}"
                st.markdown(f"- {name}")
        else:
            st.info("Nobody was marked present.")

    with col2:
        st.markdown("### ❌ Absent")
        if absent:
            for r in absent:
                name = r['students']['name'] if r.get('students') else f"ID {r['student_id']}"
                st.markdown(f"- {name}")
        else:
            st.success("Nobody was absent!")
