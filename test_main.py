import sys
import os
import pytest

# GitHub Actions'ta main.py'yi bulması için dizini ekle
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from main import Polzovatel

def test_polzovatel_positive():
    user = Polzovatel(imya="Ахмет", vozrast=25)
    assert user.vozrast == 99

def test_polzovatel_negative():
    with pytest.raises(Exception):
        Polzovatel(imya="Мехмет", vozrast="двадцать")