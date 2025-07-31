import sys


class TrieNode:
    def __init__(self):
        self.children = {}
        self.counter = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.counter += 1

    def get_min_prefix(self, word):
        node = self.root
        pressed = 0
        for char in word:
            if char not in node.children:
                return len(word)
            node = node.children[char]
            pressed += 1
            if node.counter == 1:
                return pressed
        return pressed


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    words = data[1:n + 1]

    trie = Trie()
    total_presses = 0

    for word in words:
        if not trie.root.children:
            total_presses += len(word)
        else:
            min_presses = trie.get_min_prefix(word)
            if min_presses == len(word):
                total_presses += min_presses
            else:
                total_presses += len(word)
        trie.insert(word)

    print(total_presses)


if __name__ == '__main__':
    main()