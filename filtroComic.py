import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('maye.jpg')

# Verificar si la imagen se cargó
if imagen is None:
    print("Error!! No se pudo cargar la imagen")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar desenfoque para suavizar
gris_suavizado = cv2.medianBlur(gris, 7)

# Detectar bordes con Canny (o alternativo: cv2.adaptiveThreshold)
bordes = cv2.adaptiveThreshold(gris_suavizado, 255,
                               cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, 9, 10)

# Aplicar efecto de pintura con menos colores (reducción de color)
imagen_bilateral = cv2.bilateralFilter(imagen, d=9, sigmaColor=250, sigmaSpace=250)

# Combinar la imagen reducida en color con los bordes
bordes_color = cv2.cvtColor(bordes, cv2.COLOR_GRAY2BGR)
comic = cv2.bitwise_and(imagen_bilateral, bordes_color)

# Agregar un texto indicando el filtro aplicado
cv2.putText(comic, 'Filtro: comic', (20, 40), cv2.FONT_ITALIC, 1.2, (255, 255, 0), 2)

# Mostrar las imágenes
cv2.imshow('Original', imagen)
cv2.imshow('Comic', comic)

# Guardar imagen
cv2.imwrite('Maye_comic.jpg', comic)
print("Su imagen fue guardada con éxito")

cv2.waitKey(0)
cv2.destroyAllWindows()
