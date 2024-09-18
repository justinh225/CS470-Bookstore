import tkinter as tk
import tkinter.font as tk_font

global genre_search
global author_search
global title_search
global display_frame
global cart
global cart_listbox

background_color = "#B3FF00"
text_color = "#0035FF"
store_name = "20 For 20 Bookstore"
subtitle = "A bookstore for readers"
manager = "Justin Heimes"

#Setup Window
main_window = tk.Tk()
main_window.title(store_name)
main_window.geometry = ('700x700')
#main_window.maxsize(height="1000", width="1900")
main_window.configure(background=background_color)
main_window.resizable(width=False, height=False)

cart = list()
cart.append(("Test", tk.IntVar(value=0)))
book_catalog = {
    "Kids": {
        "David Shannon": [ ("No, David", tk.PhotoImage(file="Assets\\david_no.ppm", height=200, width=155), tk.IntVar()),
                           ("David Goes to School",  tk.PhotoImage(file="Assets\\david_school.ppm", height=200, width=155), tk.IntVar()),
                           ("David Gets in Trouble", tk.PhotoImage(file="Assets\\david_trouble.ppm", height=200, width=155), tk.IntVar()),
                           ("It's Christmas, David!", tk.PhotoImage(file="Assets\\david_christmas.ppm", height=200, width=155), tk.IntVar()),
                           ("Grow Up, David", tk.PhotoImage(file="Assets\\david_grow.ppm", height=200, width=155), tk.IntVar())]
    },
    "Horror": {
        "Stephen King": [ ("It", tk.PhotoImage(file="Assets\\it.ppm", height=200, width=155), tk.IntVar()), 
                          ("The Shining", tk.PhotoImage(file="Assets\\shining.ppm", height=200, width=155), tk.IntVar())],
        "Paul G. Tremblay": [ ("Cabin at the End of the World", tk.PhotoImage(file="Assets\\cabin.ppm", height=200, width=155), tk.IntVar()) ],
        "H.P Lovecraft": [ ("The Call of Cthulhu", tk.PhotoImage(file="Assets\\cthulu.ppm", height=200, width=155), tk.IntVar()), 
                           ("The Cats of Ulthar", tk.PhotoImage(file="Assets\\ulthar.ppm", height=200, width=155), tk.IntVar()) ]
    },
    "Dystopian": {
        "Suzanne Collins": [ 
            ("The Hunger Games", tk.PhotoImage(file="Assets\\hunger.ppm", height=200, width=155), tk.IntVar()),
            ("Catching Fire", tk.PhotoImage(file="Assets\\fire.ppm", height=200, width=155), tk.IntVar()), 
            ("Mockingjay", tk.PhotoImage(file="Assets\\mockingjay.ppm", height=200, width=155), tk.IntVar()),
            ("The Ballad of Songbirds and Snakes", tk.PhotoImage(file="Assets\\ballad.ppm", height=200, width=155), tk.IntVar()) ],
        "George Orwell": [ ("1984", tk.PhotoImage(file="Assets\\1984.ppm", height=200, width=155), tk.IntVar()) ]
    },
    "Classical": { 
        "Dante Alighieri": [ ("Divine Comedy", tk.PhotoImage(file="Assets\\comedy.ppm", height=200, width=155), tk.IntVar()) ],
        "Marcus Aurelias": [ ("Meditations", tk.PhotoImage(file="Assets\\meditations.ppm", height=200, width=155), tk.IntVar()) ],
        "Fyodor Dostoevsky": [ ("Crime and Punishment", tk.PhotoImage(file="Assets\\crime.ppm", height=200, width=155), tk.IntVar()) ],
        "George Orwell": [ ("Animal Farm", tk.PhotoImage(file="Assets\\animal.ppm", height=200, width=155), tk.IntVar()) ],
        "J.D. Salinger": [ ("The Catcher in the Rye", tk.PhotoImage(file="Assets\\catcher.ppm", height=200, width=155), tk.IntVar()) ] 
    }
}

