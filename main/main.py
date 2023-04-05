import tkinter as tk
import webbrowser
import freq_resp
import time_resp
from PIL import ImageTk, Image

def github():
    webbrowser.open("https://github.com/YassineSE/Simple-Analog-Filter-Simulator-with-Python")

def plus_info():
    info_window = tk.Toplevel(app)
    yassine = tk.Label(info_window, text="Made by Yassine SAHEB ETTABAA")
    yassine.pack()
    date = tk.Label(info_window, text="Mars 2023")
    date.pack()

def second_order_hp():

    def gen_freq_resp():
        T_inf = float(T_inf_entry.get())
        w_0 = float(w_0_entry.get())
        m = float(m_entry.get())
        freq_resp.highpass_2(T_inf,w_0,m)
    def gen_step_resp():
        T_inf = float(T_inf_entry.get())
        w_0 = float(w_0_entry.get())
        m = float(m_entry.get())
        time_resp.highpass_step_2(T_inf,w_0,m)
    def gen_impulse_resp():
        T_inf = float(T_inf_entry.get())
        w_0 = float(w_0_entry.get())
        m = float(m_entry.get())
        time_resp.highpass_impulse_2(T_inf,w_0,m)



    hp2_app = tk.Toplevel(app)
    hp2_app.title("High Pass Second Order Analog Filter Simulator")
    hp2_app.geometry("600x400")
    hp2_app.resizable(False,False)
    
    tmodel = tk.Label(hp2_app, text="Enter Circuit Constants")
    
    T_inf_label = tk.Label(hp2_app,text="T_inf:")
    T_inf_entry = tk.Entry(hp2_app)
    
    w_0_label = tk.Label(hp2_app,text="w_0")
    w_0_entry = tk.Entry(hp2_app)

    m_label = tk.Label(hp2_app,text="m:")
    m_entry = tk.Entry(hp2_app)

    
    
    frame = tk.Frame(hp2_app, width=258, height=110)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.3)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("images/tfuncs/tfunc_hp_2.png"))

    # Create a Label Widget to display the text or Image
    image = tk.Label(frame, image = img)

    freq_button = tk.Button(hp2_app, text="Generate Frequency Response", borderwidth=5, command=gen_freq_resp)
    step_button = tk.Button(hp2_app, text="Generate Step Response", borderwidth=5, command=gen_step_resp)
    impulse_button = tk.Button(hp2_app, text="Generate Impulse Response", borderwidth=5, command=gen_impulse_resp)
    
    image.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    tmodel.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    T_inf_label.place(relx=0.4, rely=0.45, anchor=tk.CENTER)
    T_inf_entry.place(relx=0.6, rely=0.45, anchor=tk.CENTER)
    w_0_label.place(relx=0.4, rely=0.55, anchor=tk.CENTER)
    w_0_entry.place(relx=0.6, rely=0.55, anchor=tk.CENTER)
    m_label.place(relx=0.4, rely=0.65, anchor=tk.CENTER)
    m_entry.place(relx=0.6, rely=0.65, anchor=tk.CENTER)
    freq_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    step_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
    impulse_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)
    hp2_app.mainloop()

