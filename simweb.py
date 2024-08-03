import streamlit as st
import pandas as pd
name = st.text_input("enter your name:")
fname = st.text_input("enter your father's name:")
adr = st.text_area("enter your address:")
classdata = st.selectbox("enter your class", (1,2,3,4,5,6))
button = st.button("done")
if button :
    st.markdown(f"""
                 name:{name}
                 father's name:{fname}
                 address:{adr}
                 class:{classdata}""")