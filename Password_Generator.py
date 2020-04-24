from tkinter import *
import random

root = Tk()
root.title("Password Generator")

header = Label(root, text="Welcome to Password Generator! Please enter the specifications of your password.", bd=5, padx=5, pady=5).pack()

char_label = Label(root, text="How many characters should the password be?", padx=5, pady=5).pack()
#char_label.grid(row=1, column=0)

s = "[Select Option]"

click1 = StringVar()
click1.set(s)

click2 = StringVar()
click2.set(s)

click3 = StringVar()
click3.set(s)

click4 = StringVar()
click4.set(s)

drop_char = OptionMenu(root, click1, "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
                       "16", "17", "18", "19", "20").pack()

def response():
    if click1.get() != s:
        h = int(click1.get())
    return h

def clear1():
    if click1.get() != s:
        def all_children(root):
            _list = root.winfo_children()
            for item in _list:
                if item == header:
                    pass
                else:
                    if item.winfo_children():
                        _list.extend(item.winfo_children())
            return _list
        widget_list = all_children(root)
        for item in widget_list:
            item.pack_forget()

        i = 0
        array = []
        while i <= response():
            array.append(i)
            i = i + 1
        uletter_label = Label(root, text="How many upper case letters should the password contain?", bd=5, padx=5, pady=5).pack()
        # uletter_label.grid(row=2, column=0)
        OptionMenu(root, click2, *array).pack()
        Button(root, text="Next", command=clear2).pack()

Button(root, text="Next", command=clear1).pack()

def response2():
    if click2.get() != s:
        h = response() - int(click2.get())
    return h

def clear2():
    if click2.get() != s:
        def all_children(root):
            _list = root.winfo_children()
            for item in _list:
                if item == header:
                    pass
                else:
                    if item.winfo_children():
                        _list.extend(item.winfo_children())
            return _list
        widget_list = all_children(root)
        for item in widget_list:
            item.pack_forget()

        i = 0
        array = []
        while i <= response2():
            array.append(i)
            i = i + 1

        number_label = Label(root, text="How many numbers should the password contain?", bd=5, padx=5, pady=5).pack()
        # number_label.grid(row=3, column=0)
        OptionMenu(root, click3, *array).pack()
        Button(root, text="Next", command=clear3).pack()

def response3():
    if click3.get() != s:
        h = response2() - int(click3.get())
    return h

def clear3():
    if click3.get() != s:
        def all_children(root):
            _list = root.winfo_children()
            for item in _list:
                if item == header:
                    pass
                else:
                    if item.winfo_children():
                        _list.extend(item.winfo_children())
            return _list
        widget_list = all_children(root)
        for item in widget_list:
            item.pack_forget()

        i = 0
        array = []
        while i <= response3():
            array.append(i)
            i = i + 1

        spec_label = Label(root, text="How many special characters should the password contain?", bd=5, padx=5, pady=5).pack()
        # spec_label(row=4, column=0)
        OptionMenu(root, click4, *array).pack()
        Button(root, text="Next", command=generate).pack()

def response4():
    if click4.get() != s:
        h = response3() - int(click4.get())
        return h

def generate():
    if click4.get() != s:
        def all_children(root):
            _list = root.winfo_children()
            for item in _list:
                if item == header:
                    pass
                else:
                    if item.winfo_children():
                        _list.extend(item.winfo_children())
            return _list
        widget_list = all_children(root)
        for item in widget_list:
            item.pack_forget()

        Label(root, text="Your password is: ").pack(padx=5, pady=5)

        total_uletter = response() - response2()
        total_number = response2() - response3()
        total_spec = response3() - response4()

        password = ""
        upper_letter_array = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                              "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        lower_letter_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        number_array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        spec_char_array = ["#", "$", "%", "&", "(", ")", "*", "+", "<", "=", ">", "?", "@", "[",
                           "]", "^", "_", "{", "|", "}", "~"]

        k = 0
        while k < total_uletter:
            k = k + 1
            password = password + random.choice(upper_letter_array)

        j = 0
        while j < total_number:
            j = j + 1
            password = password + random.choice(number_array)

        l = 0
        while l < total_spec:
            l = l + 1
            password = password + random.choice(spec_char_array)

        f = -1
        while f < response4()-1:
            f = f + 1
            password = password + random.choice(lower_letter_array)

        final_password = ''.join(random.sample(password, len(password)))
        Frame(Label(root, text=final_password, cursor="xterm", bd=5, padx=5, pady=5).pack(), bg="red").pack()


root.mainloop()
