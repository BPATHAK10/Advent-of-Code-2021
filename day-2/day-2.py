def partOne(): 
  with open("data.txt","r") as file :
    lines = file.readlines()

  hor_pos = 0 
  depth = 0

  for line in lines:
    l = line.split()
    if l[0] == "forward":
      hor_pos += int(l[1]) 
    elif l[0] == "down":
      depth += int(l[1]) 
    elif l[0] == "up":
      depth -= int(l[1]) 
    else:
      print("error")
      
  print("answer = ",hor_pos*depth)

def partTwo():
  with open("data.txt", "r") as file:
    lines = file.readlines()

  hor_pos = 0 
  depth = 0
  aim = 0

  for line in lines:
    l = line.split()
    if l[0] == "forward":
      hor_pos += int(l[1]) 
      depth += int(l[1]) * aim
    elif l[0] == "down":
      aim += int(l[1])
    elif l[0] == "up":
      aim -= int(l[1]) 
    else:
      print("error")
      
  print("answer of part 2 = ",hor_pos*depth)



  

def main():
  partOne()
  partTwo()

if __name__ == "__main__":
    main()