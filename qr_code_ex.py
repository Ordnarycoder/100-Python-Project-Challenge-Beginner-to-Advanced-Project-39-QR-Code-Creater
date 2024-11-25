import qrcode

# Initialize the QR Code object
qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

# Get the data to encode in the QR Code
data = input("Please enter the text or URL you want to make a QR code for: ")

# Check if the data is a string
if not isinstance(data, str):
    print("Please provide a valid string!")
else:
    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the QR Code image with custom colors
    qr_img = qr.make_image(fill_color="blue", back_color="white")

    # Save the QR Code image to a file
    qr_img.save("qr_github.png")
    print("QR Code has been saved as 'qr_github.png'.")
