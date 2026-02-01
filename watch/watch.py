import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'^<iframe .*?src="https?://www.youtube.com/embed/(.+?)".*?></iframe>$' # ? is used in group to reduce grouping greadiness
    match = re.search(pattern,s)

    if match:
        embed = match.group(1)
        URL = f"https://youtu.be/{embed}" #New short link
        print("*"*100)
        return URL

if __name__ == "__main__":
    main()