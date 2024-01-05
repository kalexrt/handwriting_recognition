import os
import csv

def generate_csv(directory):
    images_directory = os.path.join(os.getcwd(), directory)
    output_csv = f"{directory}.csv"

    # Create the header in the CSV file
    with open(output_csv, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["FILENAME", "IDENTITY"])

    # Iterate over the images in the directory
    for image_path in os.listdir(images_directory):
        if image_path.endswith(".png"):
            # Get the filename without extension
            filename, _ = os.path.splitext(image_path)
            
            # Get the identity (remove trailing -1, -2, -3)
            identity = filename.rstrip('-1234567')

            # Append to the CSV file
            with open(output_csv, mode='a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([image_path, identity])

    print(f"CSV file generated successfully: {output_csv}")

# Generate CSV for "train", "test", and "validate" directories
generate_csv("train")
generate_csv("test")
generate_csv("validate")