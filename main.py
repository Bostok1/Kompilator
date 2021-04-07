from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from PIL import ImageTk  # $ pip install pillow


root = Tk()
root.title('Compiler')
root.geometry("1300x700")
# Set variable for open file name
global open_status_name
open_status_name = False

global selected
selected = False


# Create New File Function
def new_file():
    # Delete previous text
    text1.delete("1.0", END)
    # Update status bars
    root.title('New File')
    status_bar.config(text="New File")

    global open_status_name
    open_status_name = False


# Open Files
def open_file():
    # Delete previous text
    text1.delete("1.0", END)

    # Grab Filename
    text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open File", filetypes=(
        ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))

    # Check to see if there is a file name
    if text_file:
        # Make filename global so we can access it later
        global open_status_name
        open_status_name = text_file

    # Update Status bars
    name = text_file
    status_bar.config(text=f'{name}')
    name = name.replace("C:/gui/", "")
    root.title(f'{name} - TextPad!')

    # Open the file
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    # Add file to textbox
    text1.insert(END, stuff)
    # Close the opened file
    text_file.close()


# Save As File
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/gui/", title="Save File", filetypes=(
        ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        # Update Status Bars
        name = text_file
        status_bar.config(text=f'Saved: {name}        ')
        name = name.replace("C:/gui/", "")
        root.title(f'{name} - TextPad!')

        # Save the file
        text_file = open(text_file, 'w')
        text_file.write(text1.get(1.0, END))
        # Close the file
        text_file.close()


# Save File
def save_file():
    global open_status_name
    if open_status_name:
        # Save the file
        text_file = open(open_status_name, 'w')
        text_file.write(text1.get(1.0, END))
        # Close the file
        text_file.close()
        # Put status update or popup code
        status_bar.config(text=f'Saved: {open_status_name}        ')
        name = open_status_name
        name = name.replace("C:/gui/", "")
        root.title(f'{name} - TextPad!')
    else:
        save_as_file()


# Cut Text
def cut_text(e):
    global selected
    # Check to see if keyboard shortcut used
    if e:
        selected = root.clipboard_get()
    else:
        if text1.selection_get():
            # Grab selected text from text box
            selected = text1.selection_get()
            # Delete Selected Text from text box
            text1.delete("sel.first", "sel.last")
            # Clear the clipboard then append
            root.clipboard_clear()
            root.clipboard_append(selected)


# Copy Text
def copy_text(e):
    global selected
    # check to see if we used keyboard shortcuts
    if e:
        selected = root.clipboard_get()

    if text1.selection_get():
        # Grab selected text from text box
        selected = text1.selection_get()
        # Clear the clipboard then append
        root.clipboard_clear()
        root.clipboard_append(selected)


# Paste Text
def paste_text(e):
    global selected
    # Check to see if keyboard shortcut used
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = text1.index(INSERT)
            text1.insert(position, selected)


# Select all Text
def select_all(e):
    # Add sel tag to select all text
    text1.tag_add('sel', '1.0', 'end')


# Clear All Text
def clear_all():
    text1.delete(1.0, END)


def help_window():
    newWindow = Tk()
    newWindow.title('Help')
    newWindow.geometry("450x150")
    label5 = Label(newWindow, font=("Numeric", 10), justify=LEFT, wraplength=400,
                   text="Чтобы открыть и сохранить файлы, выберите Файл, а затем выберите Создать для создания нового документа, Открыть для работы с существующим документом или Сохранить для сохранения документа. (Если у документа нет имени, WordPad запросит указать его.)")

    label5.pack(fill=BOTH)


# Toolbar

frame_top = LabelFrame()
frame_top.pack(pady=10)

CreateImage = ImageTk.PhotoImage(file="1.png")
CreateFile = Button(frame_top, image=CreateImage, command=new_file)
CreateFile.pack(side=LEFT)
OpenImage = ImageTk.PhotoImage(file="2.png")
OpenFile = Button(frame_top, image=OpenImage, text="2", command=open_file)
OpenFile.pack(side=LEFT)
OpenFile = Button(frame_top, image=OpenImage, command=open_file)
SaveImage = ImageTk.PhotoImage(file="3.png")
SaveFile = Button(frame_top, image=SaveImage, command=save_file)
SaveFile.pack(side=LEFT)
FakeLabel = Label(frame_top, width=5, height=2)
FakeLabel.pack(side=LEFT)
UndoImage = ImageTk.PhotoImage(file="4.png")
Undo = Button(frame_top, image=UndoImage, padx=2, command=lambda: text1.edit_undo())
Undo.pack(side=LEFT)
RedoImage = ImageTk.PhotoImage(file="5.png")
Redo = Button(frame_top, image=RedoImage, padx=2, command=lambda: text1.edit_redo())
Redo.pack(side=LEFT)
CopyImage = ImageTk.PhotoImage(file="6.png")
Copy = Button(frame_top, image=CopyImage, padx=2, command=lambda: copy_text(False))
Copy.pack(side=LEFT)
CutImage = ImageTk.PhotoImage(file="7.png")
Cut = Button(frame_top, image=CutImage, padx=10, command=lambda: cut_text(False))
Cut.pack(side=LEFT)
PasteImage = ImageTk.PhotoImage(file="8.png")
Paste = Button(frame_top, image=PasteImage, padx=2, command=lambda: paste_text(False))
Paste.pack(side=LEFT)

