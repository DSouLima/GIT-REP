import sys

def doubler(number):
    #Given a number, double it and return the value
    result = number * 2
    return result

if __name__ == '__main__':
    # Retrieve command line input
    try:
        input = float(sys.argv[1])
    except (IndexError, ValueError) as e:
        # Indicates no command line paramter was provided
        print("You must provide a number as a parameter to this script")
        print("Example: ")
        print(" python example1.py 12")
        sys.exit(1)

answer = doubler(input)
print(answer)