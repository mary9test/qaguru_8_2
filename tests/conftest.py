import pytest
from selene import browser

@pytest.fixture()
def browser_management():
   browser.config.window_width = 1280
   browser.config.window_height = 720
   browser.open('https://google.com/')
   yield
   browser.quit()
