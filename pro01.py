import streamlit as st
import joblib

#載入並還原模型
clf = joblib.load('model.joblib')

st.title('IRIS 品種預測')

c1 = st.slider('花萼長度:', 3.0, 8.0, 5.8)
c2 = st.slider('花萼寬度:', 2.0, 5.0, 3.5)
c3 = st.slider('花瓣長度:', 1.0, 7.0, 4.4)
c4 = st.slider('花瓣寬度:', 0.1, 2.5, 1.3)

labels = ['setosa', 'versicolor', 'virginica']
if st.button('進行預測'):
    X_new = [[c1, c2, c3, c4]]
    st.write('### 預測品種是: ',labels[clf.predict(X_new)[0]])


