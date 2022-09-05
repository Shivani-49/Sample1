import streamlit as st
import pickle
pickle_in=open('SalaryPrediction.pkl','rb')
model=pickle.load(pickle_in)



years=st.number_input('Enter years of Experience')
salary=model.predict([[years]])
if st.button('PREDICT'):
  st.success(f'SALARY PREDICTED IS {salary}')
