# IMPORTS
from time import sleep # SERVE PARA O PROGRAMA ESPERAR UM POUQUINHO, COMO SE FOSSE UM RELÓGIO
from os import system, name # SERVE PARA LIMPAR A TELA DO COMPUTADOR, DEIXANDO TUDO ORGANIZADO
import random # SERVE PARA ESCOLHER COISAS ALEATÓRIAS, COMO DECIDIR QUEM GANHA NO EMPATE
import csv # BIBLIOTECA = SERVE PARA GUARDAR E LER DADOS EM ARQUIVOS DE PLANILHA (CSV), COMO SALVAR OS VOTOS

# FUNÇÃO DE LIMPAR TELA
def limpar_tela():
    if name == "nt": # WINDOWNS
        system("cls")
    else:
        system("clear") # LINUX AND MAC

# FUNÇÃO PRA ESCREVER DEVAGAR
def digitar(texto):
    for letra in texto:
        print(letra, end="", flush=True)
        sleep(0.02)
    print()

# FUNÇÃO PARA DIGITAR LINHAS DE DECORAÇÃO
def linha():
    print("<>" * 25)

def linha_2():
    print("=" * 25)
    
def linha_3():
    print("=" * 36)

# FUNÇÃO PRA CONFIRMAR O VOTO
def confirmar_voto(nome):
    while True:
        confirmar = input(f"Confirmar voto em {nome}? (s/n): ").strip().lower()
        if confirmar == "s":
            return True
        elif confirmar == "n":
            return False
        else:
            print("Digite apenas S ou N!")

# FUNÇÃO PARA DEFINIR O VENCEDOR NO CASO DE EMPATE
def decidir_empate(empate):
    vencedor = random.choice(empate)
    return vencedor

# INTRODUÇÃO
limpar_tela() # LIMPAR A TELA 
linha()
digitar("          ELEIÇÃO PRESIDENCIAL 2026") #    MENSAGEM 
linha()
print()
digitar("\nCarregando sistema eleitoral...")
sleep(1.5)
print()

# CANDIDATOS
candidatos = {
    1: {"nome": "Victor", "votos": 0},
    2: {"nome": "Gabriel", "votos": 0},
    3: {"nome": "Ruan", "votos": 0},
    4: {"nome": "Daniel", "votos": 0},
    5: {"nome": "Kauã", "votos": 0}
}
sleep(0.10)
print()

