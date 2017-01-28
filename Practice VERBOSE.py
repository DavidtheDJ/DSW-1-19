#David Justice
#1-25-17
#Verbose Expressions

import re

pattern = """               
            [A-Z]                           #single letter
                                            #followed by either:
            (
                [A-Z]                       #single character
                                            #followed by either:
                (                           
                    \d{1,2}                 #one or two digits 
                |                           #or 
                    \d{[A-Z]                #a digit followed by a letter 
                )
            |                               #or
                \d{1,2}                     #one or two digits 
            )
            \s\d                            #space followed by a single digit
            [A-Z]{2}                        #two letters
          """

finished = False

while not finished:
    post_code = input("Please enter your post code: ")
    if len(post_code) == 0:
        finished = True
    else:
        if re.match(pattern, post_code, re.VERBOSE):
            print("Valide post code")
        else:
            print("Invalid post code")
