import tkinter as tk
from tkinter import ttk
from data import elements


# Styling configuration
FONT_TITLE = ("Helvetica", 16, "bold")
FONT_LABEL = ("Helvetica", 12)
FONT_BUTTON = ("Helvetica", 11)
FONT_RESULT = ("Courier New", 11)
BG_COLOR = "#f0f8ff"  # Alice Blue
FG_COLOR = "#003366"  # Navy Blue
BUTTON_COLOR = "#6699cc"
BUTTON_TEXT_COLOR = "white"


def search_element(query):
    query = str(query).lower()
    for element in elements.values():
        if (
            str(element['atomic_number']) == query or
            element['name'].lower() == query or
            element['symbol'].lower() == query
        ):
            return element
    return None


def filter_by_category(category):
    return [el for el in elements.values() if el['category'].lower() == category.lower()]


def filter_by_group(group_number):
    return [el for el in elements.values() if el['group'] == group_number]


def display_element(element):
    output_text.set(
        f"Name: {element['name']}\n"
        f"Symbol: {element['symbol']}\n"
        f"Atomic Number: {element['atomic_number']}\n"
        f"Atomic Mass: {element['atomic_mass']}\n"
        f"Group: {element['group']}\n"
        f"Period: {element['period']}\n"
        f"Category: {element['category']}"
    )


def search_callback():
    query = search_entry.get()
    result = search_element(query)
    if result:
        display_element(result)
    else:
        output_text.set("Element not found.")


def category_callback():
    category = category_combo.get()
    results = filter_by_category(category)
    if results:
        output_text.set(f"{len(results)} element(s) found in '{category}':\n" +
                        "\n\n".join([f"{e['name']} ({e['symbol']})" for e in results]))
    else:
        output_text.set("No elements found in that category.")


def group_callback():
    try:
        group = int(group_entry.get())
        results = filter_by_group(group)
        if results:
            output_text.set(f"{len(results)} element(s) found in Group {group}:" "\n"+
                            "\n\n".join([f"{e['name']} ({e['symbol']})" for e in results]))
        else:
            output_text.set("No elements found in that group.")
    except ValueError:
        output_text.set("Please enter a valid group number.")

def draw_periodic_table(frame):
    layout=layout = {
        # Period 1
        "H": (0, 0), "He": (0, 17),
        
        # Period 2
        "Li": (1, 0), "Be": (1, 1), 
        "B": (1, 12), "C": (1, 13), "N": (1, 14), "O": (1, 15), "F": (1, 16), "Ne": (1, 17),
        
        # Period 3
        "Na": (2, 0), "Mg": (2, 1),
        "Al": (2, 12), "Si": (2, 13), "P": (2, 14), "S": (2, 15), "Cl": (2, 16), "Ar": (2, 17),
        
        # Period 4
        "K": (3, 0), "Ca": (3, 1),
        "Sc": (3, 2), "Ti": (3, 3), "V": (3, 4), "Cr": (3, 5), "Mn": (3, 6), "Fe": (3, 7), 
        "Co": (3, 8), "Ni": (3, 9), "Cu": (3, 10), "Zn": (3, 11),
        "Ga": (3, 12), "Ge": (3, 13), "As": (3, 14), "Se": (3, 15), "Br": (3, 16), "Kr": (3, 17),
        
        # Period 5
        "Rb": (4, 0), "Sr": (4, 1),
        "Y": (4, 2), "Zr": (4, 3), "Nb": (4, 4), "Mo": (4, 5), "Tc": (4, 6), "Ru": (4, 7),
        "Rh": (4, 8), "Pd": (4, 9), "Ag": (4, 10), "Cd": (4, 11),
        "In": (4, 12), "Sn": (4, 13), "Sb": (4, 14), "Te": (4, 15), "I": (4, 16), "Xe": (4, 17),
        
        # Period 6
        "Cs": (5, 0), "Ba": (5, 1),
        # Lanthanides
        "La": (5, 2), "Ce": (8, 3), "Pr": (8, 4), "Nd": (8, 5), "Pm": (8, 6), "Sm": (8, 7),
        "Eu": (8, 8), "Gd": (8, 9), "Tb": (8, 10), "Dy": (8, 11), "Ho": (8, 12), "Er": (8, 13),
        "Tm": (8, 14), "Yb": (8, 15), "Lu": (8, 16),
        # Transition metals
        "Hf": (5, 3), "Ta": (5, 4), "W": (5, 5), "Re": (5, 6), "Os": (5, 7), "Ir": (5, 8),
        "Pt": (5, 9), "Au": (5, 10), "Hg": (5, 11),
        "Tl": (5, 12), "Pb": (5, 13), "Bi": (5, 14), "Po": (5, 15), "At": (5, 16), "Rn": (5, 17),
        
        # Period 7
        "Fr": (6, 0), "Ra": (6, 1),
        # Actinides
        "Ac": (6, 2), "Th": (9, 3), "Pa": (9, 4), "U": (9, 5), "Np": (9, 6), "Pu": (9, 7),
        "Am": (9, 8), "Cm": (9, 9), "Bk": (9, 10), "Cf": (9, 11), "Es": (9, 12), "Fm": (9, 13),
        "Md": (9, 14), "No": (9, 15), "Lr": (9, 16),
        # Transition metals
        "Rf": (6, 3), "Db": (6, 4), "Sg": (6, 5), "Bh": (6, 6), "Hs": (6, 7), "Mt": (6, 8),
        "Ds": (6, 9), "Rg": (6, 10), "Cn": (6, 11),
        "Nh": (6, 12), "Fl": (6, 13), "Mc": (6, 14), "Lv": (6, 15), "Ts": (6, 16), "Og": (6, 17)
    }
    # Color mapping by category
    category_colors = {
        "Noble Gas": "#ffd700",
        "Nonmetal": "#90ee90",
        "Alkali Metal": "#ff4500",
        "Alkaline Earth Metal": "#ffa500",
        "Metalloid": "#dda0dd",
        "Halogen": "#1e90ff",
        "Metal": "#d3d3d3"
    }

    for symbol, pos in layout.items():
        if symbol in elements:
            el = elements[symbol]
            color = category_colors.get(el["category"], "#cccccc")
            btn = tk.Button(
                frame, text=symbol, width=4, height=2,
                bg=color, font=("Helvetica", 10, "bold"),
                command=lambda e=el: display_element(e)
            )
            btn.grid(row=pos[0], column=pos[1], padx=1, pady=1)

