import pickle
import json
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
import base64

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru' ]

pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title('IPL MATCH WINNING PREDICTOR')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('SELECT BATTING TEAM ',sorted(teams))

with col2:
    bowling_team = st.selectbox('SELECT BOWLING TEAM',sorted(teams))

selected_city = st.selectbox('SELECT VENUE',sorted(cities))
target = int(st.number_input('TARGET'))

col3,col4,col5 = st. columns(3)

with col3:
    score = st.number_input('CURRENT SCORE')

with col4:
    overs = st.number_input('OVERS COMPLETED')

with col5:
    wickets = st.number_input('WICKETS OUT')

if st.button('PREDICT WINNING PROBABLITY'):
    runs_left = int(target - score)
    balls_left = int(120 - (6*overs))
    wickets = int(10 - wickets)
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    stats = pd.DataFrame({'BATTING TEAM':[batting_team],'BOWLING TEAM':[bowling_team],
                  'CITY':[selected_city],'RUNS LEFT':[runs_left],'BALLS LEFT':
                  [balls_left],'WICKETS LEFT':[wickets],'TARGET':[target],'CRR':
                  [crr],'RRR':[rrr]})
    st.table(stats)

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],
                  'city':[selected_city],'runs_left':[runs_left],'balls_left':
                  [balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':
                  [crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    losing = result[0][0]
    win = result[0][1]
    st.subheader(batting_team + '- ' + str(round(win*100)) + '%')
    st.subheader(bowling_team + '- ' + str(round(losing*100)) + '%')





def load_lottiefile(filepath: str):
    with open(filepath,'r') as f:
        return json.load(f)

lottie = load_lottiefile('C:/Users/User/PycharmProjects/newproject/141115-bat-ball.json')
st_lottie(lottie)






#
# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
#         background-size: cover
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
#     )
# add_bg_from_local('ipl.jpg')





