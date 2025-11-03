import streamlit as st
import pickle   
import numpy as np 

st.set_page_config(page_title="Emergency Response Predictor", layout="wide", page_icon="🚑")
 


with open('C:/Users/singh/OneDrive/Documents/Projects/Machine Learning/Emergency Response/model_emergency_one_hot.sav','rb') as file:
    Emergency =pickle.load(file)

st.title('Predict Emergency Response Time  ')

Distance_km = st.number_input('Distance_Km',step=1)
Traffic_Density = st.selectbox('Traffic_Density',('low','Medium','High'))
Road_Type =   st.selectbox('Road_Type',('Primary','Secondary','Residential'))
Time_of_Day = st.selectbox('Time_of_Day',('Evening' ,'Afternoon' ,'Night' ,'Morning'))                   
Day_of_Week = st.selectbox('Day_of_Week',('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'))                   
Weather = st.selectbox('Weather',('Rain','Clear','Snow','Fog'))                       
Num_Traffic_Signals = st.number_input('Num_Traffic_Signals',step=1,min_value=0,max_value=15)           
Speed_Limit_kmph = st.number_input('Speed_Limit_kmph',step=1)              
Incident_Type = st.selectbox('Incident_Type',('Other' ,'Medical' ,'Fire' ,'Crime'))                 
# 'The number of people living in one square kilometer of area.
Population_Density_per_km2 = st.number_input('Population_Density_per_km2')

Traffic_Density_group = {'low':[0,1,0],'Medium':[0,0,1],'High':[1,0,0]}
Traffic_Density_val = Traffic_Density_group[Traffic_Density]

Road_Type_group =  {'Primary':[1,0,0],'Secondary':[0,0,1],'Residential':[0,1,0]}
Road_Type_val = Road_Type_group[Road_Type]



Time_of_Day_group = {'Evening':[0,1,0,0] ,'Afternoon':[1,0,0,0] ,'Night':[0,0,0,1] ,'Morning':[0,0,1,0]}
Time_of_Day_val = Time_of_Day_group[Time_of_Day]

Day_of_Week_group = {'Monday':[0,1,0,0,0,0,0],'Tuesday':[0,0,0,0,0,1,0],'Wednesday':[0,0,0,0,0,0,1],'Thursday':[0,0,0,0,1,0,0],'Friday':[1,0,0,0,0,0,0],'Saturday':[0,0,1,0,0,0,0],'Sunday':[0,0,0,1,0,0,0]} 
Day_of_Week_val = Day_of_Week_group[Day_of_Week]

Weather_group = {'Rain':[0,0,1,0],'Clear':[1,0,0,0],'Snow':[0,0,0,1],'Fog':[0,1,0,0]}
Weather_val = Weather_group[Weather]

Incident_Type_group  = {'Other':[0,0,0,1],'Medical':[0,0,1,0] ,'Fire':[0,1,0,0],'Crime':[1,0,0,0]}
Incident_Type_val = Incident_Type_group[Incident_Type]

if Distance_km and  Num_Traffic_Signals and Speed_Limit_kmph and  Population_Density_per_km2:
    if st.button('Predict Response In Minutes 🚑',type="primary"):
        input = [Distance_km,Num_Traffic_Signals,Speed_Limit_kmph,Population_Density_per_km2]+Traffic_Density_val+Road_Type_val+Time_of_Day_val+Day_of_Week_val+Weather_val+Incident_Type_val
        input_data = np.array(input).reshape(1,-1)
        Prediction = Emergency.predict(input_data)
        Prediction_val = max(0,np.round(Prediction[0]))
        if  Prediction_val > 60:
            Hours =   int(Prediction_val //60)
            st.subheader((f"{Hours} Hours(Estimated Response Time(Hours))"))
        else: 
            st.subheader((f"{Prediction_val} Minutes(Estimated Response Time)"))
    

