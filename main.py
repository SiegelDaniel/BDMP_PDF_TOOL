import os
from PyPDF2 import PdfReader

def get_text_after_germany(text: str):
    # Find the index of "Germany" in the text
    germany_index = text.find("Germany")

    if germany_index != -1:
        # Extract the part of the text that comes after "Germany"
        after_germany = text[germany_index + len("Germany"):].strip()
        return after_germany
    else:
        return None
def read_first_two_lines(pdf_path):
    # Open the PDF file in binary mode
    with (open(pdf_path, 'rb') as pdf_file):
        # Create a PDF reader object
        pdf_reader = PdfReader(pdf_file)

        # Get the text from the first two lines
        first_line= get_text_after_germany(pdf_reader.pages[0].extract_text().split('\n')[0]).replace('"','')
        second_line = pdf_reader.pages[0].extract_text().split('\n')[1].strip()\
        .replace('"','')\
        .replace('1.4','')\
        .replace('2.04','')


    return first_line, second_line

import os

def rename_pdf_with_lines(pdf_path, new_name, counter=1):
    # Get the directory and extension of the original PDF file
    directory, filename = os.path.split(pdf_path)
    base_name, extension = os.path.splitext(filename)

    # Create the new file name with the first two lines
    if counter == 1:
        new_filename = f"{new_name}{extension}"
    else:
        new_filename = f"{new_name}({counter}){extension}"

    new_path = os.path.join(directory, new_filename)

    # Check if the new filename already exists
    while os.path.exists(new_path):
        counter += 1
        new_filename = f"{new_name}({counter}){extension}"
        new_path = os.path.join(directory, new_filename)

    # Rename the PDF file
    os.rename(pdf_path, new_path)

    print(f"File renamed to: {new_filename}")


if __name__ == "__main__":
    # Get the current directory and its subdirectories
    for root, dirs, files in os.walk(os.getcwd()):
        for filename in files:
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(root, filename)

                # Read the first two lines from the PDF file
                first_line, second_line = read_first_two_lines(pdf_path)

                # Create a new name for the file using the first two lines
                new_name = f"{first_line}_{second_line}"

                # Rename the PDF file
                rename_pdf_with_lines(pdf_path, new_name)
