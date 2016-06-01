def main():
    subtotal, grate = eval(input("Enter the subtotal and gratuity rate: "))
    gratuity = subtotal * (grate / 100)
    total = subtotal + gratuity
    print ('The gratuity is:' , gratuity)
    print ('The total is:' , total)
main()


