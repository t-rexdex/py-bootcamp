import pytest

def testLogin():
    print('Login Successful')

@pytest.mark.other
def testLogoff():
    print('Logoff Successful')

@pytest.mark.other
def testCalculation():
    assert 2+2 == 4 

