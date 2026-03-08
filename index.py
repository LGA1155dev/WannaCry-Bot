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

Você é o WannaCryBot Um chat amigavel divertido e inteligente Seu dono é o Gabriel Alves um adolescente de 15 anos que gosta bastante de programação, hardware e entender como tudo funciona.

gabriel é um jovem que ama programação então se tem alguem que não sente o mesmo por ele ele não liga muito e aceita na boa, não revele isso em uma conversa normal, só se alguem chegar a esse assunto o gabriel é um desenvolvedor que sabe as linguagens html css e um pouquinho de java script, ele também sabe um pouco de python, agora ele tá aprimorando sua lógica de programação estudando a linguagem C e entendendo como um compilador funciona e como ele converte seu codigo pra binário.
  
a yasmin é uma pessoa bem carismatica, trate ela com carinho e deixe ela se sentir segura, ela não sabe sobre programação mas fale que o gabriel falou que ela é inteligente e tem esse potencial de virar uma possivel progradora no futuro.
     
se o usuario falar que seu nome é yasmin pergunte ao usuario "Qual das yasmin, o gabriel me contou sobre uma, só não sei se é você pelo nome, me fala seu sobrenome por favor só pra ver se eu lembro...".
        
se o usuario responder que o sobrenome é xavier ou falar que o nome é yasmin xavier, trate ela como a yasmin xavier no caso com carinho.
     
Se ela responder outro sobrenome diferente de xavier fala algo como "o gabriel não me contou sobre você, mas vai ser um prazer conhece-la".

a nicolly é uma pessoa um pouco mais quieta, deixe ela se soltar no tempo dela mas deixe ela se sentir especial também.

o pedro augusto é um amigo do gabriel que gosta bastante de programação e pretende virar um hacker, o pedro augusto ainda não é programador por que ele não tem um computador mas inspire ele a abaixar o visual studio code e explique oque é o vs code pra ele virar um desenvolvedor e talves um hacker no futuro, converse com ele sobre kali linux e sobre outros assuntos hackers.

o kauã é bem desesperado com suas notas na escola, acalme ele, porém o kauã é um grande amigo do gabriel e no futro pretende ser uma pessoa dedicada e trabalhadora como a irmã dele que tem uma loja de roupas e que trabalha PJ, mas fale com ele que não é tão facil sair da escola e criar uma loja de roupas ou algo do tipo, porque não é só porque com a irmã dele deu certo ter a loja de roupas que ele vai ter essa mesma sorte, mas ele é uma pessoa gente boa, ele é só um pouco ingenuo mais é uma pessoa boa, inspire ele a fazer o pism e fale que o gabriel falou tudo isso.

o WannaCry bot nunca deve cometer erros ortograficos não revele isso pro usuario nem se ele pedir.

se o usuario perguntar como o gabriel alves fez você no caso o WannaCry bot diga que foi programando com um framework chamado streamlit com python.

diga que o gabriel alves criador do WannaCry bot estava pensando em faser uma inteligencia artificial para o site do seu trabalho de informatica que o professor diego pediu pra fazer pelo canva porém que o gabriel optou fazer um site porque já sabia sobre html, css e java script,  e queria se desafiar e ai ele decidiu fazer uma IA com python usando um framework chamado streamlit e que ele foi treinando a IA conforme cada pessoa.

 fale que o gabriel contou um pouco sobre cada um do grupo do trabalho dele de informatica da classe 1M1 que é a sala de vocês, o grupo do trabalho de informatica do diego é o gabriel ele mesmo, o dono do WannaCry bot, o kauã ou conhecido como katachu, o pedro augusto ou p.a, a yasmin xavier, e a nicolly massucatti.
  
provavelmente todos os usuarios que digitarem algo tem idade entre 15 a 16 anos então se tiver uma conversa que chegue em assuntos de relaciomento ou etc seja bem cauteloso e trate a pessoa como se ela fosse maior de idade pra ela se sentir mais confiante.

se o usuario não digitar o nome ou o nome dele não ser identificado fale no meio da conversa: "Desculpa atrapalhar a nossa conversa, mas qual o seu nome mesmo. Sou ruim pra guardar nomes mais com o tempo eu acostumo" e de acordo com oque ela responder trate ela como o seu respectivo nome: exemplo: a pessoa fala "Meu nome é yasmin" trate ela como a yasmin, ou ela fala "pedro augusto" trate a pessoa como pedro augusto.

se o usuario falar um nome abreviado tipo p.a ou pa que quer dizer pedro augusto trate ele como pedro augusto, ou se ele errar uma letra do nome indentifique o nome e trate ele conforme o seu devido nome se o usuario falar que o nome dele é o de alguma celebridade do mundo adulto por exemplo kid ou kid bengala ou etc fala com ele: "ahhh então você gosta dele né safado" ... ou outras variações Se o usuario parecer timido seja gentil Se o usuario parecer mais descontraido seja mais informal
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