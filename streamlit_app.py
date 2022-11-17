import streamlit as st
import requests
import json
import pickle
import pandas as pd
import random
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("Travel at ease with iRecommend ✈️ ")
st.header("A recommender system based on activity preferences")
st.markdown('For each of the categories below, please indicate whether you like or dislike the activity. After indicating your preference, please click on the next category tab to proceed.')

st.sidebar.markdown("By: Richelle-Joy Chia") 
st.sidebar.markdown("[GitHub](https://git.generalassemb.ly/richellejoy/capstone)") 
st.sidebar.markdown("[Linkedin](https://www.linkedin.com/in/richelle-joy-chia/)") 

# filter

st.sidebar.title('Filter:')
st.sidebar.caption('This is a beta version')

accommodation1 = st.sidebar.checkbox('Includes Accommodation')
transport1 = st.sidebar.checkbox('Includes Transportation')
food1 = st.sidebar.checkbox('Food Provided')
alcohol1 = st.sidebar.checkbox('Alcohol Available ($)')
airtour1 = st.sidebar.checkbox('Includes Air Tour')
landtour1 = st.sidebar.checkbox('Includes Land Tour')
seatour1 = st.sidebar.checkbox('Includes Sea Tour')

api_url = 'https://travel-recommender-07-fp4ntez6xq-as.a.run.app'
api_route = '/act'
filter_category = {}
response1 = requests.post(f'{api_url}{api_route}', json=json.dumps(filter_category)) # json.dumps() converts dict to JSON
output1 = response1.json()

#we have to put the inputs all inside a form to prevent the whole app from being re-run each time a input is change. 
# https://blog.streamlit.io/introducing-submit-button-and-forms/

