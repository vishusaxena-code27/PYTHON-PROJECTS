
# Import qrcode library
import qrcode

# Take input from the user
data = input("Enter Number to Make QR: ")

# Generate QR code
qr = qrcode.make(data)  # qrcode

# Save QR code image
qr.save("FirstQR_2026_MCA.png")  # pillow

# Display success message
print("QR Code Ban Gaya")
