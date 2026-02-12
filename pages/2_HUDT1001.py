import streamlit as st
import pandas as pd

st.set_page_config(page_title="HUDT1001 Project", page_icon="📊", layout="wide")

st.markdown("# HUDT1001 Project")
st.write(
    """This is the final project done for the course HUDT1001 Essential Methods in Humanities and Digital Technologies"""
)

# picture
tab1, tab2, tab3, tab4 = st.tabs(["Dublin Core Metadata", "Results", "Poster", "Report"])

with tab1:
    df = pd.read_csv("media/projects_metadata.csv")
    st.dataframe(df.iloc[1], use_container_width=True)

    