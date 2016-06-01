def main():
    cock = eval(input("Enter size of cock: "))
    if 1 <= cock <= 12:
        print ("Congrats!")
    elif cock > 12:
        print ("That's a big cock")
    else:
        print ("Enter valid size")
    
main()
