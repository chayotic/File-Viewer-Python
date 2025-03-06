#ViewMate File Reader
#supports txt,lrc,csv,dat,py,html,css,json,log
import termcolor
from termcolor import colored
import os
import pickle
import csv
import bs4
from bs4 import BeautifulSoup
import json

def load_txt(path):
    try:
        with open(path,"r") as file:
            print(colored("File Found!","green",attrs=["bold"]))
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(colored("File Not Found!","red",attrs=["bold"]))
    except Exception as e:
        print(colored(f"an error occured: {e}","red",attrs=["bold"]))

def load_lrc(path):
    try:
        with open(path,"r",encoding="utf-8") as file:
            print(colored("File Found!","green",attrs=["bold"]))
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(colored("File Not Found!","red",attrs=["bold"]))
    except Exception as e:
        print(colored(f"an error occured: {e}","red",attrs=["bold"]))
        
def load_csv(path):
        try:
            with open(path,"r",encoding="utf-8") as file:
                f = csv.reader(file)
                print(colored("File Found!","green",attrs=["bold"]))
                for row in f:
                    print(row)
        except FileNotFoundError:
            print(colored("File Not Found!","red",attrs=["bold"]))
        except Exception as e:
            print(colored(f"an error occured: {e}","red",attrs=["bold"]))
            
def load_py(path):
    try:
        with open(path,"r",encoding="utf-8") as file:
            contents = file.read()
            print(colored("File Found!","green",attrs=["bold"]))
            print(contents)
    except FileNotFoundError:
        print(colored("File Not Found!","red",attrs=["bold"]))
    except Exception as e:
        print(colored(f"an error occured: {e}","red",attrs=["bold"]))        
            
def load_dat(path):
            try:
                with open(path,"rb") as file:
                    print(colored("File Found!","green",attrs=["bold"]))
                    try:
                        data = pickle.load(file)
                        print(colored("Pickle File loaded sucessfully","green",attrs=["bold"]))
                        if isinstance(data,(list,tuple)):
                            for item in data:
                                print(item)
                        else:
                            print(data)
                    except pickle.UnpicklingError:
                        file.seek(0)
                        data = file.read()
                        print(colored(f"binary file loaded sucessfully {len(data)}bytes","green",attrs=["bold"]))
                        print(data)
                        print()
                        print(colored("trying to decode text...","yellow",attrs=["bold"]))
                        try:
                            text = data.decode("utf-8")
                            print(colored(f"decoded text: \n{text}","yellow"))
                        except UnicodeDecodeError:
                            print(colored("File is not valid utf-8 text!","red",attrs=["bold"]))
            except FileNotFoundError:
                print(colored("File Not Found!","red",attrs=["bold"]))
            except Exception as e:
                print(colored(f"an error occured: {e}","red",attrs=["bold"]))
                
def load_html(path):
    try:
        with open(path,"r",encoding="utf-8") as file:
            soup = BeautifulSoup(file,"html.parser")
            print(soup.prettify())
    except FileNotFoundError:
        print(colored("File Not Found!","red",attrs=["bold"]))
    except Exception as e:
            print(colored(f"an error occured: {e}","red",attrs=["bold"]))
        
        
def load_css(path):
    try:
        with open(path,"r",encoding="utf-8") as file:
            content=file.read()
            print(content)
    except FileNotFoundError:
        print(colored("File Not Found!","red",attrs=["bold"])) 
    except Exception as e:
            print(colored(f"an error occured: {e}","red",attrs=["bold"]))

def load_json(path):
    try:
        with open(path,"r",encoding="utf-8") as file:
            data = json.load(file)
            print(data)
    except FileNotFoundError:
        print(colored("File Not Found!","red",attrs=["bold"]))
    except json.JSONDecodeError:
        print(colored("invalid JSON Format!","red",attrs=["bold"]))
    except Exception as e:
            print(colored(f"an error occured: {e}","red",attrs=["bold"]))
            
def load_log(path):
        try:
            with open(path,"r",encoding="utf-8") as file:
                print(colored("File Found!","green",attrs=["bold"]))
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print(colored("File Not Found!","red",attrs=["bold"]))
        except UnicodeDecodeError:
            print(colored("Error: File encoding is not UTF-8!","red",attrs=["bold"]))
        except Exception as e:
            print(colored(f"an error occured: {e}","red",attrs=["bold"]))
        
def load(path):
    parts = path.split(".")
    if len(parts) > 1:
        format = parts[-1].lower()
    else:
        format = ""
    if format == "txt":
        load_txt(path)
    elif format == "lrc":
        load_lrc(path)
    elif format == "csv":
        load_csv(path)
    elif format == "dat":
        load_dat(path)
    elif format == "py":
        load_py(path)
    elif format == "html":
        load_html(path)
    elif format == "css":
        load_css(path)
    elif format == "json":
        load_json(path)
    elif format == "log":
        load_log(path)
    else:
        print(colored("Unsupported File Format!","red",attrs=["bold"]))
          
file_path = input(colored("Enter File Path: ","yellow",attrs=["bold"]))
print()
load(file_path)
