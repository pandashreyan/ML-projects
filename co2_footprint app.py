import streamlit as st
import pandas as pd
import numpy as np

# Load database of carbon emissions factors
# (You'll need to replace this with the actual path to your CSV file)
db = pd.read_csv('/content/Carbon Emission.csv') 

# Define functions to calculate carbon footprint
def calculate_body_type_footprint(body_type):
    if body_type == 'slim':
        return 0.5
    elif body_type == 'average':
        return 1.0
    elif body_type == 'obese':
        return 1.5

def calculate_sex_footprint(sex):
    if sex == 'male':
        return 0.8
    elif sex == 'female':
        return 0.7   

def calculate_diet_footprint(diet):
    if diet == 'vegan':
        return 0.4
    elif diet == 'vegetarian':
        return 0.6
    elif diet == 'meat':
        return 1.0 

def calculate_shower_frequency_footprint(shower_frequency):
    if shower_frequency == 'daily':
        return 1.2
    elif shower_frequency == 'every other day':
        return 0.9
    elif shower_frequency == 'weekly':
        return 0.6  

def calculate_heating_energy_source_footprint(heating_energy_source):
    if heating_energy_source == 'gas':
        return 10.1
    elif heating_energy_source == 'electricity':
        return 5.9

def calculate_transport_footprint(transport):
    if transport == 'driving':
        return 20.0
    elif transport == 'public transport':
        return 10.8
    elif transport == 'cycling':
        return 10.4

def calculate_vehicle_type_footprint(vehicle_type):
    if vehicle_type == 'gasoline':
        return 15.5
    elif vehicle_type == 'electric':
        return 10.8

def calculate_social_activity_footprint(social_activity):
    if social_activity == 'active':
        return 10.2
    elif social_activity == 'moderate':
        return 5.9
    elif social_activity == 'sedentary':
        return 2.6

def calculate_monthly_grocery_bill_footprint(monthly_grocery_bill):
    if monthly_grocery_bill < 50:
        return 10.4
    elif monthly_grocery_bill < 100:
        return 20.6
    elif monthly_grocery_bill >= 100:
        return 30.8

def calculate_frequency_of_traveling_by_air_footprint(frequency_of_traveling_by_air):
    if frequency_of_traveling_by_air == 'frequent':
        return 30.0
    elif frequency_of_traveling_by_air == 'occasional':
        return 11.5
    elif frequency_of_traveling_by_air == 'rarely':
        return 10.8

def calculate_vehicle_monthly_distance_km_footprint(vehicle_monthly_distance_km):
    if vehicle_monthly_distance_km < 500:
        return 10.4
    elif vehicle_monthly_distance_km < 1000:
        return 20.6
    elif vehicle_monthly_distance_km >= 1000:
        return 30.8

def calculate_waste_bag_size_footprint(waste_bag_size):
    if waste_bag_size == 'small':
        return 10.2
    elif waste_bag_size == 'medium':
        return 20.4
    elif waste_bag_size == 'large':
        return 30.6

def calculate_waste_bag_weekly_count_footprint(waste_bag_weekly_count):
    if waste_bag_weekly_count < 2:
        return 10.1
    elif waste_bag_weekly_count < 5:
        return 20.3
    elif waste_bag_weekly_count >= 5:
        return 30.5

def calculate_tv_pc_hour_footprint(tv_pc_hour):
    if tv_pc_hour < 2:
        return 10.1
    elif tv_pc_hour < 4:
        return 20.3
    elif tv_pc_hour >= 4:
        return 30.5

def calculate_daily_hour_footprint(daily_hour):
    if daily_hour < 8:
        return 10.4
    elif daily_hour < 10:
        return 20.6
    elif daily_hour >= 10:
        return 30.8

def calculate_frequency_of_new_clothes_footprint(frequency_of_new_clothes):
    if frequency_of_new_clothes == 'frequent':
        return 11.5
    elif frequency_of_new_clothes == 'occasional':
        return 10.9
    elif frequency_of_new_clothes == 'rarely':
        return 10.4

def calculate_internet_daily_hour_footprint(internet_daily_hour):
    if internet_daily_hour < 2:
        return 10.2
    elif internet_daily_hour < 4:
        return 20.4
    elif internet_daily_hour >= 4:
        return 30.6

def calculate_energy_efficiency_footprint(energy_efficiency):
    if energy_efficiency == 'high':
        return 10.8
    elif energy_efficiency == 'medium':
        return 10.5
    elif energy_efficiency == 'low':
        return 10.2

def calculate_recycling_footprint(recycling):
    if recycling == 'yes':
        return 10.2
    elif recycling == 'no':
        return 10.8

def calculate_cooking_with_footprint(cooking_with):
    if cooking_with == 'electric':
        return 10.9
    elif cooking_with == 'gas':
        return 21.1  

