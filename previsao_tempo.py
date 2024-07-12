from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
arguments = ['--lang=pt-BR', '--window-size=500,500', '--incognito']
for argument in arguments:
    chrome_options.add_argument(argument)

# Tente instalar o ChromeDriver e iniciar o Chrome com as opções especificadas
try:
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
except Exception as e:
    print(f"Erro ao iniciar o WebDriver: {e}")
    driver = None

# Verifique se o driver foi inicializado corretamente
if driver:
    try:
        driver.get('https://weather.com/pt-BR/clima/10dias/l/Americana+S%C3%A3o+Paulo?canonicalCityId=5a0c3a2046b018c37a7c39bdb0d25213d7d5b39f5b9ae8125283dcaf9e1b237c')
        input('Aperte uma tecla para fechar')
    except Exception as e:
        print(f"Erro ao acessar a URL: {e}")
    finally:
        driver.quit()
else:
    print("O driver não foi inicializado corretamente.")
