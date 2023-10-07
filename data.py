import streamlit as st
import numpy as np
import pandas as pd

a = [1,2,3,4,5,6,7,8]

n1 =np.array(a)
n2 =n1.reshape((2,4))

dic ={'name': ['abhigyan','aniket'],
      'city': ['bangalore','mumbai'],
      'age': [32,28]}

data = pd.read_csv('Salary_Data.csv')

# st.dataframe(n1)

st.dataframe(n2)

# st.dataframe(dic)

# st.dataframe(data,height=500,width=400)

st.table(data)
st.table(dic)
