import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
import base64
import base64
import streamlit as st
import streamlit as st
import streamlit_authenticator as stauth
from pathlib import Path
import pickle
import datetime
from pymongo.mongo_client import MongoClient
import random as rd
from streamlit_chat import message
import glob as glob

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

#add_bg_from_local('bg_image.png')


__login__obj = __login__(auth_token = "courier_auth_token", 
                    company_name = "Shims",
                    width = 200, height = 250, 
                    logout_button_name = 'Logout', hide_menu_bool = False, 
                    hide_footer_bool = False, 
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()

cluster = MongoClient("mongodb+srv://SwagLikeOhio:VedanshCR7@cluster0.qtxpkyi.mongodb.net/?retryWrites=true&w=majority")
data = cluster["login"]["login"]



if LOGGED_IN == True:


    # Using object notation
    add_selectbox = st.sidebar.selectbox(
        "What would you like to do?",
        ("Home" , "Chat", "More Updates" , "Buy Merch" , "Support Us")
    )

    st.sidebar.title('Developer\'s Contact')
    st.sidebar.markdown('[![Vedansh Patel]'
                    '(https://img.shields.io/badge/Author-Vedansh%20Patel-brightgreen)]'
                    '(Nah)') 

    if add_selectbox == "Chat":
        #add_bg_from_local('back_img.webp')

        #video_file = open('main_page.mp4', 'rb')
       # video_bytes = video_file.read()

        #st.video(video_bytes)

    #elif add_selectbox == "Chat":
        # add_bg_from_local('back_img.png')


        message_history= []

        message("My message") 

        for message_ in message_history:
            message(message_)   # display all the previous message

        placeholder = st.empty()  # placeholder for latest message
        input_ = st.text_input("you:")
        message_history.append(input_)

        with placeholder.container():
            message(message_history[-1]) # display the latest message

    elif add_selectbox == "Home":
        st.title("Animetory.com")
        
