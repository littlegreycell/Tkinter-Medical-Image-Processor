def search_metadata():
    search_text = search_var.get().lower()
    listBox.delete(0, tk.END)  # Mevcut listeyi temizle
    for item in metadata_list:
        if search_text in item.lower():
            listBox.insert(tk.END, item)

def reset_search():
    search_var.set("")
    listBox.delete(0, tk.END)
    for item in metadata_list:
        listBox.insert(tk.END, item)

# read metadata file information

metadata_list = []  
        
def load_metadata():
    global metadata_list
    try:
        ds = pydicom.filereader.dcmread("C:\\Users\\SuleBesteKapci\\Desktop\\DOSYALARIM\\ProjeCalismam\\dicomimg-20231230T203506Z-001\\dicomimg\\000007.dcm")
        metadata_list.clear()
        listBox.delete(0, tk.END)
        for elem in ds:
            tag = str(elem.tag)
            name = elem.name.replace(" ", "_")
            value = str(elem.value)[:50]
            display_text = f"{tag} {name}: {value}"
            metadata_list.append(display_text)
            listBox.insert(tk.END, display_text)
    except Exception as e:
        listBox.insert(tk.END, f"Hata: {str(e)}")
