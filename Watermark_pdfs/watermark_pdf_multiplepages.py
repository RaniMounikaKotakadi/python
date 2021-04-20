# !/usr/bin/python
# Adding a watermark to a multi-page PDF
import os
from pdfrw import PdfReader, PdfWriter, PageMerge

input_file_name = "input.pdf"
output_file_name = "output.pdf"
watermark_file_name = "watermark.pdf"

# define the reader and writer objects
input_file = PdfReader(input_file_name)
watermark_file = PdfReader(watermark_file_name)
watermark_page = watermark_file.pages[0]

# go through the pages one after the next
for current_page in range(len(input_file.pages)):
    current_merge_page = PageMerge(input_file.pages[current_page])
    current_merge_page.add(watermark_page).render()

# write the modified content to disk
output_file = PdfWriter()
output_file.write(output_file_name, input_file)