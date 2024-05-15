import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets2.lottiefiles.com/packages/lf20_Jcprdh.json"
lottie_json = load_lottieurl(lottie_url)

st.title("Animasi Lottie di Streamlit")
st_lottie(lottie_json, height=300)