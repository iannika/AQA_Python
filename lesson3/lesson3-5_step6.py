import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.xfail(strict=True)
def test_succed():
    assert True

@pytest.mark.xfail
def test_no_succed():
    assert False

@pytest.mark.skip
def test_skipped():
    assert False
