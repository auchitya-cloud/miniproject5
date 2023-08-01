

# Step 1: Install necessary libraries for your quest!
# !sudo apt install tesseract-ocr
# !pip install pytesseract
# !pip install Pillow==9.0.0
# !pip install gTTS

import pytesseract
from PIL import Image
import pygame
import gtts

# Step 2: Discover the ancient riddle hidden in the image!
img = Image.open('quest_adventure_riddle.png')
print(img)

# Step 3: Unveil the secrets of the riddle using the power of Tesseract OCR!
result = pytesseract.image_to_string(Image.open('quest_adventure_riddle.png'))
print(result)

# Step 4: Decode the riddle to find the answer to your quest!
answer = "You are destined for greatness. Seek the hidden treasure deep in the enchanted forest."

# Step 5: Reveal the answer in the language of the realm!
tts = gtts.gTTS(answer)
tts.save("quest_adventure_answer.mp3")
