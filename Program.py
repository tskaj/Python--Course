from urllib.request import urlopen
def fetch_words():
# Open the URL
    story = urlopen('http://sixty-north.com/c/t.txt')

# Initialize an empty list to store the words
    story_words = []

# Read the lines from the response
    for line in story:
    # Decode each line from bytes to string
        decoded_line = line.decode('utf-8')
    # Optionally, you can split the line into words and append to the list
        story_words.extend(decoded_line.split())
# Close the URL
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
