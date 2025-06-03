import streamlit as st
from PIL import Image
from db import init_db
from views import display_saved_prompts, show_prompt
from forms import prompt_form, login_form
from utils import load_hashed_password


favicon = Image.open("static/logo.png")

init_db()

# Auth session_state check
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False


if not st.session_state.authenticated and load_hashed_password():
    st.set_page_config(page_title="PiggyPrompt", layout="centered", page_icon=favicon)
    login_form()    
else:
    st.set_page_config(page_title="PiggyPrompt", layout="wide", page_icon=favicon)
    st.sidebar.header(":primary[:material/savings: PiggyPrompt]")
    prompts = display_saved_prompts()

    if 'selected_prompt' in st.session_state and st.session_state.selected_prompt is not None:
        show_prompt()
    else:
        prompt_form()
