import calendar as cal
import tkinter as tk


def show_calendar(year, month):
    cal_text = cal.month(year, month)
    calendar_text.insert(tk.END, cal_text + '\n' + '-'*20 + '\n')

def show_next_month():
    global current_month, current_year
    current_month += 1
    if current_month > 12:
        current_month = 1
        current_year += 1
    update_calendar()

def show_previous_month():
    global current_month, current_year
    current_month -= 1
    if current_month < 1:
        current_month = 12
        current_year -= 1
    update_calendar()

def update_calendar():
    calendar_text.delete('1.0', tk.END)
    for i in range(1, 13):
        show_calendar(current_year, i)

def update_calendar_with_custom_year():
    try:
        custom_year = int(year_entry.get())
        if custom_year > 0:
            global current_year
            current_year = custom_year
            update_calendar()
    except ValueError:
        pass  # Ignore non-integer input


root = tk.Tk()
root.title("Calendário do luquinhas")

calendar_text = tk.Text(root, wrap=tk.WORD, height=20, width=40)
calendar_text.pack(padx=10, pady=10)

previous_month_button = tk.Button(root, text="Mês Anterior", command=show_previous_month)
previous_month_button.pack(side=tk.LEFT, padx=5, pady=10)

next_month_button = tk.Button(root, text="Próximo Mês", command=show_next_month)
next_month_button.pack(side=tk.LEFT, padx=5, pady=10)

year_entry = tk.Entry(root, width=10)
year_entry.pack(side=tk.LEFT, padx=5, pady=10)

custom_year_button = tk.Button(root, text="Atualizar Ano", command=update_calendar_with_custom_year)
custom_year_button.pack(side=tk.LEFT, padx=5, pady=10)


current_month = 1
current_year = 2024

update_calendar()


root.mainloop()



