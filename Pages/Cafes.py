import streamlit as st
import pandas as pd

def app():
    st.title("Cafes")

    st.header("DataFrame")
    df = pd.read_csv("Cafes Data", index_col=0)

    if st.button("Click to see full dataframe"):
        st.dataframe(df)

    st.header("Exploring the data")

    # Tab for selecting columns in dataframe
    columns_selected = st.multiselect("Please select the columns that you want to display from the above data:", df.columns)

    # Creating Slider to filter out data with a minimum number of reviews
    num_reviews_slider = st.slider("Number Of Reviews", 0, 650)
    filter_num_reviews = df[df['Number Of Reviews'] >= num_reviews_slider]

    st.dataframe(filter_num_reviews[columns_selected])

    # Slider to filter out data with a minimum rating
    cafe_ratings_slider = st.slider("Cafe Ratings", 3, 5)
    filter_cafe_ratings = df[df["Cafe Ratings"] >= cafe_ratings_slider]

    st.dataframe(filter_cafe_ratings[columns_selected])


    st.header("Plots")