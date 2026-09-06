import streamlit as st
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import update_student_voice


@st.dialog("🎙️ Voice Sample")
def voice_update_dialog():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    has_voice = bool(student_data.get('voice_embedding'))

    if has_voice:
        st.success("✅ You already have a voice sample saved.")
        st.write("You can record a new one below to **replace** the existing sample.")
    else:
        st.warning("⚠️ No voice sample found. Please record one so teachers can use voice attendance.")

    st.write("Record a short phrase like: *'I am present, my name is ...'*")

    audio_data = st.audio_input("Record your voice sample", key="voice_update_input")

    if st.button("Save Voice Sample", type="primary", width="stretch", disabled=not audio_data):
        with st.spinner("Processing your voice..."):
            voice_emb = get_voice_embedding(audio_data.read())
            if voice_emb:
                update_student_voice(student_id, voice_emb)
                # Update session state so the UI reflects the change immediately
                st.session_state.student_data['voice_embedding'] = voice_emb
                st.success("Voice sample saved successfully! 🎉")
                import time; time.sleep(1)
                st.rerun()
            else:
                st.error("Could not process your audio. Please try again.")
