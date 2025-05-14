import streamlit as st

st.title('GS')

col1,col2=st.columns(2)

with col1:
    st.write("""Hello everyone , I am Prime Minister of India ,Gyanendra Singh Yadav""")

with col2:
    st.write("""Thank you Universe I did it , I have changed the whole education system of India""")


st.header('Policies')
st.subheader('P1')
st.subheader('No Exam')
st.subheader('morals')
st.subheader('Gyanendra')

st.sidebar.title('About')
st.sidebar.subheader('Genius')
st.sidebar.subheader('Morals')
st.sidebar.subheader('Gyanendra')
st.sidebar.selectbox('Select',['virat','rohit'])
st.sidebar.button('Select')