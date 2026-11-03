from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 7a: Button Click
@when('I press the "{button}" button')
def step_press_button(context, button):
    element = context.driver.find_element(
        By.XPATH,
        f"//button[contains(text(), '{button}')]"
    )
    element.click()


# 7b: Verify text is present
@then('I should see "{name}" in the results')
def step_verify_text_present(context, name):
    results = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "search_results")
        )
    )
    assert name in results.text


# 7c: Verify text is NOT present
@then('I should not see "{name}" in the results')
def step_verify_text_absent(context, name):
    results = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "search_results")
        )
    )
    assert name not in results.text


# 7d: Verify message
@then('I should see the message "{message}"')
def step_verify_message(context, message):
    flash = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(
            (By.ID, "flash_message")
        )
    )
    assert message in flash.text
