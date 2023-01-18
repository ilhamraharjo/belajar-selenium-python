import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginRegister(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_Failed_Register_with_empty_email(self): 
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"name_register").send_keys("admin") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("") # isi email
        time.sleep(1)
         driver.find_element(By.ID,"password_register").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signup_register").click()

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')

    def test_Success_Register(self): 
        driver = self.driver
        driver.get("http://barru.pythonanywhere.com/daftar") # buka situs
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"name_register").send_keys("admin") # isi username
        time.sleep(1)
        driver.find_element(By.ID,"email_register").send_keys("admin@gmail.com") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password_register").send_keys("admin123") # isi password
        time.sleep(1)
        driver.find_element(By.ID,"signup_register").click()

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')


unittest.main()