def main():
   with open('data.txt','r') as file:
      lines = file.readlines()

   inc_count = 0

   for i in range(len(lines)-1):
      line = int(lines[i].strip())
      temp = int(lines[i-1].strip()) if i!=0 else 0

      if line>temp:
         inc_count += 1


   print(inc_count) 

   

if __name__ == "__main__":
   main()

