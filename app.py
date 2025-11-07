import streamlit as st # type: ignore
import os
from pdf2docx import Converter # type: ignore

# --- App Title ---
st.set_page_config(page_title="PDF 📝 ➜ Word Converter 📎", page_icon="🧌", layout="centered") # create streamlit app
st.title("🧌 Ogre Studios PDF 📝 ➜ Word Converter 📎") # app title
st.write("🧌 Convert your PDF files into editable Word (.docx) documents instantly.") # app description

# --- File Upload ---
uploaded_file = st.file_uploader("🧌 Upload a PDF file", type=["pdf"]) # file uploader for pdf files

if uploaded_file:
    input_path = os.path.join("input", uploaded_file.name) # path for uploaded file
    output_dir = "output" # output directory
    os.makedirs(output_dir, exist_ok=True) # create output directory if not exists

    os.makedirs("input", exist_ok=True) # create input directory if not exists
    with open(input_path, "wb") as f: # save uploaded file to input directory
        f.write(uploaded_file.read()) # write uploaded file content

    output_file = os.path.join(output_dir, uploaded_file.name.replace(".pdf", ".docx")) # output file path

    if st.button("🧌 Convert to Word"): # convert button
        with st.spinner("🧌 Converting... Please wait ⏳"): # show spinner while converting
            converter = Converter(input_path) # initialise converter
            converter.convert(output_file, start=0, end=None) # convert pdf to docx
            converter.close() # close converter
        st.success("🧌 ✅ Conversion complete!") # show success message

        with open(output_file, "rb") as f: # open converted file
            st.download_button( 
                label="🧌 ⬇️ Download Word File", # download button
                data=f, # file content
                file_name=os.path.basename(output_file), # file name
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document" # mime type
            )
