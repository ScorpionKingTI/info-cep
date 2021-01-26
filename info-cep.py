import requests, os, time
v='\033[32;1m' 
a='\033[34;1m' 
m='\033[33;1m'
def gt():
 print('\n\033[34;1mDeseja uma nova consulta?\n\n1. sim\n2. não')
 fr=input('')
 if fr == '1':
  dk()
 if fr == '2':
  print('\n\033[32;1mObrigado por ultilizar os serviços do scorpion king\n')
  exit()
 if fr != '1' and '2':
  print('\33[33;1mSeleção invalida,escolha 1 ou 2')
def dk():
 os.system('clear')
 x='''
 ██╗███╗  ██╗███████╗ █████╗        █████╗ ███████╗██████╗
 ██║████╗ ██║██╔════╝██╔══██╗      ██╔══██╗██╔════╝██╔══██╗
 ██║██╔██╗██║█████╗  ██║  ██║█████╗██║  ╚═╝█████╗  ██████╔╝
 ██║██║╚████║██╔══╝  ██║  ██║╚════╝██║  ██╗██╔══╝  ██╔═══╝
 ██║██║ ╚███║██║     ╚█████╔╝      ╚█████╔╝███████╗██║
 ╚═╝╚═╝  ╚══╝╚═╝      ╚════╝        ╚════╝ ╚══════╝╚═╝
 '''
 print(v,x)
 print(m,'        createde by scorpion king\n')
 d='''
 ____________________________________________
 |
 |---------- 1. consultar um cep
 |---------- 2. ajuda
 |---------- 3. sair 
 |___________________________________________
 
  escolha o numero da opção que deseja
 '''
 print(a,d)
 dc=input('             >\033[0;0m')
 if dc == '1':
  print(v, 'Digite o cep a ser consultado')
  cp=input('\n             >')
  if len(cp) != 8:
   print('\n\033[01;33m  o formato tem que ter 8 digitos\033[0;0m\n')
   gt()
  dadoss = requests.get('https://viacep.com.br/ws/{}/json/'.format(cp))
  dad = dadoss.json()
  zx = "\033[34;1mCep: \033[0;0m\033[32;1m{}\033[0;0m\n\033[34;1mRua: \033[0;0m\033[32;1m{}\033[0;0m\n\033[34;1mBairro: \033[0;0m\033[32;1m{}\033\n\033[34;1mCidade: \033[0;0m\033[32;1m{}\033[0;0m\n\033[34;1mEstado: \033[0;0m\033[32;1m{}\033[0;0m\n\033[34;1mDDD: \033[0;0m\033[32;1m{}\033[0;0m\n\033[34;1mSiafi: \033[0;0m\033[32;1m{}\033[0;0m\n\033[34;1mComplemento: \033[0;0m\033[32;1m{}\033[0;0m\n".format(dad['cep'],dad['logradouro'],dad['bairro'],dad['localidade'],dad['uf'],dad['ddd'],dad['siafi'],dad['complemento'])
  if 'erro' not in dad:
   print('\n\033[32;1m==>CEP ENCONTRADO<==\033[0;0m\n')
   print(zx)
   gt()
 if dc == '2':
  print(v, 'O info cep é uma ferramenta n qual foi criada para consultas de cep,basicamente na opção "1" você receberá uma frase e em seguida poderá digitar o cep que deseja consultar,na opção "2" você vem na ajuda que está lendo agora,na terceira opção "3" você sai da ferramenta,um ponto interessante é de que se caso você digitar um cep inválido ele vai mostrar uma mensagem e em seguida sair da ferramenta')
  gt()
 if dc == '3':
  print('\n\033[32;1mObrigado por ultilizar os serviços do scorpion king\n')
  exit()
 if dc != '1' and '2' and '3':
  print('\033[33;1mSeleção invalida\033[0;0m')
  time.sleep(3)
  dk()
dk()
