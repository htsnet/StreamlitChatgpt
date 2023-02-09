import streamlit as st
import openai
from io import StringIO

# Insira sua chave de API aqui
openai.api_key = st.secrets['api_key_openai']

def revise_text(text, acao):
    with st.spinner('Wait for it...'):
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=acao + '"' + text + ' "' + ", keep the same language of this text",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

    message = completions.choices[0].text
    # print(message)
    return message

def check_text(text):
    if text:
        return True
    st.info('The text field is empty!', icon="⚠️")
    return False


# título
Title = f'Analysis and Improvement of Texts with AI (ChatGPT)'
st.title(Title)

#colunas
col1, col2 = st.columns([0.7, 0.3])

with col1:
    text_base = ''

    text = st.text_area("Paste your text into the box below.", value=text_base, max_chars=10000, height=400)
    # textxsss = "Se o pessoal vê as minhas três vontades engordando desse jeito e crescendo que nem balão, eles vão rir, aposto. Eles não entendem essas coisas, acham que é infantil, não levam a sério. Eu tenho que achar depressa um lugar pra esconder as três: se tem coisa que eu não quero mais é ver gente grande rindo de mim."

with col2:
    uploaded_file = st.file_uploader("Or choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        # st.write(bytes_data)
        text_base = bytes_data


tab1, tab2, tab3, tab4 = st.tabs(['Summary', 'Sentiment', 'Rewriting', 'Change Style', ])


# show tabs to choose the action
with tab1:
    st.write('Make a short summary of the text')
    botSummary = st.button("Text Summary")
    if botSummary:
        if check_text(text):
            revised_text = revise_text(text, "Faça um resumo rápido deste texto: ")
            st.write(revised_text)

with tab2:    
    st.write('Identify the principal sentiment')
    botSentiment = st.button("Text Sentiment")
    if botSentiment:
        if check_text(text):
            revised_text = revise_text(text, "Qual o sentimento deste texto? ")
            st.write(revised_text)    
        
with tab3:        
    st.write('Rewrite and try to improve the text')
    botRewriting = st.button("Text Rewriting")
    if botRewriting:
        if check_text(text):
            revised_text = revise_text(text, "Reescreva e melhore o texto: ")
            st.write(revised_text)   

with tab4:        
    st.write('Change the style to humorous')
    botStyle = st.button("Change Style")
    if botStyle:
        if check_text(text):
            revised_text = revise_text(text, "Reescreva o texto em estilo humorístico: ")
            st.write(revised_text)                  

with st.sidebar:
    st.header('Usage guidance')
    st.write('1 - Use a text copied from another location as a base and paste it in the indicated box. The limit is 5000 characters. You can also upload an file instead of paste the text.')
    st.write('2 - Choose the tab desired and press the button to perform the action.')
    st.write('3 - The final text will be in the same language as the original.')