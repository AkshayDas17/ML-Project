import streamlit as st
import pickle
import os
model_path = os.path.abspath('ML-Project/cancer')
Model = pickle.load(open(model_path, 'rb'))
c=st.number_input('Clump Thickness')
size=st.number_input('Uniformity of Cell Size')
shape=st.number_input('Uniformity of Cell Shape')
m=st.number_input('Marginal Adhesion')
e=st.number_input('Single Epithelial Cell Size')
b=st.number_input('Bland Chromatin')
n=st.number_input('Normal Nucleoli')
mi=st.number_input('Mitoses')
if st.button('Check cancer'):
    pred=Model.predict([[c,size,shape,m,e,b,n,mi]])
    if pred==0:
        st.success('NO sign of cancer')
        st.balloons()
    else:
        st.warning('High chance of cancer')    
