import pytest

@pytest.fixture
def setUp():
    print('Launch browser')
    print('Login')
    print('Browse products')

def testAddItemtocart(setUp):
    print('Add item successful')

def testRemoveItemfromcart():
    print('Remove item successful')