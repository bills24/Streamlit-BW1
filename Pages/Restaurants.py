import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns
import time

def app():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("Restaurants")

    st.header("DataFrame")
    df = pd.read_excel("LondonRestaurants.xlsx", index_col=0)



    if st.button("Click to see full dataframe"):
        st.dataframe(df)

    st.header("Exploring the data")

    # Tab for selecting columns in dataframe
    columns_selected = st.multiselect("Please select the columns that you want to display from the above data:",
                                      df.columns)

    # Creating Slider to filter out data with a minimum number of reviews
    num_reviews_slider = st.slider("Number Of Reviews", 0, 850)
    filter_num_reviews = df[df['Number_of_Reviews'] >= num_reviews_slider]

    st.dataframe(filter_num_reviews[columns_selected])

    # Slider to filter out data with a minimum rating
    restaurants_ratings_slider = st.slider("Restaurants Ratings", 2, 5)
    filter_cafe_ratings = df[df["Ratings"] >= restaurants_ratings_slider]

    st.dataframe(filter_cafe_ratings[columns_selected])

    st.header("Plots")

    st.subheader("Countplot of price ranges for pubs ratings")

    if st.button("Counterplot Graph"):
        st.write(
            sns.countplot(data=df, x="Ratings", hue='Price_range')
        )
        st.pyplot()

    st.subheader("Jointplot of number of reviews against ratings")

    if st.button("Jointplot Graph"):
        st.write(
            sns.jointplot(data=df, x='Ratings', y='Number_of_Reviews', height=8, kind='reg'),
            sns.set(font_scale=1.5)
        )
        st.pyplot()

    st.subheader("")

    if st.button("Swarmplot Graph!"):
        st.write(
            sns.swarmplot(data= df, x ="Ratings",y = 'Number_of_Reviews', hue= 'Price_range'),
        )
        st.pyplot()

    st.subheader("Heatmap")

    if st.button("Heatmap Graph!"):
        st.write(
            sns.heatmap(pd.crosstab(df.Ratings, df.Price_range), annot=True, fmt='d', cmap='Reds', vmax=50)
        )