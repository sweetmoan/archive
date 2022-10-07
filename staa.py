import math, numpy

def var_unknown():
  nvt = input('[?]input sample size: ')
  all_values = [
    int(x) for (x) in input('[?]input all x values : ').split()
]

  #adds all values in table
  ttv = math.fsum(all_values)
  #divided with number of values in table
  stwo = float(ttv) / float(nvt)
  print('\nsample mean: ', str(stwo))

  #subtruct every values with nvt
  stre = [x - int(stwo) for x in all_values]
  print('\ntable:')
  print('\nx-x:', stre)

  print('=', ttv)
  print('')

  stfor = [x * y for x, y in zip(stre, stre)]
  print('x-x^2:', stfor)

  txby2 = math.fsum(stfor)
  print('=', txby2)

  s = float(nvt) - 1
  q = txby2 / s
  p = float(q)
  u = math.sqrt(p)

  xe = round(u, 2)

  print('\nsample standard deviation:\n', str(u), ' or ', xe,'\n\n')
  
def var_known():
  mean = float(input('sample mean x̄ : '))
  pm = float(input('population mean μ : '))
  sd = float(input('standard deviation of the sample s : '))
  ss = int(input('sample size n :'))

  sqrt = math.sqrt(int(ss))
  
  sone = sd/sqrt
  stw = mean-pm
  result= stw/sone
  print(f"\nsolution:\n")
  print(f"{mean} - {pm}")
  print('─' * 10)
  print(f"  {sd}")
  print('','─' * 5)
  print(f"  √{ss}\n")

        
  print("t = "+str(result))

  
print("""
Hypothesis testing    
[1] variance is known
[2] variance is unknown  
""")
menu = input(">> ") 
if menu == "1":
  var_known()
elif menu == "2":
  var_unknown()
  opt = input('want to compute the test statistic? [y/n]\n>>')
  if opt == 'y':
    var_known()
  elif opt == 'n':
    pass  
else:
  print("invalid input")


