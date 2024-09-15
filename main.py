import tkinter as tk
import tkinter.font as tk_font

background_color = "#B3FF00"
text_color = "#0035FF"
store_name = "20 For 20 Bookstore"
subtitle = "A bookstore for readers"
manager = "Justin Heimes"
book_catalog = {
    "Kids": {
        "No, David": "David Shannon",
        "David Goes to School": "David Shannon",
        "David Gets in Trouble": "David Shannon",
        "It's Christmas, David!": "David Shannon",
        "Grow Up, David": "David Shannon"
    },
    "Horror": {
        "It": "Stephen King",
        "The Shining": "Stephen King",
        "Cabin at the End of the World": "Paul G. Tremblay",
        "The Call of Cthulhu": "H.P. Lovecraft",
        "The Cats of Ulthar": "H.P. Lovecraft"
    },
    "Dystopian": {
        "The Hunger Games": "Suzanne Collins",
        "Catching Fire": "Suzanne Collins",
        "Mockingjay": "Suzanne Collins",
        "The Ballad of Songbirds and Snakes": "Suzanne Collins",
        "1984": "George Orwell"
    },
    "Classical": { 
        "Divine Comedy": "Dante Alighieri",
        "Meditations": "Seneca",
        "Crime and Punishment": "Fyodor Dostoevsky",
        "Animal Farm": "George Orwell",
        "The Catcher in the Rye": "J.D. Salinger" 
    }
}

global genre_search
global author_search
global title_search

# Gets the value from a search bar and updates mainpage.
# If the search bar is empty, displays all items
def search_mainpage():
    search_content = search_box.get("1.0", tk.END)
    search_content = search_content.strip()
    if(genre_search.get()):
        for key in book_catalog:
            if(key == search_content):
                label = tk.Label(text="Genre")
                label.pack(side="top", anchor="w")
    if(author_search.get()):
        for genre in book_catalog:
            for author in book_catalog[genre]:
                if(author == search_content):
                    label = tk.Label(text="Author")
                    label.pack(side="top", anchor="w")
    if(title_search.get()):
        for genre in book_catalog:
            for author in book_catalog[genre]:
                for title in book_catalog[author]:
                    if(title == search_content):
                        label = tk.Label(text="Title")
                        label.pack(side="top", anchor="w")

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
search_button = tk.Button(text="Search", height=1, command=search_mainpage)
search_button.pack(side="left", anchor="w", padx=15)
search_box = tk.Text(height=1)
search_box.pack(side="left", anchor="w", padx=15)

# Setup MenuButton
search_type = tk.Menubutton(master=main_window, text="Search Type", relief="raised")
search_type.menu = tk.Menu(search_type)
search_type["menu"] = search_type.menu

# Add Options and pack
genre_search = tk.BooleanVar()
author_search = tk.BooleanVar()
title_search = tk.BooleanVar()
search_type.menu.add_checkbutton(label="Genre", variable=genre_search)
search_type.menu.add_checkbutton(label="Author", variable=author_search)
search_type.menu.add_checkbutton(label="Title", variable=title_search)
search_type.pack(side="left", anchor="w", padx=15)

# MainLoop
main_window.mainloop()
