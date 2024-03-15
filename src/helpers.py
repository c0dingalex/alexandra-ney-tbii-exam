from PIL import Image, ImageTk
import tkinter as tk

def add_image(root, file_path, width, height):
    """This definition will place the image on the gui window."""

    global pic, f1

    # Create the frame for the first windows of the game
    f1 = tk.Frame(root)
    # read the image I want to use for the first frame
    img = Image.open(file_path)
    # resize the image to the same size as the gui window
    img = img.resize((1000, 530), Image.LANCZOS)
    # code to view the image as the frame
    pic = ImageTk.PhotoImage(img)
    Lab = tk.Label(f1, image=pic)
    # code to just place the image
    Lab.pack()
    f1.pack()

# create a close button to add on every page
def create_close_button(root):
    close_button = tk.Button(text="X",
                             font="lucida 12 bold",
                             command=root.destroy)
    close_button.place(x=935, y=33)

def clear_widgets(root):
    """This function will destroy any widgets I created"""
    for i in root.winfo_children():
        i.destroy()