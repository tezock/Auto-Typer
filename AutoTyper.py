"""
Autotyper for MonkeyType
"""

from pynput.keyboard import Key, Controller #Key Input
import time #Delays
import pyautogui #screenshots
# text recognition
import cv2
import pytesseract

keyboard = Controller()
time.sleep(5)
screenshot = pyautogui.screenshot(region=(450, 510, 950, 150))
screenshot.save("image.jpg")

def read_image(imageurl):
    img = cv2.imread(imageurl)
    config = ('-l eng --oem 1 --psm 3')

    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(img, config=config)
    text = text.split("\n")
    #text = "".join(text)
    return text

def type_message(insert_string):
    for row in insert_string:
        for char in row:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.05)
        keyboard.press(" ")
        keyboard.release(" ")

insert_string = read_image("image.jpg")
type_message(insert_string)
print("Last updated 11/2/2022")
#3/15/2022