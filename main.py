import requests

resposta = requests.get('https://viacep.com.br/ws/01001000/json/')

if resposta.status_code == 200:

    dados = resposta.json()

    #print('Endereço completo em JSON : ', dados)

    print('Logradouro : ', dados['logradouro'])

    print('Bairro : ', dados['bairro'])

else:
    print('Nao localizado!')
