def cities(num_cities, coords):
  c_list = coords.split()
  for i in range(len(c_list)):
    c_list[i] = float(c_list[i])
  for i in range(0, num_cities, 2):
    x1, y1 = c_list[i], c_list[i + 1]
    x2, y2 = c_list[i + 2], c_list[i + 3]
    d = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

  return (x, y)

def main():
  num_cities = int(input("Enter the number of cities: "))
  coords = input("Enter the coordinates of the cities: ")
  
  print ("The central city is at", cities(num_cities, coords))
main()
