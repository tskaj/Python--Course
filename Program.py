from urllib.request import urlopen
def fetch_words():
    """
    1. Opens a URL with Urlopen
    2. Initializes an empty list to store the words
    3. Decodes each line from bytes to string
    4. Reads the line from the response
    5. Decodes each line from bytes to string
    6. Closes the URL

    """     # Docstring
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []

    for line in story:  
        decoded_line = line.decode('utf-8')
    
    # Optionally, you can split the line into words and append to the list
        story_words.extend(decoded_line.split())
    
    story.close()
    
    return story_words

def print_words(story_words):
# Print the list of words
    print(story_words)

def main():
    words = fetch_words()
    print_words(words)

if __name__ == '__main__':
    main()
