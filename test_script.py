import sys
from mainfunction import dikalikan_dua

def main():
    num = int(input("masukan angka: "))
    print("kelipatan dari %d adalah %d" % (num, dikalikan_dua(num)))
    sys.exit(0)


if __name__ == "__main__":
    main()
