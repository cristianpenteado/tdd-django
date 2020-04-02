from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Ela é convidada a inserir um item de tarefa imediatamente
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Digite um item para a lista'
        )
        
        # Ela digita "Comprar penas de pavão" em uma caixa de texto
        # O hobby de Ana é fazer iscas para pescas com fly
        inputbox.send_keys('Comprar penas de pavão')


        # Quando ela tecla Enter, a página é atualizada, e agora a página lista
        # "1: Comprar penas de pavão" como um item da listas de tarefas"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Comprar penas de pavão' for row in rows)
        )

        # Ainda continua havendo uma caixa  de texto a convidado-a a acrescentar outro
        # item. Ela insere "Usar penas de pavão parta fazer uma fly"

        # A página é atualizada e agora mostra dois itens em sua lista

        self.fail('Finish the test!')

        # Ana se pergunta se o site se lembrará de sua lista. Então ela nota
        # que o site gerou um URL único para ela -- há um pequeno texto
        # explicativo para isso.

        # Ela acessa esse URL - sua lista de tarefas continua lá.

        # Satisfeita, ela volta a dormir.
if __name__ == '__main__':
    unittest.main()