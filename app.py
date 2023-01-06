import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.header("[Banpresto](https://www.amazon.com/dp/B093F4P1XQ?ref_=cm_sw_r_cp_ud_dp_K6D1K33AR23HA115FF2C)")
   st.image("image1.png")

with col2:
   st.header("A dog")
   st.image("image2.png")

with col3:
   st.header("An owl")
   st.image("image2.png")

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("image1.png")

with col2:
   st.header("A dog")
   st.image("image3.png")

with col3:
   st.header("An owl")
   st.image("image2.png")