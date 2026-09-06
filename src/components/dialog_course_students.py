import streamlit as st
from html import escape
from src.database.db import get_subject_enrolled_students


@st.dialog("👥 Enrolled Students")
def course_students_dialog(subject_name, subject_code, subject_id):
    st.markdown(f"**Course:** {subject_name} &nbsp;(`{subject_code}`)")
    st.divider()

    with st.spinner("Loading enrolled students..."):
        students = get_subject_enrolled_students(subject_id)

    if not students:
        st.info("No students enrolled in this course yet.")
        return

    st.markdown(f"**Total Enrolled: {len(students)}**")
    st.space()

    for i, student in enumerate(students, 1):
        has_voice = bool(student.get('voice_embedding'))
        voice_badge = "🎙️" if has_voice else "🔇"
        st.markdown(
            f"{i}. **{escape(str(student['name']))}** &nbsp; "
            f"<span style='font-size:0.8rem; color:#64748b;'>ID: {student['student_id']} "
            f"&nbsp;{voice_badge} {'Voice ✓' if has_voice else 'No voice'}</span>",
            unsafe_allow_html=True
        )
    st.divider()
    st.caption("🎙️ = has voice sample &nbsp;|&nbsp; 🔇 = no voice sample")
