import streamlit as st
import datetime

# This changes what appears in the tab of the browser
st.set_page_config(
    page_title="HUDT1001",
    page_icon="🖥️",
)

st.write("""# Welcome to my website!""")

st.write('This website showcases the projects I have in courses for **BA(HDT)** at *HKU.* You can navigate through the pages to see the details of each project."')

st.markdown("You can find the curriculum of BA(HDT) [here](https://arts.hku.hk/current-students/undergraduate/BAHDT/curriculum-structure)")

st.write(f"Today's date is {datetime.date.today()}")

st.link_button("Github link", "https://github.com/graceskw/HUDT1001-Streamlit-test")