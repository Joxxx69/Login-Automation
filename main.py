from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.facebook.com")

try:
    email_field = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "email")))
    email_field.send_keys("santiago@ejemplo.com")

    password_field = driver.find_element(By.ID, "pass")
    password_field.send_keys("contrasenaa")
    
    password_field.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Facebook']"))
    )
    
    print("Login exitoso")
    
    time.sleep(5)
    
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    driver.quit()