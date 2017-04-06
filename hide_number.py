def hide_numbers(s):
    l=len(s)
    return "*"*(l-4)+s[l-4:]

print("결과: " + hide_numbers("01033334444"))
