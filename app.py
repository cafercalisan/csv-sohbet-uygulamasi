# type: ignore
import streamlit as st

from utils import get_answer_csv

st.header("CSV Belgeniz İle Sohbet Edin!")
uploaded_file = st.file_uploader("CSV Dosyanızı Yükleyin!", type=["csv"])

if uploaded_file is not None:
    query = st.text_area("Belgeniz ile alakalı bir soru yöneltin!")
    button = st.button("Onayla")
    if button:
        st.write(get_answer_csv(uploaded_file, query))
