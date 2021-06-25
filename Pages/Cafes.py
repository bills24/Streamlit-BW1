import streamlit as st
import pandas as pd
import time


def app():
    st.title("Cafes")

    st.header("DataFrame")
    df = pd.read_csv("Cafes Data", index_col=0, converters={"Cafe Type": eval})

    if st.button("Click to see full dataframe"):
        with st.spinner("Loading DataFrame"):
            time.sleep(2)
            st.dataframe(df)

    st.header("Exploring the data")

    st.markdown("Now, lets analyse the data:")

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

    location = df["Area Of London"].unique()
    choice = st.multiselect("Select the area of london", location)
    mask_location = df["Area Of London"].isin(choice)
    st.dataframe(df[mask_location])


    Type = []
    for i in df["Cafe Type"]:
        for j in i:
            if j not in Type:
                Type.append(j)
    
    cafe_type = Type
    choice_cafe_type = st.multiselect("Select the type of Cafe", cafe_type)
    # mask_cafe_type = df["Cafe Type"].isin(choice_cafe_type)
    # st.dataframe(df[mask_cafe_type])

    st.error("Still trying to solve this problem")

    st.error("Also need to make one for the amenities")

    st.header("Plots")

    st.markdown("""
    Do a map graph showing all cafes in each area of london
    - Which areas of london have the most cafes?
    
    Do a graph on areas of london that are most costly
    - Why is this?
    - Does this mean that they get more customers?/Are the better rated than cheaper areas?
    
    Do a graph on most common amenities
    - Does more amenities have an affect on the rating/number of reviews
    - 
    """)