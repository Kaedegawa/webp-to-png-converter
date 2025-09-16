import os
from PIL import Image


input_folder = os.path.join(os.path.dirname(__file__), "input")
output_folder = os.path.join(os.path.dirname(__file__), "output")


os.makedirs(output_folder, exist_ok=True)


for filename in os.listdir(input_folder):
    if filename.lower().endswith(".webp"):
        webp_path = os.path.join(input_folder, filename)

        
        with Image.open(webp_path) as img:
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(output_folder, png_filename)
            img.save(png_path, "PNG")

        print(f"Converted: {filename} -> {png_filename}")

print("All conversions complete")