def second_order_lp():

    def gen_freq_resp():
        T_0 = float(T_0_entry.get())
        w_0 = float(w_0_entry.get())
        m = float(m_entry.get())
        freq_resp.lowpass_2(T_0,w_0,m)
    def gen_step_resp():
        T_0 = float(T_0_entry.get())
        w_0 = float(w_0_entry.get())
        m = float(m_entry.get())
        time_resp.lowpass_step_2(T_0,w_0,m)
    def gen_impulse_resp():
        T_0 = float(T_0_entry.get())
        w_0 = float(w_0_entry.get())
        m = float(m_entry.get())
        time_resp.lowpass_impulse_2(T_0,w_0,m)
    hp2_app = tk.Toplevel(app)
    hp2_app.title("Low Pass Second Order Analog Filter Simulator")
    hp2_app.geometry("600x400")
    hp2_app.resizable(False,False)
    
    tmodel = tk.Label(hp2_app, text="Enter Circuit Constants")
    
    T_0_label = tk.Label(hp2_app,text="T_0:")
    T_0_entry = tk.Entry(hp2_app)
    
    w_0_label = tk.Label(hp2_app,text="w_0")
    w_0_entry = tk.Entry(hp2_app)

    m_label = tk.Label(hp2_app,text="m:")
    m_entry = tk.Entry(hp2_app)

    
    
    frame = tk.Frame(hp2_app, width=258, height=110)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.3)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("images/tfuncs/tfunc_lp_2.png"))

    # Create a Label Widget to display the text or Image
    image = tk.Label(frame, image = img)

    freq_button = tk.Button(hp2_app, text="Generate Frequency Response", borderwidth=5, command=gen_freq_resp)
    step_button = tk.Button(hp2_app, text="Generate Step Response", borderwidth=5, command=gen_step_resp)
    impulse_button = tk.Button(hp2_app, text="Generate Time Response", borderwidth=5, command=gen_impulse_resp)

    image.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    tmodel.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    T_0_label.place(relx=0.4, rely=0.45, anchor=tk.CENTER)
    T_0_entry.place(relx=0.6, rely=0.45, anchor=tk.CENTER)
    w_0_label.place(relx=0.4, rely=0.55, anchor=tk.CENTER)
    w_0_entry.place(relx=0.6, rely=0.55, anchor=tk.CENTER)
    m_label.place(relx=0.4, rely=0.65, anchor=tk.CENTER)
    m_entry.place(relx=0.6, rely=0.65, anchor=tk.CENTER)
    freq_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    step_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
    impulse_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)
    hp2_app.mainloop()

def second_order_bp():

    def gen_freq_resp():
        T_m = float(T_m_entry.get())
        w_0 = float(w_0_entry.get())
        m = float(m_entry.get())
        freq_resp.bandpass_2(T_m,w_0,m)
    def gen_step_resp():
        T_m = float(T_m_entry.get())
        w_0 = float(w_0_entry.get())
        m = float(m_entry.get())
        time_resp.bandpass_step_2(T_m,w_0,m)
    def gen_impulse_resp():
        T_m = float(T_m_entry.get())
        w_0 = float(w_0_entry.get())
        m = float(m_entry.get())
        time_resp.bandpass_impulse_2(T_m,w_0,m)
    hp2_app = tk.Toplevel(app)
    hp2_app.title("Band Pass Second Order Analog Filter Simulator")
    hp2_app.geometry("600x400")
    hp2_app.resizable(False,False)
    
    tmodel = tk.Label(hp2_app, text="Enter Circuit Constants")
    
    T_m_label = tk.Label(hp2_app,text="T_m:")
    T_m_entry = tk.Entry(hp2_app)
    
    w_0_label = tk.Label(hp2_app,text="w_0")
    w_0_entry = tk.Entry(hp2_app)

    m_label = tk.Label(hp2_app,text="m:")
    m_entry = tk.Entry(hp2_app)

    
    
    frame = tk.Frame(hp2_app, width=258, height=110)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.3)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("images/tfuncs/tfunc_bp_2.png"))

    # Create a Label Widget to display the text or Image
    image = tk.Label(frame, image = img)

    freq_button = tk.Button(hp2_app, text="Generate Frequency Response", borderwidth=5, command=gen_freq_resp)
    step_button = tk.Button(hp2_app, text="Generate Step Response", borderwidth=5, command=gen_step_resp)
    impulse_button = tk.Button(hp2_app, text="Generate Impulse Response", borderwidth=5, command=gen_impulse_resp)
    
    image.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    tmodel.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    T_m_label.place(relx=0.4, rely=0.45, anchor=tk.CENTER)
    T_m_entry.place(relx=0.6, rely=0.45, anchor=tk.CENTER)
    w_0_label.place(relx=0.4, rely=0.55, anchor=tk.CENTER)
    w_0_entry.place(relx=0.6, rely=0.55, anchor=tk.CENTER)
    m_label.place(relx=0.4, rely=0.65, anchor=tk.CENTER)
    m_entry.place(relx=0.6, rely=0.65, anchor=tk.CENTER)
    freq_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    step_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
    impulse_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)
    hp2_app.mainloop()

