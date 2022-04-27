nome = str (input ("Qual éo seu nome ? \n :"))
ano = int (input ("em que ano nasceu ? \n"))
idade =int (2022) - ano
if idade < int (18):
    print("seu nome é " , nome ," e voce tem" ,idade, "Voce não pode entrar")

else:
   print ("seu nome é " , nome ," e voce tem" ,idade, "Voce pode entrar")
