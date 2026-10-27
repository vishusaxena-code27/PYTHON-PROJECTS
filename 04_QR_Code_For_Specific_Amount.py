import qrcode

# UPI details
upi_id = input("Enter UPI ID: ")
name = input("Enter your name: ")
amount = input("Enter specific amount (INR): ")

# Create UPI payment URL with specific amount
upi_url = (
    f"upi://pay?pa={upi_id}"
    f"&pn={name}"
    f"&am={amount}"
    f"&cu=INR"
)

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(upi_url)
qr.make(fit=True)

# Create QR image
qr_image = qr.make_image(
    fill_color="black",
    back_color="white"
)

# Save QR code
qr_image.save("Specific_Amount_QR_Code.png")

print("\nQR code for specific amount generated successfully!")
print("Amount: ₹" + amount)
print("Saved as: Specific_Amount_QR_Code.png")