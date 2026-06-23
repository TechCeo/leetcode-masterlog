"""
Trie (Prefix Tree)
------------------

A trie stores strings one character at a time. Words with the same prefix
share nodes, making prefix queries efficient.

Complexity for a word of length m:
- Insert, search, remove, prefix lookup: O(m)

Common Uses:
- Autocomplete
- Spell checking
- Dictionary and prefix problems
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self._size = 0

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def insert(self, word: str) -> bool:
        """Insert a word. Return False when it was already present."""
        current = self.root

        for character in word:
            if character not in current.children:
                current.children[character] = TrieNode()
            current = current.children[character]

        if current.is_word:
            return False

        current.is_word = True
        self._size += 1
        return True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_word

    def starts_with(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def remove(self, word: str) -> bool:
        """Remove a word and prune nodes that no other word needs."""
        def remove_from(node, index):
            if index == len(word):
                if not node.is_word:
                    return False, False

                node.is_word = False
                should_prune = not node.children
                return True, should_prune

            character = word[index]
            child = node.children.get(character)
            if child is None:
                return False, False

            removed, prune_child = remove_from(child, index + 1)
            if prune_child:
                del node.children[character]

            should_prune = not node.is_word and not node.children
            return removed, should_prune

        removed, _ = remove_from(self.root, 0)
        if removed:
            self._size -= 1
        return removed

    def words_with_prefix(self, prefix: str) -> list:
        """Return stored words beginning with prefix in sorted order."""
        start = self._find_node(prefix)
        if start is None:
            return []

        words = []

        def collect(node, suffix):
            if node.is_word:
                words.append(prefix + suffix)

            for character in sorted(node.children):
                collect(node.children[character], suffix + character)

        collect(start, "")
        return words

    def _find_node(self, text: str):
        current = self.root

        for character in text:
            current = current.children.get(character)
            if current is None:
                return None

        return current

    def __repr__(self) -> str:
        return f"Trie({self.words_with_prefix('')})"


if __name__ == "__main__":
    trie = Trie()
    for word in ["app", "apple", "application", "bat"]:
        assert trie.insert(word)

    assert not trie.insert("app")
    assert trie.search("app")
    assert not trie.search("ap")
    assert trie.starts_with("appl")
    assert trie.words_with_prefix("app") == ["app", "apple", "application"]

    assert trie.remove("apple")
    assert not trie.search("apple")
    assert trie.search("app")
    assert trie.search("application")
    assert not trie.remove("absent")
    assert trie.size() == 3

    print("All trie tests passed.")
