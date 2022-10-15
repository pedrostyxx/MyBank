import os

# Construção base para criação do objeto
class Account:
    def __init__(self, cardholder_name, account_number, account_balance, agency, limit) -> None:
        #--------- Atributos do objeto ---------#
        self.__cardholder_name = cardholder_name
        self.__account_number = account_number
        self.__account_balance = account_balance
        self.__account_agency = agency
        self.__account_limit = limit
        self.__account_maxdeposit = 10000
        self.__account_mindeposit = 20

         #--------- Métodos do objeto ---------#

    # Exibe extrato na tela
    def print_extract(self):
        print("[Extrato] Olá {}, seu saldo em Conta corrente é de R${:.2F} e seu cheque especial é de R${:.2F}"
        .format(self.__cardholder_name, self.__account_balance, self.__account_limit))

    # Adciona dinheiro na conta respeitando os limites
    def deposit(self, deposit_value):
        if(deposit_value) <= (self.__account_maxdeposit) and (deposit_value) > (self.__account_mindeposit):
            self.__account_balance += deposit_value
            print("Sucesso!")

        else:
            print("Ops! Você só pode movimentar valores entre R${:.2F} e R${:.2F}"
            .format(self.__account_mindeposit, self.__account_maxdeposit))

    # Saque de dinheiro da conta respeitando os limites
    def whip(self, withdrawal_amount):
        if(withdrawal_amount) <= (self.__account_balance):
            self.__account_balance -= withdrawal_amount
            print("Sucesso!")

        else:
            print("Ops! Você não tem fundos suficientes para fazer essa operação")
            print("Seu saldo é de R${:.2F}"
            .format(self.__account_balance))

    def ted(self, ted_amount, receiver):
        if(ted_amount) <= (self.__account_balance):
            self.whip(ted_amount)
            receiver.deposit(ted_amount)
            os.system('cls')

            print('Sua transferência foi realizada!')

        else:
            print("Ops! Você não tem fundos suficientes para fazer essa operação")
            print("Seu saldo é de R${:.2F}"
            .format(self.__account_balance))

    #--------- Métodos para requisições de propriedades ---------#
    @property # Informa o python que se trata de uma propriedade ( Um @decorator )
    def balance(self):
        return self.__account_balance

    @property
    def cardholder_name(self):
        return self.__cardholder_name

    @property
    def account_limit(self):
        return self.__account_limit

    #--------- Métodos para setar um novo valor ao atributo ---------#
    @account_limit.setter # Informa o python que se trata de um "setter" ( Um @decorator )
    def set_limit(self, new_limit):
        self.__account_limit = new_limit

    #--------- Métodos estáticos ---------#
    @staticmethod# Informa o python que se trata de um método estático ( Um @decorator )
    def bank_num():
        return "001"
    

            
            