import streamlit as st
import webbrowser

def app():
    st.title("Home")
    st.markdown(
        """## Team London
        - Add Description of our team
        - Add image of london
        - Add a little insight of our data
        - Need to explain graphs and what information we got from them"""
    )

    st.markdown("### Members:")
    if st.button("Manikanta Badugu"):
        webbrowser.open_new_tab("https://www.linkedin.com/in/manikanta-badugu-65a45182/")
    elif st.button("Wojtek Gradzinski"):
        webbrowser.open_new_tab("")
    elif st.button("Gozal Henggardhani"):
        webbrowser.open_new_tab("")
    elif st.button("Bilal Hussain"):
        webbrowser.open_new_tab("https://www.linkedin.com/in/bilal-hussain-546a1a20b/")