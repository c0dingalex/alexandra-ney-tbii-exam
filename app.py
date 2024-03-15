import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import datetime
from src.helpers import add_image, clear_widgets, create_close_button
import random


# create the GUI
root = tk.Tk()
# update the title of the GUI
root.title("\U0001F331 Your Sustainability Score Tracker \U0001F331")

# size the frame
# set the height and width as separate parameters to give more flexibility
screen_width = 1000
screen_height = 530

root.minsize(width=screen_width, height=screen_height)  # width, height


def create_homepage_button():
    homepage = tk.Button(root,
                         text="\U0001F3E0",
                         command=lambda: create_homepage(root)
                         )
    homepage.place(x=43, y=33)

# list with several tips on sustainability
sustainable_tips = [
    "\U0001F6AE \n CLEAN UP YOUR ENVIRONMENT:\n Use what you need, and when you \n have to throw something out,\ndispose of it properly.",
    "\U0001F6EB \n CONSIDER YOUR TRAVEL:\n Taking one less long-haul return flight \n can reduce your carbon footprint by \n up to almost 2 tons of CO2e.",
    "\U0001F4A1 \n CHANGE YOUR HOME'S SOURCE OF ENERGY:\n Switching your home from oil, gas or \n coal-powered energy to renewable sources \n of energy, such as wind or solar, \n can reduce your carbon footprint by \n up to 1.5 tons of CO2e per year.",
    "\U0001F50B \n SAVE ENERGY AT HOME:\n Improving your home’s energy efficiency, \n through better insulation for instance, \n or replacing your oil or gas furnace \n with an electric heat pump can reduce \n your carbon footprint by up to 900 kilograms \n of CO2e per year.",
    "\U0001F959 \n THROW AWAY LESS FOOD:\n Cutting your food waste can reduce \n your carbon footprint by up to \n 300 kilograms of CO2e per year.",
    "\U0001F4B8 \n MAKE YOUR MONEY COUNT: \n You have the power to choose \n which goods and services you support. \n To reduce your environmental impact,\n choose products from companies who use \n resources responsibly and are committed to \n cutting their gas emissions and waste.",
    "\U0001FAB4 \n PLANT NATIVE SPECIES:\n  Plants, animals and insects depend on each\nother. Most insects will not eat non-native\nplants, which means birds and other species\nlose a food source. Biodiversity suffers.\nEven a single tree or shrub can offer a refuge. ",
]

# Set a variable so that later on every displayed tip gets removed
# before the next one is displayed
current_tip_label = None

def display_random_tip():
    """This definition displays a random tip from the list above ata specified position."""
    global current_tip_label

    if current_tip_label:
        current_tip_label.destroy()

    current_tip_label = None

    if sustainable_tips:
        random_tip = random.choice(sustainable_tips)

    # Create a label to display the tip
        tip_label = tk.Label(root, text=random_tip)
        tip_label.place(x=510, y=463, anchor="center")

        sustainable_tips.remove(random_tip)

        current_tip_label = tip_label

    else:
        message_label = tk.Label(root, text="Come back tomorrow \n for more sustainability tips!")
        message_label.place(x=418, y=420)

message = tk.Label()
user_score = 0

def press(user_selection):
    """This definition is for increasing the user's score
    and displaying a message once a button is clicked."""
    global message, user_score, user_score_label, sustainable_tips

    message.destroy()

    if user_selection == "no meat":
         message = tk.Label(text=f"Well done, {username.get()}!")
         user_score += 5
    elif user_selection == "vegan":
         message = tk.Label(text=f"Excellent, {username.get()}!")
         user_score += 10
    elif user_selection == "tap water":
         message = tk.Label(text=f"Great Job, {username.get()}!")
         user_score += 5
    elif user_selection == "bike":
         message = tk.Label(text=f"Nice, {username.get()}!")
         user_score += 5
    elif user_selection == "walked":
         message = tk.Label(text=f"Very cool, {username.get()}!")
         user_score += 5
    elif user_selection == "to-go cup":
         message = tk.Label(text=f"You go, {username.get()}!")
         user_score += 5
    elif user_selection == "shopping bag":
         message = tk.Label(text=f"That's great, {username.get()}!")
         user_score += 5
    elif user_selection == "second hand":
         message = tk.Label(text=f"Well done, {username.get()}!")
         user_score += 10
    elif user_selection == "repaired":
         message = tk.Label(text=f"Fantastic, {username.get()}!")
         user_score += 10
    elif user_selection == "waste":
         message = tk.Label(text=f"Great work, {username.get()}!")
         user_score += 5
    elif user_selection == "fashion":
         message = tk.Label(text=f"Excellent, {username.get()}!")
         user_score += 10
    elif user_selection == "eco":
         message = tk.Label(text=f"Well done, {username.get()}!")
         user_score += 10
    elif user_selection == "plastic_free":
         message = tk.Label(text=f"You go, {username.get()}!")
         user_score += 10
    elif user_selection == "2nd_hand":
         message = tk.Label(text=f"Very nice, {username.get()}!")
         user_score += 10
    elif user_selection == "random_tip":
         message = tk.Label(text=display_random_tip())
        #brauche ich, damit kein Error im Terminal, wenn Random Tip geklickt
        #dann erscheint aber Anfang eines labels bei Score (well done etc)

        #display_random_tip()
        #bei dieser Version funktioniert zwar alles, aber gibt error im terminal

    message.place(x=505, y=248, anchor="center")

    # Add label to keep track of the score
    user_score_label = tk.Label(text=f"Your Score {user_score}",
                                relief=tk.RAISED,
                                borderwidth=5,
                                bg="#83B799",
                                fg="#ffffff",
                                padx=4,
                                pady=2)
    user_score_label.place(x=505, y= 212, anchor="center")

