import streamlit as st
import ollama



st.write('# WannaCryBot') #markdown


if not "lista_mensagem" in st.session_state:
    st.session_state["lista_mensagem"] = []


for mensagem in st.session_state["lista_mensagem"]:
        role = mensagem["role"]
        content = mensagem["content"]
        st.chat_message(role).write(content)

msg_user = st.chat_input('Digite seus pensamentos... ')

if msg_user:
      #user -> humano
      #assistent -> AI
      st.chat_message("user").write(msg_user)
      mensagem = {"role": "user", "content": msg_user}
      st.session_state["lista_mensagem"].append(mensagem)

      #resposta do modelo
      resposta_modelo = ollama.chat(
            messages = st.session_state["lista_mensagem"],
            model="llama3"
      )

      resposta_ai = resposta_modelo["message"]["content"]

      #exibir a resposta da ia na tela

      st.chat_message("assistant").write(resposta_ai)
      mensagem_ai = {"role": "assistant", "content": resposta_ai}
      st.session_state["lista_mensagem"].append(mensagem_ai)






    #para cada mensagem que estiver dentro do st.session_state (no caaso na sessão do cockie) exiba a mesagem:





    #Criar listas para o historico...

    #dicionario com .py
    


    # Mesagens...





