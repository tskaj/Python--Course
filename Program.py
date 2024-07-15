from urllib.request import urlopen

# Open the URL
story = urlopen('http://sixty-north.com/c/t.txt')

# Initialize an empty list to store the words
story_words = []

# Read the lines from the response
for line in story:
    # Decode each line from bytes to string
    decoded_line = line.decode('utf-8')
    # Print the decoded line
    print(decoded_line)
    # Optionally, you can split the line into words and append to the list
    story_words.extend(decoded_line.split())

# Close the URL
story.close()

# Print the list of words (optional)
print(story_words)
