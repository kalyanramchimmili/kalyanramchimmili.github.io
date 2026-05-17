---
title: Implement Trie Prefix Tree
description: Implement a Trie data structure for efficient string storage and prefix searching.
tags: [Data Structures, String, Tree, Design]
---

# Implement Trie (Prefix Tree)

## Problem

Design and implement a Trie (prefix tree) data structure. This structure allows for efficient storage and retrieval of strings, with applications in features like autocomplete. The Trie should support inserting words, checking if a word exists, and checking if any inserted word starts with a given prefix.

## Approach

The author initially considered a simpler approach using a list and the `startswith` string method. However, upon realizing that Trie is a distinct data structure, they opted to implement it. A Trie is visualized as a tree where each node represents a character, and paths from the root to a node form prefixes. Nodes can be marked to indicate the end of a complete word.

The implementation involves a `TrieNode` class with `children` (a dictionary mapping characters to child nodes) and an `end` boolean flag. The `Trie` class has a `root` node.

- `insert(word)`: Traverses the Trie character by character. If a character's node doesn't exist, it's created. The traversal continues until the end of the word, at which point the `end` flag of the last node is set to `True`.
- `search(word)`: Traverses the Trie. If any character is not found, the word doesn't exist. If the traversal completes, it returns `True` only if the final node's `end` flag is `True`.
- `startsWith(prefix)`: Traverses the Trie. If any character of the prefix is not found, it returns `False`. If the traversal completes, it means a word with this prefix exists, so it returns `True`.

## Solution

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]

        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        
        return True
        
        

"""
class Trie:

    def __init__(self):
        self.ans = []
        

    def insert(self, word: str) -> None:
        self.ans.append(word)
        

    def search(self, word: str) -> bool:
        if word in self.ans:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        for word in self.ans:
            if word.startswith(prefix):
                return True
        return False
        
"""

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

## Complexity

- **Time:** O(L) — where L is the length of the word or prefix being inserted, searched, or checked for prefix. In the worst case, we traverse the entire length of the string.
- **Space:** O(N * L_avg) — where N is the number of words inserted and L_avg is the average length of the words. This is because each node can store up to 26 children, and the total number of nodes is proportional to the total number of characters stored across all words.
