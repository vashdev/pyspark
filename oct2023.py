def run():
 print('..')
 # for i in range(0, 10):
 #     if i%2 ==0:
 #         print(i ** 2)
 # Write a program that finds the sum of all natural numbers below 1000 (< 1000) that are multiples of 3 or 5, and prints it.
 multipleof3=[]
 sumtotal = 0
 for i in range (1,1000):

     if i % 3 ==0:
          sumtotal+=i
 print(sumtotal)
 # get max number
 l=[1,2,3,4,5]
 print(max(l))
 print(sorted(l,reverse=True))
 firstnames = ["John","Amanda","Eric","Joanna"]
 lastnames = ["Tukey","MacPherson","Voight","Halstead"]
 ages = [31, 42, 33, 50]
 x = zip(firstnames,lastnames,ages)
 print(list(x))
 y = dict(zip(firstnames, lastnames))
 print(f" dict form two lists {y} ")
 # Unpack list of tuples
 fullnames = [('John', 'Tukey'), ('Amanda', 'MacPherson'), ('Eric', 'Voight'), ('Joanna', 'Halstead')]
 print("zip to unpack tuple")
 firstnames, lastnames = zip(*fullnames)
 print( " ==== MAP ===> ")
 numbers = [1, 2, 3, 4, 5]

 def num_doubler(number):
     return number * 2

 x = map(num_doubler, numbers)
 print(list(x))
 lamb=[x * 2  for x in numbers]
 print(lamb)

 print(" FILTER ")

 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

 def is_even(number):
     return number % 2 == 0

 x = filter(is_even, numbers)

 print(list(x))

 print(" SET unordered but unique")
 a = [1, 2, 3, 4, 5, 5, "a", "b", "b"]

 b = set(a)

 print(list(b))
 print("10. All and Any")
 print(all([number % 2 == 0 for number in [2, 4, 6, 8, 10]]))
 print(any([number % 2 == 0 for number in [1, 3, 5, 7, 9]]))

 print( "SLICING start stop step")
 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 print(numbers[1:: 2])



if __name__ == '__main__':
  print('PyCharm')
  run()