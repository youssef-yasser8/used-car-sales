import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import streamlit as st
df = pd.read_csv(r"C:\Users\NOUR SOFT\Downloads\used_cars_data400.csv")
st.set_page_config(layout="wide")
st.title("Used Cars Data Analysis")
page = st.sidebar.selectbox("Select Page", [
    "Overview", "Year Analysis", "Fuel Type Analysis", "Car Type Analysis",
    "Location Analysis", "Owner Type Analysis", "Transmission Analysis", "Comparative Analysis"])
if page == "Overview":
    st.header("📌 Context")
    st.write("""There is a huge demand for used cars in the Indian Market today. As sales of new cars have slowed down in the recent past,
    the pre-owned car market has continued to grow over the past years and is larger than the new car market now. Cars4U is a budding tech start-up that aims to find footholes in this market. In 2018-19,
    while new car sales were recorded at 3.6 million units, around 4 million second-hand cars were bought and sold. There is a slowdown in new car sales and that could mean that the demand is shifting towards the pre-owned market.
    In fact, some car sellers replace their old cars with pre-owned cars instead of buying new ones. Unlike new cars""") 

    st.header("📌 Columns Description")
    st.markdown("""
    1. **S.No.** : Serial Number  
    2. **Name** : Name of the car which includes Brand name and Model name  
    3. **Location** : The location in which the car is being sold  
    4. **Year** : Manufacturing year of the car  
    5. **Kilometers_Driven** : Total kilometers driven  
    6. **Fuel_Type** : Type of fuel used  
    7. **Transmission** : Type of transmission  
    8. **Owner** : Type of ownership  
    9. **Mileage** : Standard mileage  
    10. **Engine** : Engine displacement  
    11. **Power** : Maximum power  
    12. **Seats** : Number of seats  
    13. **Price** : Used car price in INR  
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.header("Data Numeric Overview")
        st.dataframe(df.describe())
    with col2:
        st.header("Data Categorical Overview")
        st.dataframe(df.describe(include="O"))

elif page == "Year Analysis":
    selected_years = st.sidebar.slider("Select Year of Car", int(df["Year"].min()),  int(df["Year"].max()),  (int(df["Year"].min()), int(df["Year"].max())) )
    filtered_df = df[df["Year"].between(selected_years[0], selected_years[1])]
    st.plotly_chart(px.histogram(filtered_df, x="Year", y='Price_INR', histfunc="avg", title="Year vs Price"))
    st.plotly_chart(px.histogram(filtered_df, x="Year", y="Kilometers_Driven", histfunc="avg", title="Year vs Kilometers Driven"))
    st.plotly_chart(px.histogram(filtered_df, x="Year", color="Type of Car", title="Which years have the largest number of cars?"))
    st.plotly_chart(px.histogram(filtered_df, x="Year" , y="Power_bhp" ,histfunc="avg"))
    st.plotly_chart(px.scatter(df, x="Year", y="Price_INR", title="Year vs Price of Car", labels={"Year": "Year of Manufacture", "Price_INR": "Price (INR)"}, color="Type of Car"))
    st.plotly_chart(px.scatter(df, x="Year", y="Mileage_kmpl", title="Year vs Mileage (kmpl)", labels={"Year": "Year of Manufacture", "Mileage_kmpl": "Mileage (kmpl)"}, color="Type of Car"))
    
elif page == "Fuel Type Analysis":
    selected_fuel = st.sidebar.multiselect("Select Fuel Type", df["Fuel_Type"].unique())
    filtered_data1 = df[df["Fuel_Type"].isin(selected_fuel)]
    st.plotly_chart(px.histogram(filtered_data1, x="Fuel_Type", y='Price_INR', histfunc="avg", title="Price by Fuel Type"))
    st.plotly_chart(px.histogram(filtered_data1, x="Fuel_Type", y="Mileage_kmpl", histfunc="avg", title="Mileage by Fuel Type"))
    st.plotly_chart(px.histogram(filtered_data1, x="Fuel_Type", y="Kilometers_Driven",histfunc="avg" ,title="Average Kilometers_Driven by Fuel Type"))
    st.plotly_chart(px.histogram(filtered_data1, x="Fuel_Type", y="Power_bhp", histfunc="avg", title="Average php by Fuel Type"))
    st.plotly_chart(px.histogram(filtered_data1, x="Type of Car", color="Fuel_Type", title="Type of Car with Fuel Type",barmode="group"))
    st.plotly_chart(px.pie(df, names="Fuel_Type", title="Fuel_Type Distribution"))
    st.plotly_chart(px.pie(df, facet_col="Fuel_Type",names="Location" ,title="Do some cities prefer a certain type of fuel more than others?"))

elif page == "Car Type Analysis":
    select_car_type = st.sidebar.multiselect("Select Car Type", df["Type of Car"].unique())
    filtered_data2 = df[df["Type of Car"].isin(select_car_type)]
    st.plotly_chart(px.histogram(filtered_data2, x="Type of Car", y="Price_INR", histfunc="avg", title="Price by Type of Car"))
    st.plotly_chart(px.pie(df, names="Type of Car", title="Car type Distribution"))
    st.plotly_chart(px.histogram(filtered_data2, x="Type of Car", y="Mileage_kmpl",histfunc="avg" ,title="What types of cars achieve the highest kilometers per liter of fuel? "))
    st.plotly_chart(px.histogram(filtered_data2, x="Type of Car", y="Power_bhp", histfunc="avg",title="How does the average horsepower (Power_bhp) vary depending on the type of car?"))
    st.plotly_chart(px.histogram(filtered_data2, x="Type of Car", y="Engine_CC", histfunc="avg",title="How does the average Engine_CC vary depending on the type of car?"))
    st.plotly_chart(px.histogram(df, x="Type of Car", y="Kilometers_Driven",histfunc="avg" ,title="Type with Kilometers Driven",color="Type of Car"))

elif page == "Location Analysis":
    selected_location = st.sidebar.multiselect("Select Location", df["Location"].unique())
    filtered_data3 = df[df["Location"].isin(selected_location)]
    st.plotly_chart(px.histogram(filtered_data3, x="Location", y="Price_INR", histfunc="avg", title="Price by Location"))
    st.plotly_chart(px.histogram(df,x="Location",title="What are the cities where used cars are sold the most?"))
    st.plotly_chart(px.histogram(filtered_data3, x="Location", y="Kilometers_Driven", title="Distribution of average kilometers traveled by city",color="Location",histfunc="avg"))
    st.plotly_chart(px.pie(df,names="Location",facet_col="Transmission",title="Which cities have the most automatic cars?")) 
    st.plotly_chart(px.histogram(df, x="Location", y="Power_bhp", histfunc="avg", title="Which city has the fastest cars?"))                
    st.plotly_chart(px.histogram(filtered_data3, x="Location", y="Mileage_kmpl", histfunc="avg", title="Average vehicle mileage per liter in each country")) 

elif page == "Owner Type Analysis":
    select_owner_type = st.sidebar.multiselect("Select Owner Type", df["Owner_Type"].unique())
    filtered_data4 = df[df["Owner_Type"].isin(select_owner_type)]
    st.plotly_chart(px.histogram(filtered_data4, x="Owner_Type", y="Price_INR", histfunc="avg", title="Price by Owner Type"))
    st.plotly_chart(px.histogram(df, x="Owner_Type", y="Kilometers_Driven", histfunc="avg", title="Cars that have been through more than one owner may have more wear and tear"))
    st.plotly_chart(px.pie(df, names="Owner_Type", title="Owner Type Distribution"))
    st.plotly_chart(px.histogram(df, x="Owner_Type", y="Mileage_kmpl", histfunc="avg", title="How does fuel consumption (Mileage_kmpl) vary depending on ownership type (Owner_Type)?"))



elif page == "Transmission Analysis":
    select_transmission = st.sidebar.multiselect("Select Transmission Type", df["Transmission"].unique())
    filtered_data5 = df[df["Transmission"].isin(select_transmission)]
    st.plotly_chart(px.histogram(filtered_data5, x="Transmission", y="Price_INR", histfunc="avg", title="Price by Transmission"))
    st.plotly_chart(px.histogram(filtered_data5, x="Transmission", y="Mileage_kmpl", histfunc="avg", title="Mileage by Transmission"))
    st.plotly_chart(px.histogram(filtered_data5, x="Transmission", y="Kilometers_Driven", histfunc="avg", title="Average Kilometers Driven by Transmission Type"))
    st.plotly_chart(px.pie(df, names="Transmission", title="Transmission Type Distribution"))
    st.plotly_chart(px.histogram(filtered_data5, x="Transmission", y="Engine_CC", histfunc="avg", title="Average Engine Capacity by Transmission Type"))


elif page == "Comparative Analysis":
        selected_car_types = st.sidebar.multiselect("Select Car Type", df["Type of Car"].unique(), default=df["Type of Car"].unique())
        selected_fuel_types = st.sidebar.multiselect("Select Fuel Type", df["Fuel_Type"].unique(), default=df["Fuel_Type"].unique())
        selected_owner_types = st.sidebar.radio("Select Owner Type", df["Owner_Type"].unique())
        selected_location = st.sidebar.multiselect("Select Location", df["Location"].unique(), default=df["Location"].unique())
        
        filtered_df8 = df[(df["Type of Car"].isin(selected_car_types)) & (df["Owner_Type"].isin([selected_owner_types]))]
        
        st.subheader("Effect of Car Type and Owner Type on Price (Bar Chart)")
        st.plotly_chart(px.histogram(filtered_df8, x="Type of Car", y="Price_INR", color="Owner_Type", 
                                barmode="group", title="Average Price by Car Type and Owner Type",histfunc="avg"))
        
        filtered_df9 = df[(df["Fuel_Type"].isin(selected_fuel_types)) & (df["Type of Car"].isin(selected_car_types))]
        
        st.subheader("Car Type vs Power")
        st.plotly_chart(px.histogram(filtered_df9, x="Type of Car", y="Power_bhp", color="Fuel_Type", 
                                title="Car Type vs Power by Fuel Type", barmode="group",histfunc="avg"))
        
        filtered_df10 = df[(df["Fuel_Type"].isin(selected_fuel_types)) & (df["Location"].isin(selected_location))]
        
        st.subheader("Price Distribution by Fuel Type and Location")
        st.plotly_chart(px.histogram(filtered_df10, x="Location", y="Price_INR", color="Fuel_Type",
                                 title="Price Distribution by Fuel Type and Location", nbins=30, histfunc="avg",barmode="group"))

        st.subheader("Kilometers Driven by Car Type and Fuel Type")
        st.plotly_chart(px.histogram(filtered_df9, x="Fuel_Type", y="Kilometers_Driven", color="Type of Car",
                                     title="Kilometers Driven by Car Type and Fuel Type", histfunc="avg",barmode="group"))
    
        st.subheader("Fuel Efficiency by Car Type and Fuel Type")
        filtered_df13 = df[(df["Type of Car"].isin(selected_car_types)) & (df["Fuel_Type"].isin(selected_fuel_types))]
        st.plotly_chart(px.histogram(filtered_df13, x="Type of Car", y="Mileage_kmpl", color="Fuel_Type",
                               title="Fuel Efficiency by Car Type and Fuel Type", histfunc="avg",barmode="group"))
