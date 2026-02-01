import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    START_TIME_PATTERN = r"((?P<Start_Hour1>[1-9])(:(?P<Start_Min1>[0-5][0-9]))?|(?P<Start_Hour2>1[0-2])(:(?P<Start_Min2>[0-5][0-9]))?) (?P<Start_Format>AM|PM)"
    END_TIME_PATTERN = r"((?P<End_Hour1>[1-9])(:(?P<End_Min1>[0-5][0-9]))?|(?P<End_Hour2>1[0-2])(:(?P<End_Min2>[0-5][0-9]))?) (?P<End_Format>AM|PM)"
    # One or more group selector name cannot have same name in OR selector 
    pattern = rf"^{START_TIME_PATTERN} to {END_TIME_PATTERN}$"
    match = re.search(pattern, s)

    if match:
        if match.group("Start_Hour1"): Start_Hour = match.group("Start_Hour1")
        else: Start_Hour = match.group("Start_Hour2")

        if match.group("Start_Min1"): Start_Min = match.group("Start_Min1")
        elif match.group("Start_Min2"): Start_Min = match.group("Start_Min2")
        else: Start_Min = "00" 

        if match.group("End_Hour1"): End_Hour = match.group("End_Hour1")
        else: End_Hour = match.group("End_Hour2")

        if match.group("End_Min1"): End_Min = match.group("End_Min1")
        elif match.group("End_Min2"): End_Min = match.group("Start_Min2")
        else: End_Min = "00" 

        Start_Format = match.group("Start_Format")
        End_Format = match.group("End_Format")


    else : raise ValueError


if __name__ == "__main__":
    main()