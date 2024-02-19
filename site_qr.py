# import qrcode
# import json
# from io import BytesIO
# from PIL import Image

# # Read the JSON file with site information
# with open("site_info.json", "r") as json_file:
#     site_info = json.load(json_file)

# # Define website URL
# url = site_info['url']

# # Create QR code instance and add URL data
# qr = qrcode.QRCode(version=1, box_size=10, border=5)
# qr.add_data(url)

# # Generate QR code image as binary data
# img = qr.make_image(fill_color="black", back_color="white")

# # Load company logo image and resize it
# logo = Image.open(site_info['logo'])
# logo_size = min(img.size) // 4
# logo_resized = logo.resize((logo_size, logo_size))

# # Paste logo onto center of QR code image
# qr_size = img.size
# logo_pos = ((qr_size[0] - logo_size) // 2, (qr_size[1] - logo_size) // 2)
# img.paste(logo_resized, logo_pos)

# # Save QR code with company logo as a JPEG image file
# buffer = Bytes

import qrcode
import json

# Read the JSON file with site information
with open("site_info.json", "r") as json_file:
    site_info = json.load(json_file)

# Define website URL
url = site_info['url']

# Create QR code instance and add URL data
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url)

# Generate QR code image as binary data
img = qr.make_image(fill_color="black", back_color="white")

# Save QR code as a JPEG image file
img.save("qr_code.jpg")
