import streamlit as st
import openai
from io import StringIO
import pdfplumber

# Insira sua chave de API aqui
openai.api_key = st.secrets['api_key_openai']

with st.sidebar:
    st.header('Usage guidance')
    st.write('1 - Upload an TXT file to be treated. Or paste a text in the indicated box. The limit is 5000 characters.')
    st.write('2 - Choose the tab desired and press the button to perform the action.')
    st.write('3 - The final text will be in the same language as the original.')
    st.write('4 - Use the options below to change responses.')
    
    st.header('Parameters')
    temperature = st.slider('Confidence', 0, 100, 50, 1)/100
    st.write('Temperature for action. Smaller values are more accurate, larger values are more risky.')
    
    max_tokens = st.slider('Limit words', 10, 4000, 1000, 100)
    st.write('Limit of words for the response.')
    
    

def revise_text(text, acao, max_tokens, temperature):
    with st.spinner('Wait for it...'):
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=acao + '"' + text + ' "' + ", mantenha a língua na do texto tratado",
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=temperature,
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
col1, col2 = st.columns([0.3, 0.7])

text_base = ''

with col1:
    uploaded_file = st.file_uploader("Choose a file to upload",  type=['txt', 'pdf'], help="Only txt file.")
    if uploaded_file is not None:
        nameFile = uploaded_file.name.upper().split('.')
        if nameFile[-1] == 'PDF':
            with pdfplumber.open(uploaded_file) as pdf:
                text_base = ''
                pages = pdf.pages
                for p in pages:
                    text_base = text_base + p.extract_text()
        elif nameFile[-1] == 'TXT':
            text_base = uploaded_file.read().decode('utf-8')
        else:
            st.error('Wrong type!')

with col2:
    text = st.text_area("or paste your text into the box below.", value=text_base, max_chars=10000, height=400, key='text_area_field')
    # textxsss = "Se o pessoal vê as minhas três vontades engordando desse jeito e crescendo que nem balão, eles vão rir, aposto. Eles não entendem essas coisas, acham que é infantil, não levam a sério. Eu tenho que achar depressa um lugar pra esconder as três: se tem coisa que eu não quero mais é ver gente grande rindo de mim."

tab1, tab2, tab3, tab4 = st.tabs(['Summary', 'Sentiment', 'Rewriting', 'Change Style', ])


# show tabs to choose the action
with tab1:
    st.write('Make a short summary of the text')
    botSummary = st.button("Text Summary")
    if botSummary:
        if check_text(text):
            revised_text = revise_text(text, "Faça um resumo rápido deste texto, mantendo a língua do texto: ", max_tokens, temperature)
            st.write(revised_text)

with tab2:    
    st.write('Identify the principal sentiment')
    botSentiment = st.button("Text Sentiment")
    if botSentiment:
        if check_text(text):
            revised_text = revise_text(text, "Qual o sentimento deste texto? Descreva na mesma língua do texto.", max_tokens, temperature)
            st.write(revised_text)    
        
with tab3:        
    st.write('Rewrite and try to improve the text')
    botRewriting = st.button("Text Rewriting")
    if botRewriting:
        if check_text(text):
            revised_text = revise_text(text, "Reescreva e melhore o texto, mantendo a língua do texto: ", max_tokens, temperature)
            st.write(revised_text)   

with tab4:        
    st.write('Change the style to humorous')
    botStyle = st.button("Change Style")
    if botStyle:
        if check_text(text):
            revised_text = revise_text(text, "Reescreva o texto em estilo humorístico, mantendo a língua do texto: ", max_tokens, temperature)
            st.write(revised_text)                  

