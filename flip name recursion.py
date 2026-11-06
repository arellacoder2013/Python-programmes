# reversing a string with recursion
def flip_name(s):
    if len (s) ==0:
        return s
    return flip_name(s[1:]) + s[0]

input("flip_name recurses on s[1:] then attaches s[0] at the end.Press enter")
print("Flip_name('Maya')=",flip_name('Maya'))
print("Flip_name('Code')=",flip_name('Code'))


name=input("Enter a name (try 'Riya' or'Annabelle'):")
guess=input("What is flip_name('"+ name +"')?")
input("flip_name(s) = flip_name(s[1:]) + s[0]. first character lands last.Press Enter")
print(" flip_name('"+ name +"')=", flip_name(name),"your guess:",guess)