import streamlit as st
from PIL import Image
import pandas as pd
from Pages import Cafes, Hotels, Pubs, Restaurants, Homepage

# Navigation sidebar
st.sidebar.title("Navigation")

pages = {
    "Homepage": Homepage,
    "Restaurants": Restaurants,
    "Pubs": Pubs,
    "Hotels": Hotels,
    "Cafes": Cafes
}

selection = st.sidebar.radio("Pages", list(pages.keys()))
page = pages[selection]
page.app()




