#ViewMate File Reader
#supports txt,lrc,csv,dat
import termcolor
from termcolor import colored
import os
import pickle
import csv

def load_txt(path):
    try:
        with open(path,"r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(colored("File Not Found!","red",attrs=["bold"]))
    except Exception as e:
        print(f"an error occured: {e}")

def load_lrc(path):
    try:
        with open(path,"r",encoding="utf-8") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(colored("File Not Found!","red",attrs=["bold"]))
    except Exception as e:
        print(f"an error occured: {e}")
        
def load_csv(path):
        try:
            with open(path,"r") as file:
                f = csv.reader(file)
                for row in f:
                    print(row)
        except FileNotFoundError:
            print(colored("File Not Found!","red",attrs=["bold"]))
        except Exception as e:
            print(f"an error occured: {e}")
            
def load_dat(path):
            try:
                with open(path,"rb") as file:
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
                            print(colored(f"decided text: \n{text}","yellow"))
                        except UnicodeDecodeError:
                            print(colored("File is not valid utf-8 text!","red",attrs=["bold"]))
            except FileNotFoundError:
                print(colored("File Not Found!","red",attrs=["bold"]))
            except Exception as e:
                print(f"an error occured: {e}")

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
    else:
        print(colored("Unsupported File Format!","red",attrs=["bold"]))
          
file_path = input(colored("Enter File Path: ","yellow",attrs=["bold"]))
print()
load(file_path)