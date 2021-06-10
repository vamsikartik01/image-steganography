from dearpygui.core import *
from dearpygui.simple import *
from softsteg import encrypt, decrypt

#Window settings
set_main_window_size(700,650)
set_global_font_scale(1)
set_theme('Dark')
set_main_window_title("Image Steganography")

# Call back functions

def image_encode(sender, data):
    file_path = get_data('file_path_en')
    messege = get_value('itext##2')
    status, name = encrypt(file_path, messege)
    if status:
        log_debug("Success")
        set_value("messege_en","Encoded image is saved in 'enc\output\'"+name)
    else:
        log_debug("Failed")
        set_value("messege_en","image encoding failed")
    show_item("##messegen")

def image_decode():
    filename = get_data('file_path_de')
    status, messege = decrypt(filename)
    if status:
        set_value("messege",messege)
    else:
        set_value("messege","Error decoding")
    show_item("##messegde")

def theme_callback(sender, data):
    set_theme(sender)

def open_window(sender, data):
    if does_item_exist(data):
        show_item(data) 

def file_picker_en(sender, data):
    log_debug(sender)
    log_debug(data)
    file_path = "\\".join(data)
    log_debug(file_path)
    add_data("file_path_en",file_path)

def file_picker_de(sender, data):
    log_debug(sender)
    log_debug(data)
    file_path = "\\".join(data)
    log_debug(file_path)
    add_data("file_path_de",file_path)

#window
with window("main window", no_resize=True):

    with menu_bar('menuBar'):
        with menu("menu"):
            add_menu_item("File")
            add_menu_item("encode", callback= open_window, callback_data="Encode")
            add_menu_item("decode", callback = open_window, callback_data="Decode")
            add_menu_item("close", callback=lambda: stop_dearpygui())
        
        with menu("Themes"):
            add_menu_item("Dark", callback=theme_callback)
            add_menu_item("Light", callback=theme_callback)
            add_menu_item("Classic", callback=theme_callback)
            add_menu_item("Dark 2", callback=theme_callback)
            add_menu_item("Grey", callback=theme_callback)
            add_menu_item("Dark Grey", callback=theme_callback)
            add_menu_item("Cherry", callback=theme_callback)
            add_menu_item("Purple", callback=theme_callback)
            add_menu_item("Gold", callback=theme_callback)
            add_menu_item("Red", callback=theme_callback)
        
        with menu('tools'):
            add_menu_item('Doc', callback=lambda: show_documentation())
            add_menu_item('Debug', callback=lambda: show_debug())
            add_menu_item('About', callback=lambda: show_about())
            add_menu_item('Logger', callback=lambda: show_logger())

with window("Decode", width=500, height=250, x_pos = 100, y_pos=325):
    add_text("Decode your Image here.")
    add_button("butt##2", label="pick file", callback=lambda: open_file_dialog(callback=file_picker_de, extensions=".png"))
    add_button("decode##1", label="Decode", callback= image_decode)
    add_text("##messegde", source="messege", show=False)

with window("Encode", width=500, height=250, x_pos = 100, y_pos=50):
    add_text("Encode your image here.")
    add_text("Emter filename (.jpg)")
    add_button("butt##1", label="Pick file", callback=lambda: open_file_dialog(callback=file_picker_en, extensions=".jpg"))
    #add_input_text("itext##1")
    add_text("enter messege below")
    add_input_text("itext##2", multiline=True, height=100)
    add_button("encode##1", label="Encode",callback= image_encode )
    add_text("##messegen", source="messege_en", show=False)




start_dearpygui(primary_window="main window")