from PIL import Image
import os

def augment_image(image_path, output_path):
    image = Image.open(image_path)
    # Example operations
    image = image.rotate(45)  # Rotate image by 45 degrees
    image.save(output_path)

# Loop through a dataset and augment