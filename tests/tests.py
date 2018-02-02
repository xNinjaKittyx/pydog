
import pydog
import pytest

dog = pydog.PyDog()

def test_pydog_get_all_dogs():
    assert dog.get_all_dogs()

def test_pydog_get_random_image():
    assert dog.get_random_image()
    assert dog.get_random_image(breed_name='affenpinscher')
    assert dog.get_random_image(breed_name='spaniel', sub_breed_name='japanese')
    try:
        dog.get_random_image(sub_breed_name='lol')
        assert False
    except Exception:
        assert True

def test_pydog_get_all_breeds():
    assert dog.get_all_breeds()

def test_pydog_get_breed_images():
    assert dog.get_breed_images('affenpinscher')

def test_pydog_get_all_subbreeds():
    assert dog.get_all_subbreeds('spaniel')

def test_pydog_get_subbreed_image():
    assert dog.get_subbreed_image('spaniel', 'japanese')
