import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.strip()
    SINGLE_BLOCK = "(0|[1-9][0-9]?|1[0-9]{0,2}|2([0-4][0-9]?)?|25[0-5])" # Checks whether single block number is in range of 0-255
    IPV4_PATTERN = rf"^{SINGLE_BLOCK}\.{SINGLE_BLOCK}\.{SINGLE_BLOCK}\.{SINGLE_BLOCK}$" #Checks whole IPV4 Pattern (4 individial blocks)
    match = re.search(IPV4_PATTERN, ip)

    if match: return True
    else: return False    


if __name__ == "__main__":
    main()