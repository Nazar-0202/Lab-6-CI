import pytest
from main import Polzovatel

def test_polzovatel_positive():
    user = Polzovatel(imya="Ахмет", vozrast=25)
    assert user.vozrast == 25

def test_polzovatel_negative():
    with pytest.raises(Exception):
        Polzovatel(imya="Мехмет", vozrast="двадцать")