def create_sustainability_app(root):
    """This definition creates the main app. It clears all widgets and
       places a background image and several buttons."""
    clear_widgets(root)
    add_image(root, "images/background_game.jpg", screen_width, screen_height)
    create_homepage_button()
    create_close_button(root)

    #display_random_tip()

    option1_button = tk.Button(
        text="... didn't eat meat.",
        font="lucida 10 bold",
        command=lambda: press("no meat"))
    option1_button.place(x=45, y=200)

    option2_button = tk.Button(
        text="... ate completely vegan.",
        font="lucida 10 bold",
        command=lambda: press("vegan"))
    option2_button.place(x=705, y=195)

    option3_button = tk.Button(
        text="... drank tap water (instead of bottled water).",
        font="lucida 10 bold",
        command=lambda: press("tap water"))
    option3_button.place(x=45, y=260)

    option4_button = tk.Button(
        text="... took my bike instead of driving.",
        font="lucida 10 bold",
        command=lambda: press("bike"))
    option4_button.place(x=45, y=230)

    option5_button = tk.Button(
        text="... walked instead of driving.",
        font="lucida 10 bold",
        command=lambda: press("walked"))
    option5_button.place(x=45, y=290)

    option6_button = tk.Button(
        text="... used my own to-go cup.",
        font="lucida 10 bold",
        command=lambda: press("to-go cup"))
    option6_button.place(x=45, y=320)

    option7_button = tk.Button(
        text="... used my own shopping bag.",
        font="lucida 10 bold",
        command=lambda: press("shopping bag"))
    option7_button.place(x=45, y=350)

    option8_button = tk.Button(
        text="... bought second hand.",
        font="lucida 10 bold",
        command=lambda: press("second hand"))
    option8_button.place(x=705, y=225)

    option9_button = tk.Button(
        text="... repaired something instead of replacing it.",
        font="lucida 10 bold",
        command=lambda: press("repaired"))
    option9_button.place(x=705, y=285)

    option10_button = tk.Button(
        text="... separated my waste.",
        font="lucida 10 bold",
        command=lambda: press("waste"))
    option10_button.place(x=45, y=380)

    option11_button = tk.Button(
        text="... bought slow/fair fashion.",
        font="lucida 10 bold",
        command=lambda: press("fashion"))
    option11_button.place(x=705, y=255)

    option12_button = tk.Button(
        text="... bought ecological and regional produce",
        font="lucida 10 bold",
        command=lambda: press("eco"))
    option12_button.place(x=705, y=315)

    option13_button = tk.Button(
        text="... shopped plastic-free.",
        font="lucida 10 bold",
        command=lambda: press("plastic_free"))
    option13_button.place(x=705, y=345)

    option14_button = tk.Button(
        text="... sold something second hand.",
        font="lucida 10 bold",
        command=lambda: press("2nd_hand"))
    option14_button.place(x=705, y=375)

    tips_button = tk.Button(
        text="\U0001F440 Give me more tips \n on sustainable living!",
        font='lucida 12 bold',
        command=lambda: press("random_tip"))
    tips_button.place(x=420, y=350)

    info_button = tk.Button(
        text="❓",
        command=lambda:create_infopage(root))
    info_button.place(x=46, y=464)

def check_user(root):
    """This definition checks if the user exists before moving onto the next page."""

    # read all the usernames in the username from the .csv file
    user_ids = list(pd.read_csv("user_data/users_data.csv").user_id)

    if username.get() in user_ids:
        create_sustainability_app(root)
    # otherwise give a warning
    else:
        tk.messagebox.showwarning("WARNING", "User does not exist!")


def create_returning_user_page(root):
    global username

    clear_widgets(root)
    add_image(root, "images/background_returning.jpg", screen_width, screen_height)
    create_homepage_button()
    create_close_button(root)

    # ask for a user name
    userid_label = tk.Label(root,
                            text="Enter your user name:",
                            font="lucida 19 bold",
                            fg="white",
                            bg="#b6b186"
                            )
    userid_label.place(x=245, y=255)

    # entry box
    username = tk.StringVar()
    username_box = tk.Entry(root,
                          textvar=username,
                          fg="white",
                          bg="#2e8b57"
                          )
    username_box.place(x=505, y=255)

    # add a button to login
    login_button = tk.Button(root,
                             text="Login",
                             command=lambda:check_user(root)
                             )
    login_button.place(x=448, y=333)


