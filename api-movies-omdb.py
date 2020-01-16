import requests
import json


def requisicao(titulo):
    try:
        req = requests.get('http://www.omdbapi.com/?t=' + titulo + '&apikey=fdf2fd5c')
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro de requisição.')
        return None


def printar_detalhes(filme):
    print('Título:', filme['Title'])
    print('Gênero:', filme['Genre'])
    print('Ano:', filme['Year'])
    print('Diretor:', filme['Director'])
    print('Atores:', filme['Actors'])
    print('Nota:', filme['imdbRating'])
    print(40*'#')


sair = False
while not sair:
    opcao = input('Escreva um nome de um filme ou SAIR para fechar: ')

    if opcao == 'SAIR':
        sair = True
        print('Saindo...')

    else:
        filme = requisicao(opcao)
        if filme['Response'] == 'False':
            print('Filme não encontrado :(')
            print(40*'#')
        else:
            printar_detalhes(filme)