# Gets the value from a search bar and updates mainpage.
# If the search bar is empty, displays all items
def search_mainpage():
    # Get the search content
    search_content = search_box.get("1.0", tk.END)
    search_content = search_content.strip()

    # Clear display
    while list(display_frame.children.keys()):
        key = list(display_frame.children.keys())[0]
        display_frame.children[key].destroy()

    # Search and update the display
    # Search genre
    if(genre_search.get()):
        for key in book_catalog:
            if(key == search_content):
                genre_frame = tk.Frame(master=display_frame, background=background_color)
                genre_label = tk.Label(master=genre_frame, foreground=text_color, background=background_color, font=subtitle_font, padx="5", text=key)
                genre_label.pack(side="top", anchor="w")
                for author in book_catalog[key]:
                    for title in book_catalog[key][author]:
                        title_frame = tk.Frame(master=genre_frame, background=background_color)
                        image_label = tk.Label(master=title_frame, image=title[1], background=background_color)
                        title_label = tk.Label(master=title_frame, foreground=text_color, background=background_color, font=heading_font, text=title[0])
                        add_cart_button = tk.Checkbutton(master=title_frame, variable=title[2], name="select_button")
                        image_label.pack(side = "top")
                        title_label.pack(side = "top")
                        add_cart_button.pack(side = "top")
                        title_frame.pack(side="left")
                genre_frame.pack(side="top")
    # Search authors
    if(author_search.get()):
        for key in book_catalog:
            genre_frame = tk.Frame(master=display_frame, background=background_color)
            genre_label = tk.Label(master=genre_frame, foreground=text_color, background=background_color, font=subtitle_font, padx="5", text=key)
            genre_label.pack(side="top", anchor="w")
            for author in book_catalog[key]:
                if(author == search_content):
                    for title in book_catalog[key][author]:
                        title_frame = tk.Frame(master=genre_frame, background=background_color)
                        image_label = tk.Label(master=title_frame, image=title[1], background=background_color)
                        title_label = tk.Label(master=title_frame, foreground=text_color, background=background_color, font=heading_font, text=title[0])
                        add_cart_button = tk.Checkbutton(master=title_frame, variable=title[2], name="select_button")
                        image_label.pack(side = "top")
                        title_label.pack(side = "top")
                        add_cart_button.pack(side = "top")
                        title_frame.pack(side="left", padx=20)
            genre_frame.pack(side="top")
    # Search title
    if(title_search.get()):
        for key in book_catalog:
            genre_frame = tk.Frame(master=display_frame, background=background_color)
            genre_label = tk.Label(master=genre_frame, foreground=text_color, background=background_color, font=subtitle_font, padx="5", text=key)
            genre_label.pack(side="top", anchor="w")
            for author in book_catalog[key]:
                    for title in book_catalog[key][author]:
                        if(title[0] == search_content):
                            title_frame = tk.Frame(master=genre_frame, background=background_color)
                            image_label = tk.Label(master=title_frame, image=title[1], background=background_color)
                            title_label = tk.Label(master=title_frame, foreground=text_color, background=background_color, font=heading_font, text=title[0])
                            add_cart_button = tk.Checkbutton(master=title_frame, variable=title[2], name="select_button")
                            image_label.pack(side = "top")
                            title_label.pack(side = "top")
                            add_cart_button.pack(side = "top")
                            title_frame.pack(side="left", padx=20)
            genre_frame.pack(side="top")

def add_to_cart():
    for key in book_catalog:
        for author in book_catalog[key]:
            for title in book_catalog[key][author]:
                if(title[2].get() == 1 and cart.count(title[0]) <= 0):
                    cart.append((title[0], tk.IntVar()))

def view_cart():
    # Setup Cart Window
    cart_window = tk.Toplevel(background=background_color)
    cart_window.resizable(width=False, height=False)
    cart_window.maxsize(height=500, width=700)
    
    # Setup Label
    cart_label = tk.Label(master=cart_window, text="Your Cart:", foreground=text_color, background=background_color)
    cart_label.pack(side="top")

    # Setup Listbox
    cart_listbox = tk.Listbox(master=cart_window, selectmode=tk.MULTIPLE, foreground=text_color)
    index = 0
    for title in cart:
        cart_listbox.insert(index, title[0])
    cart_listbox.pack(side="top")

    # Setup Price
    price = cart.__len__() * 20
    price_label = tk.Label(master=cart_window, text="Total: $" + price.__str__() + ".00")
    price_label.pack(side="top")

    # Setup Buttons
    remove_from_cart = tk.Button(master=cart_window, text="Remove Selected")
    remove_from_cart.pack(side="left")
    empty_cart_button = tk.Button(master=cart_window, text="Empty Cart", command= lambda:empty_cart(cart_listbox, price_label))
    empty_cart_button.pack(side="left")
    checkout_button = tk.Button(master=cart_window, text="Checkout")
    checkout_button.pack(side="left")

def empty_cart(list_box, total_label):
    cart.clear()
    list_box.delete(0, tk.END)
    total_label['text'] = "Total: $0.00"
    

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
search_frame = tk.Frame(main_window, background=background_color)
search_button = tk.Button(master=search_frame, text="Search", height=1, command=search_mainpage)
search_button.pack(side="left", anchor="w", padx=15)
search_box = tk.Text(master=search_frame, height=1)
search_box.pack(side="left", anchor="w", padx=15)

# Setup MenuButton
search_type = tk.Menubutton(master=search_frame, text="Search Type", relief="raised")
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
search_frame.pack(side="top")

# Add Container for book display
display_scroll = tk.Scrollbar(master=main_window)
display_scroll.pack(side="right", fill="y")

display_canvas = tk.Canvas(main_window, background=background_color, height=800, yscrollcommand=display_scroll.set)
display_canvas.pack(side="top")

# Add default display
for key in book_catalog:
    genre_frame = tk.Frame(master=display_canvas, background=background_color)
    genre_label = tk.Label(master=genre_frame, foreground=text_color, background=background_color, font=subtitle_font, padx="5", text=key)
    genre_label.pack(side="top", anchor="w")

    for author in book_catalog[key]:
        for title in book_catalog[key][author]:
            title_frame = tk.Frame(master=genre_frame, background=background_color)
            image_label = tk.Label(master=title_frame, image=title[1], background=background_color)
            title_label = tk.Label(master=title_frame, name="title", foreground=text_color, background=background_color, font=heading_font, text=title[0])
            select_title_button = tk.Checkbutton(master=title_frame, variable=title[2], name="select_button")
            image_label.pack(side = "top")
            title_label.pack(side = "top")
            select_title_button.pack(side = "top")
            title_frame.pack(side="left", padx=20)
    genre_frame.pack(side="top")

select_title_button = tk.Button(master=main_window, text="Add to Cart", command=add_to_cart)
select_title_button.pack(side="left", anchor="center")

view_cart_button = tk.Button(master=main_window, text="View Cart/Checkout", command=view_cart)
view_cart_button.pack(side="left", anchor="center")
    

# MainLoop
main_window.mainloop()