# INICIO DO SISTEMA DE VOTAÇÃO
while True: # ESTRUTURA DE REPETIÇÃO
    limpar_tela() # LIMPAR A TELA 
    sleep(1)
    digitar("★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★")
    digitar("           🎉 SISTEMA DE VOTOS 🎉")
    digitar("★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★")
    
    finalizar = input("\n👉 Digite 0 para encerrar a eleição ou ENTER para continuar: ").strip() # .STRIP REMOVE ESPAÇOS EM BRANCO
    print() 
    if finalizar == "0": # CASO O USUÁRIO DIGITAR '' 0 '' O PROGRAMA FINALIZA
        digitar("⚠️ Sistema de votação encerrado... Obrigado pela participação! ✅")
        sleep(2)
        break # PARAR O SISTEMA
    elif finalizar == "": # OS ASPAS SIMULA O '' ENTER '' | ESPAÇO VAZIO
        linha_3()
        digitar("➡️ Continue com o sistema de votação. ") # MENSAGEM CASO 
        linha_3()   
    else:
        digitar("❌ Entrada inválida. Digite 0 para encerrar ou ENTER para continuar. ") # SE NÃO DIGITAR "0" OU "ENTER" VOLTA AO INICIO
        sleep(1)
        continue # FAZ VOLTAR O LOOP DO INICIO
    
    # VARIÁVEL
    nome_eleitor = input("\n📝 Digite o nome do eleitor: ").strip().title() # .STRIP() = NÃO DEIXAR ESPAÇOS BRANCAS
    if nome_eleitor.isdigit():  # .ISDIGIT()                                             # .TITLE() = 1º LETRAS SEMPRE MAIÚSCULAS
        print("❌ Nome inválido! Digite apenas letras. ") # MENSAGEM
        sleep(1.5)
        continue # CASO O USUARIO DIGITE NNÚMEROS VAI VOLTAR O ALGORITMO
    try: # TRY AND EXEPT = TRATAR ERROS
        idade = int(input("🎂 Digite sua idade: ")) # PARA O USUÁRIO DIGITAR A IDADE
        if idade < 16: # SE A IDADE FOR MENOR QUE 16
            print("\n🚫 Você NÃO pode votar! ") # SE FOR MENOR DE 16 NÃO PODE VOTAR
            sleep(1.5) # PAUSA DE 1.5 SEGUNDOS
            continue # CASO SEJA MENOR DE IDADE, O PROGRAMA VAI VOLTAR AO INICIO DO LOOP
    except:
        print("\n❌ Idade inválida! ") # MENSAGEM 
        sleep(1.5) # PAUSA DE 1.5 SEGUNDOS
        continue # REINICIA O ALGORITMO CASO O ELEITOR DIGITE LETRAS

    limpar_tela() # LIMPAR A TELA 
    linha_2() # DESENHA UMA LINHA DECORATIVA
    print(f"👤 ELEITOR: {nome_eleitor} ") # MOSTRA O NOME DO ELEITOR
    linha_2() # DESENHA UMA LINHA DECORATIVA
    print(f"📊 IDADE: {idade} anos ") # MOSTRA A IDADE DO ELEITOR
    linha_2() # DESENHA UMA LINHA DECORATIVA
    limpar_tela() # LIMPAR A TELA 

    print("\n⚡ ESCOLHA SEU CANDIDATO:\n")
    for codigo, dados in candidatos.items(): # PERCORRE O DICIONARIO MOSTRANDO O NUMERO E O NOME DOS CANDIDATOS
        digitar(f"{codigo} - {dados['nome']}") # LER OS CANDIDATOS ARMAZENADOS EM DICIONÁRIO
    print("0 - Encerrar eleição") # OPÇÃO DE ENCERRAR ELEIÇÃO

    try: # TRY AND EXEPT = TRATAR ERRO
        voto = int(input("\n🗳️  Digite o número do candidato: ")) # OPÇÃO PARA O USUARIO ESCOLHER O CANDIDATO
    except:
        print("\n⚠️ Digite apenas números! ") # CASO O USUARIO DIGITE UM CARACTERE
        sleep(2) # PAUSA DE 2 SEGUNDOS
        continue # CASO O O ELEITOR DIGITE LETRAS AO INVÉS DE NÚMEROS, VOLTA PRA O INICIO DO ALGORITIMO

    if voto == 0: # ENCERRAR O PROGRAMA
        break # PARAR O ALGORITIMO
    if voto not in candidatos: # CASO O USUARIO ESCOLHA UMA OPÇAO INEXISTENTE
        print("\n❌ Candidato inválido! ") # CASO NAO ESCOLHA UMA OPÇÃO QUE NÃO EXISTA
        sleep(1.5) # PAUSA DE 1.5 SEGUNDOS
        continue # REINICIAR O ALGORITO CASO ESCOLHA UMA OPÇÃO INVÁLIDA

    nome_candidato = candidatos[voto]["nome"] # PEGA O NOME DO CANDIDATO ESCOLHIDO PELO ELEITOR
    confirmado = confirmar_voto(nome_candidato) # PERGUNTA SE O ELEITOR QUER CONFIRMAR O VOTO NESSE CANDIDATO

    # SALVAR ELEITOR + VOTO NO CSV
    with open("Dados dos Eleitores.csv", "a", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo) # CRIA UM ESCRITOR DE LINHAS NO ARQUIVO
        escritor.writerow([nome_eleitor, idade, nome_candidato]) # ESCREVE UMA LINHA COM : NOME, IDADE E CANDIDATO ESCOLHIDO
    
    if confirmado: # SE O ELEITOR CONFIRMOU O VOTO
        candidatos[voto]["votos"] += 1 # SOMA MAIS UM VOTO PARA O CANDIDATO
        print("\n🎉 VOTO CONFIRMADO COM SUCESSO! 🎉") # MOSTRA MENSAGEM DE SUCESSO
        digitar(f"Obrigado por votar ✅, {nome_eleitor}!") # AGRADECE AO ELEITOR
    else:   # SE O ELEITOR NÃO CONFIRMOU
        print("\n❌ Voto cancelado!, Você pode reiniciar o processo.")   # MOSTRA MENSAGEM DE CANCELAMENTO

    sleep(2) # PAUSA DE 2 SEGUNDOS

# RESULTADO FINAL
limpar_tela() # DESENHA UMA LINHA DECORATIVA
linha() # PULA UMA LINHA
digitar("               RESULTADO FINAL")
linha() # DESENHA UMA LINHA DECORATIVA
print() # PULA UMA LINHA

total_votos = sum(dados["votos"] for dados in candidatos.values())   # SOMA TODOS OS VOTOS DE TODOS OS CANDIDATOS

for codigo, dados in candidatos.items():   # PEGA CADA CANDIDATO DA LISTA
    votos = dados["votos"]   # GUARDA QUANTOS VOTOS ELE TEM
    porcentagem = (votos / total_votos) * 100 if total_votos > 0 else 0   # CALCULA A PORCENTAGEM DE VOTOS
    print(f"Candidato: {dados['nome']} | Votos: {votos} | Porcentagem: {porcentagem:.1f}%")   # MOSTRA NOME, VOTOS E PORCENTAGEM

print() # PULA UMA LINHA
linha() # DESENHA UMA LINHA DE DECORAÇÃO
print(f"            TOTAL DE VOTOS 📊: {total_votos}")  # MOSTRA O TOTAL DE VOTOS

