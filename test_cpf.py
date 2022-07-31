import unittest
from cpf import Cpf

class TestCpf(unittest.TestCase):
    def test_cpf_em_branco(self):
        self.Cpf = Cpf()
        self.assertEqual(self.Cpf.valida_cpf(''), False)

    def test_cpf_numeros_iguais(self):
        self.Cpf = Cpf()
        entradas_numero_cpf = (
            '11111111111', '22222222222', '33333333333', '44444444444', '55555555555', '66666666666', '77777777777',
            '88888888888', '99999999999', '00000000000')
        saida = False
        for entrada_numero_cpf in entradas_numero_cpf:
            with self.subTest(entrada_numero_cpf=entradas_numero_cpf, saida=saida):
                self.assertEqual(self.Cpf.valida_cpf(entrada_numero_cpf),
                                 saida,
                                 msg=f'"{entrada_numero_cpf}" não retornou "{saida}"'
                                 )

    def test_cpf_validos(self):
        self.Cpf = Cpf()
        entradas_numero_cpf = (
            '841.805.420-48', '317.477.400-47', '853.724.550-04', '921.013.120-77', '915.206.790-41', '668.863.720-09',
            '779.625.780-50',
            '882.907.550-74', '200.811.500-32', '574.426.240-73', '692.779.780-74', '000.071.400-37', '856.129.290-30',
            '585.114.880-22')
        saida = True
        for entrada_numero_cpf in entradas_numero_cpf:
            with self.subTest(entrada_numero_cpf=entradas_numero_cpf, saida=saida):
                self.assertEqual(self.Cpf.valida_cpf(entrada_numero_cpf),
                                 saida,
                                 msg=f'"{entrada_numero_cpf}" não retornou "{saida}"'
                                 )

    def test_cpf_invalidos(self):
        self.Cpf = Cpf()
        entradas_numero_cpf = (
            '841.805.420-47', '317.477.400-46', '853.724.550-05', '921.013.120-74', '915.206.790-40', '668.863.720-01',
            '779.625.780-51',
            '882.907.550-70', '200.811.500-31', '574.426.240-72', '692.779.780-73', '000.071.400-38', '856.129.290-31',
            '585.114.880-23')
        saida = False
        for entrada_numero_cpf in entradas_numero_cpf:
            with self.subTest(entrada_numero_cpf=entradas_numero_cpf, saida=saida):
                self.assertEqual(self.Cpf.valida_cpf(entrada_numero_cpf),
                                 saida,
                                 msg=f'"{entrada_numero_cpf}" não retornou "{saida}"'
                                 )

    def test_cpf_invalidos_diferente_11_numeros(self):
        self.Cpf = Cpf()
        entradas_numero_cpf = (
            '841.805.4-47', '317477400', '8537245500511', '92111.013.120-74', '915206791040', '68.83.20-01',
            '779625780511',
            '1', '12', '1234', '12345', '1234.5.67-1', '12345678.9.1', '33')
        saida = False
        for entrada_numero_cpf in entradas_numero_cpf:
            with self.subTest(entrada_numero_cpf=entradas_numero_cpf, saida=saida):
                self.assertEqual(self.Cpf.valida_cpf(entrada_numero_cpf),
                                 saida,
                                 msg=f'"{entrada_numero_cpf}" não retornou "{saida}"'
                                 )

    def test_cpf_invalidos_com_letras(self):
        self.Cpf = Cpf()
        entradas_numero_cpf = (
            '841.805.420-48a', '317.477.400-4b', 'a853724.550-04', '9u1.013.120-77', '915c206.790-41', '668p863p720-09',
            '779.625.780-50a',
            'aaaaaaabbbb', 'aaaaaaaaaaa', 'aaaaabbbb1234', 'b', 'a', '856.129.290c', '58511488022a')
        saida = False
        for entrada_numero_cpf in entradas_numero_cpf:
            with self.subTest(entrada_numero_cpf=entradas_numero_cpf, saida=saida):
                self.assertEqual(self.Cpf.valida_cpf(entrada_numero_cpf),
                                 saida,
                                 msg=f'"{entrada_numero_cpf}" não retornou "{saida}"'
                                 )


unittest.main(verbosity=2)
