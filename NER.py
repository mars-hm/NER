import streamlit as st
import spacy #library used for ner
from spacy import displacy #for visualization
from collections import Counter # for storing count
import newspaper #for extracting newspapers from web
from newspaper import Article # extracts data in the url of the newspaper
import en_core_web_sm #english language model
nlp = en_core_web_sm.load()

#header using markdown
st.markdown("<h1 style='text-align: center; color: #195759;'>NER - Named Entity Recognition</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #76AB9D;'>DEMO</h2>", unsafe_allow_html=True)
#st.title("Demo")
#to display informational message
st.info("This appilication takes 2 types of inputs from the User: URL or Paragraph. Based on the input given, it prints NER of the given input.")
choice=st.selectbox("Input",['Text','URL'])
if (choice=='URL'):
    url = st.text_input("Insert an URL: ") #single-line text input
else:
    ipara = st.text_area("Enter a Paragraph: ")

if(st.button("Analyze")):
    if choice=='URL':
        article = Article(url)
        article.download() #with the help of download function the content of newspaper will be stored in the variable article
        article.parse() #analysing the text, grammar & to find the relationship among words
        print(article.text) #contains the extracted & analysed content
        ourl = nlp(article.text)
        ent_html=displacy.render(ourl, style='ent', jupyter=False) #visualize ners in the data
        st.markdown(ent_html, unsafe_allow_html=True) 
      
    else:
        opara = nlp(ipara)
        ent_html = displacy.render(opara, style="ent", jupyter=False)
        # Display the entity visualization in the browser:
        st.markdown(ent_html, unsafe_allow_html=True)
