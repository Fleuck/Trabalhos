#               0,25)0,5)1,0)2,0)5,0)10)
estoque_notas = [10, 20, 30, 40, 50, 30]
valor_notas = [0.25, 0.5, 1, 2, 5, 10]
numeros_celular_historico = []
historico_valor_pix = []

#              agua)guar)coca)coca_zero
estoque_latas = [20, 15, 10, 10]
preco_produto = [2.50, 5.25, 6.50, 7.75]

comando_maquina = int() #contador

while comando_maquina != 72777231: #72777231 para acabar com o loop
    
    print('=======================================================')
    print('Olá, seja bem-vindo! Escolha o numero de sua bebida:   ')
    print('                  1 - aguinha                          ')
    print('                  2 - guarana geladinho                ')
    print('                  3 - Coca-cola normal                 ')
    print('                  4 - Coca-Cola Zero                   ')
    print('=======================================================')
        

    comando_maquina = int(input())

    if comando_maquina == 23646:
            comando_administrador = 0 #Contador do while ADM
        
            while comando_administrador >= 0 and comando_administrador < 8: 
                print("===MODO ADMINISTRADOR===")
                print("Selecione uma opção:")
                print("1 - Saldo máquina")
                print("2 - Estoque de cédulas e moedas")
                print("3 - Adicionar estoque de cédulas e moedas")
                print("4 - Remover estoque de cédulas e moedas")
                print("5 - estoque de latas")
                print("6 - Adicionar estoque de latas e garrafas")
                print("7 - historico de compras por pix")
                print("")
                print("Digite qualquer outro número para voltar ao modo de usuário")
                comando_administrador = int(input())

#calculo do saldo 
                if comando_administrador == int(1):
                    saldo_maquina = estoque_notas[0] * 0.25 + estoque_notas[1] * 0.5 + estoque_notas[2] + estoque_notas[3] * 2 + estoque_notas[4] * 5 + estoque_notas[5] * 10
                    print("O saldo da maquina é: R$", saldo_maquina)
                
#quantidade de cedulas e moedas   
                elif comando_administrador == int(2):
                    print(estoque_notas[0], "moeda(s) de 25 centavos")
                    print(estoque_notas[1], "moeda(s) de 50 centavos")
                    print(estoque_notas[2], "moeda(s) de 1 real")
                    print(estoque_notas[3], "cedula(s) de 2 reais")
                    print(estoque_notas[4], "cedula(s) de 5 reais")
                    print(estoque_notas[5], "cedula(s) de 10 reais")

#Insere cedula/moeda no estoque da maquina      
                elif comando_administrador == int(3):
                    print("Insira qual a nota ou moeda que sera inserida:")
                    valor_inserido = float(input()) 

                    if valor_inserido > 1:
                
                        print("Quantas cédulas de", valor_inserido, "$$ serão inseridas?")
                        quantidade_inseridas = int(input())
                        fator = valor_notas.index(valor_inserido)
                        estoque_notas[fator] = estoque_notas[fator] + quantidade_inseridas
                        print("Inserido", quantidade_inseridas ,"cedula(s) de", valor_inserido, "$$")

                    else:
                        print("Quantas moedas de", valor_inserido, "$$ serão inseridas?")
                        quantidade_inseridas = int(input())
                        fator = valor_notas.index(valor_inserido)
                        estoque_notas[fator] = estoque_notas[fator] + quantidade_inseridas
                        print("Inserido", quantidade_inseridas ,"moeda(s) de", valor_inserido, "$$")

                    
