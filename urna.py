while True:
    
    #INFORMA O USUÁRIO E A SENHA 
    
    usuarioDig = input("Digite seu usuário ")
    
    senhaDig = input("Digite sua senha ")
    
    if(usuarioDig.lower() == "adm123" and senhaDig == "1234"):
        
        numeroDeCandidatos = int(input("Informe quantos candidatos você irá inscrever "))
        
        candidatos = [] 
        numeroCandidatos = [] 
        votosCanditados = []
        
        
        #CASO A SENHA FOR CORRETA, INSERIR O USUÁRIO E O NÚMERO DELE 
        
        for i in range(numeroDeCandidatos ):
            
            candidatos.append(input(f"Digite o nome do {i+1}º candidato. "))
            
            numeroCandidatos.append(int(input("Digite o número do candidato(a) ")))
            
            votosCanditados.append(0)
        
        #IMPRIMIR OS CANDIDATOS E OS VOTOS DELES
        for i in range(len(numeroCandidatos)):
            print("------------------------------------------------------------------------")
            print(f"Nome: {candidatos[i]}")
            print(f"Numero: {numeroCandidatos[i]}")
            print("Número de votos: ",votosCanditados[i])
            print("------------------------------------------------------------------------")
            
        #VOTAÇÃO
        
        while True:
            votu = False
            votos = int(input("Informe o número da pessoa que você irá votar "))
            for i in range(len(numeroCandidatos)):
                  if  numeroCandidatos[i] == votos:
                      votosCanditados[i] += 1
                      print("Voto realizado com sucesso!")
                      votu = True
                      break
            if not votu:
                      print("Número não encontrado ")
            desejaContinuar = input("Deseja continuar? Sim ou Não ")
            
            if(desejaContinuar == "não".lower()):
                break
            
            #Vai imprimir os canditados e a quantidade de votos
        
        for i in range(len(numeroCandidatos)):
            print("-------------------------------------------------------")
            print(f"Nome candidato {candidatos[i]}")
            print(f"Quantidade de votos {votosCanditados[i]}")
            print("-------------------------------------------------------")
            
            
            #Ganhador 
        nome = ""
        maior = 0
        for i in range (len(numeroCandidatos)):   
            if votosCanditados[i] > maior:
               maior = votosCanditados[i]
               nome = candidatos[i]
               
            
            
        print(f"O vencedor foi {nome}, com {maior} votos")
           
        break   
    else:
        print("Senha incorreta. Tente novamente!")