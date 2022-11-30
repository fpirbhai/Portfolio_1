import streamlit as st

st.title('Contact Us for any comments or feedback')

with st.form(key='form_email'):
    user_email = st.text_input('Please enter your email address: ')
    message = st.text_area("Your message here...")
    submit_button = st.form_submit_button()
    if submit_button:
        if "@" not in user_email:
            st.error('email address format wrong')
        else:
            print('Processing Forms')