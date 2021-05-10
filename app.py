import streamlit as st
import pickle
import pandas as pd 
import numpy as np
import datetime
import time

def main():
    st.title("Flight-Price-Prediction")

    st.sidebar.subheader("Select Departure")
    m = pd.to_datetime("today").month
    d = pd.to_datetime("today").day
    y = pd.to_datetime("today").year
    
    dep = st.sidebar.date_input("Departure Day" , datetime.date(y,m,d))
    if dep is not None:
        mon_d = dep.month
        day_d = dep.day
        year_d = dep.year

    dep_time = st.sidebar.time_input('Departure Time')
    if dep_time is not None:
        hour_1 = dep_time.hour
        minute_1 = dep_time.minute
    
    st.subheader("Departure Time :")
    x = str(year_d) + "/"  +str(mon_d) + "/" + str(day_d) + " " + str(hour_1) + ":" + str(minute_1)
    if x is not None:
        op = pd.to_datetime([x])
        if op is not None:
            st.write(op[0])
    

    st.sidebar.subheader("Select Arrival")
    arr = st.sidebar.date_input("Arrival Day" , datetime.date(y,m,d+1))
    if arr is not None:
    
        mon_a = arr.month
        day_a = arr.day
        year_a = arr.year
        

    arr_time = st.sidebar.time_input('Arrival Time')
    if arr_time is not None:
        hour_2 = arr_time.hour
        minute_2 = arr_time.minute
        
    st.subheader("Arrival Time :")
    x1 = str(year_a) + "/"  +str(mon_a) + "/" + str(day_a) + " " + str(hour_2) + ":" + str(minute_2)
    if x1 is not None:
        
        op1 = pd.to_datetime([x1] )
        if op1 is not None:
            st.write(op1[0])
            



     #source
    st.subheader("Select Source")
    Source = st.selectbox(" " , ['Bangalore', 'Mumbai','Delhi','Kolkata',"Chennai"])
    if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

    elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0
    elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0

    elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1

    else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

    
    
    #destination
    st.subheader("Select Destination")
    dest = st.selectbox("" , ['Bangalore', 'Cochin', 'Hyderabad',"New Delhi",'Delhi','Kolkata'])

    if (dest == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
    elif (dest == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

    elif (dest == 'New_Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

    elif (dest == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0

    elif (dest == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

    else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0


 

    #airline
    st.subheader("Select Airline")
    airline = st.selectbox("  " , ["Air India","GoAir","IndiGo","Jet Airways","Multiple carriers","SpiceJet",
                                    "Vistara","Air Asia", "Trujet"])

    if(airline=='Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

    elif (airline=='IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 

    elif (airline=='Air India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
    elif (airline=='Multiple carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
    elif (airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
            
    elif (airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

    elif (airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

    elif (airline=='Multiple carriers Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

    elif (airline=='Jet Airways Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

    elif (airline=='Vistara Premium economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0
            
    elif (airline=='Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

    else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

   
    #stops
    st.subheader("Select Stops")
    stop = st.slider("Slide Me",min_value=0, max_value=4)
   
  
    st.sidebar.subheader("Duration")
    if op1 is not None:      
            st.sidebar.write((op1[0] - op[0]))

    
    op2 = (op1-op)
       
    hr = int(str(op2[0])[0])*24 + int(str(op2[0])[7])*10 + int(str(op2[0])[8])
    mini = int((str(op2[0])[10]))*10 + int((str(op2[0])[11]))
       
    
    rfr_model = pickle.load(open("flight_rf.pkl", "rb"))

    #prediction
    par = [stop , mon_d , day_d , hour_1 , minute_1 , hour_2 ,minute_2 ,hr , mini, Air_India, GoAir, IndiGo, Jet_Airways, Jet_Airways_Business, Multiple_carriers, Multiple_carriers_Premium_economy, SpiceJet, Trujet, 
           Vistara, Vistara_Premium_economy, s_Chennai, s_Delhi, s_Kolkata, s_Mumbai, d_Cochin, d_Delhi, d_Hyderabad, d_Kolkata, d_New_Delhi] 


    st.write("""    """)
    st.write("""    """)
    
    if st.button("PREDICT"):
        pred = rfr_model.predict([par])
        for i in pred:
            st.write("Your Fare Price is : " , round(i ,3)  , "INR")
    
    st.write("""    """)
    st.write("""    """)  
    st.write("""    """)
    st.write("""    """)  
   
    st.write("Created by: ***Sukreet Luthra***")
    st.write(''' Linkedin : https://www.linkedin.com/in/sukreetluthra ''')
 
    



if __name__ == "__main__":
    main()
