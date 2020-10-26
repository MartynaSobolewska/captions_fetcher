from selenium import webdriver
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import docx


# data from user
file_path = ""
document_name = ""
generate_definitions_table = False
panopto_link = ""


def get_data_from_user():
    global file_path, document_name, generate_definitions_table, panopto_link
    validate = URLValidator()
    doc = docx.Document()

    link_is_valid = False
    while not link_is_valid:
        panopto_link = input("Please paste link to the Panopto video: ")
        try:
            validate(panopto_link)
            if panopto_link.__contains__("panopto.eu")
                link_is_valid = True
        except ValidationError:
            print("Incorrect link.")

    document_can_be_created = False
    while not document_can_be_created:
        document_name = input("Please enter the name of the word file you wish to create: ")
        file_path = input("...and directory path (where you want to create it): ")
        print(file_path + "\\" + document_name)
        try:
            doc.add_heading(document_name, 0)
            doc.save(file_path + "\\" + document_name + ".docx")
            document_can_be_created = True
        except:
            print("incorrect path or file name.")


get_data_from_user()

# selenium setup
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)  # PATH is location of chrome web driver needed to use selenium
driver.get(panopto_link)

