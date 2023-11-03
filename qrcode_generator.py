# This is Qr Code Generator, Input any text(text, url...)

import qrcode

def generate_qrcode(text):

    qr_code = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr_code.add_data(text)
    qr_code.make(fit = True)
    image = qr_code.make_image(fill_color = "black", back_color = "white")
    image.save("qr_image.png")


text_input = input("Please enter the text to be converted: ")
generate_qrcode(text_input)