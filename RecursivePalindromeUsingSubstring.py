def isPalindrome(s):
  if len(s) <= 1:
    return True
  elif s[0] != s[len(s) - 1]:
    return False
  else:
    return isPalindrome(s[1 : len(s) - 1])

def main():
  print ("Is moon a palindrome?", isPalindrome("moon"))
  print ("Is noon a palindrome?", isPalindrome("noon"))
  print ("Is a a palindrome?", isPalindrome("a"))
  print ("Is aba a palindrome?", isPalindrome("aba"))
  print("Is ab a palindrome?", isPalindrome("ab"))
main()
