
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="ContentForge v9.2", layout="wide")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("ContentForge v9.2 — API corrigida")

prompt = st.text_input("Prompt:")

if st.button("Gerar"):
    r = client.responses.create(
        model="gpt-4.1-mini",
        input=[{"role": "user", "content": prompt}]
    )
    st.write(r.output_text)
