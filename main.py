import sys


letter0 = []
letter1 = []
letter2 = []
letter3 = []
letter4 = []


words = len(sys.argv) - 2

confirmed = []

confirmed_word = sys.argv[1]

for letter in confirmed_word:
    if letter == '_':
        confirmed.append(None)
    else:
        confirmed.append(letter)

print(confirmed)

for i in range(words):
    word = sys.argv[i + 2]
    word = word.lower()
    print(word)
    if len(word) != 5:
        print(f"Invalid input. {word} is a SHIT word. Gotta be five letters.")
        sys.exit()
    else:
        # for j in range(len(word)):
        #     letter_lists[j].append(word[i])
        letter0.append(word[0])
        letter1.append(word[1])
        letter2.append(word[2])
        letter3.append(word[3])
        letter4.append(word[4])

# if len(sys.argv) != 2 or len(sys.argv[1]) != 5:
#     print("Invalid input. Please provide a single 5-letter word as an argument.")
# else:
#     word = sys.argv[1]

#     letter1.append(word[0])
#     letter2.append(word[1])
#     letter3.append(word[2])
#     letter4.append(word[3])
#     letter5.append(word[4])

letter_lists = [letter0, letter1, letter2, letter3, letter4]
print(letter_lists)

res_words = []


print(f"1. {letter0}")
print(f"2. {letter1}")
print(f"3. {letter2}")
print(f"4. {letter3}")
print(f"5. {letter4}")



# Open the text file for reading
with open('valid-wordle-words.txt', 'r') as file:
    # Read the lines from the file and store them in a list
    word_list = file.read().splitlines()


possible_words = []

for word in word_list:
    
    flag = True
    for i in range(5):
        if confirmed[i] and confirmed[i] != word[i]:
            flag = False

            
    
    if flag:
        possible_words.append(word)


print(len(possible_words))

if len(possible_words) < 10:
    print(possible_words)