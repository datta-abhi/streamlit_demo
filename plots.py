import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.DataFrame(np.random.randn(100,3),
                  columns=['a','b','c'])

# st.dataframe(data)

# st.line_chart(data)
#
# st.area_chart(data)
#
# st.bar_chart(data)

# geographical data in streamlit
place = {'city': '[bangalore]',
         'lat': [12.9716],
            'lon': [77.5946]}

st.map(pd.DataFrame(place))



plt.scatter(data['a'],data['b'])
plt.title('scatterplot')
plt.xlabel('x-axis')
plt.ylabel('y-label')
st.pyplot()