from pytest import *
from main import *

def testaCriarUsuario():
    criar_usuario("Lucas")
    print(usuarios[len(usuarios) - 1])
    assert usuarios[len(usuarios) - 1] == {'id':1, 
    'nome':'Lucas', 
    'seguidores': [],
    'seguindo': []}    