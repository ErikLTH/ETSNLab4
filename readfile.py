import sys
import re



def openfile(file):
    """Open a file and return its contents as a list of lines."""
    
    file = open(file, 'r')
    lines = file.readlines()
    file.close()

    return lines


def main():
    """Main function to search for a pattern in a file."""


    #Atleast 3 arguments are needed
    if len(sys.argv) < 3:
        print("Usage: search <pattern> <file>")
        return

    #Pick out the passed arguments from the CLI
    pattern = sys.argv[1]
    filename = sys.argv[2]
    

    #Try open the file and handle exceptions
    try:
        lines = openfile(filename)
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    is_single_word = len(pattern.split()) == 1
    
    for line in lines:
        
        # Split the each line into a list of words, using regex to handle various delimiters such as , . ! ? ; : \n \t and spaces
        words = re.split(r"[ ,.!?;:\n\t]+", line)

        # If patterns contains only one word, we check each word in the line.
        if(is_single_word): 
            for i in words:
                if i.lower() == pattern.lower():
                    print(line)

                    # No need to check further words in the line, no need for duplicate lines
                    break 

        # If patterns contatins more than one word, we check if the whole line contains the pattern.
        else:
            if line.lower().__contains__(pattern.lower()):
                print(line)



if __name__ == '__main__':
    """Run the main function."""
    main()