import streamlit as st
import streamlit_pydantic as sp
from jobs_searcher.data_manager import JobsDataManager

st.title("New York City Job Search")

st.text("Loading latest job data...")

jobs_data_manager = JobsDataManager()
jobs_data_manager.fetch_new_data()


def print_random_job():
    sp.pydantic_output(jobs_data_manager.get_lucky())


if st.button("I'm Feeling Lucky"):
    print_random_job()
else:
    pass
