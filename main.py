import subprocess
import random
import time

# Define the number of files to create
num_files = 20

# Load a text corpus to use as a basis for generating the random text
with open("corpus.txt", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# Split the text corpus into sentences
sentences = text.split(". ")

# Generate and commit changes for each file
for i in range(num_files):
    # Select a random sentence from the corpus
    random_sentence = random.choice(sentences)

    # Check if the random sentence is None before writing it to the file
    file_name = f"./file{i}.txt"

    if random_sentence:
        # Write the sentence to a new file
        with open(file_name, "w") as f:
            f.write(random_sentence.strip() + ".\n")

        # Add and commit the changes to the Git repository
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", f"Added {file_name}"])

        # Push the changes to the Git repository (replace `origin` and `branch_name` with your actual values)
        subprocess.run(["git", "push", "origin", "master"])

        sleep_time = random.randint(8, 12)
        time.sleep(sleep_time)
    else:
        print(f"Failed to generate random sentence for file {file_name}")
