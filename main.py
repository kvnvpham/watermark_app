from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageGrab

FONT = ("Arial", 14, "normal")
my_img = None
filename = None


def select_file():
    global my_img, filename
    filename = filedialog.askopenfilename(title="Select An Image",
                                          initialdir="/",
                                          filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"))
                                          )
    my_img = ImageTk.PhotoImage(Image.open(filename).resize((1000, 600)))
    canvas.itemconfig(load_img, image=my_img)
    canvas.update()


def get_coord(event):
    x = event.x
    y = event.y

    canvas.coords(mark_img, x, y)


def edit_img():
    text = mark_entry.get()
    canvas.itemconfig(mark_img, text=text)
    mark_entry.delete(0, 'end')


def save_img(filename):
    x0 = window.winfo_rootx() + canvas.winfo_x()
    y0 = window.winfo_rooty() + canvas.winfo_y()
    x1 = x0 + canvas.winfo_width()
    y1 = y0 + canvas.winfo_height()

    # Screen adjustment
    x0 = x0*1.5
    y0 = y0*1.5
    x1 = x1*1.5
    y1 = y1*1.5

    ImageGrab.grab((x0, y0, x1, y1)).save(filename)


window = Tk()
window.title("Image Watermarker")
window.config(padx=20, pady=20)

instruct_label = Label(text="Position the watermark by clicking anywhere on the image, default is set to the "
                            "center of the image.",
                       font=FONT
                       )
instruct_label.grid(column=0, row=2, padx=(27, 0), pady=7)

mark_entry = Entry(width=70, font=FONT)
mark_entry.insert(0, "Type Watermark Text")
mark_btn = Button(text="Submit", font=FONT, padx=25, command=edit_img)
mark_entry.grid(column=0, row=3, padx=(0, 20), pady=10)
mark_btn.grid(column=1, row=3, pady=10)

canvas = Canvas(window, width=1000, height=600)
canvas.bind('<Button-1>', get_coord)
load_img = canvas.create_image(500, 300)
mark_img = canvas.create_text(500, 300, text="", font=("Arial", 30))
canvas.grid(column=0, row=0, columnspan=3)
canvas.update()

select_btn = Button(text="Select Image", font=FONT, command=select_file)
select_btn.grid(column=2, row=2, padx=10, pady=10)

save_btn = Button(text="Save Image", font=FONT, padx=7, command=lambda: save_img(filename))
save_btn.grid(column=2, row=3, padx=10, pady=10)

window.mainloop()
