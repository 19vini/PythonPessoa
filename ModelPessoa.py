# Classe Model Pessoa
class ModelPessoa:
    # Declaração de variáveis
    def __init__(self): # Representa um método construtor
        # pode criar um usuário padrão nas atribuições para as variáveis
        self.cpf = 0
        self.nome = ""
        self.telefone = 0
        self.endereco = ""
        self.email = ""

    def cadastrarPessoa(self, cpf, nome, telefone, endereco, email):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.email = email

    def consultarPessoa(self):
        consulta = (f"CPF: {self.cpf}\nNome: {self.nome}\nTelefone: {self.telefone}\n"
                    f"Endereço: {self.endereco}\nE-mail: {self.email}")
        return consulta

    def atualizarPessoa(self, opcao, dado):
        if opcao == 1:
            self.nome = dado
        elif opcao == 2:
            self.telefone = dado
        elif opcao == 3:
            self.endereco = dado
        elif opcao == 4:
            self.email = dado

    def excluirPessoa(self):
        self.cpf = 0
        self.nome= ""
        self.telefone = 0
        self.endereco = ""
        self.email = ""
