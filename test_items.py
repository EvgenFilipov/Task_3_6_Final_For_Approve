import time

# Тест проверяет название кнопки Ajouter au panier,
# Команда запуска: pytest --language=fr test_items.py
def test_add_to_cart_button_from_language(browser):
    print("\nstart test_for_test")
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."

    browser.get(link)
    browser.implicitly_wait(10)

    searchTextOnTheButton = browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert "Ajouter au panier" in searchTextOnTheButton.text, "Текст на кнопке не соответствует ожиданиям!"

    time.sleep(30)




