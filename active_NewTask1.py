def is_multiplу_of_three(n):
  if n % 3 == 0:
    return True
    
  return False

try: 
  number = int(input("Enter a number: "))
  
  print(is_multiplу_of_three(number))
except ValueError:
  print("Not a number")
except:
  print("Unknown error, something was wrong...")