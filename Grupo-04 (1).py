import psutil
import time
from datetime import datetime

while True:
  while True:
    number = input(" Digite 1 para CPU; \n Digite 2 para Memória RAM; \n Digite 3 para Memória SWAP; \n Digite 4 para Disco; \n")
    try:
      num = int(number)
      mensagem = "\nPara escolher outro pressione Ctrl + C"
      conversao_memoria = 1000000000
      conversao_ghz = pow(10,-18)
      i = 1
      while True:
        if num == 1 :
          while True:
            a = psutil.cpu_times()
            b = psutil.cpu_percent(interval=1, percpu=True)
            c = psutil.cpu_percent(interval=1)
            d = psutil.cpu_count(logical=True)
            print("Informações da CPU:")
            print(" Execução no modo usuário:",datetime.fromtimestamp(a.user), "GHz")
            print(" Em execução do sistema:",round((a.system/conversao_ghz),34), "GHz")
            print(" Sem fazer nada:",round((a.idle/conversao_ghz), 34), "GHz")
            print(" Manutenção de interrupções de hardware:",round((a.interrupt/conversao_ghz),34), "GHz")
            print(" Atendendo chamadas de procedimento adiado:",round((a.dpc/conversao_ghz), 34), "GHz")
            print(" Porcentagem de uso dos Threads:",b)
            print(" Porcentagem de uso da CPU:",c)
            print(" Número de processadores lógicos:",d)
            print(mensagem)
            print("\n" * 20)
            time.sleep(2)
            i += 1

        elif num == 2 :
          while True:
            a = psutil.virtual_memory()
            print("Informações da Memória RAM:")
            print(" Total: ",round((a.total / conversao_memoria),2),"GB")
            print(" Disponível:",round((a.available / conversao_memoria),2),"GB")
            print(" Usada:",round((a.used / conversao_memoria),2),"GB")
            print(mensagem)
            print("\n" * 20)
            time.sleep(2)
            i += 1

        elif num == 3 :
          while True:
            a = psutil.swap_memory()
            print("Informações da memória swap:")
            print(" Total:",round((a.total / conversao_memoria),2),"GB")
            print(" Usada:",round((a.used / conversao_memoria),2),"GB")
            print(" Livre:",round((a.free / conversao_memoria),2),"GB")
            print(mensagem)
            print("\n" * 20)
            time.sleep(2)
            i += 1

        elif num == 4 :
          while True:
            a = psutil.disk_partitions(all=True)
            count = 0
            for x in a:
                x = str(x.device)
                print(count,"-", x)
                count +=1
                
            part = int(input('Escolha a partição (digite o número da partição):'))
            print("Informações do Disco", a[part].device)
            a = psutil.disk_usage(a[part].device)
            print(" Total:",round((a.total / conversao_memoria),2),"GB")
            print(" Usada:",round((a.used / conversao_memoria),2),"GB")
            print(" Livre:",round((a.free / conversao_memoria),2),"GB")
            print(" Porcentagem:",a.percent,"%")
            print(mensagem)
            print("\n" * 20)
            time.sleep(2)
            i += 1
            
    except:
      print("Digite somente números")


