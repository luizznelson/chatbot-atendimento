from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import streamlit as st

# Instancia o chatbot
bot = ChatBot('AtendimentoBot')

# Treinamento (perguntas e respostas frequentes)
faq = [
    "Quais planos vocês oferecem?",
    "Oferecemos planos residencial, empresarial e gamer, com velocidades de 100 a 1000 Mbps.",
    "Como faço para pagar minha fatura?",
    "Você pode pagar sua fatura pelo nosso site, pelo app ou presencialmente em nossos pontos de atendimento.",
    "Como falar com o suporte?",
    "O suporte está disponível pelo telefone, WhatsApp ou chat em nosso site 24h por dia.",
    "Preciso de segunda via da fatura.",
    "A segunda via pode ser emitida no site ou app, na área do cliente.",
    "Qual o horário de atendimento presencial?",
    "O atendimento presencial funciona das 8h às 18h, de segunda a sexta.",
]

trainer = ListTrainer(bot)
trainer.train(faq)

# Interface Streamlit
st.set_page_config(page_title="Chatbot de Atendimento", layout="centered")
st.title("🤖 Chatbot de Atendimento - Prova de Conceito")

st.write("""
Este chatbot responde às perguntas mais frequentes dos clientes de um provedor de internet.
Experimente perguntar sobre planos, pagamento, suporte e horários!
""")

user_input = st.text_input("Digite sua pergunta:")

if user_input:
    response = bot.get_response(user_input)
    st.markdown(f"**Bot:** {response}")

st.write("""
---
> _Obs.: Este é um protótipo inicial de chatbot, ideal para ser expandido com mais perguntas e integração com canais de atendimento reais._
""")
