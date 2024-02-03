import tkinter as tk


root = tk.Tk()
root.title('callculater')

lbl_result_calc = tk.Label(
    root,
    text='0',
    width=30,
    height=3
)
lbl_result_calc.grid(row=0,column=0,columnspan=4)

calc_keys = [
    {
        'text' : '7',
        'command' : lambda: insert_number_in_result_calc('7'),
    },
    {
        'text' : '8',
        'command' : lambda: insert_number_in_result_calc('8'),
    },
    {
        'text' : '9',
        'command' : lambda: insert_number_in_result_calc('9'),
    },
    {
        'text' : '+',
        'command' : lambda: insert_number_in_result_calc('+'),
    },
    {
        'text' : '4',
        'command' : lambda: insert_number_in_result_calc('4'),
    },
    {
        'text' : '5',
        'command' : lambda: insert_number_in_result_calc('5'),
    },
    {
        'text' : '6',
        'command' : lambda: insert_number_in_result_calc('6'),
    },
    {
        'text' : '-',
        'command' : lambda: insert_number_in_result_calc('-'),
    },
    {
        'text' : '1',
        'command' : lambda: insert_number_in_result_calc('1'),
    },
    {
        'text' : '2',
        'command' : lambda: insert_number_in_result_calc('2'),
    },
    {
        'text' : '3',
        'command' : lambda: insert_number_in_result_calc('3'),
    },
    {
        'text' : '*',
        'command' : lambda: insert_number_in_result_calc('*'),
    },
    {
        'text' : '.',
        'command' : lambda: insert_number_in_result_calc('.'),
    },
    {
        'text' : '0',
        'command' : lambda: insert_number_in_result_calc('0'),
    },
    {
        'text' : 'C',
        'command' : lambda: insert_number_in_result_calc('C'),
    },
    {
        'text' : '=',
        'command' : lambda: insert_number_in_result_calc('='),
    },
]

def is_last_number_decimal(current):
    for char in current[::-1]:
        if char == '.':
            return True
        elif char in ['*','+','-']:
            return False
    return False

def insert_number_in_result_calc(btn_text):
    current = lbl_result_calc['text']
    # clear button
    if btn_text  == 'C':
        lbl_result_calc['text'] = '0'

    # The first character should not be zero
    # it should be deleted after entering the number
    elif current == '0':
        lbl_result_calc['text'] = btn_text  

    # Calculate values
    elif btn_text == '=':
        lbl_result_calc['text'] = str(eval(current))

    # Bet on decimal numbers
    elif btn_text == '.':
        if not is_last_number_decimal(current):
            lbl_result_calc['text'] += btn_text

    # Updating calculation operators
    elif btn_text in ['*','+','-'] and current[-1] in ['*','+','-']:
            lbl_result_calc['text'] = current[:-1] + btn_text
    else:
        lbl_result_calc['text'] += btn_text


calc_btn_obj = []

for calc_data_keys in enumerate(calc_keys):
    if ((calc_data_keys[0]))== 14:
        btn_calc = tk.Button(
        root,
        text=calc_data_keys[1]['text'],
        command=calc_data_keys[1]['command'],
        height=3,
        bg= '#ff9017',fg= 'white'
        )
    elif ((calc_data_keys[0]+1) %4) == 0:
        btn_calc = tk.Button(
        root,
        text=calc_data_keys[1]['text'],
        command=calc_data_keys[1]['command'],
        height=3,
        bg= '#595959',fg= 'white'
        )
    else:
        btn_calc = tk.Button(
            root,
            text=calc_data_keys[1]['text'],
            command=calc_data_keys[1]['command'],
            height=3,
            bg= '#cccccc',fg= 'black'
        )
    calc_btn_obj.append(btn_calc)

for i, calc_btn_obj in enumerate(calc_btn_obj):
    calc_btn_obj.grid(row=(i//4)+1,column=i%4,sticky='nsew')


root.mainloop()