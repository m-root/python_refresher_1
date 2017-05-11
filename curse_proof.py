import urllib

def read_text():
    quotes = open("C:\detect\movies.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profinity(contents_of_file)

def check_profinity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q"+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

    if "true" in output:
        print("There is a profane word in the output.")
    elif "false" in output:
        print("There is no profane word in the output.")
    else:
        print("Could not scan the text file.")

read_text()