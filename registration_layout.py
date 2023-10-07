import streamlit as st

st.title("Registration Page")

first,last =st.columns(2)

first.text_input('first name')
last.text_input('last name')

email,phone =st.columns([3,1])

email.text_input('email id')
phone.text_input('mobile number')

username,password, repeat_password  =st.columns([3,2,2])

username.text_input('usernam')
password.text_input('password', type ='password')
repeat_password.text_input('repeat password',type = 'password')

chk,bl,sub =st.columns([1,3,1])
chk.radio("select",['I agree',"don't agree"])
sub.button('Submit')

