import os
import subprocess

def convert_to_tiff(nd2_file, output_dir):
    output_file = os.path.join(output_dir, os.path.basename(nd2_file).replace(".nd2", ".tif"))

    bfconvert_path = "/Users/sritejpadmanabhan/Downloads/bioformats_package.jar"

    print(f"Converting {nd2_file} to TIFF...")
    command = f'java -Xmx8192m -jar "{bfconvert_path}" "{nd2_file}" "{output_file}"'
    subprocess.run(command, shell=True)
    print("Conversion complete.")

def main():
    input_dir = "/Users/sritejpadmanabhan/Desktop/nd2 files"
    output_dir = "/Users/sritejpadmanabhan/Desktop/tiff files"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    nd2_files = [file for file in os.listdir(input_dir) if file.lower().endswith(".nd2")]

    for nd2_file in nd2_files:
        nd2_file_path = os.path.join(input_dir, nd2_file)
        convert_to_tiff(nd2_file_path, output_dir)

if __name__ == "__main__":
    main()
