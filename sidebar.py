import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


plt.style.use('ggplot')

data = {'num' : [x for x in range(1,11)],
        'square': [x**2 for x in range(1,11)],
         'twice': [2*x for x in range(1,11)],
          'thrice': [3*x for x in range(1,11)]
        }

df =pd.DataFrame(data)

# st.table(df)

# # single select sidebar
# col = st.sidebar.selectbox("Select a column: ",df.columns)
# plt.plot(df['num'],df[col])
#
# st.set_option('deprecation.showPyplotGlobalUse', False)
# st.pyplot()

# # multiselect sidebar
# mul = st.sidebar.multiselect('Select columns: ',df.columns)
# plt.plot(df['num'],df[mul])
#
# st.pyplot()

# multipage in streamlit
pages = st.sidebar.radio("Navigation",['about us','home'])

if pages == 'about us':
    st.write('Welcome to Homepage')
elif pages == 'home':
    mul = st.sidebar.multiselect('Select columns: ', df.columns)
    plt.plot(df['num'], df[mul])

    st.pyplot()
