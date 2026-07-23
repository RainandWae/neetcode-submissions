class TrieNode:
    def __init__(self):
        # maps char -> next TrieNode
        self.children = {}
        # mark end of a valid word
        self.word = False


class WordDictionary:
    def __init__(self):
        # empty root, no char, starting point
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            # create path if char doesn't exist yet
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # move down to that node
            cur = cur.children[c]
        # mark last node as end of word
        cur.word = True

    def search(self, word: str) -> bool:
        # dfs from position j in word, starting at given trie node
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    # wildcard, try every possible child path
                    for child in cur.children.values():
                        # recurse deeper with rest of word
                        if dfs(i + 1, child):
                            return True
                    # none of the children worked
                    return False
                else:
                    # no matching path, dead end
                    if c not in cur.children:
                        return False
                    # move forward normally
                    cur = cur.children[c]
            # reached end of word, check if it's a valid word
            return cur.word

        # start search from beginning of word, at root
        return dfs(0, self.root)