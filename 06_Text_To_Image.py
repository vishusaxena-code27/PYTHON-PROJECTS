from PIL import Image, ImageDraw, ImageFont

# Get text from user
text = input("Enter the text: ")

# Create a blank image
image = Image.new("RGB", (800, 400), "white")

# Create drawing object
draw = ImageDraw.Draw(image)

# Use default font
font = ImageFont.load_default()

# Draw text on image
draw.text((50, 150), text, fill="black", font=font)

# Save the image
image.save("Text_To_Image.png")

print("\nText converted to image successfully!")
print("Saved as: Text_To_Image.png")