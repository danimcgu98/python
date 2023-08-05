from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, StringVar, END
from re import search
import filecmp as fc
from os.path import exists, join, dirname, abspath
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets")


class App():
    def __init__(self):
        self.root = Tk()
        self.root.title('Foldoff')
        self.root.geometry('500x450')
        self.root.configure(bg = "#E7C9A9")
        self.icon = PhotoImage(file=self.resource_path("foldoff.png"))
        self.root.iconphoto(False, self.icon)
        
        self.canvas = Canvas(
            self.root,
            bg = "#E7C9A9",
            height = 450,
            width = 500,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        
        self.canvas.place(x = 0, y = 0)
        
        self.image_image_1 = PhotoImage(file=self.resource_path("title.png"))
        
        self.image_1 = self.canvas.create_image(
            273.0,
            72.0,
            image=self.image_image_1
        )
            
        self.canvas.create_text(
            51.0,
            179.0,
            anchor="nw",
            text="Folder #1:",
            fill="#967BB6",
            font=("Inter Bold", 20 * -1)
        )
        
        self.canvas.create_text(
            51.0,
            232.0,
            anchor="nw",
            text="Folder #2:",
            fill="#967BB6",
            font=("Inter Bold", 20 * -1)
        )
        
        self.canvas.create_text(
            51.0,
            281.0,
            anchor="nw",
            text="Save To:",
            fill="#967BB6",
            font=("Inter Bold", 20 * -1)
        )
        
        self.canvas.create_text(
            51.0,
            332.0,
            anchor="nw",
            text="File Name:",
            fill="#967BB6",
            font=("Inter Bold", 20 * -1)
        )
        
        self.button_image_1 = PhotoImage(
            file=self.resource_path("browse_icon.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.get_folder1,
            relief="flat"
        )
        
        self.button_1.place(
            x=155.0,
            y=179.0,
            width=26.0,
            height=26.0
        )
        
        self.button_image_2 = PhotoImage(
        file=self.resource_path("browse_icon.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.get_folder2,
            relief="flat"
        )
        
        self.button_2.place(
            x=155.0,
            y=232.0,
            width=26.0,
            height=26.0
        )
        
        self.button_image_3 = PhotoImage(
        file=self.resource_path("browse_icon.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.get_folder3,
            relief="flat"
        )
        
        self.button_3.place(
            x=155.0,
            y=281.0,
            width=26.0,
            height=26.0
        )

        self.canvas.create_text(
            51.0,
            133.0,
            anchor="nw",
            text="Enter 2 Folders below to compare",
            fill="#967BB6",
            font=("Inter Bold", 20 * -1)
        )

        self.image_image_2 = PhotoImage(file=self.resource_path("directory_field.png"))
        self.image_2 = self.canvas.create_image(
            320.0,
            192.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(file=self.resource_path("directory_field.png"))
        self.image_3 = self.canvas.create_image(
            320.0,
            245.0,
            image=self.image_image_3
        )
        
        self.image_image_4 = PhotoImage(file=self.resource_path("directory_field.png"))
        self.image_4 = self.canvas.create_image(
            320.0,
            294.5,
            image=self.image_image_4
        )
        
        self.folder1_var = StringVar()
        
        self.path1 = self.canvas.create_text(
            196.0,
            182.0,
            anchor="nw",
            text=self.folder1_var.get(),
            fill="#000000",
            font=("Inter", 16 * -1)
        )

        self.folder2_var = StringVar()
        
        self.path2 = self.canvas.create_text(
            196.0,
            235.0,
            anchor="nw",
            text=self.folder2_var.get(),
            fill="#000000",
            font=("Inter", 16 * -1)
        )
        
        self.folder3_var = StringVar()
        
        self.path3 = self.canvas.create_text(
            196.0,
            287.0,
            anchor="nw",
            text=self.folder3_var.get(),
            fill="#000000",
            font=("Inter", 16 * -1)
        )
        
        self.image_image_6 = PhotoImage(
            file=self.resource_path("input_field.png"))
        
        self.image_6 = self.canvas.create_image(
            308.0,
            345.0,
            image=self.image_image_6
        )
        
        self.entry1 = Entry(self.root)
        self.input = self.canvas.create_window(308.0, 345.0, window=self.entry1, width=260)
        
        self.submit_image = PhotoImage(
        file=self.resource_path("submit_button.png"))
        self.submit_button = Button(
            image=self.submit_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.submit_form,
            relief="flat"
        )
        
        self.submit_button.place(
            x=144.0,
            y=382.0,
            width=258.0,
            height=35.0
        )
        
        self.root.resizable(False, False)
        
        self.root.mainloop()
        
    def resource_path(self, relative_path):
        base_path = getattr(sys, '_MEIPASS', dirname(abspath(__file__)))
        return join(base_path, relative_path)

    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    def get_folder1(self):
        self.folder1_var.set(filedialog.askdirectory())
        self.canvas.itemconfigure(self.path1, text=self.folder1_var.get())
        
    def get_folder2(self):
        self.folder2_var.set(filedialog.askdirectory())
        self.canvas.itemconfigure(self.path2, text=self.folder2_var.get())
        
    def get_folder3(self):
        self.folder3_var.set(filedialog.askdirectory())
        self.canvas.itemconfigure(self.path3, text=self.folder3_var.get())
        
    def submit_form(self):
        
        if matches := search(r'.*\/(.+)$', self.folder1_var.get()):
            folder1 = matches.group(1)
        
        if matches := search(r'.*\/(.+)$', self.folder2_var.get()):
            folder2 = matches.group(1)
        
        if exists(self.folder1_var.get()) and exists(self.folder2_var.get()) and self.entry1.get() and exists(self.folder3_var.get()):
            comparer = fc.dircmp(self.folder1_var.get(), self.folder2_var.get())
            file_path = self.folder3_var.get() + '/' + self.entry1.get()
            with open(file_path, 'w') as f:
                new_content = ''
                if len(comparer.diff_files) != 0:
                    new_content += 'Files with same name but different content:\n'
                    for file in sorted(comparer.diff_files):
                        new_content += f'- {file}\n'
                    new_content += '\n'
                           
                if len(comparer.left_only) != 0:
                    new_content += f'Files only found in [{folder1}]:\n'
                    for file in sorted(comparer.left_only):
                        new_content += f'- {file}\n'
                    new_content += '\n'
                        
                if len(comparer.right_only) != 0:
                    new_content += f'Files only found in [{folder2}]:'                 
                    for file in sorted(comparer.right_only):
                        new_content += f'- {file}\n'
                    
                f.write(new_content)  
                
        else:
            print('missing fields')
    
App()