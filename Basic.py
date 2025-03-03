import streamlit as st


st.title("Welcome to my page")

st.header("this is my new page")

st.subheader("I am Akshay....")

st.text("I am welcoming you all....")

st.markdown("&this is a markdown")

st.success("Python  for life")

st.info("informations are worthy")

st.warning("this is your last warning")

st.error("error  happened")

st.exception("typeError('name is not defined')")

st.help(range(2,10,2))

st.write("iAM writing the text")

st.write(range(0,10))



from PIL import Image
#img= Image.open("C:/Users/91812/Desktop/ML.jpg")
#st.image(img)


#img1= Image.open("C:/Users/91812/Desktop/ML.jpg")
#st.image(img1,width=300,caption="Iam MOHANLAL")


#img2= Image.open("C:/Users/91812/Desktop/imposter.jpg")
#st.image(img2,width=600)

#vedio1=open("C:/Users/91812/Desktop/veena/white kite.mp4",'rb').read()
#st.video(vedio1)

#vedio12=open('C:/Users/91812/Desktop/veena/pink kite.mp4','rb').read()
#st.video(vedio12)

#audiofile=open("C:/Users/91812/Downloads/Vennila-Chandanakkinnam-K-J-Yedudas-Sabnam.mp3",'rb').read()
#st.audio(audiofile)


if st.checkbox("show/hide"):
    st.text("showing or hide widget")


status=st.radio("what's your status",("active","inactive"))


if status == "active":
    st.success("CONGRATSS...You are active now")

else:
    st.success("SORRY...you are inactive")

#select box

occupation = st.selectbox("your occupation",["datascientist","programmer","business"])
st.write("you selected the option",occupation)


#multiselect

location=st.multiselect("where do you work?",("london","newyork","greece","india","dubai","maldives"))
st.write("you are selected",len(location),"locations")

level=st.slider("what is your level",1,2,3)

st.button("simple_button")

if st.button("About"):
    st.text("streamlit is cool")

#input

first_name=st.text_input("entered your name as:","Type here...")
if st.button("summit"):
    result=first_name.title()
    st.success(result)



#textarea
message=st.text_area("enter please","Type here...")
if st.button("ok"):
    resu=message.title()
    st.success(resu)