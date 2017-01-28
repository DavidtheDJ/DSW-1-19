#David Justice
#1-25-17
#Practice

import re

pattern = "[A-Z]([A-Z](\d{1,2}|\d{[A-Z])|\d{1,2})\s\d[A-Z]{2}"

finished = False

while not finished:
    post_code = input("Please enter your post code: ")
    if len(post_code) == 0:
        finished = True
    else:
        if re.match(pattern, post_code):
            print("Valide post code")
        else:
            print("Invalid post code")
                  
