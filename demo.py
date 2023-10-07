import streamlit as st

st.title('hello streamlit')

st.header('myheader')

st.subheader('this is a subheader')
st.text("abhigyan's first streamlit project")

st.markdown("""
    # h1 tag
    ## h2 tag
    ### h3 tag
    """)

st.write("abhigyan","datta","python")
d={'name' : 'abhigyan',
   'profession': 'Data Scientist'}
st.write(d)