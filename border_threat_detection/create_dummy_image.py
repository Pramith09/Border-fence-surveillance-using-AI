from PIL import Image
import os

# Ensure the assets directory exists
os.makedirs('assets', exist_ok=True)

# Create a blank image (640x480) with a background color
img = Image.new('RGB', (640, 480), color=(73, 109, 137))

# Save the image in the assets folder
img_path = 'assets/border_intrusion1.jpg'
img.save(img_path)

print(f"Dummy image created at {img_path}")
