import qrcode
from PIL import Image

# Data to be stored in the QR code
data = input("Enter the text or URL: ")

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

# Generate coloured QR code
qr_image = qr.make_image(
    fill_color="blue",
    back_color="white"
)

# Save the QR code
qr_image.save("Coloured_QR_Code.png")

print("Coloured QR code generated successfully!")
print("Saved as: Coloured_QR_Code.png")