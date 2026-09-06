import streamlit as st
from PIL import Image


@st.dialog("Capture or upload photos")
def add_photos_dialog():

    st.write('Add classroom photos to scan for attendance')

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    # Widget keys carry a nonce. Streamlit keeps a camera/uploader widget's
    # value in session state under its key, so reusing a fixed key meant that
    # reopening this dialog re-read the previous capture and appended the same
    # photos again. Bumping the nonce after each capture gives the next dialog
    # a fresh, empty widget.
    if 'photo_nonce' not in st.session_state:
        st.session_state.photo_nonce = 0
    nonce = st.session_state.photo_nonce

    t1, t2 = st.columns(2)

    with t1:
        type_camera = "primary" if st.session_state.photo_tab == 'camera' else 'tertiary'
        if st.button('Camera', type=type_camera, width='stretch'):
            st.session_state.photo_tab = 'camera'

    with t2:
        type_upload = "primary" if st.session_state.photo_tab == 'upload' else 'tertiary'
        if st.button('Upload photos', type=type_upload, width='stretch'):
            st.session_state.photo_tab = 'upload'

    if st.session_state.photo_tab == 'camera':
        cam_photo = st.camera_input('Take Snapshot', key=f'dialog_cam_{nonce}')
        if cam_photo:
            st.session_state.attendance_images.append(Image.open(cam_photo))
            st.session_state.photo_nonce += 1
            st.toast('Photo Captured')
            st.rerun()

    if st.session_state.photo_tab == 'upload':
        uploaded_files = st.file_uploader(
            'choose image files',
            type=['jpg', 'png', 'jpeg'],
            accept_multiple_files=True,
            key=f'dialog_upload_{nonce}',
        )

        if uploaded_files:
            for f in uploaded_files:
                st.session_state.attendance_images.append(Image.open(f))
            st.session_state.photo_nonce += 1
            st.toast('Photo Uploaded Successfully')
            st.rerun()

    st.divider()
    if st.button('Done', type='primary', width='stretch'):
        st.rerun()
