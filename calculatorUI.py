import tkinter as tk
import csv
from tkinter import filedialog
import pickle
# calculate the clothing size, change the code to calculate the size correctly,the M in size is just a default
def calculate_size():
  # Get the user's input values
  chest = float(chest_entry.get())
  waist = float(waist_entry.get())
  hips = float(hips_entry.get())
  #Loading and interpreting the model
  size_key = {'0': 'L', '1': 'M', '2': 'S', '3': 'XL'}
  tree = pickle.load(open('TreeModel.pkl', 'rb'))
  size = size_key[str(tree.predict([[chest, waist, hips]])[0])]
  size_label.config(text=f"Recommended size: {size}")

# avaliable the user to import the data, if you need can change the code 
def import_data():
  file_path = filedialog.askopenfilename()
  with open(file_path, "r") as f:
    lines = f.readlines()
    chest_entry.delete(0, tk.END)
    chest_entry.insert(0, lines[0].strip())
    waist_entry.delete(0, tk.END)
    waist_entry.insert(0, lines[1].strip())
    hips_entry.delete(0, tk.END)
    hips_entry.insert(0, lines[2].strip())


#create the main window
window = tk.Tk()
window.title("Clothing Size Calculaor")

#create the user input field
chest_label = tk.Label(window,text = "Chest (inches):")
chest_label.grid(row=0, column=0, padx=10, pady=10)
chest_entry = tk.Entry(window)
chest_entry.grid(row=0, column=1, padx=10, pady=10)

waist_label = tk.Label(window,text = "waist (inches):")
waist_label.grid(row=1, column=0, padx=10, pady=10)
waist_entry = tk.Entry(window)
waist_entry.grid(row=1, column=1, padx=10, pady=10)

hips_label = tk.Label(window,text = "hips (inches):")
hips_label.grid(row=2, column=0, padx=10, pady=10)
hips_entry = tk.Entry(window)
hips_entry.grid(row=2, column=1, padx=10, pady=10)

#create the import button
import_button = tk.Button(window, text="Import data", command=import_data)
import_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

#create the calculate button
calculate_button = tk.Button(window, text="Calculate",command=calculate_size)
calculate_button.grid(row=5,column=0,columnspan=2,padx=10,pady=10)

#create the output lable
size_label = tk.Label(window,text ="")
size_label.grid(row=7,column=0,columnspan=2,padx=10,pady=10)

window.mainloop()
