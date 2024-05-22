import streamlit as st
import os

from views.dashboard_view import DashboardView
from views.sidebar import Sidebar

def main():
    st.set_page_config(
        page_title="Rocks segmentation",
        page_icon="🪨",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    sidebar = Sidebar()
    sidebar.choose_folder_view(st.sidebar)
    sidebar.file_selector_view(st.sidebar)

    dashboard = DashboardView()
    uploaded_file = dashboard.main_view(st)

if __name__ == "__main__":
    main()

