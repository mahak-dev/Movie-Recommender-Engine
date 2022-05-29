from pickle import TRUE
from typing import Container
from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import webbrowser


st.set_page_config(page_title="Mahak Gupta", page_icon=":alien:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
         
local_css("style/style.css")
#--load ASSETS -----
lottie_Hello = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_coahzstz.json")
lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_SqEf0A.json")
lottie_github = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_Cko7Sr.json")
lottie_linkedin = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_b04ltv0r.json")
lottie_mail = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_xntsaeql.json")
lottie_whatsapp = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_qnpfavmd.json")

img_ss1 = Image.open("images/ss1.png")
img_Demo = Image.open("images/Demo.png")
#header section
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Hii, I am Mahak Gupta :wave:")
        st.title("A Student from INDIA")
        st.write("I'm an enthusiastic Python Developer based in India. I'm also passionate about ML and AI. I like to explore tech and grow my knowledge everyday.")
        
        url = 'https://errortb.blogspot.com'

        if st.button('Errortb'):
            webbrowser.open_new_tab(url)
    with right_column:
        st_lottie(lottie_Hello, height=300, key="Hello")
        
#-- What I DO

with st.container():
    st.write("---")
    left_column, right_column = st.columns((1, 2))
    with left_column:
        st_lottie(lottie_coding,height=400, key="movie")
        
    with right_column:
        st.header("Project Abstract")
        st.write("##")
        st.subheader("This project is divided into two parts:")
        st.write(
            """The Story of Film: This section aims at narrating the history, trivia and facts behind the world of cinema through the lens of data. Casts, Crews, Budgets, etc. through the years. Through the two models, we also aim at discovering what features have the most significant impact in determining revenue and success."""

        )
        st.write("""
                 Movie Recommender Systems: This part is focused around building various kinds of recommendation engines; namely the Simple Generic Recommender, the Content Based Filter and the User Based Filter. 
                """)
        
        url = 'https://mrs-engine.herokuapp.com/'

        if st.button('Here is the Project'):
            webbrowser.open_new_tab(url)
            
with st.container():
    st.write("---")
    st.header("The Approach")
    st.write("")
    st.markdown("""
            <ul style='justify-content:center;'><li style='justify-content:center; font-size:20px;'><strong>Data Collection: </strong> Data was collected from the MovieLens website and through a script that queried for data from various TMDB Endpoints.</li>
            
            <li style = 'justify-content:center; font-size:20px;'><strong>Data Wrangling: </strong>The datasets were uploaded to a dataframe and explored. Null values were filled in wherever appropriate and polluted values were discarded or wrangled.</li>
            
            <li style = 'justify-content:center; font-size:20px;'><strong>EDA: </strong>Extensive data visualisation and summary statistics were used to extract insights and pattern from the various datasets. The history, facts and trivia behind movies were narrated through data.</li>
            
            <li style = 'justify-content:center; font-size:20px;'><strong>Machine Learning: </strong>Gradient Boosting Classifer and Regressor were trained on our feature engineered dataset to predict movie success and revenue respectively. Their feature importances were noted to gain insights into what factors influence the revenues of a movie relative to budget.</li>
            
            <li style = 'justify-content:center; font-size:20px;'><strong>Recommendation Systems: </strong>Four different recommendation systems were built using various ideas and algorithms such as TMDB's Weighted Rating, Content Based Filtering and Collaborative Filtering. A Gradient Boosting Regressor and Classifier were built in Jupyter to predict Movie Revenue and Success respectively with a Score of 0.78 and 0.8 respectively. In addition, four recommendation engines were built based on different ideas and algorithms:</li>
            
            <li style = 'justify-content:center; font-size:20px;'><strong>Simple Recommender: </strong>The TMDB Weighted Rating System was used to calculate ratings on which the sorting was finally performed.</li>
            
            <li style = 'justify-content:center; font-size:20px;'><strong>Hybrid Engine: </strong>I brought together ideas from content and collaborative filtering to build an engine that gave movie suggestions to a particular user based on the estimated ratings that it had internally calculated for that user.</li>
            
            </ul>
            """, unsafe_allow_html=True)
    


#-----Projects------
with st.container():
    st.write("---")
    st.header("Movie Recommender Engine using Machine Learning")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_ss1)
    with text_column:
        st.subheader("Machine Learning based recommender Engine")
        st.write(
            """
            Whole code and files are uploaded on Github Repo.
            """
        )
        url = 'https://github.com/mahak-dev/Movie-Recommender-Engine'

        if st.button('Github Repo'):
            webbrowser.open_new_tab(url)
            
with st.container():
    st.write("---")
    st.header("Watch Video Demo")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_Demo)
    with text_column:
        st.subheader("Machine Learning based recommender Engine")
        st.write(
            """
              A Video Demo of project based on Recommendation Engine with Machine Learnong.
            """
        )
        url = 'https://www.youtube.com/watch?v=p4cw3cZ9Fr4&t=4s'

        if st.button('Demo Video'):
            webbrowser.open_new_tab(url)
        
# ------ Contact ------
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    
    # Docuemenation 
    contact_form = """
    <form action="https://formsubmit.co/guptamahak740@gmail.com" method="POST">
     <input type="hidden" name = "_captcha" value = "false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
        
    


with st.container():
    st.write("---")
    
    st.header("Let's Connect :envelope:")
    st.write("##")
    Linkedin = 'https://www.linkedin.com/in/mahak-gupta-60197a1aa/'
    Github = 'https://github.com/mahak-dev'
    Mail = 'mailto:guptamahak740@gmail.com'
    Whatsapp = 'https://www.hackerrank.com/guptamahak740'
    
    col1, col2, col3, col4 =st.columns(4)
    with col1:
        st_lottie(lottie_github,height=150, key="social-github")
        if st.button('Github'):
            webbrowser.open_new_tab(Github)
        
    with col2:
        st_lottie(lottie_mail,height=150, key="social-mail")
        if st.button("Email"):
            webbrowser.open_new_tab(Mail)
    with col3:
        st_lottie(lottie_linkedin,height=150, key="social-linkedin")
        if st.button("LinkedIn"):
            webbrowser.open_new_tab(Linkedin)
    with col4:
        st_lottie(lottie_whatsapp,height=150, key="social-whatsapp")
        if st.button("Whatsapp"):
            webbrowser.open_new_tab(Whatsapp)
    
    st.write("###")
    
    
    st.markdown("<p style='text-align: center; color: white;'>2022 © MahakGupta | Developed by Mahak Gupta®</p>", unsafe_allow_html=True)
    

    