def second_order_bs():

    def gen_freq_resp():
        T_0 = float(T_0_entry.get())
        w_0 = float(w_0_entry.get())
        m = float(m_entry.get())
        freq_resp.notch_2(T_0, w_0,m)
    def gen_step_resp():
        T_0 = float(T_0_entry.get())
        w_0 = float(w_0_entry.get())
        m = float(m_entry.get())
        time_resp.notch_step_2(T_0,w_0,m)
    def gen_impulse_resp():
        T_0 = float(T_0_entry.get())
        w_0 = float(w_0_entry.get())
        m = float(m_entry.get())
        time_resp.bandpass_impulse_2(T_0,w_0,m)
    hp2_app = tk.Toplevel(app)
    hp2_app.title("Band-Stop/Notch Second Order Analog Filter Simulator")
    hp2_app.geometry("600x400")
    hp2_app.resizable(False,False)
    
    tmodel = tk.Label(hp2_app, text="Enter Circuit Constants")
    
    T_0_label = tk.Label(hp2_app,text="T_0:")
    T_0_entry = tk.Entry(hp2_app)
    
    w_0_label = tk.Label(hp2_app,text="w_0")
    w_0_entry = tk.Entry(hp2_app)

    m_label = tk.Label(hp2_app,text="m:")
    m_entry = tk.Entry(hp2_app)

    
    
    frame = tk.Frame(hp2_app, width=258, height=110)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.3)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("images/tfuncs/tfunc_bs_2.png"))

    # Create a Label Widget to display the text or Image
    image = tk.Label(frame, image = img)

    freq_button = tk.Button(hp2_app, text="Generate Frequency Response", borderwidth=5, command=gen_freq_resp)
    step_button = tk.Button(hp2_app, text="Generate Step Response", borderwidth=5, command=gen_step_resp)
    impulse_button = tk.Button(hp2_app, text="Generate Impulse Response", borderwidth=5, command=gen_impulse_resp)
    
    image.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    tmodel.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    T_0_label.place(relx=0.4, rely=0.45, anchor=tk.CENTER)
    T_0_entry.place(relx=0.6, rely=0.45, anchor=tk.CENTER)
    w_0_label.place(relx=0.4, rely=0.55, anchor=tk.CENTER)
    w_0_entry.place(relx=0.6, rely=0.55, anchor=tk.CENTER)
    m_label.place(relx=0.4, rely=0.65, anchor=tk.CENTER)
    m_entry.place(relx=0.6, rely=0.65, anchor=tk.CENTER)
    freq_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    step_button.place(relx=0.5, rely=0.85, anchor=tk.CENTER)
    impulse_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)
    hp2_app.mainloop()

def second_order_select():
    app2 = tk.Toplevel(app)
    app2.title("Second Order Filter Simulator")
    app2.geometry("400x400")
    app2.resizable(False,False)

    text1 = tk.Label(app2, text="Please Select The Type of Filter To Simulate")
    hp = tk.Button(app2,text="High Pass", borderwidth=2, command=second_order_hp)
    lp = tk.Button(app2,text= "Low Pass", borderwidth=2, command=second_order_lp)
    bp = tk.Button(app2,text="Band Pass", borderwidth=2, command=second_order_bp)
    bs = tk.Button(app2, text="Band Stop/Notch", borderwidth=2, command=second_order_bs)
    
    text1.place(relx = 0.5, rely = 0.1, anchor=tk.CENTER)
    hp.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    lp.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    bp.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    bs.place(relx=0.5,rely=0.9, anchor=tk.CENTER)
    app2.mainloop()


def first_order_hp():

    def gen_freq_resp():
        T_inf = float(T_inf_entry.get())
        w_0 = float(w_0_entry.get())
        freq_resp.highpass_1(T_inf,w_0)
    def gen_step_resp():
        T_inf = float(T_inf_entry.get())
        w_0 = float(w_0_entry.get())
        time_resp.highpass_step_1(T_inf,w_0)
    
    def gen_impulse_resp():
        T_inf = float(T_inf_entry.get())
        w_0 = float(w_0_entry.get())
        time_resp.highpass_impulse_1(T_inf,w_0)
    
    hp1_app = tk.Toplevel(app)
    hp1_app.title("High Pass First Order Analog Filter Simulator")
    hp1_app.geometry("600x400")
    hp1_app.resizable(False,False)
    
    tmodel = tk.Label(hp1_app, text="Enter Circuit Constants")
    
    T_inf_label = tk.Label(hp1_app,text="T_inf:")
    T_inf_entry = tk.Entry(hp1_app)
    
    w_0_label = tk.Label(hp1_app,text="w_0")
    w_0_entry = tk.Entry(hp1_app)

    
    
    frame = tk.Frame(hp1_app, width=258, height=110)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.3)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("images/tfuncs/tfunc_hp_1.png"))

    # Create a Label Widget to display the text or Image
    image = tk.Label(frame, image = img)

    freq_button = tk.Button(hp1_app, text="Generate Frequency Response", borderwidth=5, command=gen_freq_resp)
    step_button = tk.Button(hp1_app, text="Generate Step Response", borderwidth=5, command=gen_step_resp)
    impulse_button = tk.Button(hp1_app, text="Generate Impulse Response", borderwidth=5, command=gen_impulse_resp)
    
    image.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    tmodel.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    T_inf_label.place(relx=0.4, rely=0.5, anchor=tk.CENTER)
    T_inf_entry.place(relx=0.6, rely=0.5, anchor=tk.CENTER)
    w_0_label.place(relx=0.4, rely=0.6, anchor=tk.CENTER)
    w_0_entry.place(relx=0.6, rely=0.6, anchor=tk.CENTER)
    freq_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    step_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    impulse_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    hp1_app.mainloop()


