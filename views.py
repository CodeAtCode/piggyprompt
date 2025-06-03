import streamlit as st
from streamlit_space import space
from db import load_prompts, save_prompt as db_save_prompt, delete_prompt
from utils import escape_filename


def back_to_index():
    st.session_state.selected_prompt = None
    st.session_state.selected_label = None
    st.session_state.selected_provider = None
    st.session_state.selected_model = None
    st.session_state.messages = None
    st.rerun()


@st.dialog("Confirm Deletion")
def delete_confirm():
    st.write(f"Are you sure you want to delete this prompt?")
    st.write(f"**This action cannot be undone.**")
    space(lines=3)

    col1, col2, col3 = st.columns([4, 2, 2])

    with col3:
        if st.button("Delete", icon=":material/delete:", type="primary"):
            delete_prompt(st.session_state.selected_provider, st.session_state.selected_model, st.session_state.selected_label)
            back_to_index()
        
    with col2:
        if st.button("Cancel", type="secondary", icon=":material/cancel:"):
            st.rerun()


def display_saved_prompts():
    prompts = load_prompts()
    if not prompts:
        st.markdown(
        """
        <style>
            p.small-line-h {
                line-height:0.5;
            }
        </style>
        """,
            unsafe_allow_html=True,
        )
        st.sidebar.write(" ")
        st.sidebar.html("<p class='small-line-h'>No prompts saved yet.</p><p class='small-line-h'>Add your first one to get started!</p>")
        return []

    if 'model_visibility' not in st.session_state:
        st.session_state.model_visibility = {}

    for provider, models in prompts.items():
        st.sidebar.subheader(f":material/network_intelligence: {provider}")
        for model, prompt_list in models.items():
            if model not in st.session_state.model_visibility:
                st.session_state.model_visibility[model] = False
            
            toggle_key = f"toggle_{provider}_{model}"
            toggle_label = f"**:gray[{model} :material/expand_circle_down:]**"
            
            if st.sidebar.button(toggle_label, key=toggle_key, type="tertiary"):
                st.session_state.model_visibility[model] = not st.session_state.model_visibility[model]

            if st.session_state.model_visibility[model]:
                for prompt, label in prompt_list:
                    prompt_key = f"btn_{provider}_{model}_{label.strip()}"
                    if st.sidebar.button(label.strip(), key=prompt_key, icon=":material/article:", type="tertiary"):
                        st.session_state.selected_prompt = prompt.strip()
                        st.session_state.selected_label = label.strip()
                        st.session_state.selected_provider = provider
                        st.session_state.selected_model = model
                        st.rerun()

    return [label.strip() for provider in prompts for model in prompts[provider] for prompt, label in prompts[provider][model]]

def show_prompt():
    col1, col2 = st.columns([13, 1])

    with col1:
        if st.button("**Back**", icon=":material/arrow_back:", type="tertiary"):
            back_to_index()

    with col2:
        with st.popover(label="", icon=":material/settings:", use_container_width=True):
            
            st.download_button(
                label="Export",
                icon=":material/download:",
                type="tertiary",
                data=st.session_state.selected_prompt,
                file_name=f"{escape_filename(st.session_state.selected_label + '-' + st.session_state.selected_model)}.md",
                mime="text/markdown",
                key="prompt_export"
            )

            if st.button("Delete", icon=":material/delete:", type="tertiary"):
                delete_confirm()
            
            

    if 'selected_prompt' in st.session_state and 'selected_label' in st.session_state:
        st.header(f":primary[:material/article: {st.session_state.selected_label}]", anchor=False)
        st.subheader(f":material/network_intelligence: {st.session_state.selected_provider} | :gray[{st.session_state.selected_model}]", anchor=False)
        space(lines=2)

        st.code(f"{st.session_state.selected_prompt}", language="markdown", wrap_lines=True)
        

def save_prompt(provider, model, prompt_text, label):
    prompts = load_prompts()  
    if prompts:
        for prov, models in prompts.items():
            if prov == provider:
                for mdl, prompt_list in models.items():
                    if mdl == model:
                        for _, existing_label in prompt_list:
                            if existing_label.strip() == label.strip():
                                return False

    db_save_prompt(provider, model, prompt_text, label)
    return True


def display_message():
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    if st.session_state.messages:
        last_message = st.session_state.messages[-1]

        if last_message == "Prompt saved successfully!":
            st.info(last_message, icon=":material/done_outline:")
        else:
            st.error(last_message, icon=":material/error:")

    return st.session_state.messages
