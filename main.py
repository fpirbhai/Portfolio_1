import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images\mypic.png')

with col2:
    st.title("Fazleali Pirbhai")
    content ="""Hi. Love programming and currently designing this website using 
    python. """
    st.info(content)