import qrcode
#Generate QR Code

def generate_qr_code():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )   
    qr.add_data("https://abhijithchandradas.medium.com/")
    qr.make(fit=True)
    img = qr.make_image(fill_color="red", back_color="black")
    img.save("medium.png")