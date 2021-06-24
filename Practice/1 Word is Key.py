
"(TCS Ninja – Aug 2019 Slot 1)"

keyword = """ break, case, continue, default, defer, else, 
      for, func, goto, if, map, range, return, struct, type, var
       """
inputt = input('Enter a Word: ')

if inputt in keyword:
    print(inputt,'is a Keyword')
else:
    print(inputt,'is not a keyword')