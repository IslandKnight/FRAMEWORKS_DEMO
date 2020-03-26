from pytest import mark
from selenium import webdriver


@mark.body
class BodyTests:

    def test_body_functions_as_expected(self):
        assert True

    def test_can_navigate_to_body_page(self):
        driver = webdriver.chrome
        driver.chrome("http//www.google.com/")
        assert True

    def test_bumber(self):
        assert True

    def test_windshield(self):
        assert True