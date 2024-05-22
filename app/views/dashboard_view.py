class DashboardView():
    def __init__(self):
        pass

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
                with ct.expander("masked image"):
                    ct.image(file_contents, use_column_width=True)

            
        return uploaded_file