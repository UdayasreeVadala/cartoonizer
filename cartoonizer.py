import cv2


def cartoonizer(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray,9,75,75)
    edge = cv2.adaptiveThreshold(blur,255 ,cv2.ADAPTIVE_THRESH_MEAN_C ,cv2.THRESH_BINARY ,5 ,5)
    output = cv2.bitwise_and(image ,image ,mask=edge)
    cv2.imshow('image' , output)
    cv2.waitKey(1)


image = cv2.imread(r"C:\\Users\\Udayasree\\Downloads\\Radha_Krishna.jpg")
cartoonizer(image)
