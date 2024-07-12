import pyautogui
import pytesseract
from PIL import Image
import pyperclip

#zoom240
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Example: Capture a 400x300 region starting from (0, 0)
screenshot_region = pyautogui.screenshot(region=(50, 750, 1350, 90))
screenshot_region.save("screenshot_region.png")
# Open the color image
image_file = Image.open("screenshot_region.png")

# Convert the image to black and white (grayscale)
bw_image = image_file.convert("L")

# Save the black and white image
bw_image.save("bw_image.png")

# Load the screenshot image
screenshot = Image.open('bw_image.png')

# Extract text using OCR
extracted_text = pytesseract.image_to_string(screenshot)
stripped_text = extracted_text.replace(" ", "")
stripped_text = stripped_text.replace("0", "O")
stripped_text = stripped_text.replace("1", "l")


reversed_text = stripped_text[::-1]
print("Reversed text:")
print(reversed_text)
pyperclip.copy(reversed_text)