def open_periodic_table_window():
    # Create new window
    table_window = tk.Toplevel(root)
    table_window.title("Periodic Table")
    table_window.configure(bg=BG_COLOR)
    
    # Add title label
    tk.Label(table_window, 
             text="🧪 Periodic Table View", 
             font=FONT_TITLE, 
             bg=BG_COLOR, 
             fg=FG_COLOR).pack(pady=(20, 5))
    
    # Create frame for the table
    grid_frame = tk.Frame(table_window, bg=BG_COLOR)
    grid_frame.pack(pady=10)
    
    # Draw the periodic table
    draw_periodic_table(grid_frame)


# ---------------- GUI Setup ---------------- #

root = tk.Tk()
root.title("🧪 Periodic Table Explorer")
root.geometry("650x600")
root.configure(bg=BG_COLOR)


tk.Label(root, text="🔍 Search Element", font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR).pack(pady=(10, 5))

search_frame = tk.Frame(root, bg=BG_COLOR)
search_frame.pack(pady=5)
search_entry = tk.Entry(search_frame, width=30, font=FONT_LABEL)
search_entry.pack(side="left", padx=5)
tk.Button(search_frame, text="Search", font=FONT_BUTTON, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, command=search_callback).pack(side="left")

tk.Label(root, text="📂 Filter by Category", font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR).pack(pady=(20, 5))
category_frame = tk.Frame(root, bg=BG_COLOR)
category_frame.pack(pady=5)
category_combo = ttk.Combobox(category_frame, values=['Alkali Metal', 'Alkaline Earth Metal', 'Transition Metal', 'Post-Transition Metal', 
 'Metalloid', 'Nonmetal', 'Halogen', 'Noble Gas', 'Lanthanide', 'Actinide'], font=FONT_LABEL, state="readonly")
category_combo.pack(side="left", padx=5)
tk.Button(category_frame, text="Filter", font=FONT_BUTTON, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, command=category_callback).pack(side="left")

tk.Label(root, text="🔢 Filter by Group", font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR).pack(pady=(20, 5))
group_frame = tk.Frame(root, bg=BG_COLOR)
group_frame.pack(pady=5)
group_entry = tk.Entry(group_frame, width=10, font=FONT_LABEL)
group_entry.pack(side="left", padx=5)
tk.Button(group_frame, text="Filter", font=FONT_BUTTON, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, command=group_callback).pack(side="left")

output_text = tk.StringVar()

tk.Button(root, 
          text="Show Periodic Table", 
          command=open_periodic_table_window,
          bg=BUTTON_COLOR,  # You can define this color
          fg=FG_COLOR).pack(pady=20)


# Output Section
tk.Label(root, text="📋 Results", font=FONT_TITLE, bg=BG_COLOR, fg=FG_COLOR).pack(pady=(20, 5))
output_label = tk.Label(
    root, textvariable=output_text,
    font=FONT_RESULT, justify="left",
    wraplength=600, bg="white",
    fg="black", relief="solid",
    anchor="nw", bd=2, padx=10, pady=10
)
output_label.pack(fill="both", expand=True, padx=20, pady=10)


root.mainloop()
