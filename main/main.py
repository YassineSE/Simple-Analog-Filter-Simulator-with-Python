import tkinter as tk
import webbrowser


def github():
    webbrowser.open("https://git.enib.fr/m1sahebe/application-pour-la-zg2")

def plus_info():
    info_window = tk.Toplevel(app)
    yassine = tk.Label(info_window, text="Made by Yassine SAHEB ETTABAA")
    yassine.pack()
    date = tk.Label(info_window, text="Mars 2023")
    date.pack()

def io():
    
    order = input("Enter Filter's order (1 or 2) \n")
    while 1:
        if  order not in [1,2,"1","2"]:
            order = input("Enter Filter's order (1 or 2) \n")
        else:
            break

    print("order = " + order)

def first_order():
    info_window = tk.Toplevel(app)
    yassine = tk.Label(info_window, text="1")
    yassine.pack()
    date = tk.Label(info_window, text="Mars 2023")
    date.pack()

def second_order():
    info_window = tk.Toplevel(app)
    yassine = tk.Label(info_window, text="2")
    yassine.pack()
    date = tk.Label(info_window, text="Mars 2023")
    date.pack()

if __name__ == "__main__":
    app = tk.Tk()
    app.geometry("900x700")
    app.title("Analog Filter Simulator")
    app.resizable(False, False)


    #Image Buttons
    first_order_image= tk.PhotoImage(file='images/first_order.png')
    first_order_image_label = tk.Label(image=first_order_image)

    second_order_image = tk.PhotoImage(file='images/second_order.png')
    second_order_image_label = tk.Label(image=second_order_image)
    
    first_order_button = tk.Button(app, image=first_order_image, command = first_order, borderwidth=5)
    second_order_button = tk.Button(app, image=second_order_image, command = second_order, borderwidth=5)

    #Labels
    first_order_label = tk.Label(app, text= "First Order Analog Filter")
    second_order_label = tk.Label(app, text= "Second Order Analog Filter")

    
    #Info Buttons
    git_button = tk.Button(app,
                        text="Accéder au Github",
                        command=github,
                        height=2,
                        width=30)
    

    info_button = tk.Button(app,
                            text="Plus d'informations",
                            command=plus_info,
                            height=2,
                            width=30)
    
    #Placement of elements
    first_order_label.place(relx = 0.3, rely = 0.1, anchor=tk.CENTER)
    second_order_label.place(relx = 0.7, rely = 0.1, anchor=tk.CENTER)
    first_order_button.place(relx = 0.3, rely = 0.3, anchor=tk.CENTER)
    second_order_button.place(relx = 0.7, rely = 0.3, anchor=tk.CENTER)
    git_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    info_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    app.mainloop()