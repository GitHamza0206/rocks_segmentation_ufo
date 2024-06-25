import json
from PIL import Image
import os
import streamlit as st 
import pandas as pd

class DashboardView():
    def __init__(self):
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.samples_path = os.path.join(self.current_path, '../samples')
        json_path = os.path.join(self.samples_path, 'samples.json')
        self.samples = json.loads(open(json_path).read())

    def main_view(self,ct):
        ct.title("Rocks segmentation")
        uploaded_file = ct.file_uploader("Choose a file", type=["jpeg", "png", "jpg"])
        if uploaded_file is not None:
            file_contents = uploaded_file.read()
            #two columns
            col1, col2 = ct.columns(2)
            with col1:
                with ct.expander("original image"):
                    ct.image(file_contents, use_column_width=True)

            with col2:
                with ct.expander("no background image"):
                    self.nobackground_image_view(ct,uploaded_file.name)

            col3, col4 = ct.columns(2)
            with col3:
                with ct.expander("masked image"):
                    self.masked_image_view(ct,uploaded_file.name)

            with col4:
                with ct.expander("segmented image"):
                    self.segmented_image_view(ct,uploaded_file.name)


            
        return uploaded_file
    
    def nobackground_image_view(self,ct,image_path):
        # get current path 
        try:
            masked_image_path = os.path.join(self.samples_path, self.samples[image_path]['no_background_path'])
            masked_image = Image.open(masked_image_path)
            ct.image(masked_image, use_column_width=True)
        except:
            ct.error("An error has occured...")
    
    def masked_image_view(self,ct,image_path):
        # get current path 
        try:
            masked_image_path = os.path.join(self.samples_path, self.samples[image_path]['masked_path'])
            masked_image = Image.open(masked_image_path)
            ct.image(masked_image, use_column_width=True)
        except:
            ct.error("An error has occured...")

    def segmented_image_view(self,ct,image_path):
        # get current path 
        try:
            segmented_image_path = os.path.join(self.samples_path, self.samples[image_path]['segmentation_path'])
            segmented_image = Image.open(segmented_image_path)
            ct.image(segmented_image, use_column_width=True)
        except:
            ct.error("An error has occured...")

    def save_image_tojson_view(self,ct, data):
        # get current path 
        try:
            data_path = os.path.join(self.current_path, '../db/data.json')
            with open(data_path, 'w') as f:
                json.dump(data, f)
            ct.success("The image has been saved")
        except:
            ct.error("An error has occured...")

        
    def load_data_from_folder(self, ct):
        # get current path 
        try:
            data_path = os.path.join(self.current_path, '../db/reports')
            data = os.listdir(data_path)
            report = ct.selectbox('📁 Select a report', data, key="csv_key")            
            report_path = os.path.join(data_path, report)
            df = pd.read_csv(report_path)
            ct.dataframe(df)


        except:
            ct.error("An error has occured...")

    def load_reports_from_folder(self, ct):
                # get current path 
        try:
            reports_path = os.path.join(self.current_path, '../db/pdf_reports')
            reports = os.listdir(reports_path)
            print(reports)
            report = st.selectbox('📁 Select a report', reports, key="pdf_key")            
            report_path = os.path.join(reports_path, report)
            with open(report_path, 'rb') as f:
                pdf_data = f.read()

            # with st.expander("PDF Viewer"):
            #     with open(report_path, 'rb') as f:
            #         pdf_data = f.read()
            #     ct.write(f'<iframe src="data:application/pdf;base64,{pdf_data.encode("base64")}" width="700" height="1000" type="application/pdf"></iframe>', unsafe_allow_html=True)
            ct.download_button(
                    label=f"Download {report}",
                    data=pdf_data,
                    file_name=report_path,
                    mime="application/pdf"
                )
            
        except Exception as e:
            ct.write(e)
            ct.error("An error has occurred...")
                    
                
    def display_psd_chart(self,ct):
        charts_path = os.path.join(self.current_path, '../db/graphs')
        chart = os.path.join(charts_path, 'psd1.png')
        ct.image(chart, use_column_width=False, width=400)