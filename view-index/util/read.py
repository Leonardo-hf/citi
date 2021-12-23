def read_txt(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        txt = f.read()
    return txt
