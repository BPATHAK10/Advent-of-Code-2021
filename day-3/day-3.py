import copy

def main():
    # partOne()
    partTwo()

def partOne():
   # parse the data.txt file
    with open('data.txt','r') as file:
       lines = file.readlines()

    bitlen = len(lines[0].strip())
    # print(bitlen)

    gamma = []
    for i in range(bitlen):
        bits = [line[i] for line in lines]
        count_1 = bits.count('1')
        count_0 = bits.count('0')
        # print(bits, count_0, count_1)

        if count_1 > count_0:
            gamma.insert(i,1)
            # print(f"1 inserted at {i}")
        else:
            gamma.insert(i,0)
            # print(f"o inserted at {i}")

    # print(gamma)

    gamma_str = ''.join([str(elem) for elem in gamma])
    print(int(gamma_str,2))

    epsilon = [1 if i==0 else 0 for i in gamma]

    epsilon_str = ''.join([str(elem) for elem in epsilon])
    print(int(epsilon_str,2))

    product = int(gamma_str,2) * int(epsilon_str,2)
    print(product)

def partTwo():
    with open("./data.txt",'r') as file:
        lines_original = file.readlines()

    bitlen = len(lines_original[0].strip())

    # for oxygen rating
    lines_oxy = copy.deepcopy(lines_original) 
    for i in range(bitlen):
        bits = [line[i] for line in lines_oxy]
        count_1 = bits.count('1')
        count_0 = bits.count('0')

        def oxygenGenCriteria(line):
            if count_1 >= count_0:
                if line[i] == '1':
                    return True
                else:
                    return False
            
            else:
                if line[i] == '0':
                    return True
                else:
                    return False


        lines_oxy = list(filter(oxygenGenCriteria,lines_oxy))

        if len(lines_oxy) == 1:
            break
 
    oxygen_rating = int(lines_oxy[0].strip(),2)
    # print(oxygen_rating)

    # for co2 scrubber rating
    lines_co2 = copy.deepcopy(lines_original) 
    for i in range(bitlen):
        bits = [line[i] for line in lines_co2]
        count_1 = bits.count('1')
        count_0 = bits.count('0')

        def co2Criteria(line):
            if count_0 <= count_1:
                if line[i] == '0':
                    return True
                else:
                    return False
            
            else:
                if line[i] == '1':
                    return True
                else:
                    return False


        lines_co2 = list(filter(co2Criteria,lines_co2))

        if len(lines_co2) == 1:
            break

    # print(lines_co2)    
    co2_rating= int(lines_co2[0].strip(),2)
    # print(co2_rating)


    print(f"Answer == {oxygen_rating*co2_rating}")

if __name__ == "__main__":
    main()