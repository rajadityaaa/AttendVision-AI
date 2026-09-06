import streamlit as st
from src.database.db import get_all_subjects_with_teachers, enroll_student_to_subject
from src.database.config import supabase
import time


@st.dialog("Browse Available Courses")
def browse_courses_dialog():
    student_id = st.session_state.student_data['student_id']

    with st.spinner("Loading courses..."):
        all_subjects = get_all_subjects_with_teachers()

    if not all_subjects:
        st.info("No courses are available yet.")
        return

    # Fetch which subjects this student is already enrolled in
    enrolled_res = supabase.table('subject_students').select('subject_id').eq(
        'student_id', student_id
    ).execute()
    enrolled_ids = {row['subject_id'] for row in enrolled_res.data}

    st.write(f"**{len(all_subjects)} course(s) available.** Click **Join** to enroll instantly.")
    st.divider()

    for sub in all_subjects:
        sid = sub['subject_id']
        already = sid in enrolled_ids

        col_info, col_btn = st.columns([3, 1], vertical_alignment='center')

        with col_info:
            st.markdown(
                f"**{sub['name']}**  \n"
                f"Code: `{sub['subject_code']}` &nbsp;|&nbsp; "
                f"Section: {sub['section']} &nbsp;|&nbsp; "
                f"Teacher: {sub['teacher_name']} &nbsp;|&nbsp; "
                f"👥 {sub['total_students']} enrolled"
            )

        with col_btn:
            if already:
                st.button(
                    "✅ Enrolled",
                    key=f"browse_join_{sid}",
                    disabled=True,
                    width='stretch',
                )
            else:
                if st.button(
                    "Join",
                    key=f"browse_join_{sid}",
                    type="primary",
                    width='stretch',
                ):
                    enroll_student_to_subject(student_id, sid)
                    st.toast(f"Enrolled in {sub['name']}!")
                    time.sleep(1)
                    st.rerun()

        st.divider()
