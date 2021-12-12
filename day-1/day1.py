def partOne():
   with open('data.txt','r') as file:
      lines = file.readlines()

   inc_count = 0

   for i in range(len(lines)-1):
      line = int(lines[i].strip())
      temp = int(lines[i-1].strip()) if i!=0 else 0

      if line>temp:
         inc_count += 1


   print(inc_count) 

def partTwo():
   with open('data.txt','r') as file:
      lines = file.readlines()

   inc_count = 0

   for i in range(len(lines)-3):
      sum1 = int(lines[i].strip()) + int(lines[i+1].strip())+ int(lines[i+2].strip())
      sum2 = int(lines[i+1].strip()) + int(lines[i+2].strip()) + int(lines[i+3].strip())

      if sum2 > sum1:
         inc_count += 1

   
   print(inc_count)

def main():
   partOne()
   partTwo()

  

if __name__ == "__main__":
   main()

