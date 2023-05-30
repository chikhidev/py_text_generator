import os
import random
import time

# Define the number of files to create
num_files = 50

# Load a text corpus to use as a basis for generating the random text
with open("corpus.txt") as f:
    text = f.read()

# Split the text corpus into sentences
sentences = text.split(". ")

# Generate and commit changes for each file
for i in range(num_files):
    # Select a random sentence from the corpus
    random_sentence = random.choice(sentences)

    # Check if the random sentence is None before writing it to the file
    file_name = f"file{i}.txt"
	
    if random_sentence:
        # Write the sentence to a new file
        with open(os.path.join(file_name), "w") as f:
            f.write(random_sentence.strip() + ".\n")

        # Add, commit, and push the changes to the Git repository
        os.system(f"git add {file_name}")
        os.system(f"git commit -m 'Added {file_name}'")
        os.system("git push origin master")
        sleep_time = random.randint(10, 30)
        time.sleep(sleep_time)
    else:
        print(f"Failed to generate random sentence for file {file_name}")

