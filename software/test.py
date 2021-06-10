def file_picker(sender, data):
    open_file_dialog(callback= apply_file, extensions=".*,.jpg")

def apply_file(sender, data):
    log_debug(data)
    directory = data[0]
    file = data[1]
    set_value("directory", directory)
    set_value("file", file)
    set_value("file_path", f"{directory}\\{file}")

def apply_encode(sender, data):
    file_path = get_value("File_path")
    log_debug(file_path)
    print(file_path)

def enable_window(sender, data):
    with window("Encode", collapsed=False, show=True) as widget:
        add_text("Encode your Image here.")
        show_logger()
        add_button("Directory Selector", callback=file_picker)
        add_text("Directory Path: ")
        add_same_line()
        add_label_text("##filedir", source="directory", color=[255, 0, 0])
        add_text("File: ")
        add_same_line()
        file_path1 = get_value("file_path")
        add_label_text("##file", source="file", color=[255, 0, 0])
        add_text("File Path: ")
        add_same_line()
        add_label_text("##filepath", source="file_path", color=[255, 0, 0])
        add_text("Enter the messege to encode")
        add_input_text("input", default_value="Type the messege!")
        add_button("encode")