s = raw_input()
b = s.lower()
first = b[0]

if len(s) > 0 and s.isalpha():
    if first == "a" or "e" or "i" or "o" or "u":
        print "vowel"
else:
    print "Not a vowel"
