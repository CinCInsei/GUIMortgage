from tkinter import *

root = Tk()
root.title("GUI Mortgage Calculator")
root.geometry("500x500")
bg = PhotoImage(file="houses.png")
canvas1 = Canvas(root, width=10000, height=1000)

canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg, anchor="nw")

def payment():
    if amount_entry.get() and interest_entry.get() and term_entry.get() and down_entry.get():
        y = int(term_entry.get())
        m = y * 12
        r = float(interest_entry.get())
        loan = int(amount_entry.get())
        down = int(down_entry.get())
        monthly_rate = r / 100 / 12
        mp = (monthly_rate / (1 - (1 + monthly_rate)**(-m))) * (loan-down)
        mp = f"{mp:,.2f}"
        payment_label.config(text=f"Monthly Payment: ${mp}")
    else:
        payment_label.config(text="Error")


my_label_frame = LabelFrame(root)
my_label_frame.pack(pady=100)
my_frame = Frame(my_label_frame)
my_frame.pack(pady=5, padx=10)
amount_label = Label(my_frame, text="Amount")
amount_entry = Entry(my_frame)
down_label = Label(my_frame, text="Down Payment")
down_entry = Entry(my_frame)
interest_label = Label(my_frame, text="Interest")
interest_entry = Entry(my_frame)
term_label = Label(my_frame, text="Years")
term_entry = Entry(my_frame)
amount_label.grid(row=0, column=0)
amount_entry.grid(row=0, column=1, pady=10)
down_label.grid(row=1, column=0)
down_entry.grid(row=1, column=1, pady=10)
interest_label.grid(row=2, column=0)
interest_entry.grid(row=2, column=1, pady=10)
term_label.grid(row=3, column=0)
term_entry.grid(row=3, column=1, pady=10)
my_button = Button(my_label_frame, text="Calculate", command=payment)
my_button.pack(pady=20)
payment_label = Label(my_label_frame, text="")
payment_label.pack(pady=20)

amount_label_canvas = canvas1.create_window(100, 10, anchor="nw",window=my_label_frame)
down_label_canvas = canvas1.create_window(100, 40, anchor="nw",window=my_label_frame)
interest_label_canvas = canvas1.create_window(100, 70, anchor="nw", window=my_label_frame)


root.mainloop()