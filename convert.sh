#!/bin/bash

# Specify the folder containing the JPEG files
image_folder="downloaded_images"

# Specify the output PDF file
pdf_output="output.pdf"

# Use a loop to sort and create PDF
for ((i=1; i<=225; i++)); do
    image_file="${image_folder}/page_${i}.jpg"
    [ -f "$image_file" ] && image_files+=("$image_file")
done

# Use img2pdf to create PDF from sorted JPEG files
img2pdf "${image_files[@]}" -o "$pdf_output"

echo "PDF created successfully at $pdf_output"
