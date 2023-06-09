import os
from moviepy.editor import *

# Function to convert GIF to MP4
def convert_gif_to_mp4(input_file, output_file):
    clip = VideoFileClip(input_file)
    clip.write_videofile(output_file, codec="libx264")
    clip.close()

# Directory containing the GIF files
directory = "/Users/guest/Desktop/kk"

# Iterate over files in the directory
for file_name in os.listdir(directory):
    if file_name.endswith(".gif"):
        # Get the full file path
        input_file = os.path.join(directory, file_name)
        
        # Create the output file name by replacing the extension
        output_file = os.path.splitext(input_file)[0] + ".mp4"

        # Convert the GIF to MP4
        convert_gif_to_mp4(input_file, output_file)

        print(f"Converted {file_name} to {os.path.basename(output_file)}")

        # Remove the old .gif file
        os.remove(input_file)

print("Conversion complete.")
