def reverse(text):
    return text[::-1]
    
def is_palindrome(text):
    text=text.replace("!","")
    text=text.replace("-","")
    text=text.replace(",","")
    text=text.lower()
    if text==reverse(text):
        return True
    else:
        return False
    
text=input("Enter text\n")
if is_palindrome(text):
    print "Palindrome"
else:
    print "Not palindrome"
