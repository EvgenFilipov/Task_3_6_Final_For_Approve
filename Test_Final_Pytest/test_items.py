import time
def test_vsyakoy_schlyapi(browser):
    print("\nstart test_for_test")
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."

    browser.get(link)
    browser.implicitly_wait(10)

    searchTextOnTheButton = browser.find_element_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert "Añadir al carrito" in searchTextOnTheButton.text, "Текст на кнопке не соответствует ожиданиям!"

    time.sleep(5)




