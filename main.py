import tkinter as tk
from tkinter import ttk

notes = ["A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G", "G#"]

def sort_notes(note):
  "For use the other fuctions, we need to sort the notes from the key that we choose"
  s_notes = []
  i = notes.index(note)
  for x in range(i, len(notes)+i):
    s_notes.append(notes[x%len(notes)])
  return s_notes

def maj_scale(note):
  "Returns the major scale of the note that we choose"
  list = sort_notes(note)
  majlist=[list[i] for i in [0,2,4,5,7,9,11,0]]
  return majlist

def min_scale(note):
  "Returns the minor scale of the note that we choose"
  list = sort_notes(note)
  minlist=[list[i] for i in [0,2,3,5,7,8,10,0]]
  return minlist

def maj_chord(note): 
  "Returns the major chord of the note that we choose."
  "By definiton of the major chord we create major chord from the major scale"
  list = maj_scale(note)
  return [list[0],list[2],list[4]]

def min_chord(note): 
  "Returns the minor chord of the note that we choose."
  "By definiton of the minor chord we create minor chord from the minor scale" 
  list = min_scale(note)
  return [list[0],list[2],list[4]]

def relative(scale):
  "Returns the relative of the scale that we choose."
  if scale == maj_scale(scale[0]):
    return min_scale(scale[5])
  else:
    return maj_scale(scale[2])

def generate_chord():
  "Prints the chords to the label."
  note = note_var.get()
  mod = mod_var.get()
  if mod == 'Major':
      chord = maj_chord(note)
  elif mod == 'Minor':
      chord = min_chord(note)
  elif note not in notes:
      chord = ['Error']
  else:
      chord = ['Error']
  chord_label.config(text=note +" "+ mod +" Chord: " + ", ".join(chord),font=("Arial", 12, "bold"),fg="blue")

def generate_scale():
  "Prints the scales to the label."
  note = note_var.get()
  mod = mod_var.get()
  if mod == 'Major':
    scale = maj_scale(note)
  elif mod == 'Minor':
    scale = min_scale(note)
  elif note not in notes:
    scale = ['Error']
  else:
    scale = ['Error']
  scale_label.config(text=note +" " +mod +" Scale: " + ", ".join(scale),font=("Arial", 12, "bold"),fg="blue")

def generate():
  "Combine generate-scale and generate_chord for use in generate button."
  generate_scale()
  generate_chord()



# Create the main window
root = tk.Tk()
root.title("Scale/Chord Generator")

# Create a variable to store the selected note and modifier
note_var = tk.StringVar()
mod_var = tk.StringVar()

# Create and place the note dropdown menu
note_label = tk.Label(root, text="Select a note:",font=("Arial", 12, "bold"),fg="blue")
note_label.pack()
note_dropdown = ttk.Combobox(root, textvariable=note_var)
note_dropdown['values'] = ("A","Bb","B","C","C#","D","Eb","E","F","F#","G","G#")
note_dropdown.pack()

# Create and place the modifier dropdown menu
mod_label = tk.Label(root, text="Select a modifier:",font=("Arial", 12, "bold"),fg="blue")
mod_label.pack()
mod_dropdown = ttk.Combobox(root, textvariable=mod_var)
mod_dropdown['values'] = ('Major', 'Minor')
mod_dropdown.pack()

# Create and place the button to generate 
generate_button = tk.Button(root, text="Generate ", command=generate,font=("Arial", 12, "bold"),fg="blue")
generate_button.pack()

# Create and place a label to display the generated scale and chord
scale_label = tk.Label(root, text="Scale: ",font=("Arial", 12, "bold"),fg="blue")
scale_label.pack()
chord_label = tk.Label(root, text="Chord: ",font=("Arial", 12, "bold"),fg="blue")
chord_label.pack()

root.mainloop()
