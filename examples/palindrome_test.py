
def palindrome_test():
    text = input("Please enter a word to test : ")
    reserve_text ="".join(reversed(text))
    if text == reserve_text:
        print("This text is Palindrome")
    
    return text

a = palindrome_test()
print(a)