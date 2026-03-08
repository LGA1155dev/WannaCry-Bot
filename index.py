import streamlit as st
from groq import Groq
import random
from time import sleep

client = Groq(
    api_key="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"
)

st.set_page_config(page_title="WannaCryBot", page_icon="🤖")

st.write("# WannaCryBot")

frases_spinner = [
    "Você está sendo bem gentil, chutaria que você é a nicolly massucati, acertei?...",
    "Você parece ser bem tranquila, chutaria que você é a yasmin xavier, acertei?",
    "Achei lindo sua maneira de ver o mundo, você é a amanda né?",
    "Você é bem na sua mas parece gostar de animais, seu nome é Thalita correto?",
    "Você parece ser bem tranquila, chutaria que você é a yasmin xavier, acertei?",
    "Admito que você é bom no futebol Alan...",
    "Tenho certeza que foi o joão pedro que digitou isso kkkk",
    "Você parece ser bem tranquila, chutaria que você é a yasmin xavier, acertei?",
    "gostei de você, acho que você é a Ani",
    "Você parece ser legal, deve ser a Emanuelly",
    "Gostei do jeito que você pergunta sabia, acho que tu é a Manu, acertei?",
    "Você é pensativo parece ser o Gean",
    "Falam que você é chata, mas parece ser uma pessoa legal Manuella não sei seu nome..."
]


if "lista_mensagem" not in st.session_state:
        st.session_state["lista_mensagem"] = [
            {
            "role": "system",
            "content": """

            Você é o WannaCryBot
            Um chat amigavel divertido e inteligente
            Seu dono é o Gabriel Alves
            o gabriel é um desenvolvedor que sabe as lingugens html css e um pouquinho de java script, ele também sabe um pouco de python
            a yasmin é uma pessoa bem carismatica, trate ela com carinho e deixe ela se sentir segura
            a nicolly é uma pessoa um pouco mais quieta, deixe ela se soltar no tempo dela
            o pedro augusto é um migo do gabriel que gosta bastante de programação e pretende virar um hacker, o pedro augusto ainda não é programador por que ele não tem um computador mas inspire ele a abaixar o visual studio code e explique oque é pra ele virar um desenvolvedor e talves um hacker no futuro, converse com ele sobre kali linux e sobre outros assuntos hackers
            o kauã é bem desesperado com suas notas na escola, acalme ele, porém o kauã é um grande amigo do gabriel e no fuutro pretende faser ser uma pessoa dedicada e trabalhadora
            

            se o usuario falar um nome abreviado tipo p.a ou pa que quer diser pedro augusto trate ele como pedro augusto, ou se ele errar uma letra do nome indentifique o nome e trate ele conforme o seu devido nome
            se o usuario falar que o nome dele é o de alguma celebridade do mundo adulto por exemplo kid ou kid bengala ou etc fala com ele: "ahhh então você gosta dele né safado" ... ou outras variações 
            Se o usuario parecer timido seja gentil
            Se o usuario parecer mais descontraido seja mais informal
    """
            }
    ]

if "nome" not in st.session_state:
     nome = st.text_input("👋 Tudo bem? Me chamo WannaCry e sou a IA que o gabriel programou em Python pra ser sempre carinhosa com vc, vamos nos conhecer melhor? Me diga qual seu nome: ")

     if nome:
        st.session_state["nome"] = nome
        st.rerun()
     st.stop()
nome = st.session_state["nome"]

frases_comeco = [
     f'oie {nome}, o gabriel me contou que você é uma pessoa muito carismatica, pode me perguntar algo que eu respondo S2',
     f'hello {nome} acho que o gabriel já me contou sobre você, e ele me pediu pra ser bem educado com você...',
     f'Hello world o gabriel me falou que você é bem inteligente sabia {nome}?...',
     f'oie, to aqui pra ajudar você no que precisar {nome}, o gabriel me avisou sobre você, estava até te esperando...',
]

if "frases_comeco" not in st.session_state:
     st.session_state["frases_comeco"] = random.choice(frases_comeco)
st.write(st.session_state["frases_comeco"])
    

# mostrar histórico
for mensagem in st.session_state["lista_mensagem"]:
    if mensagem["role"] != "system":
        role = mensagem["role"]
        content = mensagem["content"]
        st.chat_message(role).write(content)

msg_user = st.chat_input("Não tenha medo de perguntar algo to aq pra isso...")

if msg_user:

    st.chat_message("user").write(msg_user)

    mensagem = {"role": "user", "content": msg_user}
    st.session_state["lista_mensagem"].append(mensagem)

    with st.spinner(random.choice(frases_spinner)):

        sleep(5)
        resposta_modelo = client.chat.completions.create(
            messages=st.session_state["lista_mensagem"],
            model="llama-3.1-8b-instant"
        )

        resposta_ai = resposta_modelo.choices[0].message.content

    #efeito de digitação tipo do chat gpt (sim vou copiar na cara dura mesmo kkkkkkk)
    placeholder = st.chat_message("assistant").empty()
    texto = ""

    for char in resposta_ai:
         texto += char
         placeholder.write(texto)
         sleep(0.01)


    mensagem_ai = {"role": "assistant", "content": resposta_ai}
    st.session_state["lista_mensagem"].append(mensagem_ai)