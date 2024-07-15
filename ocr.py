import pyautogui
import pytesseract
from PIL import Image, ImageOps
import pyperclip

#zoom240
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Example: Capture a 400x300 region starting from (0, 0)
screenshot_image: Image = pyautogui.screenshot(region=(60, 780, 1450, 120))
# screenshot_region = pyautogui.screenshot(region=(50, 750, 1350, 90))

# Convert the image to black and white (grayscale)
bw_image: Image = screenshot_image.convert("L")

post_image: Image = ImageOps.posterize(bw_image, 2)

# Save the posterized image
post_image.save("post_image.png")

# Extract text using OCR
extracted_text = pytesseract.image_to_string(post_image)[::-1]
stripped_text = extracted_text.replace(" ", "")
stripped_text = stripped_text.replace("0", "O")
stripped_text = stripped_text.replace("1", "l")

print("Reversed text:")
print(stripped_text)
pyperclip.copy(stripped_text)
