import qrcode
from colorama import Fore, Style

def generate_qr_code(link, name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image()
    img.save(f'qr_code\\{ name }.png')

link = input(Fore.RED + 'Enter link or text: ')
name = input(Fore.BLUE + 'Enter your output file: ')

generate_qr_code(link, name)
print(Fore.GREEN + f'QR code saved as { name }.png')
print(Style.RESET_ALL, end='')
