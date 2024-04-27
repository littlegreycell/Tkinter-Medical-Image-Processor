" WINDOW-2 - imagePreprocessing - Data augmentation process"
def imagePreprocessing():
    
    " Creating Second Window"
    
    secondWindow = tk.Toplevel()
    secondWindow.geometry("450x650")
    secondWindow.wm_title("Görüntü Ön İşleme Penceresi")

    frame_top= tk.Frame(secondWindow, width = 450, height = 50 ) 
    frame_top.grid(row=0 , column=0 )
    frame_middle2 = tk.Frame(secondWindow, width=450, height=550 )
    frame_middle2.grid (row=1, column=0 )
    frame_bottom = tk.Frame(secondWindow, width = 450, height = 50 )
    frame_bottom.grid(row=2, column=0)

    label_frame3 = tk.LabelFrame (frame_top,  width= 440, height = 48 )
    label_frame3.grid(row=0, column=0, padx=5 , pady=1) 
    label_frame4 = tk.LabelFrame(frame_middle2, width = 440, height = 548)
    label_frame4.grid(row=1, column=0 , padx=5 , pady=1 )
    label_frame5 = tk.LabelFrame(frame_bottom,   width = 440, height = 48)
    label_frame5.grid(row=2, column=0 , padx=5 , pady=1)
    
    def selectImage():  
        pass
    
    def selectFolder():
        pass
        
    def create():  
        pass
    
    # Creating Butons
    
    buton_selectImage = tk.Button(label_frame3 , text= "Select Images",  command=selectImage , width = 13)        
    buton_selectImage.place(relx = 0.38 , rely = 0.1)
    buton_create = tk.Button(label_frame5, text= "Cretae", command=create ,width = 13 )        
    buton_create.place(relx = 0.4 , rely = 0.1)
    buton_selectFolder= tk.Button(label_frame5, text= "Save", command=selectFolder ,width = 13 )        
    buton_selectFolder.place(relx = 0.2 , rely = 0.1)
    
    # Creating Labels
    
    aralik = 0.1
    tk.Label(label_frame4, text="Featurewise Center:",              font="Times 11").place(relx = 0.01 , rely = aralik )
    tk.Label(label_frame4, text="Samplewise Center:",               font="Times 11").place(relx = 0.01 , rely = aralik + 0.06*1)
    tk.Label(label_frame4, text="Featurewise Std Normalization:",   font="Times 11").place(relx = 0.01 , rely = aralik + 0.06*2)
    tk.Label(label_frame4, text="Samplewise Std Normalization:",    font="Times 11").place(relx = 0.01 , rely = aralik + 0.06*3)
    tk.Label(label_frame4, text="Vertical Flip:"  ,                 font="Times 11").place(relx = 0.01 , rely = aralik + 0.06*4)
    tk.Label(label_frame4, text="Horizontal Flip:"  ,               font="Times 11").place(relx = 0.01 , rely = aralik + 0.06*5)
    tk.Label(label_frame4, text="Fill Mode:",                       font="Times 11").place(relx = 0.01 , rely = aralik + 0.06*6)
    tk.Label(label_frame4, text="Height Shift Range:",              font="Times 11").place(relx = 0.01 , rely = aralik + 0.06*7)
    tk.Label(label_frame4, text="Width Shift Range:",               font="Times 11").place(relx = 0.01 , rely = aralik + 0.06*8)
    tk.Label(label_frame4, text="Shear Range:",                     font="Times 11").place(relx = 0.01 , rely = aralik + 0.06*9)
    tk.Label(label_frame4, text="Zoom Range:",                      font="Times 11").place(relx = 0.01 , rely = aralik + 0.06*10)
    tk.Label(label_frame4, text="Channel Shift Range:",             font="Times 11").place(relx = 0.01 , rely = aralik + 0.06*11)
    tk.Label(label_frame4, text="cval:",                            font="Times 11").place(relx = 0.01 , rely = aralik + 0.06*12)
    tk.Label(label_frame4, text="Rotation Range:",                  font="Times 11").place(relx = 0.01,  rely = aralik + 0.06*13)
    tk.Label(label_frame4, text="Number of Image :",                font="Times 11").place(relx = 0.01,  rely = aralik + 0.06*14)

    
    
    " Creating Combobox and Entry Widget"
    
    n = tk.StringVar() 
    featurewiseChoosen = ttk.Combobox(label_frame4, width = 10, textvariable = n)
    featurewiseChoosen['values'] = ("True", "False")
    featurewiseChoosen.place(relx = 0.6,  rely = aralik) 
    featurewiseChoosen.current()
    
    n1 = tk.StringVar() 
    samplewiseChoosen = ttk.Combobox(label_frame4, width = 10, textvariable = n1)
    samplewiseChoosen['values'] = ("True", "False")
    samplewiseChoosen.place(relx = 0.60,  rely = aralik + 0.06*1) 
    samplewiseChoosen.current()
    
    n2 = tk.StringVar() 
    featurewiseNormChoosen = ttk.Combobox(label_frame4, width = 10, textvariable = n2)
    featurewiseNormChoosen['values'] = ("True", "False")
    featurewiseNormChoosen.place(relx = 0.60,  rely = aralik + 0.06*2) 
    featurewiseNormChoosen.current()
    
    n3 = tk.StringVar() 
    samplewiseNormChoosen = ttk.Combobox(label_frame4, width = 10, textvariable = n3)
    samplewiseNormChoosen['values'] = ("True", "False")
    samplewiseNormChoosen.place(relx = 0.60,  rely = aralik + 0.06*3) 
    samplewiseNormChoosen.current()
 
    n4 = tk.StringVar() 
    verticalChoosen = ttk.Combobox(label_frame4, width = 10, textvariable = n4)
    verticalChoosen['values'] = ("True", "False")
    verticalChoosen.place(relx = 0.60,  rely = aralik + 0.06*4) 
    verticalChoosen.current()
    
    n5 = tk.StringVar() 
    horizontalChoosen = ttk.Combobox(label_frame4, width = 10, textvariable = n5)
    horizontalChoosen['values'] = ("True", "False")
    horizontalChoosen.place(relx = 0.60,  rely = aralik + 0.06*5) 
    horizontalChoosen.current()
    
    n6 = tk.StringVar() 
    fillChosen = ttk.Combobox(label_frame4, width = 10, textvariable = n6)
    fillChosen['values'] = ("constant", "nearest" , "reflect", "wrap")
    fillChosen.place(relx = 0.60,  rely = aralik + 0.06*6) 
    fillChosen.current()
    
    deger1 = tk.Entry(label_frame4, width =5 , bd =4)
    deger1.place(relx = 0.60,  rely = aralik + 0.06*7) 
    
    deger2 = tk.Entry(label_frame4, width =5, bd =4)
    deger2.place(relx = 0.60,  rely = aralik + 0.06*8)
    
    deger3 = tk.Entry(label_frame4, width =5 , bd =4)
    deger3.place(relx = 0.60,  rely = aralik + 0.06*9)
    
    deger4 = tk.Entry(label_frame4, width =5 , bd =4)
    deger4.place(relx = 0.60,  rely = aralik + 0.06*10)
    
    deger5 = tk.Entry(label_frame4, width =5 , bd =4)
    deger5.place(relx = 0.60,  rely = aralik + 0.06*11)
    
    deger6 = tk.Entry(label_frame4, width =5 , bd =4)
    deger6.place(relx = 0.60,  rely = aralik + 0.06*12)
    
    deger7 = tk.Entry(label_frame4, width =5 , bd =4)
    deger7.place(relx = 0.60,  rely = aralik + 0.06*12)
    
    deger8 = tk.Entry(label_frame4, width =5 , bd =4)
    deger8.place(relx = 0.60,  rely = aralik + 0.06*13)

    deger9 = tk.Entry(label_frame4, width =5 , bd =4)
    deger9.place(relx = 0.60,  rely = aralik + 0.06*14)
    
