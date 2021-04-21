import random
import requests, json



def suma(a,b):
    resultado = a + b
    return resultado







class UserNotFoundException(Exception):
    pass

def get_user_info(username):
    usuarios = {
        'test_jstrah': {
            'nombre': 'Julian',
            'apellido': 'Strah'
        },
        'test_mdemolli': {
            'nombre': 'Mariano',
            'apellido': 'Demolli'
        }
    }
    if username in usuarios:
        return usuarios[username]
    else:
        raise UserNotFoundException





def does_user_exists(username):
    try:
        get_user_info(username)
        return True
    except UserNotFoundException:
        return False








def get_random_number():
    num = random.randrange(100)
    return num



def sumar_numero_aleatorio(num):
    result = num + get_random_number()
    return result



def sumar_dos_numeros_aleatorios():
    result = get_random_number() + get_random_number()
    return result



def imprimir_bienvenida(nombre):
    print('Bienvenido '.format(nombre))

def imprimir_menu_julian():
    print('-----------------------')
    imprimir_bienvenida('Julian')
    print('-----------------------')






def get_ssff_info(username):
    token = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MTkwMjIxNzcsIm5iZiI6MTYxOTAyMjE3NywianRpIjoiMWY4ODIwMTktZTQ0Zi00OTc1LWFkOTgtMjZlY2U4ZGE0NzAzIiwiZXhwIjoxNjE5MDUwOTc3LCJpZGVudGl0eSI6ImpzdHJhaCIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyIsInVzZXJfY2xhaW1zIjp7InJvbGVzIjpbInNlZ2luZl9mdWxsIl19fQ.LS5wNtMSGra26tXhwx9vr2c8joSAoHqE1RQNmwL7NnETTrde62fKV9CaZQmMQcWvP8KnKEjdJ6C7IElFejEJaewRZ25I79szPzsMnVupfzFfjcI5TVIHAUwWvT_Vu_mB994YiyDh2bYhhDDpv2nqG4aChfR-p39vSZjJ3jrK-0GKmmUhEE1snleZW7r4z8hqnrps66RsunVg_b8fYa06dEAca8SEzqwPKx_687HZS_Y1c83bCnH0_F95UZqYtuHbRh77QrTBav_SfB0ASGWPDwSiUIy7xj2uOHjp_EZCSDD82z0yub0Pe_t0Xa64nsLPnCZxlgMo7z4bqSEMjuF8pw'}
    response = requests.get(url="http://mordor-api.meliseginf.com/api/ssff/user/{}/username".format(username), headers=token)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise UserNotFoundException
