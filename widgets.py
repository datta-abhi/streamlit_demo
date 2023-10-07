import streamlit as st

st.title('Widget tutorial')

if st.button('Subscribe'):
    st.write('Channel Subscribed')

name = st.text_input('Enter your name:')
st.write(name)

address =st.text_area('Enter address')
st.write(address)

st.number_input('age:',value=30,step=1,min_value=10,max_value=100)

st.date_input('enter a date')

st.time_input('enter time')

if st.checkbox('accept t&c'):
    st.write('Thank you')

st.radio('take the pill:',['red','green','blue'],index=None)
st.selectbox('which pill to take: ',['R','G','B'])

st.slider('age',min_value=18,max_value=120,value=30,step=5)

img = st.file_uploader('Upload a file')

st.image(img)
