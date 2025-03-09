import pyqrcode

text = input("Enter text to generate QR: ")

qr_code = pyqrcode.create(text)

qr_code.svg(
    "qr_code.svg", title="My QR", scale=8, module_color="#fff", background="#333"
)
