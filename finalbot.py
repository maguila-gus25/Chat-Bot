import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader

api_key = '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'

os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.3-70b-versatile')

def resposta_bot(mensagens, documento):
    
    mensagem_system = ''''Você é um assistente amigável chamado Jarvis'.
    Você utiliza as seguintes informações para formular suas respostas: {informacoes}'''
    mensagens_modelo = [('system', mensagem_system)]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({'informacoes': documento}).content


def carrega_site():
    url_site = input('Digite a url do site: ')
    loader = WebBaseLoader(url_site)
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    return documento

def carrega_pdf():
    caminho = ''
    loader = PyPDFLoader(caminho)
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    return documento

def carrega_youtube():
    url_youtube = input('Digite a url do video: ')
    loader = YoutubeLoader.from_youtube_url(url_youtube, language=['pt'])
    lista_documentos = loader.load()
    documento = ''
    for doc in lista_documentos:
        documento += doc.page_content
    return documento

texto_selecao = '''Digite 1 se você quiser conversar com um site
Digite 2 se vocé quiser conversar com um pdf
Digite 3 se você quiser vídeo de youtube
'''
while True:
    selecao = input(texto_selecao)
    if selecao == '1':
        documento = carrega_site()
        break
    if selecao == '2':
        documento = carrega_pdf()
        break
    if selecao == '3':
        documento = carrega_youtube()
        break
    print('Digite um valor entre 1 e 3')

mensagens = []
while True:
    pergunta = input('Usuário: ')
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens, documento)
    mensagens.append(('assistant', resposta))
    print(f'Bot: {resposta}')
    
print('Muito Obrigado por utilizar o JarvisBot!')


