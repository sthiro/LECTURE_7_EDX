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
        if match.group("Start_Hour1"): Start_Hour = int(match.group("Start_Hour1"))
        else: Start_Hour = int(match.group("Start_Hour2"))

        if match.group("Start_Min1"): Start_Min = int(match.group("Start_Min1"))
        elif match.group("Start_Min2"): Start_Min = int(match.group("Start_Min2"))
        else: Start_Min = 0 

        if match.group("End_Hour1"): End_Hour = int(match.group("End_Hour1"))
        else: End_Hour = int(match.group("End_Hour2"))

        if match.group("End_Min1"): End_Min = int(match.group("End_Min1"))
        elif match.group("End_Min2"): End_Min = int(match.group("End_Min2"))
        else: End_Min = 0 

        Start_Format = match.group("Start_Format")  # AM|PM
        End_Format = match.group("End_Format")  # AM|PM
        
        Converted_Start_Hour = Hour_Conversion(Start_Hour, Start_Format)
        Converted_End_Hour = Hour_Conversion(End_Hour, End_Format)

        return f"{Converted_Start_Hour}:{Start_Min:02} to {Converted_End_Hour}:{End_Min:02}"


    else : raise ValueError("Invalid time input")

def Hour_Conversion(Hour, Format):
    if Format == "AM" and Hour == 12: Converted_Hour = 0 #If it's 12 midnight 24h => 00h
    if (1 <= Hour <= 11 and Format == "AM") or (Hour == 12 and Format == "PM"): Converted_Hour = Hour # if it's 1<->11 AM or 12 noon 12H hour = 24h hour
    if (1 <= Hour <= 11) and Format == "PM": Converted_Hour = Hour + 12

    return f"{Converted_Hour:02}" # Makes format in 2 digit. Ex 1 AM => 01




if __name__ == "__main__":
    main()