import importlib

dupka = importlib.import_module("..").dupka


def test_aa():
    dupka()
    assert 1 == 1
