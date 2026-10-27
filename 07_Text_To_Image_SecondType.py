from PIL import Image, ImageDraw, ImageFont

# Create a blank image
image = Image.new("RGB", (800, 400), "white")

# Create drawing object
draw = ImageDraw.Draw(image)

# Load font
font = ImageFont.truetype("arial.ttf", 40)

# Text
text = input("Enter text: ")

# Find text position
position = (200, 170)

# Draw text on image
draw.text(position, text, fill="black", font=font)

# Save image
image.save("Text_To_Image_2.png")

print("Image created successfully!")
print("Saved as: Text_To_Image_2.png")