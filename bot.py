from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico, options=chrome_options)

try:
    #navegador.get("https://www.google.com")
    navegador.get("https://www.wikipedia.org/")
    
    campo_busca = navegador.find_element(By.NAME, "search")
    campo_busca.send_keys("Inteligencia Artificial")
    campo_busca.send_keys(Keys.ENTER)
    
    navegador.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)  # Aguarda a página carregar completamente
    
    #resultado = navegador.find_element((By.CSS_SELECTOR, 'span[data-value]')).get_attribute("data-value")
    
    #link_teste = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Aprendizado de máquina")))
    link_teste = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "A_forte_e_IA_fraca")))

    
    link_teste.click()
    
    time.sleep(4)  # Aguarda a página carregar completamente
    
except Exception as e:
    print(f"Ocorreu um erro: {e}")
#finally:
#    navegador.quit()