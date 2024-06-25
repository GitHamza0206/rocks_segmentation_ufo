import streamlit as st
import os

from views.dashboard_view import DashboardView
from views.sidebar import Sidebar

st.set_page_config(
        page_title="Rocks segmentation",
        page_icon="🪨",
        layout="wide",
        initial_sidebar_state="expanded",
    )

def main():
    
    sidebar = Sidebar()
    sidebar.choose_folder_view(st.sidebar)
    sidebar.file_selector_view(st.sidebar)

    dashboard = DashboardView()
    uploaded_file = dashboard.main_view(st)

    st.divider()

    dashboard.display_psd_chart(st.expander("PSD chart"))

    st.divider()
    dashboard.load_data_from_folder(st)

    st.divider() 
    # show PDF generated reports 
    dashboard.load_reports_from_folder(st)



if __name__ == "__main__":
    main()

