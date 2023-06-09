# Video-Automation-Scripts
## 1. Video Silence Removal
## 2. .gif 2 .mp4

## GIF to MP4 Converter

This Python script converts all the .gif files in a specified directory to .mp4 files using the `moviepy` library.

### Prerequisites

- Python 3.x
- `moviepy` library

### Installation

1. Clone this repository or download the script directly.
2. Install the required dependencies by running the following command:

### Usage

1. Place your .gif files in the desired directory.
2. Update the `directory` variable in the script to point to the directory containing your .gif files.
3. Run the script using the following command:

The script will convert each .gif file to an .mp4 file using the `libx264` codec and save it in the same directory.
The original .gif files will be removed after successful conversion.

## Video Silence Removal

This Python script removes silence from videos by extracting non-silent sections and creating a modified video with proper audio.

### Requirements

- Python 3.x
- Install the required dependencies using the following command:
pip install moviepy pydub joblib tqdm

python
Copy code

### Usage

1. Clone the repository or download the `video_silence_removal.py` script.

2. Import the required libraries

## Customization

Adjust the decibel_threshold variable to set the threshold for silence detection. Lower values indicate quieter sounds will be considered as silence.
Modify the min_section_duration variable to specify the minimum duration (in milliseconds) for a non-silent section to be included in the output.
Change the margin_duration variable to add extra time (in milliseconds) before and after each non-silent section for smoother transitions.
Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
