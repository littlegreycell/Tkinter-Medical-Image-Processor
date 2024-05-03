import tkinter as tk
from tkinter import ttk
from ctypes import windll

# Resolution Scaling
windll.shcore.SetProcessDpiAwareness(1)

# Create Window
window = tk.Tk()
window.geometry("1280x600")
window.title("Medical Image Processing")

# Configure the grid to expand frames proportionally
window.grid_rowconfigure(0, weight=1)
for i in range(3):
    window.grid_columnconfigure(i, weight=1)

# Create main frames with sticky to expand with window
frame_left = tk.Frame(window, width=280, height=600)
frame_left.grid(row=0, column=0, sticky='nsew')

frame_middle = tk.Frame(window)
frame_middle.grid(row=0, column=1, sticky='nsew')

frame_right = tk.Frame(window, width=360, height=600)
frame_right.grid(row=0, column=2, sticky='nsew')

# Set grid configuration within frames to fill them as well
frame_left.grid_rowconfigure(0, weight=1)
frame_left.grid_columnconfigure(0, weight=1)
frame_middle.grid_rowconfigure(0, weight=1)
frame_middle.grid_columnconfigure(0, weight=1)
frame_right.grid_rowconfigure(0, weight=1)
frame_right.grid_columnconfigure(0, weight=1)

# Create label frames for main frames with sticky to expand
label_frame0 = tk.LabelFrame(frame_left, text="Filters", width=270, height=600)
label_frame0.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

label_frame1 = tk.LabelFrame(frame_middle, text="Images", width=630, height=600)
label_frame1.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

label_frame2 = tk.LabelFrame(frame_right, text="Images Info", width=350, height=600)
label_frame2.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

# Configure each label frame to expand its content
label_frame0.grid_rowconfigure(0, weight=1)
label_frame0.grid_columnconfigure(0, weight=1)
label_frame1.grid_rowconfigure(0, weight=1)
label_frame1.grid_columnconfigure(0, weight=1)
label_frame2.grid_rowconfigure(0, weight=1)
label_frame2.grid_columnconfigure(0, weight=1)
      
"frame0"    
    
# Filters 
def negative():
    pass

def histogram():
    pass
    
def medianFilter():
    pass
    
def minFilter():
    pass
        
def maxFilter():
    pass
    
def gaussianFilter():
    pass
    
def sobelFilter():
    pass
    
def gamaFilter():
    pass
      
def openingFilter():
    pass
    
def closingFilter():
    pass
    
def erosionFilter():
    pass
    
def dilationFilter():
    pass
       
# Create Filter butons
aralik = 0.03

buton_negative = tk.Button(label_frame0, text= "Negative" , command=negative, width= 13 )        
buton_negative.place(relx = 0.04 , rely = aralik)

buton_histogram = tk.Button(label_frame0, text= "Histogram Equ." , command=histogram, width= 13  )        
buton_histogram.place(relx = 0.04 , rely = aralik + 0.07*1)

buton_median = tk.Button(label_frame0, text= "Median" , command=medianFilter, width= 13  )        
buton_median.place(relx = 0.04 , rely = aralik + 0.07*2)

buton_min = tk.Button(label_frame0, text= "Min" , command=minFilter, width= 13  )        
buton_min.place(relx = 0.04 , rely = aralik + 0.07*3)

buton_max = tk.Button(label_frame0, text= "Max " , command=maxFilter, width= 13  )        
buton_max.place(relx = 0.04 , rely = aralik + 0.07*4)

buton_gaussian = tk.Button(label_frame0, text= "Gaussian" , command=gaussianFilter, width= 13  )        
buton_gaussian.place(relx = 0.04 , rely = aralik + 0.07*5)

buton_sobel = tk.Button(label_frame0, text= "Sobel " , command=sobelFilter, width= 13  )        
buton_sobel.place(relx = 0.55 , rely = aralik)

buton_gama = tk.Button(label_frame0, text= "Gama Transform" , command=gamaFilter, width= 13  )        
buton_gama.place(relx = 0.55 , rely = aralik + 0.07*1)

buton_opening = tk.Button(label_frame0, text= "Opening " , command=openingFilter, width= 13  )        
buton_opening.place(relx = 0.55 , rely = aralik + 0.07*2)

