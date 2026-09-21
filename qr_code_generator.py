import qrcode
data = input("Enter a URL or text: ")
qr = qrcode.make(data)
qr.save("my_qr_code.png")
print("QR Code generated successfully!")
print("Saved as my_qr_code.png")