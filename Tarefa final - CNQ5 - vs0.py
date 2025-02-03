# Tarefa final - CNQ5
from abc import ABC, abstractmethod

# Códigos de escape ANSI para cores
Verde = '\033[1;32m' 
Vermelho = '\033[1;91m'
Magenta = '\033[1;35m' 
Amarelo= '\033[5;33m'
RESET = '\033[0m' # o reset serve para terminar a cor

print("_______________________________________________________________________________________")
print("                            Bem-vindo ao Gestor de Tarefas")
print("_______________________________________________________________________________________")

#1º  Classe Abstrata - Ao criar uma classe abstrata qualquer classse concreta que herde da classe Abstrata é obrigada a implementar estes métodos
class Tarefa(ABC): 
    @abstractmethod #Utiliza-se a classe base abstrata (ABC) para garantir que os métodos sejam implementados em subclasses
    def adicionar_tarefa(self, tarefa):
        pass ## o pass é usado para criar um método que não faz nada, apenas "ocupa o lugar" até que uma classe filha implemente a lógica.
    #Basicamente o pass não faz nada aqui, mas diz que sabe que este método existe e será tratado noutro lugar

    @abstractmethod
    def visualizar_tarefa(self):
        pass

    @abstractmethod
    def editar_tarefa(self, indice, nova_tarefa):
        pass
    
    @abstractmethod
    def eliminar_tarefa(self, indice, delete_tarefa):
        pass

#2º  Classe concreta que herda da classe Tarefa. Aqui vamos definir as funções a utilizar no menu do programa
class Tarefa_diaria(Tarefa):
    def __init__(self,ficheiro):
        self.ficheiro = ficheiro

    # a) Criar método para adicionar as tarefas ao ficheiro
    def adicionar_tarefa(self, tarefa):
        try:
            with open(self.ficheiro, "a", encoding="utf-8") as fic: #O parâmetro encoding='utf-8' na função open especifica que o ficheiro deve ser lido usando a codificação de caracteres UTF-8
                                                                        #quando lê um ficheiro que contém caracteres especiais (como acentos ou símbolos), especificar encoding='utf-8'
                fich.write(tarefa + '\n') #adicionou-se um paragrafo para que a tarefa seja adicionada na linha abaixo e não adicionada na mesma linha da última tarefa
            print("Tarefa adicionada com sucesso!")
        except:
            print("Erro ao adicionar tarefa.")
    
    # b) Criar método para visualizar as tarefas do ficheiro na consola
    def visualizar_tarefa(self, tarefa):
        try:
            with open(self.ficheiro, "a", encoding="utf-8") as fic:
                tarefas = fich.readlines()
                if tarefas:
                    print("\n")
                    print("Lista de tarefas no ficheiro:")
                    for i, tarefa in enumerate(tarefas, start=1): #enumerate-  função que adiciona um contador a uma lista (neste casao a tarefa), por exemplo. start=1: indica que a contagem começa em 1 (o padrão é 0).
                        print(f"{i}- {tarefa.strip()}")
                else:
                    print("Nenhuma tarefa encontrada.")
               
        except:
            print("Ficheiro não encontrado! Adicione primeiro uma tarefa para criar o ficheiro")


    # c) Criar método para editar tarefas
    def editar_tarefa(self, indice, nova_tarefa):
        try:
            with open(self.ficheiro, "r", enconding="utf-8") as fic:
            tarefas = fich.readlines()
            if 1 <= indice <= len(tarefas):
                tarefas[indice - 1] = nova_tarefa + '\n' # As listas começam com índice 0, mas o utilizador fornece um índice a partir de 1, então subtraímos 1.
                                                         # Adicionou-se \n para manter a formatação do ficheiro e passar para a linha de baixo.
            with open(self.ficheiro, "w", encoding="utf-8") as fich:
                fich.writelines(tarefas) # Aqui vamos escrever o resultado de cima na lista
                print("Tarefa modificada com sucesso!")
            else:
                print("Índice não válido.")
        except:
            print("Erro ao editar a tarefa! Verifique se o ficheiro existe!")
    
    # d) Criar método para eliminar tarefas
    def eliminar_tarefa(self, indice, nova_tarefa):   
        try:
            with open(self.ficheiro, "r", encoding="utf-8") as fich:
                tarefas = fich.readlines()
            if 1 <= indice <= len(tarefas):
                tarefa_eliminar=tarefas.pop(indice-1).strip() #a diferença do código deste método para o acima é esta linha, enquanto no de cima adiciona aqui remove
                with open(self.ficheiro, "w", encoding="utf-8") as fich:
                    fich.writelines(tarefas) ## Aqui vamos escrever o resultado de cima na lista
                print("Tarefa removida com sucesso!")
            else:
                print("Índice inválido.")
        except:
            print("Erro ao remover a tarefa! Verifique se o ficheiro existe!")


#3º Funções para contar o número de tarefas e o tempo medio para cada tarefa
    # a) função para contar o numero de linhas que existem no ficheiro. Nº de linhas= nº de tarefas
def contar_tarefas(ficheiro):
    try:
        with open(ficheiro, "r", encoding="utf-8") as fich:
            tarefas = fich.readlines()
        return len(tarefas)
    except:
        print("Erro! Verifique se ficheiro existe ou contém informação")
        return 0

    # b) função para calcular o tempo médio disponivel em 8h para realizar as tarefas do ficheiro
def tempo_por_tarefa(ficheiro):
    total_tarefas=contar_tarefas(ficheiro) #chamo a função contar_tarefas definida no ponto 3 alinea a)
    if total_tarefas>0:
        media_tempo=(8*60)/total_tarefas # passei para minutos
        return media_tempo
    else:
        return 0

# 4º Vamos perguntar ao utilizador qual o nome do ficheiro que vai utilizar
ficheiro=input("Qual o nome do ficheiro a utilizar? Use a extenção .txt no final do nome").strip().lower()

# 5º Definir o Objecto dda classe Tarefa_diaria
lista=Tarefa_diaria(ficheiro)
            
# 6º Definir qual vai ser o ciclo do programa
while True:
    print("\n")
    print("Menu:")
    print("1. Adicionar Tarefa")
    print("2. Visualizar Tarefas")
    print("3. Editar Tarefa")
    print("4. Eliminar Tarefa")
    print("5. Ver nº total de Tarefas e tempo médio para cada tarefa")
    print("6. Sair")
    print("\n")
    
    while True:  # Mantém o loop até que o utilizador insira um número válido
        opcao = input("Escolha o número do menu que pretende utilizar: ").strip()  # Obtém a entrada como string
        if opcao.isdigit():  # Verifica se a entrada contém apenas números
            opcao = int(opcao)  # Converte para inteiro
            if 1 <= opcao <= 6:
                break  # Sai do loop se for válido
        else:
            print("Opção inválida! Digite um número entre 1 e 6.")
    
    if opcao ==1: #Adiconar a tarefa
        tarefa=input("Digite a tarefa a adicionar: ").strip()
        lista.adicionar_tarefa(tarefa)
    elif opcao ==2: #Visualizar a tarefa
        lista.visualizar_tarefa()