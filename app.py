import streamlit as st


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
    background-image: url(https://cdna.artstation.com/p/assets/images/images/015/608/430/large/artur-sadlos-leg-duo-sh030-background-as-v002.jpg);
    background-size: cover;
}
"""


with st.container():
    st.subheader('**Hi Everyone! **')
    st.title('**Project League of Legends**')
    st.write('**Our trained model will help you predict the outcome**')



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
        st.image('https://giffiles.alphacoders.com/527/52704.gif', width = 500)
