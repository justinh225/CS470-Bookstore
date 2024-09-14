import tkinter as tk
import tkinter.font as tk_font

global search_type

background_color = "#B3FF00"
text_color = "#0035FF"
store_name = "20 For 20 Bookstore"
subtitle = "A bookstore for readers"
manager = "Justin Heimes"
book_catalog = {
    "Kids": [ {
        "No, David": "David Shannon",
        "David Goes to School": "David Shannon",
        "David Gets in Trouble": "David Shannon",
        "It's Christmas, David!": "David Shannon",
        "Grow Up, David": "David Shannon"
    }],
    "Horror": [{
        "It": "Stephen King",
        "The Shining": "Stephen King",
        "Cabin at the End of the World": "Paul G. Tremblay",
        "The Call of Cthulhu": "H.P. Lovecraft",
        "The Cats of Ulthar": "H.P. Lovecraft"
    }],
    "Dystopian": [{
        "The Hunger Games": "Suzanne Collins",
        "Catching Fire": "Suzanne Collins",
        "Mockingjay": "Suzanne Collins",
        "The Ballad of Songbirds and Snakes": "Suzanne Collins",
        "1984": "George Orwell"
    }],
    "Classical": [{ 
        "Divine Comedy": "Dante Alighieri",
        "Meditations": "Seneca",
        "Crime and Punishment": "Fyodor Dostoevsky",
        "Animal Farm": "George Orwell",
        "The Catcher in the Rye": "J.D. Salinger" 
    }]
}

# Gets the value from a search bar and updates mainpage.
# If the search bar is empty, displays all items
def search_mainpage():
    search_string = search_box.get()


#Setup Window
main_window = tk.Tk()
main_window.title(store_name)
main_window.geometry = ('700x700')
main_window.configure(background=background_color)
main_window.resizable(width=False, height=False)

# Setup Fonts
title_font = tk_font.Font(family="Arial", size=34)
subtitle_font = tk_font.Font(family="Arial", size=24)
heading_font = tk_font.Font(family="Arial", size=12)

# Init Header Text
title_label = tk.Label(text = store_name, font=title_font, foreground=text_color, background=background_color)
subtitle_label = tk.Label(text=subtitle, font=subtitle_font, foreground=text_color, background=background_color)
heading_label = tk.Label(text=manager, font=heading_font, foreground=text_color, background=background_color)
title_label.pack(side="top")
subtitle_label.pack(side="top")
heading_label.pack(side="top")

# Add Search Bar
search_button = tk.Button(text="Search", height=1)
search_button.pack(side="left", anchor="w", padx=15)
search_box = tk.Text(height=1)
search_box.pack(side="left", anchor="w", padx=15)
search_menu = tk.Menu()

search_menu.add_radiobutton(label="Genre")
search_menu.add_radiobutton(label="Author")
search_menu.add_radiobutton(label="Title")
search_type = tk.Menubutton(text="Search Type", relief="raised", menu=search_menu)
search_type.pack(side="left", anchor="w", padx=15)

main_window.mainloop()