def first_order_lp():

    def gen_freq_resp():
        T_0 = float(T_0_entry.get())
        w_0 = float(w_0_entry.get())
        freq_resp.lowpass_1(T_0,w_0)

    def gen_step_resp():
        T_0 = float(T_0_entry.get())
        w_0 = float(w_0_entry.get())
        time_resp.lowpass_step_1(T_0,w_0)
    
    def gen_impulse_resp():
        T_0 = float(T_0_entry.get())
        w_0 = float(w_0_entry.get())
        time_resp.lowpass_impulse_1(T_0,w_0)

    hp1_app = tk.Toplevel(app)
    hp1_app.title("Low Pass First Order Analog Filter Simulator")
    hp1_app.geometry("600x400")
    hp1_app.resizable(False,False)
    
    tmodel = tk.Label(hp1_app, text="Enter Circuit Constants")
    
    T_0_label = tk.Label(hp1_app,text="T_0:")
    T_0_entry = tk.Entry(hp1_app)
    
    w_0_label = tk.Label(hp1_app,text="w_0")
    w_0_entry = tk.Entry(hp1_app)

    
    
    frame = tk.Frame(hp1_app, width=258, height=110)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.3)

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("images/tfuncs/tfunc_lp_1.png"))

    # Create a Label Widget to display the text or Image
    image = tk.Label(frame, image = img)

    freq_button = tk.Button(hp1_app, text="Generate Frequency Response", borderwidth=5, command=gen_freq_resp)
    step_button = tk.Button(hp1_app, text="Generate Step Response", borderwidth=5, command=gen_step_resp)
    impulse_button = tk.Button(hp1_app, text="Generate Impulse Response",borderwidth=5, command=gen_impulse_resp)

    image.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    tmodel.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    T_0_label.place(relx=0.4, rely=0.5, anchor=tk.CENTER)
    T_0_entry.place(relx=0.6, rely=0.5, anchor=tk.CENTER)
    w_0_label.place(relx=0.4, rely=0.6, anchor=tk.CENTER)
    w_0_entry.place(relx=0.6, rely=0.6, anchor=tk.CENTER)
    freq_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    step_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    impulse_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    hp1_app.mainloop()


def first_order_select():
    app1 = tk.Toplevel(app)
    app1.title("First Order Filter Simulator")
    app1.geometry("400x250")
    app1.resizable(False,False)

    text1 = tk.Label(app1, text="Please Select The Type of Filter To Simulate")
    hp = tk.Button(app1,text="High Pass", borderwidth=2, command=first_order_hp)
    lp = tk.Button(app1,text= "Low Pass", borderwidth=2, command=first_order_lp)

    
    text1.place(relx = 0.5, rely = 0.1, anchor=tk.CENTER)
    hp.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    lp.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    app1.mainloop()

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
    
    first_order_button = tk.Button(app, image=first_order_image, command = first_order_select, borderwidth=5)
    second_order_button = tk.Button(app, image=second_order_image, command = second_order_select, borderwidth=5)

    #Labels
    first_order_label = tk.Label(app, text= "First Order Analog Filter")
    second_order_label = tk.Label(app, text= "Second Order Analog Filter")

    
    #Info Buttons
    git_button = tk.Button(app,
                        text="Github Repository",
                        command=github,
                        height=2,
                        width=30)
    

    info_button = tk.Button(app,
                            text="About",
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