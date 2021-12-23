from util.read import read_txt
from emotion import prop

if __name__ == "__main__":
    txt = read_txt("data/test.txt")
    print(prop(txt))
