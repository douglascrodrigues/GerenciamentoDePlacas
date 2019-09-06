from django.test import TestCase, SimpleTestCase

class CoreViewTest(SimpleTestCase):
    def test_index_200(self):
       resposta = self.client.get("/")
       self.assertEqual(resposta.status_code, 200)
    
    def test_index_template(self):
        resposta = self.client.get("/")
        self.assertTemplateUsed(self, resposta, 'index.html')
        
    def test_login_200(self):
       resposta = self.client.get("entrar")
       self.assertEqual(resposta.status_code, 200)
       