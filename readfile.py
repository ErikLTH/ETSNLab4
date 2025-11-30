

def openfile(file):
    """Open a file and return its contents as a list of lines."""
    
    file = open(file, 'r')
    lines = file.readlines()
    file.close()

    return lines


def main():
    try:
        lines = openfile('nilsholg.txt')
    except Exception as e:
        print(f"An error occurred: {e}")
        return


    counter = 0
    
    for line in lines:
        ord = line.split(' ') # Splittar varje rad i ord.
        #print(ord)
        for i in ord:
            if i.lower() == 'kristna':
                counter += 1
                print(i)

    print("Totalt antal ord av: " + str(counter))

if __name__ == '__main__':
    main()