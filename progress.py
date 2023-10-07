import streamlit as st
import time


st.error('Error msg')
st.success("Success msg")
st.info("Information")
st.exception(RuntimeError("this is runtime error"))
st.warning('this is warning')

progress = st.progress(0)

for i in range(1,100):
    time.sleep(0.2)
    progress.progress(i+1)