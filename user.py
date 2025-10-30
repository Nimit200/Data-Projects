import streamlit as st
import pickle   
import numpy as np 

st.set_page_config(page_title="Emergency Response Predictor", layout="wide", page_icon="🚑")
 


with open('C:/Users/singh/OneDrive/Documents/Projects/Machine Learning/Emergency Response/model_emergency.sav','rb') as file:
    Emergency =pickle.load(file)

st.title('Predict Emergency Response Time  ')

Distance_km = st.sidebar.slider('Distance_Km',step=1)
Traffic_Density = st.selectbox('Traffic_Density',('low','Medium','High'))
Road_Type =   st.selectbox('Road_Type',('Primary','Secondary','Residential'))
Time_of_Day = st.selectbox('Time_of_Day',('Evening' ,'Afternoon' ,'Night' ,'Morning'))                   
Day_of_Week = st.selectbox('Day_of_Week',('Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday'))                   
Weather = st.selectbox('Weather',('Rain','Clear','Snow','Fog'))                       
Num_Traffic_Signals = st.sidebar.slider('Num_Traffic_Signals',step=1,min_value=0,max_value=15)           
Speed_Limit_kmph = st.sidebar.slider('Speed_Limit_kmph',step=1)              
Incident_Type = st.selectbox('Incident_Type',('Other' ,'Medical' ,'Fire' ,'Crime'))                 
Population_Density_per_km2 = st.sidebar.slider('Population_Density_per_km2')

Traffic_Density_group = {'low':1,'Medium':2,'High':0}
Traffic_Density_val = Traffic_Density_group[Traffic_Density]

Road_Type_group =  {'Primary':0,'Secondary':2,'Residential':1}
Road_Type_val = Road_Type_group[Road_Type]


Time_of_Day_group = {'Evening':1 ,'Afternoon':0 ,'Night':3 ,'Morning':2}
Time_of_Day_val = Time_of_Day_group[Time_of_Day]

Day_of_Week_group = {'Monday':1,'Tuesday':5,'Wednesday':6,'Thrusday':4,'Friday':0,'Saturday':2,'Sunday':3} 
Day_of_Week_val = Day_of_Week_group[Day_of_Week]

Weather_group = {'Rain':2,'Clear':0,'Snow':3,'Fog':1}
Weather_val = Weather_group[Weather]

Incident_Type_group  = {'Other':3,'Medical':2 ,'Fire':1,'Crime':0}
Incident_Type_val = Incident_Type_group[Incident_Type]

if Distance_km and  Num_Traffic_Signals and Speed_Limit_kmph and  Population_Density_per_km2:
    if st.button('Pedict Response In Minutes 🚑',type="primary"):
        input = Distance_km,Traffic_Density_val,Road_Type_val,Traffic_Density_val,Day_of_Week_val,Weather_val,Num_Traffic_Signals,Speed_Limit_kmph,Incident_Type_val,Population_Density_per_km2
        input_data = np.array(input).reshape(1,-1)
        Prediction = Emergency.predict(input_data)
        Prediction_val = max(0,np.round(Prediction[0]))
        if  Prediction_val > 60:
            Hours =   int(Prediction_val //60)
            st.subheader((f"{Hours} Hours(Estimated Response Time(Hours))"))
        else: 
            st.subheader((f"{Prediction_val} Minutes(Estimated Response Time)"))
    

