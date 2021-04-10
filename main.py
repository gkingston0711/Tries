class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        parent = self.root
        for c in word:  # Go each character in the word
            if not c in parent.child:
                parent.child[c] = TrieNode()
            # Go to the next word
            parent = parent.child[c]
        # End of the word, turn flag - True
        parent.end = True

    def search(self, word):
        parent = self.root
        for c in word:
            if not c in parent.child:
                return False
            parent = parent.child[c]

        return parent.end

    def searchPre(self, word):
        parent = self.root

        for pre in word:
            if not pre in parent.child:
                return False
            parent = parent.child[pre]

        return True

    def replaceWord(self, word):
        parent = self.root
        ans = ''
        for c in word:
            if not c in parent.child:
                return word
            parent = parent.child[c]
            ans += c
            if parent.end==True:
                return ans

        return word







def menu():
    print('1. Add word in the Trie')
    print('2. Search a word')
    print('3. Search the prefix')
    print('4. Replace the word from a sentence')
    print('10. Exit')


def pickOption():
    try:
        choice = int(input('Enter your choice: '))
        if choice < 1:
            print('Invalid option. Must be a positive number')
            pickOption()
        return choice
    except ValueError:
        print('Invalid option. It must be a number')
        pickOption()


def main():
    # Read from the file
    # Build the Trie
    myTrie = Trie()
    # read in .txt file into trie
    inFile = open('words.txt', 'r')
    # looping and striping to add all words to trie
    for line in inFile:
        line = line.rstrip('\n')
        myTrie.insert(line)

    while True:
        menu()
        choice = pickOption()
        if choice == 1:
            word = input('Enter the word: ')
            myTrie.insert(word)
        elif choice == 2:
            word = input('Enter the word: ')
            found = myTrie.search(word)
            if (found):
                print(word, 'is inside the Trie')
            else:
                print(word, 'is not inside the Trie')
        elif choice == 3:
            word = input('Enter prefix: ')
            found = myTrie.searchPre(word)
            if (found):
                print(word, 'Prefix IS inside the Trie')
            else:
                print(word, 'Prefix IS NOT inside the Trie')
        elif choice == 4:
            sentence = input('Enter the sentence: ')
            words = sentence.split(' ')
            output = ''
            for word in words:
                output += myTrie.replaceWord(word) + ' '

            print('OUtput sentence after replacing:', output)

        else:
            break

        print()


main()
