# Importing tkinter module
from tkinter import *
# Importing calendar module
import calendar

# Function to show calendar of the given year
def showCalender():
    try:
        year = int(year_field.get())
        gui = Tk()
        gui.config(background='grey')
        gui.title(f"Calendar for {year}")
        gui.geometry("550x600")

        gui_content = calendar.calendar(year)
        calYear = Label(gui, text=gui_content, font=("Consolas", 10, "bold"), bg="grey")
        calYear.grid(row=5, column=1, padx=20, pady=20)

        gui.mainloop()
    except ValueError:
        error_label.config(text="❌ Please enter a valid year!")

# Main Program (Driver Code)
if __name__ == '__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calendar")
    new.geometry("300x200")

    cal = Label(new, text="Calendar", bg='grey',
                font=("Times", 24, "bold"))
    year = Label(new, text="Enter Year:", bg='dark grey')
    year_field = Entry(new, width=15, font=("Arial", 12))

    button = Button(new, text='Show Calendar',
                    fg='white', bg='blue',
                    command=showCalender)

    exit_button = Button(new, text="Exit",
                         fg='white', bg='red',
                         command=new.destroy)

    error_label = Label(new, text="", bg='grey', fg='yellow')

    # Widget layout
    cal.grid(row=0, column=0, padx=10, pady=10)
    year.grid(row=1, column=0)
    year_field.grid(row=2, column=0, pady=5)
    button.grid(row=3, column=0, pady=10)
    exit_button.grid(row=4, column=0, pady=5)
    error_label.grid(row=5, column=0)

    new.mainloop()
