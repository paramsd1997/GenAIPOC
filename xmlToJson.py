from google.colab import drive
import xml.etree.ElementTree as ET
import os
import json
import bleach


# Remount Google Drive
drive.mount("/content/drive", force_remount=True)


# Specify the allowed tags for bleach (empty list means all tags will be stripped)
allowed_tags = []


def process_xml_files(directory_path):
    """Recursively processes XML files in the given directory and its subdirectories."""
    for current_root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if file_name.endswith('.xml'):
                file_path = os.path.join(current_root, file_name)


                # Extract filename without extension automatically
                file_name_no_extension = os.path.splitext(file_name)[0]


                data = {f"{file_name_no_extension}": []}


                def extract_text(element):
                    """Recursively extracts text from the XML tree."""
                    if element.text:
                        # Remove extra spaces and newlines
                        text = ' '.join(element.text.strip().split())
                        if text:
                            # Use bleach to clean HTML and CSS tags
                            cleaned_text = bleach.clean(text, tags=allowed_tags, strip=True)
                            data[f"{file_name_no_extension}"].append(cleaned_text)
                    for child in element:
                        extract_text(child)


                try:
                    tree = ET.parse(file_path)
                    root = tree.getroot()
                    extract_text(root)
                    # Convert data to JSON without escaping UTF-8 characters
                    json_data = json.dumps(data, indent=4, ensure_ascii=False)


                    # Save JSON data to a file with the extracted filename without extension
                    json_file_path = os.path.join(current_root, f"{file_name_no_extension}.json")
                    with open(json_file_path, 'w',  encoding='utf8') as json_file:
                        json_file.write(json_data)


                    print(f"JSON file '{json_file_path}' created successfully.")
                except ET.ParseError:
                    print(f"XML parsing error for file '{file_path}'. Please check if the XML file is well-formed.")


# Specify the main directory path in Google Drive
main_directory_path = '/content/drive/MyDrive/GenAI_Translation_Platform'


# Process XML files in the main directory and its subdirectories
process_xml_files(main_directory_path)


