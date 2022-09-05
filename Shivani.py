import streamlit as st
st.header('SHIVANI IS GOOD')
a=st.number_input('Enter any value')
if st.button('HIT ME'):
  st.success(f'Your lucky number is{a}')
