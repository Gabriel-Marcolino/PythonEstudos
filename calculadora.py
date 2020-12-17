def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def subtracao(numero1, numero2):
    resultado = numero1 - numero2
    return resultado

def multiplicacao(multiplicador, numero):
    resultado = multiplicador * numero
    return resultado

def divisao(divisor, numero):
    resultado = numero / divisor
    return resultado

def menu():
    escolha = ''
    while(escolha != '0'):
        print ('[1] para soma')
        print ('[2] para subtração')
        print ('[3] para multiplicação')
        print ('[4] para divisão')
        print ('[0] FINALIZAR PROGRAMA')

        escolha = raw_input()
        if(escolha == '1'):
            print ('Digite o primeiro número para soma')
            
            numero1 = float(numero1)
            print ('Digite o segundo número para soma')
           
            numero2 = float(numero2)            
            resultado = soma(numero1, numero2)
            print ('O resultado da soma é %s ' % (resultado))

        if(escolha == '2'):
            print ('Digite o primeiro número para substração')
            
            numero1 = float(numero1)
            print ('Digite o segundo número para substração')
          
            numero2 = float(numero2)            
            resultado = subtracao(numero1, numero2)
            print ('O resultado da subtração é %s ' % (resultado))

        if(escolha == '3'):
            print ('Digite o multiplicador')
         
            multiplicador = float(multiplicador)
            print ('Digite o número que será multiplicado')
         
            numero = float(numero)            
            resultado = multiplicacao(multiplicador, numero)
            print ('O resultado da multiplicação é %s ' % (resultado))

        if(escolha == '4'):
            print ('Digite o divisor')
          
            divisor = float(divisor)
            print ('Digite o número que será dividido')
            
            numero = float(numero)            
            resultado = divisao(divisor, numero)
            print ('O resultado da divisão é %s ' % (resultado))

menu()