maior = max(dados["votos"] for dados in candidatos.values()) # PEGA O MAIOR NÚMERO DE VOTOS ENTRE OS CANDIDATOS
empate = [dados["nome"] for dados in candidatos.values() if dados["votos"] == maior]  # CRIA UMA LISTA COM OS CANDIDATOS QUE TIVERAM O MESMO MAIOR NÚMERO DE VOTOS (EMPATE)

if len(empate) > 1:   # SE MAIS DE UM CANDIDATO TEVE O MESMO NÚMERO DE VOTOS
    print("\nEMPATE DETECTADO! ⚖️\n")   # MOSTRA QUE DEU EMPATE
    vencedor = decidir_empate(empate)   # ESCOLHE UM VENCEDOR ALEATÓRIO ENTRE OS EMPATADOS
    digitar(f"O algoritmo decidiu que o vencedor é: {vencedor}")   # MOSTRA QUEM FOI ESCOLHIDO
else:   # SE NÃO TEVE EMPATE
    vencedor = empate[0]   # PEGA O CANDIDATO COM MAIS VOTOS
    print(f"VENCEDOR DA ELEIÇÃO 🏆: {vencedor}")   # MOSTRA O VENCEDOR

linha()   # DESENHA UMA LINHA DECORATIVA
print()   # PULA UMA LINHA

linha()   # DESENHA UMA LINHA DECORATIVA
match vencedor:  #FORMA MAIS LIMPA E ORGANIZADA DE FAZER UMA COMPARAÇÃO DE VALORES
    case "Victor":
        digitar("""
    Consequências do governo Victor:
    
    - Salário minímo vai passar a ser 5 mil
    - Todo ônibus terá ar-condicionado congelante
    - Café virou patrimônio nacional
    - Churrasco aos domingos será obrigatório
""")
    case "Gabriel":
        digitar("""
    Consequências do governo Gabriel:
    
    - Toda população tem que se batizar 
    - Toda reunião começa com oração
    - Wi-Fi das escolas toca louvor automaticamente
    - Instagram virou ministério oficial
""")
    case "Ruan":
        digitar("""
    Consequências do governo Ruan:
    
    - Laje do planato agora tem festival de pipa
    - Bailes funk agora são eventos culturais
    - Neymar virou ministro do esporte
    - Toda sexta é dia do futebol nacional
""")
    case "Daniel":
        digitar("""
        Consequências do governo Daniel:
        
        - Criação da bolsa GAMER  
        - Wi-Fi grátis até na padaria
        - Lag virou crime federal
        - Todo estudante ganhou notebook gamer
""")
    case "Kauã":
        digitar("""
    Consequências do governo Kauã:
    
    - Segunda-feira passa a ser folga obrigatória 
    - Sexta-feira virou feriado nacional
    - Pastel com caldo de cana subsidiado
    - Vale churrasco aprovado por unanimidade
""")

# CASO O USUÁRIO QUEIRA VER OS DADOS
print() # PULAR UMA LINHA
# PERGUNTA SE O USUÁRIO DESEJA VER OS DADOS DOS ELEITORES
ver_dados = input("Deseja visualizar os dados dos eleitores? (S/N): ").strip().upper()   # PERGUNTA SE O USUÁRIO QUER VER OS DADOS DOS ELEITORES
limpar_tela()  # LIMPA A TELA

if ver_dados == "S":   # SE O USUÁRIO DIGITAR S
    print()  # PULA UMA LINHA 
    linha()  # DESENHA UMA LINHA DECORATIVA
    print("           📋 DADOS DOS ELEITORES 📋")   # MOSTRA O TÍTULO
    linha()  # DESENHA UMA LINHA DECORATIVA

    try:
        with open("Dados dos Eleitores.csv","r",encoding="utf-8") as arquivo:   # ABRE O ARQUIVO CSV PARA LER OS DADOS
            leitor = csv.reader(arquivo)   # CRIA UM LEITOR DE LINHAS
            for linha_csv in leitor:   # PEGA CADA LINHA DO ARQUIVO
                print(   # MOSTRA NOME, IDADE E CANDIDATO DE CADA ELEITOR
                
                   # EXIBE OS DADOS ORGANIZADOS 
                    f"Eleitor: {linha_csv[0]} | " # NOME DO ELEITOR 
                    f"Idade: {linha_csv[1]} | "# IDADE DO ELEITOR
                    f"Votou em: {linha_csv[2]}"# CANDIDATO ESCOLHIDO
                )             

    except FileNotFoundError:   # SE O ARQUIVO NÃO EXISTIR
        print("\nNenhum eleitor foi registrado. ")   # MOSTRA QUE NINGUÉM FOI REGISTRADO

    linha()   # DESENHA UMA LINHA DE DECORAÇÃO
    print()   # PULA UMA LINHA

linha_3()   # DESENHA UMA LINHA DECORATIVA
digitar("Sistema encerrado com sucesso! ✅")   # MOSTRA MENSAGEM DE ENCERRAMENTO
linha_3()   # DESENHA OUTRA LINHA DECORATIVA