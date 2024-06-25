import os 
import streamlit as st
from views.utils import * 
from PIL import Image

class Sidebar:
    def __init__(self):
        pass
   
    def choose_folder_view(self,ct):
        with ct:
            
            #read image with pillow
            current_dir = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(current_dir, 'assets/drilldocs_logo.jpeg')
            image = Image.open(image_path)
            new_height = 200  # Desired height
            aspect_ratio = image.width / image.height
            new_width = int(new_height * aspect_ratio)
            resized_image = image.resize((new_width, new_height))
            ct.image(resized_image,use_column_width=False) 

            ct.header('⚙️ Parameters')
            ct.subheader('Choose the folder to store the images')

    def file_selector_view(self,ct):
        folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'uploads'))
        folders = []
        files = os.listdir(folder_path)
        new_folder = '➕ new client'
        for folder in files:
            flags =['.streamlit','__pycache__']
            if os.path.isdir(folder) and folder not in flags:
                folders.append(folder)
        
        folders.append(new_folder)
        selected_filename = ct.selectbox('📁 Select a folder for saving', folders, key="folder_selectbox")
        if selected_filename==folders[-1]: #if we select "add new folder"
            fn,fb=ct.columns(2)
            folder_name = fn.text_input('Client name',placeholder="Client name", label_visibility='collapsed')
            add_btn = fb.button('Add')
            if add_btn:
                try:
                    on_click_btn(folder_name=folder_name)
                    st.experimental_rerun()
                except:
                    ct.error("Error with folder name ")
                
        elif is_any_directory_not_empty(selected_filename):
            ct.warning("This folder is not empty! it's content will be erased ")
        
        return os.path.join(folder_path, selected_filename)
    