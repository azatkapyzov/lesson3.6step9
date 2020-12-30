def test_items_add_to_basket_button(browser):
	browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
	button = browser.find_element_by_css_selector("button.btn-add-to-basket")
	assert button, "No button Add_to_basket"