def write_file(file_path, content):
    """Faylga yozish."""
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            return f"Fayl {file_path} ga muvaffaqiyatli yozildi."
    except Exception as e:
        return f"Xato: {str(e)}"
    


