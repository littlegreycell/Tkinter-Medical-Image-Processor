" WINDOW-3 - Filter Gallery"
def imageFileFilters():

    thirdWindow = tk.Toplevel()
    thirdWindow.geometry("700x560") 
    thirdWindow.wm_title("Filter Gallery") 

    frameLEFT= tk.Frame(thirdWindow, width = 350, height = 500 ) 
    frameLEFT.grid(row=0 , column=0 )

    frameRIGHT = tk.Frame(thirdWindow, width=350, height=500  )
    frameRIGHT.grid (row=0, column=1)

    frameBOTTOM = tk.Frame(thirdWindow, width = 700, height = 60 )
    frameBOTTOM.grid(row=1, column =0, columnspan=2)

    labelLeft = tk.LabelFrame(frameLEFT, width=346, height=494)
    labelLeft.grid(row = 0, column = 0, padx=2, pady=3)

    labelRight= tk.LabelFrame(frameRIGHT, width = 346, height=494)
    labelRight.grid(row=0, column =1, padx=2, pady=3)

    labelBottom = tk.LabelFrame(frameBOTTOM,width = 696, height=56 )
    labelBottom.grid(row=1, column=0, columnspan=2 ,padx=2, pady=2)


    #List the contents of the file

    listBox = tk.Listbox(labelLeft,width = 38, height = 23) 
    listBox.pack(side = tk.LEFT, fill = tk.BOTH )
    scrollbar2 = tk.Scrollbar(labelLeft,  orient = tk.VERTICAL,  command = listBox.yview) 
    scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)
    scrollbar2.config(command=listBox.yview) 
    listBox.config(yscrollcommand =scrollbar2.set)

    #Labels
    
    aralik = 0.01
    tk.Label(labelRight, text="Size of Image",           font="Times 11").place(relx = 0.2 , rely = aralik)
    tk.Label(labelRight, text="Median",               font="Times 11").place(relx = 0.2 , rely = aralik + 0.06*1)
    tk.Label(labelRight, text="Min",                  font="Times 11").place(relx = 0.2 , rely = aralik + 0.06*2)
    tk.Label(labelRight, text="Max",                  font="Times 11").place(relx = 0.2 , rely = aralik + 0.06*3)
    tk.Label(labelRight, text="Gaussian"  ,           font="Times 11").place(relx = 0.2 , rely = aralik + 0.06*4)
    tk.Label(labelRight, text="Gama Transform",       font="Times 11").place(relx = 0.2 , rely = aralik + 0.06*5)
    tk.Label(labelRight, text="Opening",              font="Times 11").place(relx = 0.2 , rely = aralik + 0.06*6)
    tk.Label(labelRight, text="Closing",              font="Times 11").place(relx = 0.2 , rely = aralik + 0.06*7)
    tk.Label(labelRight, text="Erosion",              font="Times 11").place(relx = 0.2 , rely = aralik + 0.06*8)
    tk.Label(labelRight, text="Dilation",             font="Times 11").place(relx = 0.2 , rely = aralik + 0.06*9)
    tk.Label(labelRight, text="Adaptive His.",        font="Times 11").place(relx = 0.2 , rely = aralik + 0.06*10)
    tk.Label(labelRight, text="Negative",             font="Times 11").place(relx = 0.2 , rely = aralik + 0.06*11)


    # Creating combobox
    
    durum1 = tk.StringVar() 
    durum1Choosen = ttk.Combobox(labelRight, width = 3, textvariable = durum1)
    durum1Choosen['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
    durum1Choosen.place(relx = 0.01,  rely = aralik + 0.06*1 ) 
    durum1Choosen.current()
    
    durum2 = tk.StringVar() 
    durum2Choosen = ttk.Combobox(labelRight, width = 3, textvariable = durum2)
    durum2Choosen['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
    durum2Choosen.place(relx = 0.01,  rely = aralik + 0.06*2) 
    durum2Choosen.current()
    
    durum3 = tk.StringVar() 
    durum3Choosen = ttk.Combobox(labelRight, width = 3, textvariable = durum3)
    durum3Choosen['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
    durum3Choosen.place(relx = 0.01,  rely = aralik + 0.06*3) 
    durum3Choosen.current()
    
    durum4 = tk.StringVar() 
    durum4Choosen = ttk.Combobox(labelRight, width = 3, textvariable = durum4)
    durum4Choosen['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
    durum4Choosen.place(relx = 0.01,  rely = aralik + 0.06*4) 
    durum4Choosen.current()
    
    durum5 = tk.StringVar() 
    durum5Choosen = ttk.Combobox(labelRight, width = 3, textvariable = durum5)
    durum5Choosen['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
    durum5Choosen.place(relx = 0.01,  rely = aralik + 0.06*5) 
    durum5Choosen.current()
    
    durum6 = tk.StringVar() 
    durum6Choosen = ttk.Combobox(labelRight, width = 3, textvariable = durum6)
    durum6Choosen['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
    durum6Choosen.place(relx = 0.01,  rely = aralik + 0.06*6) 
    durum6Choosen.current()
    
    durum7 = tk.StringVar() 
    durum7Choosen = ttk.Combobox(labelRight, width = 3, textvariable = durum7)
    durum7Choosen['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
    durum7Choosen.place(relx = 0.01,  rely = aralik + 0.06*7) 
    durum7Choosen.current()
    
    durum8 = tk.StringVar() 
    durum8Choosen = ttk.Combobox(labelRight, width = 3, textvariable = durum8)
    durum8Choosen['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
    durum8Choosen.place(relx = 0.01,  rely = aralik + 0.06*8) 
    durum8Choosen.current()
    
    durum9 = tk.StringVar() 
    durum9Choosen = ttk.Combobox(labelRight, width = 3, textvariable = durum9)
    durum9Choosen['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
    durum9Choosen.place(relx = 0.01,  rely = aralik + 0.06*9) 
    durum9Choosen.current()
    
    durum10 = tk.StringVar() 
    durum10Choosen = ttk.Combobox(labelRight, width =3, textvariable = durum10)
    durum10Choosen['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
    durum10Choosen.place(relx = 0.01,  rely = aralik + 0.06*10) 
    durum10Choosen.current()
    
    durum11 = tk.StringVar() 
    durum11Choosen = ttk.Combobox(labelRight, width =3, textvariable = durum11)
    durum11Choosen['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
    durum11Choosen.place(relx = 0.01,  rely = aralik + 0.06*11) 
    durum11Choosen.current()


    # Creating entry box
    
    degerSize1 = tk.Entry(labelRight, width =4 , bd =4)
    degerSize1.place(relx = 0.65,  rely = aralik)
    
    degerSize2 = tk.Entry(labelRight, width =4 , bd =4)
    degerSize2.place(relx = 0.75,  rely = aralik)
    
    degerMedian = tk.Entry(labelRight, width =5, bd =4)
    degerMedian.place(relx = 0.65,  rely = aralik + 0.06*1)
        
    degerMin = tk.Entry(labelRight, width =5 , bd =4)
    degerMin.place(relx = 0.65,  rely = aralik + 0.06*2)
        
    degerMax = tk.Entry(labelRight, width =5 , bd =4)
    degerMax.place(relx = 0.65,  rely = aralik + 0.06*3)
        
    degerGaussian = tk.Entry(labelRight, width =5 , bd =4)
    degerGaussian.place(relx = 0.65,  rely = aralik + 0.06*4)
        
    degerGama = tk.Entry(labelRight, width =5 , bd =4)
    degerGama.place(relx = 0.65,  rely = aralik + 0.06*5)
        
    degerOpening = tk.Entry(labelRight, width =5 , bd =4)
    degerOpening.place(relx = 0.65,  rely = aralik + 0.06*6)
        
    degerClosing = tk.Entry(labelRight, width =5 , bd =4)
    degerClosing.place(relx = 0.65,  rely = aralik + 0.06*7)
    
    degerErosion = tk.Entry(labelRight, width =5 , bd =4)
    degerErosion.place(relx = 0.65,  rely = aralik + 0.06*8)
    
    degerDilation = tk.Entry(labelRight, width =5 , bd =4)
    degerDilation.place(relx = 0.65,  rely = aralik + 0.06*9)

    histogram = tk.StringVar() 
    histogramChoosen = ttk.Combobox(labelRight, width = 10, textvariable = histogram)
    histogramChoosen['values'] = ("Uygula")
    histogramChoosen.place(relx = 0.65 , rely =  aralik + 0.06*10) 
    histogramChoosen.current()
        
    negative = tk.StringVar() 
    negativeChoosen = ttk.Combobox(labelRight, width = 10, textvariable = negative)
    negativeChoosen['values'] = ("Uygula")
    negativeChoosen.place(relx = 0.65,  rely = aralik + 0.06*11) 
    negativeChoosen.current()

    def openFolder():
        pass

    def save():
        pass
    
    def apply():
        pass
                
    buttonOpenProcessing = tk.Button(labelBottom, text = "Open Folder", command=openFolder )
    buttonOpenProcessing.place(relx = 0.25, rely = 0.15  )
    buttonKayitProcessing = tk.Button(labelBottom, text ="Save", command=save)
    buttonKayitProcessing.place(relx = 0.41 , rely = 0.15 )
    buttonCreateProcessing = tk.Button(labelBottom, text="Apply", command = apply)
    buttonCreateProcessing.place(relx = 0.60, rely = 0.15 )
