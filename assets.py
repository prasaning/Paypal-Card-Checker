
import os, datetime, string, random, ctypes
from tkinter.messagebox import NO

class utils:
    
    def center(var: str, space: int = None):  # From Pycenter
        if not space:
            space = (os.get_terminal_size().columns -
                     len(var.splitlines()[int(len(var.splitlines())/2)])) / 2

        return "\n".join((' ' * int(space)) + var for var in var.splitlines())

    def isempty(list_t:list):
        count = 0
        for i in list_t:
            if len(i.strip()) == 0 and i.isspace():
                count += 1
        return count == len(list_t)
    
    def faded(data:str):
        faded = ''
        red = 40
        for line in data.splitlines():
            faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
            if not red == 255:
                red += 15
                if red > 255:
                    red = 255
        return faded

    def input(prompt, type):
        while True:
            try:
                if type == "int":
                    result = int(input(prompt))
                    return result
                elif type == "string":
                    result = input(prompt)
                    return result
                elif type == "bool":
                    result = input(prompt)
                    if result.lower() == "true":
                        return True
                    else:
                        return False
                elif type == "question":
                    result = input(prompt).lower()
                    if result == "yes" or result == "y":
                        return True
                    else:
                        return False
                else:
                    result = input(prompt)
                    return result
            except:
                continue
    
    def Mbox(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    
    def cls():
        os.system('cls')
    
    def random_string(length):
        chars=string.ascii_uppercase + string.digits + string.ascii_lowercase
        return ''.join(random.choice(chars) for _ in range(length))

    def set_window_size(width, height):
        os.system(f'mode con: cols={width} lines={height}')