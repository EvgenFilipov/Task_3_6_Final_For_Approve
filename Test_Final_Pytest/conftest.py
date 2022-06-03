import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# В выводе на печать пишем по-русски, чтобы в отчете увидеть когда отрабатывает conftest с фикстурами

# добавляем опцию командной строки
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Вероятно ты отправил не тот 'язык'")
    print("\nПарсер отработал!")

# добавляем фикстуру для языка
@pytest.fixture
def language(request):
    return request.config.getoption("--language")
    print("\nбраузер в конфтесте отработал")

# добавляем фикстуру для двух браузеров
@pytest.fixture()
def browser(language):

    # получаем параметры для языка браузера
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    # убедимся что браузер готов
    print("\nбраузер готов")

    yield browser
    # этот код выполнится после завершения теста
    print("\nбраузер закрыт..")
    browser.quit()