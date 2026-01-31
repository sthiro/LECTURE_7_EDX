import re

string_val = "#ABCDEF"

matches = re.search("[B-F]+", string_val)
if matches:
    print(f"Valid {matches.group()}")
else:
    print("Invalid")