from flet import Column, TextField, DatePicker, TimePicker

def extract_data(form_column: Column) -> dict:
    data = {}

    for control in form_column.controls:
        # TextField
        if isinstance(control, TextField):
            key = control.label.lower().replace(" ", "_")
            data[key] = control.value if control.value != "" else None

        # DatePicker
        elif isinstance(control, DatePicker):
            key = control.label.lower().replace(" ", "_")
            if control.value is not None:
                data[key] = control.value.strftime("%Y-%m-%d")
            else:
                data[key] = None

        # TimePicker
        elif isinstance(control, TimePicker):
            key = control.label.lower().replace(" ", "_")
            if control.value is not None:
                data[key] = control.value.strftime("%H:%M")
            else:
                data[key] = None


    return data