import os
import tempfile
import streamlit as st
from matcher import match_job, pdf_to_text


st.title('CV Job Matcher')

job_title = st.text_input('Job Title', placeholder="Enter job title")
job_description = st.text_area('Job Description', placeholder='Enter job description...')
job_keywords = st.text_input('Keywords [Optional]', placeholder='Comma separated values: python, llm, langchain')
resume_file = st.file_uploader("Choose a file", type="pdf")

job_data = {
  "title": job_title,
  "description": job_description,
  "keywords": job_keywords
}

resume_text = ""
match_percentage = "0.00%"

if resume_file is not None:
    with st.status("Processing..."):
        temp_dir = tempfile.mkdtemp()
        path = os.path.join(temp_dir, resume_file.name)
        with open(path, "wb") as f:
            f.write(resume_file.getvalue())
            st.write("Reading file...")
            resume_text = pdf_to_text(path)
            st.write("Converted PDF to text...")
           
        if(resume_text != ""):
            st.write("Matching the uploaded resume with the job...")
            match_percentage = match_job(job_data, resume_text)
        
    st.success('Matching done!')
    match_data = [
        {"Resume file": resume_file.name, "Job Title": job_data['title'], "Match (%)": match_percentage}
    ]
    st.table(match_data)


