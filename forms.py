import streamlit as st
from streamlit_space import space
from views import save_prompt, display_message
from models_list import get_models
from utils import check_password

def prompt_form():
    st.title(":primary[:material/savings: PiggyPrompt]", anchor=False)
    st.subheader(":gray[Add new prompt]", anchor=False)
    space()

    display_message()

    label = st.text_input("Enter a label for the prompt")

    prompt_text = st.text_area("Enter your prompt text", height=150)

    if 'provider' not in st.session_state:
        st.session_state.provider = "OpenAI"

    provider = st.selectbox(
        "Select AI Provider", 
        ["OpenAI", "Anthropic", "Google", "Meta", "DeepSeek", "Other"], 
        index=["OpenAI", "Anthropic", "Google", "Meta", "DeepSeek", "Other"].index(st.session_state.provider)
    )

    st.session_state.provider = provider

    models = get_models(provider)

    if provider == "Other":
        model = st.text_input("Enter model name")
    else:
        model = st.selectbox("Select Model", models)

    if st.button("Save Prompt", icon=":material/save:", type="primary"):
        st.session_state.messages = []
        if prompt_text and label:
            if save_prompt(provider, model, prompt_text, label):
                st.session_state.messages.append("Prompt saved successfully!")
            else:
                st.session_state.messages.append("A prompt with the same label, model, and provider already exists.")
            st.rerun()
        else:
            st.session_state.messages.append("Please fill out all fields.")


def login_form():
    st.title(":primary[:material/savings: PiggyPrompt]", anchor=False)
    st.subheader(":gray[The Trusty Vault for Your AI Prompts]", anchor=False)
    space(lines=2)

    password = st.text_input("Enter your password", type="password", icon=":material/key:")


    if st.button("**Login**", icon=":material/lock_open_right:", type="primary",use_container_width=True):
        if check_password(password):
            st.session_state.authenticated = True
            st.success("Logged in successfully!")
            st.rerun()
        else:
            st.error("Incorrect password. Try again.")