from app.main import *
import tests.mock_variables as mocks
import unittest
from unittest import mock
from unittest.mock import patch


class MainTest(unittest.TestCase):

    def test_suma(self):
        response = suma(2,3)
        self.assertEquals(response, 5)








    def test_get_user_info_ok(self):
        response = get_user_info('test_mdemolli')
        self.assertEquals(response, mocks.user_info)





    def test_get_user_info_not_found(self):
        self.assertRaises(UserNotFoundException, get_user_info, 'test_mfesta')











    @patch("app.main.get_random_number")
    def test_sumar_numero_aleatorio(self, mock_get_random_number):
        mock_get_random_number.return_value = 10
        response = sumar_numero_aleatorio(5)
        self.assertEquals(response, 15)

    @patch('random.randrange')
    def test_get_random_number(self, mock_randrange):
        mock_randrange.return_value = 50
        response = get_random_number()
        self.assertEquals(response, 50)






##################################





    def test_does_user_exists_true(self):
        response = does_user_exists('test_mdemolli')
        self.assertEquals(response, True)


    @patch('app.main.get_user_info')
    def test_does_user_exists_false(self, mock_get_user_info):
        mock_get_user_info.side_effect = UserNotFoundException
        response = does_user_exists('test_mdemolli')
        self.assertEquals(response, False)
















    @patch("app.main.get_random_number")
    def test_sumar_dos_numeros_aleatorios(self, mock_get_random_number):
        mock_get_random_number.side_effect = [10,30]
        response = sumar_dos_numeros_aleatorios()
        self.assertEquals(response, 40)






    @patch('app.main.imprimir_bienvenida')
    def test_imprimir_menu_julian(self, mock_bienvenida):
        response = imprimir_menu_julian()
        mock_bienvenida.assert_called_with('Julian')











    @patch('requests.get')
    def test_get_ssff_info_200(self, mock_requests):
        get_response = mock.MagicMock()
        type(get_response).status_code = mock.PropertyMock(return_value=200)
        mock_requests.return_value = get_response
        r = get_ssff_info('jstrah')
        self.assertEquals(r, get_response.json())


    @patch('requests.get')
    def test_get_ssff_info_404(self, mock_requests):
        get_response = mock.MagicMock()
        type(get_response).status_code = mock.PropertyMock(return_value=404)
        mock_requests.return_value = get_response
        self.assertRaises(UserNotFoundException, get_ssff_info, 'jstrah')




