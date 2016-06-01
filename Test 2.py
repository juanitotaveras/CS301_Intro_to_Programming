def rotate(st, rot):
  end = st[-(rot):]
  start = st[:(rot)]
  return (end + start)

def main():
  rotate("computer", 2)
main()
