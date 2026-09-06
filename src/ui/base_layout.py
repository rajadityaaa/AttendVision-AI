import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
                .stApp {
                    background: #5865F2 !important;
                }
                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>""", unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
                .stApp {
                    background: #E0E3FF !important;
                }
        </style>""", unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

            #MainMenu, footer, header { visibility: hidden; }

            .block-container {
                padding-top:1.5rem !important;
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
            }

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }

            h3, h4, p {
                font-family: 'Outfit', sans-serif;
            }

            /* Streamlit renders a `kind` attribute on every button, including its
               own chrome: the dialog close X (headerNoPadding), the dataframe
               and image toolbars (elementToolbar), and icon-only controls.
               An unscoped `button {}` rule turned all of those into big blue
               pills - the close X became a blank blue blob and the dataframe
               toolbar icons floated over the table. Style only real widget
               buttons and leave the chrome alone. */
            button:not([kind="header"]):not([kind="headerNoPadding"]):not([kind="elementToolbar"]):not([kind="borderlessIcon"]):not([kind="borderlessIconActive"]):not([kind="minimal"]){
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="primary"]:hover,
            button[kind="secondary"]:hover,
            button[kind="tertiary"]:hover{ transform: scale(1.05); }

        </style>""", unsafe_allow_html=True)