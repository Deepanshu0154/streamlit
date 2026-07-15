import streamlit as st

email = st.text_input('Enter Email')
password = st.text_input('Enter Password')
opt = st.radio('Select Gender',('Male','Female')
               
         )


st.divider()
if opt=='Male':
    st.write(f'your gender is {opt}')

else:
    st.write(f'your gender is {opt}')

btn = st.button('Click here to login')

if btn:
    if email=='deepanshu@gmail.com' and password=='deep123':
        st.success('Login')
        st.balloons()

    else:
        st.error('Login Failed')
        st.snow()