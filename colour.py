import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv

class ColorGUI:
    def __init__(self, root, input_file):
        self.root = root
        self.root.title("Color GUI")

        try:
            self.colors = self.read_input_file(input_file)
        except Exception as e:
            messagebox.showerror("Error", f"Error reading input file: {e}")
            root.destroy()
            return

        # Filter out rows with less than 3 elements and sort based on the third element
        self.colors = [row for row in self.colors if len(row) >= 3]
        self.colors.sort(key=lambda x: x[2])  # Sort based on the third element (color name)

        self.create_widgets()

    def read_input_file(self, input_file):
        colors = []
        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                colors.append(row)
        return colors

    def create_widgets(self):
        for i, color_info in enumerate(self.colors):
            if len(color_info) >= 3:
                color_frame = ttk.Frame(self.root, padding=(5, 5), relief="solid")
                color_frame.grid(row=i, column=0, padx=5, pady=5)

                color_label = ttk.Label(color_frame, text=color_info[0], width=10)
                color_label.grid(row=0, column=0)

                number_label = ttk.Label(color_frame, text=color_info[1], width=5)
                number_label.grid(row=1, column=0)

                name_label = ttk.Label(color_frame, text=color_info[2], width=10)
                name_label.grid(row=2, column=0)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    input_file = "colour.txt"  # Change this to your input file name
    root = tk.Tk()
    color_gui = ColorGUI(root, input_file)
    color_gui.run()
















import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv

class ColorGUI:
    def __init__(self, root, input_file):
        self.root = root
        self.root.title("Color GUI")

        try:
            self.colors = self.read_input_file(input_file)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error reading input file: {e}")
            root.destroy()
            return

        # # Sort the colors based on your preferred order
        # self.colors.sort(key=lambda x: x[2])  # Sort based on the third element (color name)
        # Filter out rows with less than 3 elements and sort based on the third element
        self.colors = [row for row in self.colors if len(row) >= 3]
        self.colors.sort(key=lambda x: x[2])  # Sort based on the third element (color name)

        self.create_widgets()

    def read_input_file(self, input_file):
        colors = []
        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                colors.append(row)
        return colors

    def create_widgets(self):
        for i, color_info in enumerate(self.colors):
            if len(color_info) >= 3:
                color_label = ttk.Label(self.root, text=color_info[0], width=10)
                color_label.grid(row=i, column=0, padx=5, pady=5)

                number_label = ttk.Label(self.root, text=color_info[1], width=5)
                number_label.grid(row=i, column=1, padx=5, pady=5)

                name_label = ttk.Label(self.root, text=color_info[2], width=10)
                name_label.grid(row=i, column=2, padx=5, pady=5)
            else:
                print(f"Skipping row {i + 1} due to insufficient values: {color_info}")


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    input_file = "colour.txt"  # Change this to your input file name
    root = tk.Tk()
    color_gui = ColorGUI(root, input_file)
    color_gui.run()


























# import tkinter as tk
# from tkinter import ttk
# import csv

# class ColorGUI:
#     def __init__(self, root, input_file):
#         self.root = root
#         self.root.title("Color GUI")

#         try:
#             self.colors = self.read_input_file(input_file)
#         except Exception as e:
#             tk.messagebox.showerror("Error", f"Error reading input file: {e}")
#             root.destroy()
#             return

#         self.create_widgets()

#     def read_input_file(self, input_file):
#         colors = []
#         with open(input_file, 'r') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 colors.append(row)
#         return colors

#     def create_widgets(self):
#         for i, color_info in enumerate(self.colors):
#             if len(color_info) >= 3:
#                 color_label = ttk.Label(self.root, text=color_info[0], width=10)
#                 color_label.grid(row=i, column=0, padx=5, pady=5)

#                 number_label = ttk.Label(self.root, text=color_info[1], width=5)
#                 number_label.grid(row=i, column=1, padx=5, pady=5)

#                 name_label = ttk.Label(self.root, text=color_info[2], width=10)
#                 name_label.grid(row=i, column=2, padx=5, pady=5)

#     def run(self):
#         self.root.mainloop()

# if __name__ == "__main__":
#     input_file = "colour.txt"   # Change this to your input file name
#     root = tk.Tk()
#     color_gui = ColorGUI(root, input_file)
#     color_gui.run()





















