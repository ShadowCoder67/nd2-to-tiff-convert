# ND2 to TIFF Converter
Simple file converter from nd2 form to tiff. There is a bit of set up before using it. Will modify into web application for simplicity. 

## Prerequisites

Before running the script, make sure you have the following prerequisites installed:

1. Python: You can download Python from the official website: https://www.python.org/downloads/

2. Java: The script relies on the Bio-Formats library, which is a Java-based library. Make sure you have Java installed on your system.

3. Bio-Formats Library: Download the Bio-Formats library from the official website: https://www.openmicroscopy.org/bio-formats/downloads/ Make sure you have the correct version compatible with your Java installation.

4. Python Libraries: Install the required Python libraries using pip. The script relies on the following Python libraries:
   - `os`: Included in Python's standard library.
   - `subprocess`: Included in Python's standard library.
   - `google.oauth2.credentials`: You might need to install this if you want to access files from Google Drive using OAuth 2.0.
   - `google_auth_oauthlib.flow`: You might need to install this if you want to access files from Google Drive using OAuth 2.0.

## Usage

1. Place the ND2 files that you want to convert into a folder on your computer.

2. Create a separate folder on your computer where you want to save the converted TIFF files.

3. Open the `main.py` file and set the `input_dir` and `output_dir` variables to the paths of your input and output folders respectively.

4. Run the script using Python:

5. Make sure to edit directory depending on where the files are saved.


The script will convert all the ND2 files in the input folder to TIFF format and save them in the output folder.


## Troubleshooting

- If you encounter any errors related to Java heap space, you can increase the Java heap space allocated to the JVM. Modify the `command` variable in the `convert_to_tiff` function to include the `-Xmx` option with a larger value.

- 
This sets the maximum heap size to 2 GB. You can adjust the value according to your system's memory.

## Disclaimer

This script is provided as-is without any warranty. Use it at your own risk.

