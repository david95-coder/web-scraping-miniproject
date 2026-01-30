import requests
import bs4
import os
from pathlib import Path

resultado = requests.get("https://www.marca.com/")

sopa = bs4.BeautifulSoup(resultado.text, "lxml")

t = sopa.select(".main-header.site-header-cover img")

c= 0
for i in t:
    if c >=1:
        l = i["src"]
        imagen = requests.get(l)
        imagen = imagen.content

        ruta = Path("c:/Users/dguer/OneDrive/Escritorio/Master_Python/Python_Fede/Seccion 11/imagenes_furbo", "image"+str(c)).with_suffix(".jpg")
        image = open(ruta, "wb")
        image.write(imagen)
    c+=1

"""imagen_curso_1 = requests.get("https://objetos.estaticos-marca.com/assets/sports/logos/football/png/36x36/449.png")
imagen_curso_1 = imagen_curso_1.content

image = open(r"c:/Users/dguer/OneDrive/Escritorio/Master_Python/Python_Fede/Seccion 11/image.jpg", "wb")
image.write(imagen_curso_1)"""


"""lista_titulos = []

for i in t:
    lista_titulos.append(i.get_text())

for l in lista_titulos:
    if "Flick" in l:
        print(l)"""