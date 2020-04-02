from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_latter(self):

        # Ana ouviu falar de uma nova aplicação online interessante para
        # lista de tarefas. Ela decide verificar sua homepage
        self.browser.get('http://localhost:8000')

        # Ela percebe que p título da página e o cabeçalho mencionam listas
        # de tardeas (to-do)

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # Ela é convidada a inserir um item de tarefa imediatamente

        # Ela digita "Comprar penas de pavão" em uma caixa de texto
        # O hobby de Ana é fazer iscas para pescas com fly

        # Quando ela tecla Enter, a página é atualizada, e agora a página lista
        # "1: Comprar penas de pavão como um item da listas de tarefas"

        # Ainda continua havendo uma caixa  de texto a convidado-a a acrescentar outro
        # item. Ela insere "Usar penas de pavão parta fazer uma fly"

        # A página é atualizada e agora mostra dois itens em sua lista

        # Ana se pergunta se o site se lembrará de sua lista. Então ela nota
        # que o site gerou um URL único para ela -- há um pequeno texto
        # explicativo para isso.

        # Ela acessa esse URL - sua lista de tarefas continua lá.

        # Satisfeita, ela volta a dormir.
if __name__ == '__main__':
    unittest.main()