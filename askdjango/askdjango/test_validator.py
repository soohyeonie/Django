import re

val="0101231234";
pattern=r"^01[016789][1-9]\d{6,7}$";

if re.match(pattern, val):
    print("matched")
else:
    print("invalid")