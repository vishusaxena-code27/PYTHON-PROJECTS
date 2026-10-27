from PIL import Image
import pytesseract

# Open image
image = Image.open("image.png")

# Convert image to text
text = pytesseract.image_to_string(image)

# Display text
print("Text from Image:")
print(text)