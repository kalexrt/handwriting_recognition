import os
import pyvips

def convert_svg_to_jpg(input_folder, output_folder):
    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through SVG files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".svg"):
            svg_path = os.path.join(input_folder, filename)

            # Create output file path with the same name but different extension
            output_filename = os.path.splitext(filename)[0] + ".jpg"
            jpg_path = os.path.join(output_folder, output_filename)

            # Convert SVG to JPG using pyvips
            image = pyvips.Image.svgload(svg_path, dpi=300)
            image.write_to_file(jpg_path, Q=90)

            print(f"Converted: {filename} to {output_filename}")

if __name__ == "__main__":
    # Specify input and output folders
    input_folder = "C:/Users/Kalash2/Downloads/svgs"
    output_folder = "C:/Users/Kalash2/Downloads/jpg_out"

    # Set target dimensions
    target_dimensions = (224, 224)

    convert_svg_to_jpg(input_folder, output_folder)