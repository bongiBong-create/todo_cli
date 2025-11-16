def check_index(index):
    try:
        return int(index)
    except ValueError:
        print("Введите число!")
        return None