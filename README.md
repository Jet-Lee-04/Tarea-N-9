# Filtro Cómic con OpenCV

Este proyecto aplica un filtro de estilo cómic a una imagen utilizando OpenCV y Python, creando un efecto artístico que simula un dibujo animado.

## Descripción

El programa toma una imagen de entrada y la transforma aplicando técnicas de procesamiento de imágenes para crear un efecto similar a un cómic o dibujo animado. El resultado combina:
- Reducción de colores para un aspecto más plano
- Detección y resaltado de bordes
- Suavizado de la imagen para eliminar detalles innecesarios

## Requisitos

```bash
pip install opencv-python numpy
```

## Uso

1. Coloca tu imagen en el directorio del proyecto con el nombre `maye.jpg`
2. Ejecuta el proyecto.

## Funcionamiento

### Proceso paso a paso:

1. **Carga de imagen**: Lee la imagen `maye.jpg` del directorio actual
2. **Conversión a escala de grises**: Convierte la imagen a escala de grises para el procesamiento de bordes
3. **Suavizado**: Aplica un filtro mediano para reducir el ruido
4. **Detección de bordes**: Utiliza threshold adaptativo para crear líneas definidas
5. **Reducción de colores**: Aplica filtro bilateral para suavizar colores manteniendo bordes
6. **Combinación**: Fusiona la imagen con colores reducidos y los bordes detectados
7. **Texto decorativo**: Añade etiqueta "Filtro: comic" a la imagen final

### Parámetros clave:

- `medianBlur(7)`: Suavizado con kernel de 7x7 píxeles
- `adaptiveThreshold`: Detección de bordes adaptativa
- `bilateralFilter(d=9, sigmaColor=250, sigmaSpace=250)`: Reducción de colores preservando bordes

## Resultados

- **Ventana "Original"**: Muestra la imagen original
- **Ventana "Comic"**: Muestra el resultado con efecto cómic
- **Archivo guardado**: `Maye_comic.jpg` en el directorio del proyecto

## Personalización

Para adaptar el filtro a diferentes imágenes, puedes ajustar:
- Tamaño del kernel del filtro mediano (línea del `medianBlur`)
- Parámetros del threshold adaptativo
- Valores del filtro bilateral para mayor o menor reducción de color

## Notas

- La imagen debe llamarse exactamente `maye.jpg`
- El programa verifica que la imagen se cargue correctamente antes de proceder
- Presiona cualquier tecla para cerrar las ventanas de visualización
