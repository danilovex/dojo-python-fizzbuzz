import service    # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):

    def test_deve_retornar_fizz_numeros_divisiveis_por3(self):
        self.assertEqual(service.eh_divisivel_por3(15), True)

    def test_deve_retornar_true_numeros_divisiveis_por5(self):
        self.assertEqual(service.eh_divisivel_por5(5), True)
 
    def test_deve_retornar_true_numeros_divisiveis_por3e5(self):
        self.assertEqual(service.eh_divisivel_por3e5(15), True)

    def test_3_deve_retornar_fizz(self):
        self.assertEqual(service.substituir(3), 'FIZZ')

    def test_5_deve_retornar_buzz(self):
        self.assertEqual(service.substituir(5), 'BUZZ')

    def test_15_deve_retornar_fizzbuzz(self):
        self.assertEqual(service.substituir(15), 'FIZZBUZZ')

    def test_4_deve_retornar_4(self):
        self.assertEqual(service.substituir(4), '4')

    def test_contem_31_retornar_fizz(self):
        self.assertEqual(service.substituir(31),'FIZZ')

    def test_contem_51_retornar_fizzbuzz(self):
        self.assertEqual(service.substituir(51),'FIZZBUZZ')

if __name__ == '__main__':
    unittest.main()