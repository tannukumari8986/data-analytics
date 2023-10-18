import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.header('hey')
st.subheader('welcome to my project')

st.number_input('select marks', min_value=1,max_value=10)
#a = st.file_uploader("Upload your marksheet")
#sst.image(a)
st.select_slider('grade',['fail','pass', 'first class', 'distinction'])
st.slider('select feedback' , 0 , 1000)

st.multiselect('select subject',['html' , 'css' , 'js' , 'python'])
st.radio(' select your gender',['female' , 'male' , 'transgender'])
st.button('submit')

#st.caption('caption')
st.code('huehuehue')
st.markdown('markdown')


if st.checkbox('check'):
	st.write("Thankyou")

st.image('tz.jpg')


df = pd.read_csv("details.csv")
name_filter = st.selectbox("Select Name",pd.unique(df["Name"]))

st.title("My streamlit Web app")
st.write("This is the raw dataset")

st.write(df)
st.write("Data Description")

st.write(df.describe())
st.write("Data Info")
st.write(df.info())

fig = plt.figure(figsize = (19,10))
plt.bar(df['Name'], df['Maths'], color = 'blue')
plt.xlabel('Name')
plt.ylabel('Marks')
plt.title('Matplotlib Bar Chart')

st.pyplot(fig)