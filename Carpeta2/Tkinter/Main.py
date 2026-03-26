import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import scrolledtext

import json 
class FileLoader:
    
    root = tk.Tk()
    root.title("Text File Reader")
    root.geometry("600x400")
    
    def open_file(self):
        """Open a text file and insert its content into the text widget."""
        filetypes = (
            ('Text files', '*.json'),
            ('All files', '*.*')
        )

        # Open a file dialog to select a single file and return an open file handle
        file_handle = fd.askopenfile(
            title='Open a file',
            initialdir='/', # You can change the initial directory
            filetypes=filetypes
        )

        if file_handle:
            # Read the file's content
            content = file_handle.read()
            json_obj =  json.loads(content)
            # Clear previous content in the Text widget
            
            
            columns = list(json_obj[0].keys( ))

            # Create Treeview
            tree = ttk.Treeview(self.root, columns=columns, show="headings")
            tree.pack(fill="both", expand=True)

            # Set headings
            for col in columns:
                tree.heading(col, text=col)

            # Insert data
            data = []
            for item in json_obj:
                tree.insert("", tk.END, values=list(item.values()))
                
           
            
            # Close the file handle
            file_handle.close()

    def draw_app(self):

        # Create a Button to open the file dialog
        open_button = tk.Button(
            self.root,
            text='Open Text File',
            command=self.open_file
        )
        open_button.pack(pady=10)

        # Run the Tkinter event loop
        self.root.mainloop()
    
    def draw_treeview(self):
       

        root.mainloop()

test = FileLoader()
test.draw_app()