#Remove cedula/moeda no estoque da maquina 
                elif comando_administrador == int(4):
                    print("Insira qual a nota ou moeda que sera removida:")
                    valor_remover = float(input())
                    fator = valor_notas.index(valor_remover)

                    if valor_remover > 1:    
                        print("Na máquina existem", estoque_notas[fator], "cédula(s) de", valor_remover,"$$""]. Quantas serão removidas?")
                        quantidade_removidas = int()
                        subtracao_cedula = int(-1)
                        while subtracao_cedula < 0:
                            quantidade_removidas = int(input())
                            subtracao_cedula = estoque_notas[fator] - quantidade_removidas
                            if subtracao_cedula >= 0:
                                estoque_notas[fator] = estoque_notas[fator]  - quantidade_removidas
                                print("Removido", quantidade_removidas ,"cedula(s) de", valor_remover, "$$")
                            else:
                                print('Valor inválido. Quantas cédulas deseja remover?')
                    else:
                        print("Na máquina existem", estoque_notas[fator], "moeda(s) de", valor_remover,"$$""]. Quantas serão removidas?")
                        quantidade_removidas = int()
                        subtracao_cedula = int(-1)
                        while subtracao_cedula < 0:
                            quantidade_removidas = int(input())
                            subtracao_cedula = estoque_notas[fator] - quantidade_removidas
                            if subtracao_cedula >= 0:
                                estoque_notas[fator] = estoque_notas[fator]  - quantidade_removidas
                                print("Removido", quantidade_removidas ,"moeda(s) de", valor_remover, "$$")
                            else:
                                print('Valor inválido. Quantas moedas deseja remover?')
                    

                elif comando_administrador == int(5):
                    print(estoque_latas[0],"garrafas de agua")
                    print(estoque_latas[1],"latas de guarana")
                    print(estoque_latas[2],"latas de coca-cola normal")
                    print(estoque_latas[3],"latas de coca-cola zero")

                elif comando_administrador == int(6):

                    print("1- adicionar garrafas de agua ")
                    print("2- adicionar latas de guarana ")
                    print("3- adicionar latas de coca cola normal ")
                    print("4- adicionar latas de coca cola zero ")
                   
                    escolhe_lata = float(input()) 

                    if escolhe_lata == 1:
                
                        print("Quantas garrafas de agua serão inseridas?")
                        quantidade_latas = int(input())
                        estoque_latas[0] = estoque_latas[0] + quantidade_latas
                        print("Inserido", quantidade_latas ,"garrafas de agua") 

                    elif escolhe_lata == 2:
                
                        print("Quantas latas de guarana serão inseridas?")
                        quantidade_latas = int(input())
                        estoque_latas[1] = estoque_latas[1] + quantidade_latas
                        print("Inserido", quantidade_latas ,"latas de guarana") 

                    elif escolhe_lata == 3:
                
                        print("Quantas latas de coca normal serão inseridas?")
                        quantidade_latas = int(input())
                        estoque_latas[2] = estoque_latas[2] + quantidade_latas
                        print("Inserido", quantidade_latas ,"latas de coca normal") 

                    elif escolhe_lata == 4:
                
                        print("Quantas latas de coca zero serão inseridas?")
                        quantidade_latas = int(input())
                        estoque_latas[3] = estoque_latas[3] + quantidade_latas
                        print("Inserido", quantidade_latas ,"latas de coca zero")
                
                elif comando_administrador == int(7):
                    fator = 0
                    if len(numeros_celular_historico) > 0:
                        for contador in range(len(numeros_celular_historico)):
                            print("numero:", numeros_celular_historico[fator], "no valor de", historico_valor_pix[fator], ("$$"))
                            fator = fator + 1 
                    else:
                        print("sem pagamentos por pix ate o momento")
    #Modo do comprador
    elif comando_maquina > 0 and comando_maquina < 5:
            valor_produto = int() 
            confirmacao = int()
            if comando_maquina == int(1):
                valor_produto = preco_produto[0]
                if estoque_latas[0] > 0:
                    confirmacao = 1
                else:
                    print("o produto esta em falta")
            elif comando_maquina == int(2):
                valor_produto = preco_produto[1]
                if estoque_latas[1] > 0:
                    confirmacao = 1
                else:
                    print("o produto esta em falta")
            elif comando_maquina == int(3):
                valor_produto = preco_produto[2]
                if estoque_latas[2] > 0:
                    confirmacao = 1
                else:
                    print("o produto esta em falta")
            elif comando_maquina == int(4):
                valor_produto = preco_produto[3]
                if estoque_latas[3] > 0:
                    confirmacao = 1
                else:
                    print("o produto esta em falta")

            if confirmacao == 1: 
                print("1- pagar com dinheiro" )
                print("2- pagar com pix" )
                pix_ou_dinheiro = int(input())

                if pix_ou_dinheiro == 1:

                    print('Ótimo! O custo é de R$', valor_produto ,'. Insira o dinheiro em cédulas e/ou moedas na máquina.')
                    troco = float() 
                    total_pago = float() 
                    dinheiro_depositado = float() 

                    quantidade_moeda_vinte_e_cinco_centavos_inserida = int()
                    quantidade_moeda_cinquenta_centavos_inserida = int()
                    quantidade_moeda_um_real_inserida = int()
                    quantidade_cedula_dois_reais_inserida = int()
                    quantidade_cedula_cinco_reais_inserida = int()
                    quantidade_cedula_dez_reais_inserida = int()

                    while total_pago < valor_produto: 
                        dinheiro_depositado = float(input()) 
                        if dinheiro_depositado == 0: #'Comando' para cancelar a operação!!
                                troco = total_pago 
                                break

                        elif dinheiro_depositado == 10:
                            estoque_notas[5] = estoque_notas[5] + 1
                            quantidade_cedula_dez_reais_inserida = quantidade_cedula_dez_reais_inserida + 1
                            
                        elif dinheiro_depositado == 5:
                            estoque_notas[4] = estoque_notas[4] + 1
                            quantidade_cedula_cinco_reais_inserida = quantidade_cedula_cinco_reais_inserida + 1
                            
                        elif dinheiro_depositado == 2:
                            estoque_notas[3] = estoque_notas[3] + 1
                            quantidade_cedula_dois_reais_inserida = quantidade_cedula_dois_reais_inserida + 1
                            
                        elif dinheiro_depositado == 1:
                            estoque_notas[2] = estoque_notas[2] + 1
                            quantidade_moeda_um_real_inserida = quantidade_moeda_um_real_inserida + 1
                            
                        elif dinheiro_depositado == 0.5:
                            estoque_notas[1] = estoque_notas[1] + 1
                            quantidade_moeda_cinquenta_centavos_inserida = quantidade_moeda_cinquenta_centavos_inserida + 1

                        elif dinheiro_depositado == 0.25:
                            estoque_notas[0] = estoque_notas[0] + 1
                            quantidade_moeda_vinte_e_cinco_centavos_inserida = quantidade_moeda_vinte_e_cinco_centavos_inserida + 1

                        total_pago = total_pago + dinheiro_depositado 
                        
                        if total_pago >= valor_produto: 
                            troco = total_pago - valor_produto
                        else:
                            print('Você pagou um total de R$', total_pago, '. Faltam R$:', (valor_produto - total_pago) ,' para finalizar a compra.')
                            print('                 Ou cancele a operação clicando no botão - 0 -')

                    quantidade_moeda_vinte_e_cinco_centavos_removida = int()
                    quantidade_moeda_cinquenta_centavos_removida = int()
                    quantidade_moeda_um_real_removida = int()
                    quantidade_cedula_dois_reais_removida = int()
                    quantidade_cedula_cinco_reais_removida = int()
                    quantidade_cedula_dez_reais_removida = int()

                    calculo_de_cedulas_e_moedas_do_troco = troco  #Calcula quantidade de cédulas e moedas necessárias para o troco. "Contador".

                    while calculo_de_cedulas_e_moedas_do_troco >= 10:
                        if estoque_notas[5] - quantidade_cedula_dez_reais_removida >= 1:        
                            calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - 10
                            quantidade_cedula_dez_reais_removida = quantidade_cedula_dez_reais_removida + 1
                        else:
                            break

                    while calculo_de_cedulas_e_moedas_do_troco >= 5:
                        if estoque_notas[4] - quantidade_cedula_cinco_reais_removida >= 1:         
                            calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - 5
                            quantidade_cedula_cinco_reais_removida = quantidade_cedula_cinco_reais_removida + 1
                        else:
                            break

                    while calculo_de_cedulas_e_moedas_do_troco >= 2:
                        if estoque_notas[3] - quantidade_cedula_dois_reais_removida >= 1:        
                            calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - 2
                            quantidade_cedula_dois_reais_removida = quantidade_cedula_dois_reais_removida + 1
                        else:
                            break
                            
                    while calculo_de_cedulas_e_moedas_do_troco >= 1:
                        if estoque_notas[2] - quantidade_moeda_um_real_removida >= 1:        
                            calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - 1
                            quantidade_moeda_um_real_removida = quantidade_moeda_um_real_removida + 1
                        else:
                            break

                    while calculo_de_cedulas_e_moedas_do_troco >= 0.5:
                        if estoque_notas[1] - quantidade_moeda_cinquenta_centavos_removida >= 1:        
                            calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - 0.5
                            quantidade_moeda_cinquenta_centavos_removida = quantidade_moeda_cinquenta_centavos_removida + 1
                        else:
                            break

                    while calculo_de_cedulas_e_moedas_do_troco >= 0.25:
                        if estoque_notas[0] - quantidade_moeda_vinte_e_cinco_centavos_removida >= 1:        
                            calculo_de_cedulas_e_moedas_do_troco = calculo_de_cedulas_e_moedas_do_troco - 0.25
                            quantidade_moeda_vinte_e_cinco_centavos_removida = quantidade_moeda_vinte_e_cinco_centavos_removida + 1
                        else:
                            break
                    if calculo_de_cedulas_e_moedas_do_troco > 0:
                        print('Compra cancelada. Troco insuficiente. Retornando R$' , total_pago , 'depositado')

                        #devolve exatamente o que o usuário inseriu na máquina
                        if quantidade_moeda_vinte_e_cinco_centavos_inserida  > 0:
                            estoque_notas[0] = estoque_notas[0] - quantidade_moeda_vinte_e_cinco_centavos_inserida 
                        
                        if quantidade_moeda_cinquenta_centavos_inserida  > 0:
                            estoque_notas[1] = estoque_notas[1] - quantidade_moeda_cinquenta_centavos_inserida 
                        
                        if quantidade_moeda_um_real_inserida  > 0:
                            estoque_notas[2] = estoque_notas[2] - quantidade_moeda_um_real_inserida 
                        
                        if quantidade_cedula_dois_reais_inserida  > 0:
                            estoque_notas[3] = estoque_notas[3] - quantidade_cedula_dois_reais_inserida 
                        
                        if quantidade_cedula_cinco_reais_inserida  > 0:
                            estoque_notas[4] = estoque_notas[4] - quantidade_cedula_cinco_reais_inserida 
                        
                        if quantidade_cedula_dez_reais_inserida  > 0:
                            estoque_notas[5] = estoque_notas[5] - quantidade_cedula_dez_reais_inserida 
                    
                    else:
    #            remove do estoque todos as cedulas e moedas necessarias para o troco
                        if quantidade_moeda_vinte_e_cinco_centavos_removida > 0:
                            estoque_notas[0] = estoque_notas[0] - quantidade_moeda_vinte_e_cinco_centavos_removida
                        
                        if quantidade_moeda_cinquenta_centavos_removida > 0:
                            estoque_notas[1] = estoque_notas[1] - quantidade_moeda_cinquenta_centavos_removida
                        
                        if quantidade_moeda_um_real_removida > 0:
                            estoque_notas[2] = estoque_notas[2] - quantidade_moeda_um_real_removida
                        
                        if quantidade_cedula_dois_reais_removida > 0:
                            estoque_notas[3] = estoque_notas[3] - quantidade_cedula_dois_reais_removida
                        
                        if quantidade_cedula_cinco_reais_removida > 0:
                            estoque_notas[4] = estoque_notas[4] - quantidade_cedula_cinco_reais_removida
                        
                        if quantidade_cedula_dez_reais_removida > 0:
                            estoque_notas[5] = estoque_notas[5] - quantidade_cedula_dez_reais_removida
                        
                        #maquina libera refrierantes 
                        if comando_maquina == int(1) and dinheiro_depositado != 0:
                            print('aguinha liberada, pegue-a no compartimento!')
                            print('Obrigado pela compra, seu troco é de R$', troco,)
                            estoque_latas[0] = estoque_latas[0] - 1
                            
                        elif comando_maquina == int(2) and dinheiro_depositado != 0:
                            print('guarana geladinho liberada, pegue-o no compartimento!')
                            print('Obrigado pela compra, seu troco é de R$', troco,)
                            estoque_latas[1] = estoque_latas[1] - 1

                        elif comando_maquina == int(3) and dinheiro_depositado != 0:
                            print('Coquinha normal liberada, pegue-a no compartimento!')
                            print('Obrigado pela compra, seu troco é de R$', troco,)
                            estoque_latas[2] = estoque_latas[2] - 1

                        elif comando_maquina == int(4) and dinheiro_depositado != 0:
                            print('coquinha zero liberada, pegue-a no compartimento!')
                            print('Obrigado pela compra, seu troco é de R$', troco,)
                            estoque_latas[3] = estoque_latas[3] - 1

                elif pix_ou_dinheiro == 2:
                    numero_celular = str(input("digite seu numero de celular[(xx)xxxxx-xxxx] para pagamento com pix: "))
                    if len(numero_celular) == 11:
                        numeros_celular_historico.append(numero_celular)

                        if comando_maquina == int(1):
                            print('aguinha liberada, pegue-a no compartimento!')
                            historico_valor_pix.append(preco_produto[0])
                            estoque_latas[0] = estoque_latas[0] - 1
                            
                        elif comando_maquina == int(2):
                            print('guarana geladinho liberado, pegue-o no compartimento!')
                            historico_valor_pix.append(preco_produto[1])
                            estoque_latas[1] = estoque_latas[1] - 1

                        elif comando_maquina == int(3):
                            print('Coquinha normal liberada, pegue-a no compartimento!')
                            historico_valor_pix.append(preco_produto[2])
                            estoque_latas[2] = estoque_latas[2] - 1

                        elif comando_maquina == int(4):
                            print('coquinha zero liberada, pegue-a no compartimento!')
                            historico_valor_pix.append(preco_produto[3])
                            estoque_latas[3] = estoque_latas[3] - 1
                    else: 
                        print("numero invalido")




            