buton_closing = tk.Button(label_frame0, text= "Closing" , command=closingFilter, width= 13  )        
buton_closing.place(relx = 0.55 , rely = aralik + 0.07*3)

buton_erosion = tk.Button(label_frame0, text= "Erosion" , command=erosionFilter, width= 13  )        
buton_erosion.place(relx = 0.55 , rely = aralik + 0.07*4)

buton_dilation = tk.Button(label_frame0, text= "Dilation" , command=dilationFilter, width= 13  )        
buton_dilation.place(relx = 0.55 , rely = aralik + 0.07*5)

# Create Entry box for input 
value = tk.Entry(label_frame0, width =3 , bd =4)
value.place(relx = 0.3 , rely = 0.49)

# Rotate
def rotate_left():
    pass 

def rotate_right():
    pass 
 
# Create Rotate Buttons  
tk.Label(label_frame0, text="Values:", font="Times 10").place(relx = 0.05 , rely = 0.49)
buton_mean = tk.Button(label_frame0, text= "Left" , command=rotate_left, width= 5  ).place(relx = 0.58 , rely = 0.48)     
buton_mean = tk.Button(label_frame0, text= "Right" , command=rotate_right, width= 5  ).place(relx = 0.78 , rely =0.48)     
    
"frame 2 " 

# Show Metadata for DICOM Images
def search_metadata():
    pass

def reset_search():
    pass
        
def load_metadata():
    pass

scroll1 = tk.Scrollbar(label_frame2, orient = tk.VERTICAL)
scroll1.pack(side=tk.RIGHT, fill=tk.Y)

scroll2 = tk.Scrollbar(label_frame2, orient = tk.HORIZONTAL)
scroll2.pack(side=tk.BOTTOM, fill=tk.X)

listBox = tk.Listbox(label_frame2, width =40, height = 10, yscrollcommand =scroll1.set , xscrollcommand =scroll2.set)
listBox.pack(fill=tk.BOTH, expand=True)
scroll1.pack(side=tk.RIGHT, fill=tk.Y)
scroll2.pack(side=tk.BOTTOM, fill=tk.X)

label_frame2.grid_rowconfigure(0, weight=1)  # ListBox için yer ayır
label_frame2.grid_columnconfigure(0, weight=1)

# Buttons for search
search_var = tk.StringVar()
search_entry = tk.Entry(label_frame2, textvariable=search_var, width=30)
search_entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

reset_button = tk.Button(label_frame2, text="Back", command=reset_search)
reset_button.pack(side=tk.RIGHT, padx=10)

search_button = tk.Button(label_frame2, text="Search", command=search_metadata)
search_button.pack(side=tk.LEFT, padx=10)

" Menubar Options"

# File menu options
def openImage():
    pass

def imageReset ():
    pass

def close_window():
    pass
    
def saveImage():
    pass

 #  creation of window-2
def imagePreprocessing():
    pass

# creation of window-3
def imageFileFilters():
    pass     

#Creating Menubar and Buttons 
menubar = tk.Menu (window)
window.config(menu = menubar)
file = tk.Menu(menubar, tearoff=0) # tearoff seçenekleri en üstten koymaya başlamamızı sağlar
imageOperations= tk.Menu(menubar, tearoff=0)

# Adding Parent Buttons to the Menubar
menubar.add_cascade (label="File", menu = file) 
menubar.add_cascade (label= "Image Tools", menu=imageOperations)

" Creating submenus "

# Creating submenus for file menu
file.add_command (label = "Open", command = openImage)
file.add_command (label = "Save", command = saveImage ) 

file.add_command (label="Reset Image", command = imageReset)
file.add_separator()  # menü seçenekleri arasına bir ayırıcı çizgi ekler
file.add_command (label = "Exit", command = close_window ) 

#  Creating submenus for imageOperations
imageOperations.add_command (label = "Metadata Info", command = metadata) 
imageOperations.add_command (label = "Expand Dataset", command = imagePreprocessing)
imageOperations.add_command (label = "Filter Gallery", command = imageFileFilters) 

window.mainloop() 
