def read_file(file_path):
    """Faylni o'qiydi va uning mazmunini qaytaradi."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Fayl {file_path} topilmadi."
