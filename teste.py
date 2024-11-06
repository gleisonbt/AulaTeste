import pytest
from main import *

def setup_function():
    usuarios.clear()
    postagens.clear()
    proximo_id_usuario = 1
    proximo_id_postagem = 1

def testaCriarUsuarioValido():
    criar_usuario("Gleison")
    assert usuarios[0] == {
        'id':1, 'nome':'Gleison',
         'seguidores':[], 'seguindo':[]}

def testaCriarUsuarioSemNome():
    with pytest.raises(Exception) as error:
        criar_usuario("")





