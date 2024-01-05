import os
import cairosvg


def convert_svg_folder_to_jpg(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".svg"):
            # Generate full file paths
            svg_file_path = os.path.join(input_folder, filename)
            jpg_file_path = os.path.join(
                output_folder, os.path.splitext(filename)[0] + ".jpg"
            )

            # Convert SVG to JPG with a white background
            convert_svg_to_jpg(svg_file_path, jpg_file_path)


def convert_svg_to_jpg(svg_file, jpg_file):
    # Convert SVG to PNG using cairosvg with a white background
    cairosvg.svg2png(
        url=svg_file,
        write_to=jpg_file,
        output_width=224,
        output_height=224,
        parent_width=1000,
        parent_height=1000,
    )


if __name__ == "__main__":
    input_folder_path = "C:/Users/Kalash2/Downloads/svgs"  # Change this to the path of your input SVG folder
    # Change this to the desired output JPG folder path
    output_folder_path = "C:/Users/Kalash2/Downloads/jpg_out"

    convert_svg_folder_to_jpg(input_folder_path, output_folder_path)
