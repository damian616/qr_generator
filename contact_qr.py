import qrcode
import json
from io import BytesIO
from PIL import Image

# Read the JSON file with contact information
with open("contact_info.json", "r") as json_file:
    contact_info = json.load(json_file)

# Create vCard object
vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{contact_info['name']}\nORG:{contact_info['company']}\nTEL:{contact_info['phone']}\nEMAIL:{contact_info['email']}\nURL:{contact_info['website']}\nNOTE:{contact_info['note']}\nEND:VCARD"

# Create QR code instance and add vCard data
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(vcard)

# Generate QR code image as binary data
img = qr.make_image(fill_color="black", back_color="white")
buffer = BytesIO()
img.save(buffer, format='PNG')

# Convert image to PIL Image object
pil_img = Image.open(buffer)

# Save QR code as a JPEG image file
pil_img.save("contact_qr_code.jpg")

