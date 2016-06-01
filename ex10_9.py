# Compute the standard deviation of values
def deviation(x):
  sum = 0
  for i in range(len(x)):
    sum += ((x[i]) - mean(x)) ** 2
  return (sum / (len(x) - 1)) ** 0.5

# Compute the mean of a list of values
def mean(x):
  sum = 0
  for i in range(len(x)):
    sum += (x[i])    # sum = (x[i]) + sum
  return sum / len(x)


def main():
  nums = input("Enter numbers: ")
  x = nums.split()
  for i in range(len(x)):
    x[i] = float(x[i])
  print ("The mean is", mean(x))
  print ("The standard deviation is", deviation(x))
main()
