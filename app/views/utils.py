import os 
import streamlit as st

def on_click_btn(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    else:
        st.error('Folder exists')

def is_any_directory_not_empty(directories):
    """Check if any of the specified directories is not empty."""
    
    if os.listdir(directories):
        # Found a non-empty directory
        return True
    # All directories are empty
    return False

