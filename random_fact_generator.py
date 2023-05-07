import random
import tkinter as tk

def read_facts(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

def get_random_fact(facts):
    return random.choice(facts)

def display_fact():
    random_fact = get_random_fact(facts)
    fact_label.config(text=random_fact)

facts_file_path = "facts.txt"
facts = read_facts(facts_file_path)

app = tk.Tk()
app.title("Random Fact Generator")

fact_label = tk.Label(app, text="", wraplength=300, justify=tk.LEFT)
fact_label.pack(padx=20, pady=20)

button = tk.Button(app, text="Generate Fact", command=display_fact)
button.pack(pady=10)

app.mainloop()
