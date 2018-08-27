import re

#load file
file_to_load = "raw_data/paragraph_2.txt"

#output file for later
file_to_output = "analysis/paragraph_analysis.txt"

#variable to hold the paragraph
paragraph = ""

#Read the text file
with open(file_to_load) as txt_data:

    #Store contents into string 
    paragraph = txt_data.read().replace("\n", " ")

#Split the paragraph to calculate word count between spaces
word_split = paragraph.split(" ")
word_count = len(word_split)

#Make a list to hold all letter counts
total_letter_count = []

#Calculate the length of each word
for word in word_split:
    #add each individual word to total_letters
    total_letter_count.append(len(word))

#Calculate the average letter count
avg_letter_count = sum(total_letter_count) / float(len(total_letter_count))

#Split the paragraph based on the punctuations
sentence_split = re.split("(?<=[.!?] +", paragraph)
print(sentence_split)

#Sentence Counts
sentence_count = len(sentence_split)

#Words per sentence
words_per_sentence = []

#Loop sentence_split and calculate the number of words in each sentence
for sentence in sentence_split:

    #Calculate the words in each sentence and store to list
    words_per_sentence.append(len(sentence.split(" ")))
    
#Average Word Count per sentence
avg_sentence = sum(words_per_sentence) / float(len(words_per_sentence))

#Output Results
results = (
    f"\nParagraph Analysis\n"
    f"-----------------\n"
    f"Approximate Word Count: {word_count}\n"
    f"Approximate Sentence Count: {sentence_count}\n"
    f"Average Letter Count: {avg_letter_count}\n"
    f"Average Sentence Length: {avg_sentence}\n")

#Print to terminal to test
print(results)

#Write results to a text file
with open(file_to_output, "a") as txt_file:
    txt_file.write(results)