def enter_user_data():
    """This function will capture and store all the data from the new user"""

    create_homepage_button()
    # this will keep track of when the user registered
    current_timestamp = datetime.now()

    # create a dictionary that stores the information the user enters and a timestamp field
    user_data = {
        "name_of_user": name.get(),
        "user_id": username.get(),
        "created_at": current_timestamp
    }

    # read the list of existing user ids
    user_ids = list(pd.read_csv("user_data/users_data.csv").user_id)

    # additional validation to make sure the user does not enter nothing
    if len(username.get()) == 0 and len(name.get()) == 0:
        messagebox.showerror('Error', 'Please enter a name and username!')
    elif len(name.get()) == 0:
        messagebox.showerror('Error', 'Please enter your name!')
    elif len(username.get()) == 0:
        messagebox.showerror('Error', 'Please enter a user name!')
    else:
        # if the username already exists, print a warning box
        if username.get() in user_ids:
            tk.messagebox.showwarning("WARNING!", "This username already exists")
        # otherwise write the user_data to the .csv file and then move onto the next page
        else:
            # convert the dictionary into a user_data frame
            user_data_df = pd.DataFrame([user_data])
            # write to a csv file - to add future iterations of user_data: set mode to append and header to be false
            user_data_df.to_csv("user_data/users_data.csv", index=False, mode="a", header=False)
            # clear the widgets and create the next page with general information
            clear_widgets(root)
            create_infopage(root)


def create_new_user_page(root):
    global username, name # globalise these variables as they will be stored in the .csv file

    clear_widgets(root)
    add_image(root, "images/background_new.jpg", screen_width, screen_height)
    create_homepage_button()
    create_close_button(root)

    # Create labels and entry boxes to get user information
    name_label = tk.Label(root,
                          text="What is your name?",
                          font="lucida 19 bold",
                          fg="white",
                          bg="#b6b186"
                          )
    name_label.place(x=275, y=190)

    name = tk.StringVar()
    name_box = tk.Entry(root,
                        textvar=name,
                        fg="white",
                        bg="#2e8b57"
                        )
    name_box.place(x=505, y=190)

    username_label = tk.Label(root,
                              text="Create a user name:",
                              font="lucida 19 bold",
                              fg="white",
                              bg="#b6b186"
                              )
    username_label.place(x=275, y=258)

    username = tk.StringVar()
    username_box = tk.Entry(root,
                            textvar=username,
                            fg="white",
                            bg="#2e8b57"
                            )
    username_box.place(x=505, y=257)

    # create a button to store all the information
    enter_data = tk.Button(root,
                           text="SUBMIT INFO",
                           command=enter_user_data
                           )
    enter_data.place(x=463, y=340)

def create_infopage(root):
    global username

    clear_widgets(root)
    add_image(root, "images/background_info.jpg", screen_width, screen_height)
    create_homepage_button()
    create_close_button(root)

    welcome= tk.Label(text=f"💚 Welcome, {username.get()}! 💚",
                       font="lucida 20 bold",
                       fg="white",
                       bg="#2e8b57")
    welcome.place(x=530, y=150, anchor="center")

    info = tk.Label(text="🌱This “Sustainability Score Tracker” can be used to keep track of your sustainable actions,\nlike repairing something instead of replacing it or separating your waste!\n\n"
                         "➕ Each clickable option is linked to a certain number of points\n(5 or 10, depending on the level of “difficulty”).\n\n"
                         "Also, you can get more tips on how to live a life that is more sustainable and eco-friendlier:\n\n 💡 If you don’t know which small steps exactly you can take in your everyday life to\n"
                         "counteract global warming, these tips offer an opportunity to get a deeper understanding\nand maybe even long-lasting commitment to environmentally conscious acts.\n\n"
                         "👀 If everyone tries to focus just a little more on the way they live and consume,\ntogether we can collectively work to create a more sustainable and habitable world for all! 🤝🏼",
                    font="lucida 13")
    info.place(x=530, y=283, anchor="center")

    # place a button to go to the main game
    play_button = tk.Button(root,
                                 text="Got it! Let's play!",
                                 font=('lucida 18 bold'),
                                 command=lambda:create_sustainability_app(root))
    play_button.place(x=440, y=442)

def create_homepage(root):
    clear_widgets(root)
    add_image(root, "images/background1.jpg", screen_width, screen_height)
    create_close_button(root)

    # place a button that will go a new user page
    new_user = tk.Button(root,
                         text="NEW USER",
                         font=("Lucida", 19, "bold"),
                         command=lambda: create_new_user_page(root)
                         )
    new_user.place(x=270, y=337)

    # place a button that will go the returning user page
    returning_user = tk.Button(root,
                               text="RETURNING USER",
                               font=("Lucida", 19, "bold"),
                               command=lambda: create_returning_user_page(root)
                               )
    returning_user.place(x=570, y=337)


# call my homepage definition to create the homepage when launching the gui
create_homepage(root)

root.mainloop()