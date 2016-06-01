def string_bits(st):
    st = eval(input("Enter a string: ")
    final_string = ("")
    for i in range(len(st)):
        if i % 2 == 0:
            final_string += st[i]
    return (final_string)

