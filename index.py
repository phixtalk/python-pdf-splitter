import os
from pikepdf import Pdf
import math

def get_pdf_page_mappings():
    total_pdf_pages = 39
    pages_per_pdf = 7

    total_pdf = math.ceil(total_pdf_pages / pages_per_pdf)

    file2pages = {}
    for num in range(0,total_pdf):
        file2pages[num] = [num*pages_per_pdf, (num+1)*pages_per_pdf]
    
    return file2pages


file2pages = get_pdf_page_mappings()
filename = 'my-document.pdf'
pdf = Pdf.open(f"data/{filename}")

# make the new splitted PDF files
new_pdf_files = [ Pdf.new() for i in file2pages ]

# the current pdf file index
new_pdf_index = 0

# iterate over all PDF pages
for n, page in enumerate(pdf.pages):
    if n in list(range(*file2pages[new_pdf_index])):
        # add the `n` page to the `new_pdf_index` file
        new_pdf_files[new_pdf_index].pages.append(page)
        print(f"[*] Assigning Page {n} to the file {new_pdf_index}")
    else:
        # make a unique filename based on original file name plus the index
        name, ext = os.path.splitext(filename)
        output_filename = f"splitted/{name}-{new_pdf_index}.pdf"
        # save the PDF file
        new_pdf_files[new_pdf_index].save(output_filename)
        print(f"[+] File: {output_filename} saved.")
        # go to the next file
        new_pdf_index += 1
        # add the `n` page to the `new_pdf_index` file
        new_pdf_files[new_pdf_index].pages.append(page)
        print(f"[*] Assigning Page {n} to the file {new_pdf_index}")

# save the last PDF file
name, ext = os.path.splitext(filename)
output_filename = f"splitted/{name}-{new_pdf_index}.pdf"
new_pdf_files[new_pdf_index].save(output_filename)
print(f"[+] File: {output_filename} saved.")