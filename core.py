import os
import shutil

import cv2
from pdf2image import convert_from_path
from pyzbar import pyzbar


class Core:

    def __init__(self, files_folder_path, delete_files=True):
        self.delete_files = delete_files
        if os.path.isdir(files_folder_path):
            shutil.rmtree(files_folder_path)
        os.mkdir(files_folder_path)

    def extract_barcode_from_image(self, image_path):
        # load the input image
        image = cv2.imread(image_path)

        # find the barcodes in the image and decode each of the barcodes
        barcodes = pyzbar.decode(image)

        barcode_results = []

        for barcode in barcodes:
            # extract the bounding box location of the barcode and draw the
            # bounding box surrounding the barcode on the image
            (x, y, w, h) = barcode.rect
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # the barcode data is a bytes object so if we want to draw it on
            # our output image we need to convert it to a string first
            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type

            # draw the barcode data and barcode type on the image
            text = "{} ({})".format(barcode_data, barcode_type)
            cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 255), 2)

            # print the barcode type and data to the terminal
            print("[INFO] Found {} barcode: {}".format(barcode_type, barcode_data))
            barcode_results.append([barcode_type, barcode_data])

        if self.delete_files:
            os.remove(image_path)

        return barcode_results

    @staticmethod
    def pdf_pages_to_jpg_images(pdf_path):
        # Store all the pages of the PDF in a variable
        pages = convert_from_path(pdf_path, 500)

        # Counter to store images of each page of PDF to image
        image_counter = 1

        # Iterate through all the pages stored above
        pages_jpg = []
        for page in pages:
            # Declaring filename for each page of PDF as JPG
            # For each page, filename will be:
            # PDF page 1 -> page_1.jpg
            # PDF page 2 -> page_2.jpg
            # PDF page 3 -> page_3.jpg
            # ....
            # PDF page n -> page_n.jpg
            filename = "files/page_" + str(image_counter) + ".jpg"

            # Save the image of the page in system
            page.save(filename, 'JPEG')

            # Increment the counter to update filename
            image_counter = image_counter + 1

            pages_jpg.append(filename)

        return pages_jpg

    def extract_barcode_from_pdf(self, pdf_path):
        image_files = self.pdf_pages_to_jpg_images(pdf_path)
        barcodes = []
        for image in image_files:
            barcodes.append([barcode for barcode in self.extract_barcode_from_image(image)])
        return barcodes
