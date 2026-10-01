import cv2 # type: ignore
import numpy as np

# vision artificial ACT 10 NC = 0105
# Lee la imagen en escala de grises
img = cv2.imread("fortnite.jpg", cv2.IMREAD_GRAYSCALE)

# Abre la ventana con la imagen
if img is not None:
    cv2.imshow("fortnite.jpg", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No se pudo encontrar fortnite.jpg")

#Line
print("la linea 0105")

# Crea una imagen negra
img = np.zeros((512,512,3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)

# Abre la ventana con la imagen
cv2.imshow("LA line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("el circulo 0105")

# Dibuja un circulo azul de radio 10px al centro de la imagen
img = cv2.circle(img, (260,260), 10, (255,0,0),-1)

# Abre la ventana con la imagen
cv2.imshow("el circulo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("el texto 0105")

# Añade a la imagen el texto "Example Text" en color blanco
img = cv2.putText(img, "Iker Montoya", (200, 30),
                  cv2.FONT_HERSHEY_SIMPLEX,
                  0.5, (255, 255, 255), 2)

# Abre la ventana con la imagen
cv2.imshow("el circulo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("los Trackbars 0105")

r = 0
g = 0
b = 0

def cambiar_r(val):
    global r
    r = val

def cambiar_g(val):
    global g
    g = val

def cambiar_b(val):
    global b
    b = val

# Crea a una imagen negra, y una ventana llamada 'frame'
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('frame')

# Crea tres trackbar en frame
cv2.createTrackbar('R','frame',0,255,cambiar_r)
cv2.createTrackbar('G','frame',0,255,cambiar_g)
cv2.createTrackbar('B','frame',0,255,cambiar_b)

# Muestra una sola ventana
cv2.imshow('frame',img)

# Espera 3 segundos
cv2.waitKey(3000)

cv2.destroyAllWindows()

print("el Thresholding 0105")

img = cv2.imread('fortnite.jpg',0)

if img is not None:

    ret,thr1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    ret,thr2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    ret,thr3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    ret,thr4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
    ret,thr5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

    cv2.imshow('BINARY',thr1)
    cv2.imshow('BINARY_INV',thr2)
    cv2.imshow('TRUNC',thr3)
    cv2.imshow('TOZERO',thr4)
    cv2.imshow('TOZERO_INV',thr5)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("No se pudo encontrar fortnite.jpg")

print("Iker Montoya NC = 0105")







