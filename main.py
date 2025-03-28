import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

api_key = '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'

os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.3-70b-versatile')


def resposta_do_bot(lista_mensagens):
    template = ChatPromptTemplate.from_messages(
        [('system', 'Você é um assitente amigável chamado Jarvis')],
        lista_mensagens
    )
    
    chain = template | chat
    
    return chain.invoke({}).content

print('Bem-vindo ao ChatBot Jarvis! (Digite x se você quiser sair!)\n')
mensagens = []
while True:
    pergunta = input('Usuário: ')
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_do_bot(mensagens)
    mensagens.append(('assistant', resposta))
    print(f'Bot: {resposta}')
    
print('\nMuito Obrigado por utilizar o JarvisBot!')
