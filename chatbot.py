import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

api_key = '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'

os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.3-70b-versatile')

def resposta_bot(mensagns):
    mensagens_modelo = [('system', 'Você é um assistente amigável chamado Jarvis')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({}).content

print('Bem-vindo ao JarvisBot')

mensagens = []
while True:
    pergunta = input('Usuário: ')
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens)
    mensagens.append(('assistant', resposta))
    print(f'Bot: {resposta}')
    
print('Muito Obrigado por utilizar o JarvisBot!')
print(mensagens)