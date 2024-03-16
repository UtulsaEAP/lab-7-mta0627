'''
Name: Mason Anderson
Time: 3/15/24 11:41 PM
'''


def wordInRange():
    #Type your code here
        
    with open(input(), 'r') as file:
 
        line = file.readline()
        
        range_min = input()

        range_max = input()

        while line:

            if range_min < line < range_max:

                print(f'{line.strip()} - in range')
            
            else:

                print(f'{line.strip()} - not in range')

            line = file.readline()

    
if __name__ == '__main__':
    wordInRange()