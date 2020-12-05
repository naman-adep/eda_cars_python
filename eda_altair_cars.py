from vega_datasets import data
import streamlit as st
import altair as alt

def main():
    df = load_data()
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration"])

    if page == "Homepage":
        st.header("Cars dataset")
        st.write("Please select a page on the left.")
        st.write(df)
    elif page == "Exploration":
        st.title("Exploratory Data Analysis of Cars")
        x_axis = st.selectbox("Choose a variable for the x-axis", df.columns, index=3)
        y_axis = st.selectbox("Choose a variable for the y-axis", df.columns, index=4)
        visualize_data(df, x_axis, y_axis)

@st.cache
def load_data():
    df = data.cars()
    return df

def visualize_data(df, x_axis, y_axis):
    brush = alt.selection(type='interval')
    graph = alt.Chart(df).mark_point().encode(x='Horsepower', y='Miles_per_Gallon', color=alt.condition(brush, 'Origin', alt.value('lightgray'))).add_selection(brush)
    bars = alt.Chart(df).mark_bar().encode(y='Origin', color='Origin', x='count(Origin)').transform_filter(brush)
    graph & bars

if __name__ == "__main__":
    main()

