import streamlit as st
from PIL import Image
# from predictleague.ml_logic import data, preprocessor
# from predictleague.api import fast
# from predictleague.interface import main
#from tensorflow.keras.models import load_model
#from predictleague.ml_logic.preprocessor import preprocess_input_data
from predictleague.api.fast import predict



st.set_page_config(page_title='Our Data Science Project', page_icon='🍁', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)




# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#background
CSS = """
h1 {
    color: red;
}
.stApp {
    #background-image: url(https://cdn.vox-cdn.com/uploads/chorus_asset/file/22991847/Sisters4.JPG);
    background-image: url(https://cdna.artstation.com/p/assets/images/images/015/609/184/large/mathias-zamecki-1.jpg?1548953774);
    background-size: cover;
}
"""

#if st.checkbox('click me', True):
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)


with st.container():
    st.subheader('**Hi Everyone!**')
    st.title('**Project Head-hunting for League of Legends teams**')
    st.write('**Our trained model will help you predict if you can actually become a pro**')



#   What do I do

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2,  gap= 'large')
    with left_column:
        st.header("Let's have a look together")
        st.write('##')
        st.write(
        '''
        - **We have collected data of all the matches that's been played in 2022**
        - **We have then created a model which group each team in different cluster based on their game style and match planning**
        - **The idea of our model is to help individuals find out their opponents or favorite teams game tactics**
        - **This can also help E-sports team coaches to prepare their teams accordingly by looking at their opponents weakness and strong points**
        - **lets find more in details**

        '''
    )

    with right_column:
        #st.image('https://giffiles.alphacoders.com/527/52742.gif', width = 500)
        st.image('https://cdna.artstation.com/p/assets/images/images/045/824/282/original/jan-turkiewicz-zeri-animtaion.gif', width = 500)

st.markdown(f'<h1 style="color:##FF0000	;font-size:24px;">{"Please insert your last matches result"}</h1>', unsafe_allow_html=True)

x = st.text_input(" Please put 1 for won and 0 for lost match ")


st.write("**Can you be a major league player** ?    ",   predict(x))
