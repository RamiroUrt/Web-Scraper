
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import json

# Configura el servicio de Selenium (ajusta el path al chromedriver)
service = #Service(r"C:.../chromedriver.exe")  # Cambia esto por la ruta de tu chromedriver
driver = webdriver.Chrome(service=service)

# URL del sitio web
url = #"URL_PARA_CHUSMEAR"
driver.get(url)

# Esperar que la página cargue
time.sleep(3)

all_products = []

try:
    while True:
        # Obtener el HTML actual
        soup = BeautifulSoup(driver.page_source, "html.parser")
        cards = soup.find_all("div", {"class": "products-feed__product-wrapper"})
        
        # Extraer productos de la página actual
        for card in cards:
            title = card.find("h3", {"class": "products-feed__product-name"}).text.strip() #cambiar atributo a inspeccionar "h3" // class o id 
            price = card.find("p", {"class": "products-feed__product-price"}).text.strip() #cambiar atributo a inspeccionar "h3" // class o id 
            image = card.find("img", {"class": "products-feed__product-image"}).get("src") #cambiar atributo a inspeccionar "h3" // class o id 
            all_products.append({
                "title": title,
                "price": price,
                "image": image
            })
            print(title)
            print(price)
            print(image)
            print("------------")
        
        # Intentar encontrar el botón de paginación
        try:
            load_more_button = driver.find_element(By.ID, "products_feed-btn") #cambiar atributo a inspeccionar "h3" // class o id 
            if "display: none" in load_more_button.get_attribute("style"):
                print("No hay más páginas.")
                break
            load_more_button.click()
            time.sleep(2)  # Esperar que se cargue el contenido
        except Exception as e:
            print("Error al encontrar o hacer clic en el botón:", e)
            break

finally:
    driver.quit()

# Guardar los productos en un archivo JSON
with open("productos.json", "w", encoding="utf-8") as file:
    json.dump(all_products, file, ensure_ascii=False, indent=4)

print("Total de productos:", len(all_products))
print("Los datos se han guardado en 'productos.json'.")



