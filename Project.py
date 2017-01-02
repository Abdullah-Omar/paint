##LIBRARIES
import numpy as np
import cv2
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        self.root.iconbitmap("paint.ico")
        self.root.resizable(width=False, height=False)

        self.header()
        self.body()

        self.x = self.y = 0
        self.shape = "rectangle"
        self.shape_border_color = "#000000"
        self.font_color = "Black"
        self.shape_border_color_bgr = (0, 0, 0)
        self.font_size = 10
        self.shape_border_width = 1
        self.rect = None
        self.circ = None
        self.triang = None
        self.pencil_eraser_list = []
        self.start_x = None
        self.start_y = None

        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.file_img = ImageTk.PhotoImage(Image.open("file.png"))
        self.filemenu.add_command(label="  New", image=self.file_img, compound="left", command=self.new_fun)
        self.save_img = ImageTk.PhotoImage(Image.open("save.png"))
        self.filemenu.add_command(label="  Save as ...", image=self.save_img, compound="left", command=self.save_fun)
        self.exit_img = ImageTk.PhotoImage(Image.open("exit.png"))
        self.filemenu.add_command(label="   Exit", image=self.exit_img, compound="left", command=self.exit_fun)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.root.config(menu=self.menubar)

    def header(self):
        self.background = Frame(self.root, height="600", width="900", bg="#ced7e6")
        self.background.pack()

        self.header = Frame(self.background, height="100", width="900", bg="#f0f0f0")
        self.header.place(x="0", y="0")
        self.ribbon = ttk.LabelFrame(self.header, text="Home", relief="flat")
        self.ribbon.place(x="5", y="3", height="90", width="890")

        # TOOLS
        self.tool = ttk.LabelFrame(self.header, text="Tools", relief="flat", labelanchor='s')
        self.tool.place(x="80", y="20", height="70", width="400")

        self.text_label = Label(self.header, text="Text")
        self.text_label.place(x="90", y="25")
        self.text = Text(self.header, bd=1)
        self.text.place(x="120", y="30", height="40", width="130")

        self.X_label = Label(self.header, text="X")
        self.X_label.place(x="260", y="25")
        self.X_text = Entry(self.header, bd=1)
        self.X_text.place(x="275", y="28", height="15", width="30")

        self.Y_label = Label(self.header, text="Y")
        self.Y_label.place(x="260", y="50")
        self.Y_text = Entry(self.header, bd=1)
        self.Y_text.place(x="275", y="53", height="15", width="30")

        self.font_size_label = Label(self.header, text="Size")
        self.font_size_label.place(x="315", y="25")
        font_variable = StringVar()
        font_variable.set("10")
        self.font_size = ttk.OptionMenu(self.header, font_variable, "10", "1", "2", "3", "4", "5", "6", "7", "8",
                                        "9", "10", "11", "12", "14", "16", "18",
                                        command=lambda font_variable=font_variable: self.font_size_fun(font_variable))
        self.font_size.place(x="350", y="25", height="20", width="80")

        self.font_color_label = Label(self.header, text="Color")
        self.font_color_label.place(x="315", y="50")
        color_variable = StringVar()
        color_variable.set("Black")
        self.font_color_label = ttk.OptionMenu(self.header, color_variable, "Black", "Black", "Red", "Blue", "Yellow",
                                               "Green", command=lambda color_variable=color_variable: self.color_variable_fun(color_variable))
        self.font_color_label.place(x="350", y="50", height="20", width="80")

        self.insert_img = ImageTk.PhotoImage(Image.open("text.png"))
        self.insert = ttk.Button(self.header, image=self.insert_img, command=self.insert_fun)
        self.insert.place(x="445", y="25", width="25", height="25")

        self.eraser_img = ImageTk.PhotoImage(Image.open("erase.png"))
        self.eraser = ttk.Button(self.header, image=self.eraser_img, command=self.eraser_fun)
        self.eraser.place(x="445", y="50", width="25", height="25")

        # COLORS
        self.color = ttk.LabelFrame(self.header, text="Colors", relief="flat", labelanchor='s')
        self.color.place(x="500", y="20", height="70", width="125")

        self.red_img = ImageTk.PhotoImage(Image.open("red.png"))
        self.red = ttk.Button(self.header, image=self.red_img, command=self.red_fun)
        self.red.place(x="505", y="25", width="25", height="25")

        self.dark_red_img = ImageTk.PhotoImage(Image.open("dark red.png"))
        self.dark_red = ttk.Button(self.header, image=self.dark_red_img, command=self.dark_red_fun)
        self.dark_red.place(x="505", y="50", width="25", height="25")

        self.orange_img = ImageTk.PhotoImage(Image.open("orange.png"))
        self.orange = ttk.Button(self.header, image=self.orange_img, command=self.orange_fun)
        self.orange.place(x="535", y="25", width="25", height="25")

        self.yellow_img = ImageTk.PhotoImage(Image.open("yellow.png"))
        self.yellow = ttk.Button(self.header, image=self.yellow_img, command=self.yellow_fun)
        self.yellow.place(x="535", y="50", width="25", height="25")

        self.blue_img = ImageTk.PhotoImage(Image.open("blue.png"))
        self.blue = ttk.Button(self.header, image=self.blue_img, command=self.blue_fun)
        self.blue.place(x="565", y="25", width="25", height="25")

        self.purple_img = ImageTk.PhotoImage(Image.open("purple.png"))
        self.purple = ttk.Button(self.header, image=self.purple_img, command=self.purple_fun)
        self.purple.place(x="565", y="50", width="25", height="25")

        self.green_img = ImageTk.PhotoImage(Image.open("green.png"))
        self.green = ttk.Button(self.header, image=self.green_img, command=self.green_fun)
        self.green.place(x="595", y="25", width="25", height="25")

        self.black_img = ImageTk.PhotoImage(Image.open("black.png"))
        self.black = ttk.Button(self.header, image=self.black_img, command=self.black_fun)
        self.black.place(x="595", y="50", width="25", height="25")

        # SHAPES
        self.shape = ttk.LabelFrame(self.header, text="Shapes", relief="flat", labelanchor='s')
        self.shape.place(x="645", y="20", height="70", width="65")

        self.oval_img = ImageTk.PhotoImage(Image.open("circle.png"))
        self.oval = ttk.Button(self.header, image=self.oval_img, command=self.oval_fun)
        self.oval.place(x="650", y="25", width="25", height="25")

        self.rectangle_img = ImageTk.PhotoImage(Image.open("rectangle.png"))
        self.rectangle = ttk.Button(self.header, image=self.rectangle_img, command=self.rectangle_fun)
        self.rectangle.place(x="650", y="50", width="25", height="25")

        self.triangle_img = ImageTk.PhotoImage(Image.open("triangle.png"))
        self.triangle = ttk.Button(self.header, image=self.triangle_img, command=self.triangle_fun)
        self.triangle.place(x="680", y="25", width="25", height="25")

        self.pencil_img = ImageTk.PhotoImage(Image.open("pencil.png"))
        self.pencil = ttk.Button(self.header, image=self.pencil_img, command=self.pencil_fun)
        self.pencil.place(x="680", y="50", width="25", height="25")

        # BRUSH
        self.brush = ttk.LabelFrame(self.header, text="Brush Size", relief="flat", labelanchor='s')
        self.brush.place(x="730", y="20", height="70", width="80")

        brush_variable = DoubleVar()
        brush_variable.set(1)
        self.brush_size = ttk.Scale(self.root, variable=brush_variable, from_=1, to=10, value=1,
                                    command=lambda brush_variable=brush_variable: self.brush_size_fun(brush_variable))
        self.brush_size.place(x="740", y="30", width="60")
        self.brush_label = Label(self.header, text="PX")
        self.brush_label.place(x="780", y="50")
        self.scale_label = Label(self.header, text="1")
        self.scale_label.place(x="765", y="50")

    def red_fun(self):
        self.shape_border_color = "#ed1c24"
        self.shape_border_color_bgr = (36, 28, 237)

    def dark_red_fun(self):
        self.shape_border_color = "#880015"
        self.shape_border_color_bgr = (21, 0, 136)

    def orange_fun(self):
        self.shape_border_color = "#ff7f27"
        self.shape_border_color_bgr = (39, 127, 255)

    def yellow_fun(self):
        self.shape_border_color = "#fff200"
        self.shape_border_color_bgr = (0, 242, 255)

    def blue_fun(self):
        self.shape_border_color = "#323cd4"
        self.shape_border_color_bgr = (204, 72, 63)

    def purple_fun(self):
        self.shape_border_color = "#a349a4"
        self.shape_border_color_bgr = (164, 73, 163)

    def green_fun(self):
        self.shape_border_color = "#22b14c"
        self.shape_border_color_bgr = (76, 177, 34)

    def black_fun(self):
        self.shape_border_color = "#000000"
        self.shape_border_color_bgr = (0, 0, 0)

    def brush_size_fun(self, brush_variable):
        self.shape_border_width = int(round(float(brush_variable), 0))
        self.scale_label.config(text=str(self.shape_border_width))
    def font_size_fun(self, font_variable):
        self.font_size = int(float(font_variable))

    def color_variable_fun(self, color_variable):
        if color_variable == "Black":
            self.shape_border_color_bgr = (0, 0, 0)
        elif color_variable == "Red":
            self.shape_border_color_bgr = (36, 28, 237)
        elif color_variable == "Blue":
            self.shape_border_color_bgr = (204, 72, 63)
        elif color_variable == "Yellow":
            self.shape_border_color_bgr = (0, 242, 255)
        elif color_variable == "Green":
            self.shape_border_color_bgr = (76, 177, 34)

        self.font_color == color_variable


        self.font_color = color_variable

    def insert_fun(self):
        if(len(self.text.get("1.0", END)) == 0 or len(self.X_text.get()) == 0 or len(self.Y_text.get()) == 0):
            messagebox.showwarning("warning", "please enter text, x-axis and y-axis to perform this action")
        else:
            self.frame.create_text(self.X_text.get(), self.Y_text.get(), fill=self.font_color,
                                   font="HERSHEY "+str(self.font_size),
                                   text=self.text.get("1.0", END))

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(self.arr, self.text.get("1.0", END), (int(self.X_text.get()), int(self.Y_text.get()))
                        , font, float((self.font_size*4)/100), self.shape_border_color_bgr)


    def rectangle_fun(self):
        self.shape = "rectangle"

    def oval_fun(self):
        self.shape = "circle"

    def triangle_fun(self):
        self.shape = "triangle"

    def eraser_fun(self):
        self.shape = "eraser"

    def pencil_fun(self):
        self.shape = "pencil"

    def body(self):
        self.arr = np.zeros(shape=(480, 880, 3))
        self.arr[:] = 255
        self.frame = Canvas(self.background, width=880, height=480, cursor="tcross", bg="white")
        self.frame.place(x="8", y="108")
        self.frame.bind("<ButtonPress-1>", self.on_button_press)
        self.frame.bind("<B1-Motion>", self.on_move_press)
        self.frame.bind("<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = event.x
        self.start_y = event.y

        if(self.shape=="rectangle"):
            self.rect = self.frame.create_rectangle(self.x, self.y, 1, 1, width=self.shape_border_width,
                                                    outline=self.shape_border_color)
        elif(self.shape=="circle"):
            self.circ = self.frame.create_oval(self.x, self.y, 1, 1, width=self.shape_border_width,
                                               outline=self.shape_border_color)
        elif(self.shape == "triangle"):
            self.triang = self.frame.create_polygon(self.x, self.y, 1, 1, 1, 1, width=self.shape_border_width, fill='',
                                                outline=self.shape_border_color)


    def on_move_press(self, event):
        self.curX, self.curY = (event.x, event.y)
        if(self.shape=="rectangle"):
            # expand rectangle as you drag the mouse
            self.frame.coords(self.rect, self.start_x, self.start_y, self.curX, self.curY)
        elif(self.shape=="circle"):
            # expand oval as you drag the mouse
            self.r = int(abs(self.start_x-self.curX))
            self.frame.coords(self.circ, int(self.start_x-round(self.r/2, 0)), int(self.start_y-round(self.r/2, 0)),
                              int(self.curX+round(self.r/2, 0)), int(self.curY+round(self.r/2, 0)))
        elif(self.shape == "triangle"):
            # expand triangle as you drag the mouse
            self.frame.coords(self.triang, self.start_x, self.start_y, int(round((self.curX+self.start_x)/2, 0)),
                              int(round(self.curX/2, 0)),
                              self.curX, self.start_y)
        elif(self.shape == "eraser"):
            self.frame.create_rectangle(self.curX, self.curY, self.curX+int(self.font_size),
                                                     self.curY+self.font_size, width=self.font_size, fill="white",
                                                     outline="white")
            self.pencil_eraser_list.append((self.curX, self.curY))
            self.pencil_eraser_list.append((self.curX+self.font_size, self.curY+self.font_size))

        elif(self.shape == "pencil"):
            self.frame.create_rectangle(self.curX, self.curY, self.curX + self.shape_border_width,
                                        self.curY + self.shape_border_width,
                                        width=self.shape_border_width, fill=self.shape_border_color,
                                        outline=self.shape_border_color)
            self.pencil_eraser_list.append((self.curX, self.curY))
            self.pencil_eraser_list.append((self.curX + self.shape_border_width,
                                            self.curY+self.shape_border_width))



    def on_button_release(self, event):
        self.curX, self.curY = (event.x, event.y)
        if(self.shape=="rectangle"):
            cv2.rectangle(self.arr, (self.start_x, self.start_y), (self.curX, self.curY),
                          color=self.shape_border_color_bgr, thickness=self.shape_border_width)

        elif(self.shape=="circle"):
            cv2.circle(self.arr, (self.start_x+int(self.r/2), self.start_y+self.r), self.r,
                       color=self.shape_border_color_bgr, thickness=self.shape_border_width)

        elif (self.shape == "triangle"):
            self.cor = np.array([[self.start_x, self.start_y], [float((self.curX+self.start_x)/2), self.curX/2],
                                 [self.curX, self.start_y]], np.int32)
            cv2.polylines(self.arr, [self.cor], True, color=self.shape_border_color_bgr,
                          thickness=self.shape_border_width)
        elif(self.shape == "eraser"):
            for i in range(len(self.pencil_eraser_list)):
                if i < len(self.pencil_eraser_list) - 1:
                    cv2.rectangle(self.arr, (self.pencil_eraser_list[i]), (self.pencil_eraser_list[i + 1]), color=(255, 255, 255),
                                  thickness=self.font_size)
            del self.pencil_eraser_list[:]


        elif (self.shape == "pencil"):
            for i in range(len(self.pencil_eraser_list)):
                if i < len(self.pencil_eraser_list) - 1:
                    cv2.rectangle(self.arr, (self.pencil_eraser_list[i]), (self.pencil_eraser_list[i + 1]),
                                  color=self.shape_border_color_bgr,
                                  thickness=self.shape_border_width)
            del self.pencil_eraser_list[:]

        pass

    def new_fun(self):
        self.frame.create_rectangle(0, 0, 879, 479, fill="white",
                                    outline="white")
        self.arr[:] = 255

    def save_fun(self):
        self.ftypes = [('JPEP Image', '.jpeg'), ('Png Image', '.png')]
        self.dir = filedialog.asksaveasfile(filetypes=self.ftypes, mode="w", defaultextension=".jpg")
        cv2.imwrite(self.dir.name, self.arr)

    def exit_fun(self):
        self.root.destroy()



master = Tk()
paint = GUI(master)
master.mainloop()
