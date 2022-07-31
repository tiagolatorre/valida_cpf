class Cpf:
    """
        Classe que verifica se os CPFs são válidos ou inválidos
    """
    def __init__(self):
        pass

    def __extrai_numeros(self, texto: str):
        texto = [letra for letra in texto if letra in '1234567890']
        texto = "".join(texto)
        return texto

    def __numeros_repetidos(self, texto: str) -> bool:
        primeiro_numero = texto[0]
        for letra in texto:
            if letra != primeiro_numero:
                return False
        return True

    def __valida_apenas_numeros(self, numero_cpf: str):
        numero_cpf = numero_cpf.replace('.', '').replace('-', '').strip()
        return numero_cpf.isnumeric()

    def __valida_tamanho_cpf(self, numero_cpf: str):
        return len(numero_cpf) == 11

    def __calcula_cpf_com_digito_verificador(self, numero_cpf: str, multiplicador_inicial: int) -> str:
        soma_cpf = 0
        digito = 0
        cpf_com_digito = ''
        for indice, numero_multiplicar in enumerate(range(multiplicador_inicial, 1, -1)):
            soma_cpf += int(numero_cpf[indice]) * numero_multiplicar
            cpf_com_digito += numero_cpf[indice]
        else:
            digito = 11 - (soma_cpf % 11)
            if digito > 9:
                digito = 0
            cpf_com_digito += str(digito)
            return cpf_com_digito

    def valida_cpf(self, numero_cpf: str):
        """
        Valida se o CPF informado é válido ou inválido
        :param numero_cpf: informa o número de CPF a ser validado
        :return: Retorna True se o CPF for válido. Retorna Falso se o CPF for inválido
        """
        numero_cpf_informado = self.__extrai_numeros(numero_cpf)
        if numero_cpf_informado != "" and self.__valida_apenas_numeros(numero_cpf) and self.__valida_tamanho_cpf(numero_cpf_informado) and not self.__numeros_repetidos(numero_cpf_informado):
            numero_cpf_gerado = self.__calcula_cpf_com_digito_verificador(numero_cpf_informado, multiplicador_inicial=10)
            numero_cpf_gerado = self.__calcula_cpf_com_digito_verificador(numero_cpf_gerado, multiplicador_inicial=11)

            return numero_cpf_informado == numero_cpf_gerado
        return False