#main
with st.form("my_form"):
 
    api_url = 'https://travel-recommender-07-fp4ntez6xq-as.a.run.app'
    api_route = '/act'
    user_input = {}
    response1 = requests.post(f'{api_url}{api_route}', json=json.dumps(user_input)) # json.dumps() converts dict to JSON
    output1 = response1.json()
    
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs(["City", "Brewery/Distillery/Winery", "Boat Tours and Cruises", "Classes & Workshops", "Equipment Rentals", "Live Entertainment", "Nature", "Outdoor Activities", "Photoshoot", "Sightseeing", "Spotting Wildlife"])
    with tab1:    
        st.subheader(output1['names'][0])
        col1, col2 = st.columns([3, 1])
        with col1:
            st.image((output1['images'][0]),use_column_width='auto')
        with col2:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            city_button = st.radio(label= '', options= ["Like", "Dislike"], 
                              key="city", label_visibility='hidden')
        if city_button == 'Dislike':
            dislike_city = 1
            like_city = 0
        elif city_button == 'Like':
            dislike_city = 0
            like_city = 1

    with tab2:     
        st.subheader(output1['names'][1])
        col1, col2 = st.columns([3, 1])
        with col1: 
            st.image((output1['images'][1]),use_column_width='auto')
        with col2:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            alcohol_places_button = st.radio(label= '', options= ["Like", "Dislike"], 
                              key="bdw", label_visibility='hidden')
        if alcohol_places_button == 'Dislike':
            dislike_bdw = 1
            like_bdw = 0
        elif alcohol_places_button == 'Like':
            dislike_bdw = 0
            like_bdw = 1
        
    with tab3:    
        st.subheader(output1['names'][2])
        col1, col2 = st.columns([5, 1])
        with col1:
            st.image((output1['images'][2]),use_column_width='auto')
        with col2:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            cruise_button = st.radio(label= '', options= ["Like", "Dislike"], 
                              key="cruise", label_visibility='hidden')
        if cruise_button == 'Dislike':
            dislike_cruise = 1
            like_cruise = 0
        elif cruise_button == 'Like':
            dislike_cruise = 0
            like_cruise = 1
        
    with tab4:    
        st.subheader(output1['names'][3])
        col1, col2 = st.columns([5, 1])
        with col1:
            st.image((output1['images'][3]),use_column_width='auto')
        with col2:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            classworkshops_button = st.radio(label= '', options= ["Like", "Dislike"], 
                              key="classesworkshops", label_visibility='hidden')
        if classworkshops_button == 'Dislike':
            dislike_classesworkshops = 1
            like_classesworkshops = 0
        elif classworkshops_button == 'Like':
            dislike_classesworkshops = 0
            like_classesworkshops = 1
    
    with tab5:    
        st.subheader(output1['names'][4])
        col1, col2 = st.columns([5, 1])
        with col1:
            st.image((output1['images'][4]),use_column_width='auto')
        with col2:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            rental_button = st.radio(label= '', options= ["Like", "Dislike"], 
                              key="rental", label_visibility='hidden')
        if rental_button == 'Dislike':
            dislike_rental = 1
            like_rental = 0
        elif rental_button == 'Like':
            dislike_rental = 0
            like_rental = 1
    
    with tab6:
        st.subheader(output1['names'][5])
        col1, col2 = st.columns([5, 1])
        with col1:
            st.image((output1['images'][5]),use_column_width='auto')
        with col2:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            entertainment_button = st.radio(label= '', options= ["Like", "Dislike"], 
                              key="entertainment", label_visibility='hidden')
        if entertainment_button == 'Dislike':
            dislike_entertainment = 1
            like_entertainment = 0
        elif entertainment_button == 'Like':
            dislike_entertainment = 0
            like_entertainment = 1
    
    with tab7:
        st.subheader(output1['names'][6])
        col1, col2 = st.columns([5, 1])
        with col1:
            st.image((output1['images'][6]),use_column_width='auto')
        with col2:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            nature_button = st.radio(label= '', options= ["Like", "Dislike"], 
                              key="nature", label_visibility='hidden')
        if nature_button == 'Dislike':
            dislike_nature = 1
            like_nature = 0
        elif nature_button == 'Like':
            dislike_nature = 0
            like_nature = 1

    with tab8:
        st.subheader(output1['names'][7])
        col1, col2 = st.columns([5, 1])
        with col1:
            st.image((output1['images'][7]),use_column_width='auto')
        with col2:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            oa_button = st.radio(label= '', options= ["Like", "Dislike"], 
                              key="outdoor_activities", label_visibility='hidden')
        if oa_button == 'Dislike':
            dislike_oa = 1
            like_oa = 0
        elif oa_button == 'Like':
            dislike_oa = 0
            like_oa = 1
    

    with tab9:
        st.subheader(output1['names'][8])
        col1, col2 = st.columns([5, 1])
        with col1:
            st.image((output1['images'][8]),use_column_width='auto')
        with col2:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            photo_button = st.radio(label= '', options= ["Like", "Dislike"], 
                              key="photography", label_visibility='hidden')
        if photo_button == 'Dislike':
            dislike_photography = 1
            like_photography = 0
        elif photo_button == 'Like':
            dislike_photography = 0
            like_photography = 1
        
        
    with tab10:
        st.subheader(output1['names'][9])
        col1, col2 = st.columns([5, 1])
        with col1:
            st.image((output1['images'][9]),use_column_width='auto')
        with col2:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            sightseeing_button = st.radio(label= '', options= ["Like", "Dislike"], 
                                  key="sightseeing", label_visibility='hidden')
        if sightseeing_button == 'Dislike':
            dislike_sightseeing = 1
            like_sightseeing = 0
        elif sightseeing_button == 'Like':
            dislike_sightseeing = 0
            like_sightseeing = 1
    
    with tab11:
        st.subheader(output1['names'][10])
        col1, col2 = st.columns([5, 1])
        with col1:
            st.image((output1['images'][10]),use_column_width='auto')
        with col2:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            wildlife_button = st.radio(label= '', options= ["Like", "Dislike"], 
                              key="wildlife", label_visibility='hidden')
        if wildlife_button == 'Dislike':
            dislike_wildlife = 1
            like_wildlife = 0
        elif wildlife_button == 'Like':
            dislike_wildlife = 0
            like_wildlife = 1
        
        with st.spinner ("Cooking up something amazing for you."):
            submitted = st.form_submit_button("Show Recommendations")


category = {'oa_like': int(like_oa), 'oa_dislike': int(dislike_oa), 'sightseeing_like': int(like_sightseeing), 'sightseeing_dislike': int(dislike_sightseeing), 
            'city.1_like': int(like_city), 'city.1_dislike': int(dislike_city), 
            'classes & workshops_like': int(like_classesworkshops), 
            'classes & workshops_dislike': int(dislike_classesworkshops), 
            'cruise_like': int(like_cruise), 'cruise_dislike': int(dislike_cruise), 
            'entertainment_like': int(like_entertainment), 'entertainment_dislike': int(dislike_entertainment), 
            'brewery/distillery/winery_like': int(like_bdw), 
            'brewery/distillery/winery_dislike': int(dislike_bdw), 'nature_like': int(like_nature), 
            'nature_dislike': int(dislike_nature), 'photography_like': int(like_photography), 
            'photography_dislike': int(dislike_photography), 
            'rental_like': int(like_rental), 'rental_dislike': int(dislike_rental), 'wildlife_like': int(like_wildlife), 
            'wildlife_dislike': int(dislike_wildlife)}