# Create a toolbar frame
toolbar_frame1 = Frame(root)
toolbar_frame1.pack(fill=X)

toolbar_frame2 = Frame(root)
toolbar_frame2.pack(fill=X)

# Create Main Frame
main_frame = Frame(root)
main_frame.pack()

frame_text1 = Frame(main_frame)
frame_text1.pack(pady=5)
frame_text2 = Frame(main_frame)
frame_text2.pack(pady=5)

# Create our Scrollbar For the Text Box
text_scroll1 = Scrollbar(frame_text1)
text_scroll1.pack(side=RIGHT, fill=Y)

text_scroll2 = Scrollbar(frame_text2)
text_scroll2.pack(side=RIGHT, fill=Y)

# Horizontal Scrollbar
hor_scroll1 = Scrollbar(frame_text1, orient='horizontal')
hor_scroll1.pack(side=BOTTOM, fill=X)

hor_scroll2 = Scrollbar(frame_text2, orient='horizontal')
hor_scroll2.pack(side=BOTTOM, fill=X)

# Create Text Box
text1 = Text(frame_text1, width=100, height=12, font=("Numeric", 16), selectbackground="#9ab999",
             selectforeground="black", undo=True, yscrollcommand=text_scroll1.set, wrap="none",
             xscrollcommand=hor_scroll1.set)
text1.pack()

text2 = Text(frame_text2, width=100, height=11, font=("Numeric", 16), selectbackground="#9ab999",
             selectforeground="black", undo=True, yscrollcommand=text_scroll1.set, wrap="none",
             xscrollcommand=hor_scroll2.set)
text2.pack()

# Configure our Scrollbar
text_scroll1.config(command=text1.yview)
hor_scroll1.config(command=text1.xview)

text_scroll2.config(command=text2.yview)
hor_scroll2.config(command=text2.xview)

# Main Menu
mainmenu = Menu(root)
root.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=False)
filemenu.add_command(label="Создать", command=new_file)
filemenu.add_command(label="Открыть", command=open_file)
filemenu.add_command(label="Сохранить", command=save_file)
filemenu.add_command(label="Сохранить как", command=save_as_file)
filemenu.add_command(label="Выход", command=root.quit)

editmenu = Menu(mainmenu, tearoff=False)
editmenu.add_command(label="Отменить", command=lambda: text1.edit_undo(), accelerator="(Ctrl+z)")
editmenu.add_command(label="Повторить", command=lambda: text1.edit_redo(), accelerator="(Ctrl+y)")
editmenu.add_command(label="Вырезать", command=lambda: cut_text(False), accelerator="(Ctrl+x)")
editmenu.add_command(label="Копировать", command=lambda: copy_text(False), accelerator="(Ctrl+c)")
editmenu.add_command(label="Вставить", command=lambda: paste_text(False), accelerator="(Ctrl+v)")
editmenu.add_command(label="Удалить всё", command=clear_all)
editmenu.add_command(label="Выделить всё", command=lambda: select_all(True), accelerator="(Ctrl+a)")

textmenu = Menu(mainmenu, tearoff=False)
textmenu.add_command(label="Постановка задачи")
textmenu.add_command(label="Грамматика")
textmenu.add_command(label="Классификация грамматики")
textmenu.add_command(label="Метод анализа")
textmenu.add_command(label="Диагностика и нейтyрализация ошибок")
textmenu.add_command(label="Тестовый пример")
textmenu.add_command(label="Список литературы")
textmenu.add_command(label="Исходный код программы")

startmenu = Menu(mainmenu, tearoff=False)

helpmenu = Menu(mainmenu, tearoff=False)
helpmenu.add_command(label="Вызов справки", command=help_window)
helpmenu.add_command(label="О программе")

mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Правка", menu=editmenu)
mainmenu.add_cascade(label="Текст", menu=textmenu)
mainmenu.add_cascade(label="Пуск", menu=startmenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

# Add Status Bar To Bottom Of App
status_bar = Label(root, text='Ready', anchor=E)
status_bar.pack(fill=X, side=BOTTOM)

# Undo,Redo Bindings
root.bind('<Control-Key-z>', text1.edit_undo)
root.bind('<Control-Key-y>', text1.edit_redo)

# Edit Bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)
# Select Binding
root.bind('<Control-A>', select_all)
root.bind('<Control-a>', select_all)

root.mainloop()