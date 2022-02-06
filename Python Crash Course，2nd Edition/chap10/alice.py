# with open('alice.txt', encoding = 'utf-8') as f:
# 	contents = f.read()
# print(contents)


filename = 'alice.txt'

try:
	with open('alice.txt', encoding = 'utf-8') as f:
		contents = f.read()
except FileNotFoundError as e:
	print(f"Sorry, the file {filename} does not exist.")
else:
	# print(contents)
# How many words are calculated the documents
	words = contents.split()
	num_words = len(words)
	print(f"The file {filename} has about {num_words} words. ")