# Define main function
def main():
    # Create a Streamlit app
    st.set_page_config(layout="wide",page_title="Carbon Footprint Calculator", page_icon="./media/favicon.ico")
    #st.set_page_title("CO2 Emissions by Individual")
    st.header("Calculate your carbon footprint")

    # Ask user for input
    body_type = st.selectbox('Body Type', ['slim', 'average', 'obese'])
    sex = st.selectbox('Sex', ['male', 'female'])
    diet = st.selectbox('Diet', ['vegan', 'vegetarian', 'meat'])
    shower_frequency = st.selectbox('Shower Frequency', ['daily', 'every other day', 'weekly'])
    heating_energy_source = st.selectbox('Heating Energy Source', ['gas', 'electricity'])
    transport = st.selectbox('Transport', ['driving', 'public transport', 'cycling'])
    vehicle_type = st.selectbox('Vehicle Type', ['gasoline', 'electric'])
    social_activity = st.selectbox('Social Activity', ['active', 'moderate', 'sedentary'])
    monthly_grocery_bill = st.number_input('Monthly Grocery Bill')
    frequency_of_traveling_by_air = st.selectbox('Frequency of Traveling by Air', ['frequent', 'occasional', 'rarely'])
    vehicle_monthly_distance_km = st.number_input('Vehicle Monthly Distance (km)')
    waste_bag_size = st.selectbox('Waste Bag Size', ['small', 'medium', 'large'])
    waste_bag_weekly_count = st.number_input('Waste Bag Weekly Count')
    tv_pc_hour = st.number_input('TV/PC Hour')
    daily_hour = st.number_input('Daily Hour')
    frequency_of_new_clothes = st.selectbox('Frequency of New Clothes', ['frequent', 'occasional', 'rarely'])
    internet_daily_hour = st.number_input('Internet Daily Hour')
    energy_efficiency = st.selectbox('Energy Efficiency', ['high', 'medium', 'low'])
    recycling = st.selectbox('Recycling', ['yes', 'no'])
    cooking_with = st.selectbox('Cooking With', ['electric', 'gas'])

    # Calculate carbon footprint
    body_type_footprint = calculate_body_type_footprint(body_type)
    sex_footprint = calculate_sex_footprint(sex)
    diet_footprint = calculate_diet_footprint(diet)
    shower_frequency_footprint = calculate_shower_frequency_footprint(shower_frequency)
    heating_energy_source_footprint = calculate_heating_energy_source_footprint(heating_energy_source)
    transport_footprint = calculate_transport_footprint(transport)
    vehicle_type_footprint = calculate_vehicle_type_footprint(vehicle_type)
    social_activity_footprint = calculate_social_activity_footprint(social_activity)
    monthly_grocery_bill_footprint = calculate_monthly_grocery_bill_footprint(monthly_grocery_bill)
    frequency_of_traveling_by_air_footprint = calculate_frequency_of_traveling_by_air_footprint(frequency_of_traveling_by_air)
    vehicle_monthly_distance_km_footprint = calculate_vehicle_monthly_distance_km_footprint(vehicle_monthly_distance_km)
    waste_bag_size_footprint = calculate_waste_bag_size_footprint(waste_bag_size)
    waste_bag_weekly_count_footprint = calculate_waste_bag_weekly_count_footprint(waste_bag_weekly_count)
    tv_pc_hour_footprint = calculate_tv_pc_hour_footprint(tv_pc_hour)
    daily_hour_footprint = calculate_daily_hour_footprint(daily_hour)
    frequency_of_new_clothes_footprint = calculate_frequency_of_new_clothes_footprint(frequency_of_new_clothes)
    internet_daily_hour_footprint = calculate_internet_daily_hour_footprint(internet_daily_hour)
    energy_efficiency_footprint = calculate_energy_efficiency_footprint(energy_efficiency)
    recycling_footprint = calculate_recycling_footprint(recycling)
    cooking_with_footprint = calculate_cooking_with_footprint(cooking_with)

    # Display results
    total_footprint = body_type_footprint + sex_footprint + diet_footprint + shower_frequency_footprint + heating_energy_source_footprint + transport_footprint + vehicle_type_footprint + social_activity_footprint + monthly_grocery_bill_footprint + frequency_of_traveling_by_air_footprint + vehicle_monthly_distance_km_footprint + waste_bag_size_footprint + waste_bag_weekly_count_footprint + tv_pc_hour_footprint + daily_hour_footprint + frequency_of_new_clothes_footprint + internet_daily_hour_footprint + energy_efficiency_footprint + recycling_footprint + cooking_with_footprint
    st.write("Your carbon footprint is:", total_footprint)

    # Display recommendations
    if total_footprint > 250:
        st.write("Consider reducing your energy consumption and transportation habits.")
    elif total_footprint > 350:
        st.write("Consider reducing your energy consumption and food choices.")
    else:
        st.write("Great job! Your carbon footprint is already low.")

if __name__ == "__main__":
    main()
