import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'(wwww\.)?hi'
    match = re.search(pattern,s)

    if match:
        print("True")

if __name__ == "__main__":
    main()
