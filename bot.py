from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

try:
    navegador.get("https://www.google.com")
    campo_busca = navegador.find_element(By.NAME, "q")
    campo_busca.send_keys("qual a temperatura de hoje em São Paulo")
    campo_busca.send_keys(Keys.ENTER)
    time.sleep(5000)  # Aguarda a página carregar completamente
    resultado = navegador.find_element((By.CSS_SELECTOR, 'span[data-value]')).get_attribute("data-value")
    print(f"O bot encontrou o valor: {resultado}")
    
except Exception as e:
    print(f"Ocorreu um erro: {e}")
finally:
    navegador.quit()