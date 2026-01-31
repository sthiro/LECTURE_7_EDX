import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.strip()
    pattern = r"^.+[0-255]{1-3}\..+[0-255]{1-3}\..+[0-255]{1-3}\..+[0-255]{1-3}$"
    match = re.search(pattern, ip)

    if match: return True
    else: return False    


if __name__ == "__main__":
    main()