
import PyPDF2
import os
import time

cwd = os.getcwd()

print("Welcome to PDF Merger \n")
print("Hope the files to be merged are in the folder \n")
print("Starting to merge \n")
max_number_of_files = 5

merger = PyPDF2.PdfFileMerger()

folders = []

with open("folder-info.txt", "r") as f:
    for line in f.readlines():
        line = line.rstrip("\n")
        folders.append(line)

last = int(folders[-1])
last += 1

with open("folder-info.txt", "a") as f:
    if str(last) not in folders:
        f.write(str(last))
    else:
        raise Exception("Folder alredy exists please correct folder-info.txt")

for file in os.listdir("To-Merge"):
    if file.endswith(".pdf"):
        merger.append(f"To-Merge/{file}")

new_file_name = input("Enter New name for merged file (Without (.pdf)) ")
new_file_name += ".pdf"

os.chdir("Merged")
os.mkdir(str(last))
os.chdir(str(last))

merger.write(new_file_name)
print("Writing: \n")
time.sleep(2)
os.chdir(cwd)
print("Changing to home: \n")
print("Done: \n")


'''
# Python3 program to convert image to pdf
# using img2pdf library
 
# importing necessary libraries
import img2pdf
from PIL import Image
import os
 
# storing image path
img_path.resize((300, 300))
img_path.save(path)
img_path = ""
 
# storing pdf path
pdf_path = ""
 
# opening image
image = Image.open(img_path)
 
# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)
 
# opening or creating pdf file
file = open(pdf_path, "wb")
 
# writing pdf files with chunks
file.write(pdf_bytes)
 
# closing image file
image.close()
 
# closing pdf file
file.close()
 
# output
print("Successfully made pdf file")
'''
