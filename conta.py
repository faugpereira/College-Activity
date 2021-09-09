class Conta:
        def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

        def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def extrato(self):
        print("numero:	{}	\nsaldo:	{}".format(self.__numero, self.__saldo))
