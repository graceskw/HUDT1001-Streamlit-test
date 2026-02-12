import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Project 1", page_icon="📊", layout="wide")

st.markdown("# Project 1")
st.write(
    """This is a project done for the course HUDT1002 Essential Methods in Humanities and Digital Technologies"""
)

# picture
tab1, tab2, tab3 = st.tabs(["Dublin Core Metadata", "Poster", "Results"])

with tab1:
    df = pd.read_csv("media/projects_metadata.csv")
    st.dataframe(df.iloc[0], use_container_width=True)

with tab2:
    st.image("media/p1_poster.png", caption="poster", width="stretch")
    
with tab3:
    df_prince = pd.read_csv("media/chapter_sentiment_HP_prince.csv")
    #generate a line plot to show the sentiment evolution across chapters
    plt.figure(figsize=(10,6))
    plt.plot(df_prince['chapter'], df_prince['polarity'], marker='o', label='Polarity')
    plt.plot(df_prince['chapter'], df_prince['subjectivity'], marker='s', label='Subjectivity')

    plt.xlabel('Chapter')
    plt.ylabel('Score')
    plt.title('Sentiment Analysis by Chapter - Harry Potter and the Half-Blood Prince')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    st.pyplot(plt)
    
    