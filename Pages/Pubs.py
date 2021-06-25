import streamlit as st
import pandas as pd
import matplotlib as plt
import numpy as np
import seaborn as sns
from pandas import ExcelFile
from pandas import ExcelWriter


def app():
    st.title("Pubs")

    st.header("DataFrame")
    df = pd.read_excel("LondonPubs.xlsx", index_col=0)

    if st.button("Click to see full dataframe"):
        st.dataframe(df)

    st.header("Exploring the data")

    # Tab for selecting columns in dataframe
    columns_selected = st.multiselect("Please select the columns that you want to display from the above data:",
                                      df.columns)

    # Creating Slider to filter out data with a minimum number of reviews
    num_reviews_slider = st.slider("Number Of Reviews", 0, 550)
    filter_num_reviews = df[df['Pubs_reviews'] >= num_reviews_slider]

    st.dataframe(filter_num_reviews[columns_selected])

    # Slider to filter out data with a minimum rating
    Pubs_ratings_slider = st.slider("Pub Ratings", 2, 5)
    filter_cafe_ratings = df[df["Pubs_ratings"] >= Pubs_ratings_slider]

    st.dataframe(filter_cafe_ratings[columns_selected])

    st.write("\n")
    st.write("\n")

    st.header("Plots")

    st.subheader("Countplot of price ranges for pubs ratings")
    if st.button("Countplot Graph"):
        st.write(
            sns.countplot(data=df, x="Pubs_ratings", hue='Pubs_price_range'),
            sns.set(font_scale=1, palette='viridis')
        )
        st.pyplot()

    st.subheader("Pubs Ratings Against Reviews")
    if st.button("Jointplot Graph"):
        st.write(
            sns.jointplot(data = df, x ='Pubs_ratings', y='Pubs_reviews', height =8 , kind ='reg'),
            sns.set(font_scale=1.5)
        )
        st.pyplot()

    st.subheader("Swarmplot")
    if st.button("Swarmplot Graph"):
        st.write(
            sns.swarmplot(data=df, x="Pubs_ratings", y='Pubs_reviews', hue='Pubs_price_range')
        )
        st.pyplot()

    st.subheader("Heatmap")
    if st.button("Heatmap Graph"):
        st.write(
            sns.heatmap(pd.crosstab(df.Pubs_ratings, df.Pubs_price_range), annot=True, fmt='d', cmap='Reds', vmax=50)
        )
        st.pyplot()
