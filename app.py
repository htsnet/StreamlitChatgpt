import streamlit as st
import openai

# Insira sua chave de API aqui
openai.api_key = st.secrets['api_key_openai']

def revise_text(text, acao):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=acao + '"' + text + ' "',
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

#colunas
col1, col2 = st.columns([0.9, 0.1])

# título
Titulo = f'Análise e melhoria de Textos com IA (ChatGPT)'
col1.title(Titulo)

text = st.text_area("Cole o seu texto na caixa abaixo. Depois, clique no botão desejado.")
# textxsss = "Se o pessoal vê as minhas três vontades engordando desse jeito e crescendo que nem balão, eles vão rir, aposto. Eles não entendem essas coisas, acham que é infantil, não levam a sério. Eu tenho que achar depressa um lugar pra esconder as três: se tem coisa que eu não quero mais é ver gente grande rindo de mim."

# escolha de ação a executar
botResumo = st.button("Resumo do Texto")
if botResumo:
    revised_text = revise_text(text, "Faça um resumo rápido deste texto.")
    # print(revised_text)
    st.experimental_show(revised_text)
    
botSentimento = st.button("Sentimento do Texto")
if botSentimento:
    revised_text = revise_text(text, "Qual o sentimento deste texto?")
    # print(revised_text)
    st.experimental_show(revised_text)    
