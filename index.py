import streamlit as st
from groq import Groq
import random
from time import sleep

client = Groq(
    api_key="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"
)

frases_spinner = [
    "Você está sendo bem gentil, chutaria que você é a nicolly ou a yasmin...",
    "gostei de você, acho que você é Ani",
    "Você parece ser legal, deve ser a Emanuelly",
    "Gostei do jeito que você pergunta sabia, acho que tu é a Manu, acertei?",
    "Você é pensativo parece ser o Gean namorado do afonso",
    "Falam que você é chata, mas parece ser uma pessoa legal..."
]

st.write("# WannaCryBot")

if "lista_mensagem" not in st.session_state:
    st.session_state["lista_mensagem"] = []

# mostrar histórico
for mensagem in st.session_state["lista_mensagem"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

msg_user = st.chat_input("Digite seus pensamentos...")

if msg_user:

    st.chat_message("user").write(msg_user)

    mensagem = {"role": "user", "content": msg_user}
    st.session_state["lista_mensagem"].append(mensagem)

    with st.spinner(random.choice(frases_spinner)):

        sleep(4)
        resposta_modelo = client.chat.completions.create(
            messages=st.session_state["lista_mensagem"],
            model="llama-3.1-8b-instant"
        )

        resposta_ai = resposta_modelo.choices[0].message.content

    st.chat_message("assistant").write(resposta_ai)

    mensagem_ai = {"role": "assistant", "content": resposta_ai}
    st.session_state["lista_mensagem"].append(mensagem_ai)