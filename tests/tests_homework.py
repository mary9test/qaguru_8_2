from selene import be, have
from selene.support.shared import browser


def test_search_google(browser_management):
   browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
   browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser ...'))

def test_search_not_found(browser_management):
   browser.element('[name="q"]').should(be.blank).type('0000000jjfdss').press_enter()
   browser.element('#result-stats').should(have.text('Результатов: примерно 0'))