from behave import when, then
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

@when('I click the "{button_text}" button')
def step_impl(context, button_text):
    """Click a button with the given text"""
    button = context.driver.find_element(By.XPATH, f"//button[text()='{button_text}']")
    button.click()

@then('I should see "{text}" in the "{field}" field')
def step_impl(context, text, field):
    """Verify that specific text is present in a field"""
    element = context.driver.find_element(By.NAME, field)
    assert element.get_attribute('value') == text, f"Expected {text} in {field}, but got {element.get_attribute('value')}"

@then('I should not see "{text}" in the product list')
def step_impl(context, text):
    """Verify that specific text is not present in the product list"""
    try:
        context.driver.find_element(By.XPATH, f"//*[contains(text(), '{text}')]")
        assert False, f"Found unexpected text '{text}' in the product list"
    except NoSuchElementException:
        pass

@then('I should see the message "{message}"')
def step_impl(context, message):
    """Verify that a specific message is present"""
    element = context.driver.find_element(By.ID, "message")
    assert message in element.text, f"Expected message '{message}', but got '{element.text}'"
