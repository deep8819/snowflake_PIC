import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# Load HTML file
with open("snowflake_pic.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render HTML
components.html(html_content, height=1200, scrolling=True)
