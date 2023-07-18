from tags import *
from bs4 import BeautifulSoup
import requests
import os 

def print_to_console():
    url_input = input("What URL do you want to scrape? ")
    url = f"{url_input}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    tags = input(f"What tags do you want to scrape? "+ " | ".join(tag_list) + " ")
    while True:
        if tags not in tag_list:
            print("Tag not supported.")
            tags = input(f"What tags do you want to scrape? "+ " | ".join(tag_list) + " ")
            continue
        for tag in tag_list:
            if tag == tags:
                printags(tags, soup)
        break

def printags(tag, soup):
    data = soup.find_all(f"{tag}")
    if tag == "anker":
        for link in data:
            print(link["href"])
    else:
        for thing in data:
            print(thing)

def create_writing_boilerplate():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "data.txt")
    open(file_path, "a").close()

    url_input = input("What URL do you want to scrape? ")
    url = f"{url_input}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    tags = input(f"What tags do you want to scrape? "+ " | ".join(tag_list) + " ")

    return file_path, url, soup, tags

def overwrite_file():
    file_path, url, soup, tags = create_writing_boilerplate()

    data = soup.find_all(f"{tags}")
    
    try:
        with open(file_path, "w") as file_data:
            file_data.write(f"{tags} in {url}: \n")
            file_data.write(str(data))
    except UnicodeEncodeError:
        print("ERROR: charset of website is not supported.")
    else:
        data = soup.find_all(f"{tags}")
        with open(file_path, "w") as file_data:
            file_data.write(f"{tags} in {url}: \n")
            file_data.write(str(data))
        print("Succesfully added to file.")

def add_to_file():
    file_path, url, soup, tags = create_writing_boilerplate()

    data = soup.find_all(f"{tags}")
    
    try:
        data = soup.find_all(f"{tags}")
        with open(file_path, "w") as file_data:
            file_data.write(f"{tags} in {url}: \n")
            file_data.write(str(data))
    except UnicodeEncodeError:
        print("ERROR: charset of website is not supported.")
    else:
        data = soup.find_all(f"{tags}")
        with open(file_path, "w") as file_data:
            file_data.write(f"{tags} in {url}: \n")
            file_data.write(str(data))
        print("Succesfully added to file.")

while True:
    write_print = input("Do you want to print the data or write it to a file? write/print: ").lower()
    if write_print == "print":
        print_to_console()
        again = input("Do you want to scrape a another tag? Y/N ").upper()
        if again == "Y":
            print()
            continue
        else:
            break
    elif write_print == "write":
        overwrite_add = input("Do you want to overwrite or add to the file? overwrite/add: ").lower()
        if overwrite_add == "overwrite":
            overwrite_file()
            again = input("Do you want to scrape a another tag? Y/N ").upper()
            if again == "Y":
                print()
                continue
            else:
                break
        elif overwrite_add == "add":
            add_to_file()
            again = input("Do you want to scrape a another tag? Y/N ").upper()
            if again == "Y":
                print()
                continue
            else:
                break
    else:
        print("Wrong input.")
        continue