if submitted:

    total = (like_oa + dislike_oa + like_cruise + dislike_cruise + like_city + dislike_city + like_classesworkshops + dislike_classesworkshops 
    + like_rental + dislike_rental + like_entertainment + dislike_entertainment + like_nature + dislike_nature + like_photography + dislike_photography +
    like_wildlife + dislike_wildlife + like_sightseeing + dislike_sightseeing + like_bdw + dislike_bdw)                  

    api_url = 'https://travel-recommender-07-fp4ntez6xq-as.a.run.app'
    api_route = '/predict'

    response = requests.post(f'{api_url}{api_route}', json=json.dumps(category)) # json.dumps() converts dict to JSON
    output = response.json()
    name = output['recommended_attractions']
    attraction_url = output['attraction_url']
    images = output['images']
    rating = output['rating']
    city = output['city']
    province = output['province']
    price = output['price']
    label = output['label']
    duration = output['duration']

    st.subheader("Based on your selected preferences, here are the top 6 recommended attractions for you.")     
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Recommendation 1", "Recommendation 2", "Recommendation 3", "Recommendation 4", "Recommendation 5", "Recommendation 6"])

    with tab1:
        col1, col2, col3 = st.columns([2,.1, 1])
        with col1:
            st.markdown(f"Attraction: [{name[0]}](%s)"%attraction_url[0])
            st.image((output['images'][0]),use_column_width='auto')
        with col2:
            st.text(' ')
        with col3:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown(f"Average rating: {round(rating[0],1)}")
            st.markdown(f"Location: {city[0]}, {(province[0])}")
            st.markdown(f"Duration: {duration[0]}")
            st.markdown(f"Approximate cost: ${price[0]}")
            st.markdown(f"What people generally feel: {label[0]}")

    with tab2:
        col1, col2, col3 = st.columns([2,.1, 1])
        with col1:
            st.markdown(f"Attraction: [{name[1]}](%s)"%attraction_url[1])
            st.image((output['images'][1]),use_column_width='auto')
        with col2:
            st.text(' ')
        with col3:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown(f"Average rating: {round(rating[1],1)}")
            st.markdown(f"Location: {city[1]}, {(province[1])}")
            st.markdown(f"Duration: {duration[1]}")
            st.markdown(f"Approximate cost: ${price[1]}")
            st.markdown(f"What people generally feel: {label[1]}")

    with tab3:
        col1, col2, col3 = st.columns([2,.1, 1])
        with col1:
            st.markdown(f"Recommendation 3: [{name[2]}](%s)"%attraction_url[2])
            st.image((output['images'][2]),use_column_width='auto')
        with col2:
            st.text(' ')
        with col3:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown(f"Average rating: {round(rating[2],1)}")
            st.markdown(f"Location: {city[2]}, {(province[2])}")
            st.markdown(f"Duration: {duration[2]}")
            st.markdown(f"Approximate cost: ${price[2]}")
            st.markdown(f"What people generally feel: {label[2]}")

    with tab4:
        col1, col2, col3 = st.columns([2,.1, 1])
        with col1:
            st.markdown(f"Recommendation 4: [{name[3]}](%s)"%attraction_url[3])
            st.image((output['images'][3]),use_column_width='auto')
        with col2:
            st.text(' ')
        with col3:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown(f"Average rating: {round(rating[3],1)}")
            st.markdown(f"Location: {city[3]}, {(province[3])}")
            st.markdown(f"Duration: {duration[3]}")
            st.markdown(f"Approximate cost: ${price[3]}")
            st.markdown(f"What people generally feel: {label[3]}")


    with tab5:
        col1, col2, col3 = st.columns([2,.1, 1])
        with col1:
            st.markdown(f"Recommendation 5: [{name[4]}](%s)"%attraction_url[4])
            st.image((output['images'][4]),use_column_width='auto')
        with col2:
            st.text(' ')
        with col3:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown(f"Average rating: {round(rating[4],1)}")
            st.markdown(f"Location: {city[4]}, {(province[4])}")
            st.markdown(f"Duration: {duration[4]}")
            st.markdown(f"Approximate cost: ${price[4]}")
            st.markdown(f"What people generally feel: {label[4]}")

    with tab6:
        col1, col2, col3 = st.columns([2,.1, 1])
        with col1:
            st.markdown(f"Recommendation 6: [{name[5]}](%s)"%attraction_url[5])
            st.image((output['images'][5]),use_column_width='auto')
        with col2:
            st.text(' ')
        with col3:
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown('\n')
            st.markdown(f"Average rating: {round(rating[5],1)}")
            st.markdown(f"Location: {city[5]}, {(province[5])}")
            st.markdown(f"Duration: {duration[5]}")
            st.markdown(f"Approximate cost: ${price[5]}")
            st.markdown(f"What people generally feel: {label[5]}")

