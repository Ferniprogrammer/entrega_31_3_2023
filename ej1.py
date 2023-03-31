import unidecode
class palindrome:
    def __init__(self, word):
        self.word = word
    def is_palindrome(self):
        word = self.word.lower()
        word = word.replace(" ", "")
        word = unidecode.unidecode(word)
        word = ''.join(filter(str.isalnum, word))
        right = len(word) -1
        left = 0
        if len(word) % 2 == 0:
            repeticiones = len(word)//2
        else:
            repeticiones = (len(word) -1)//2
        for _ in range(repeticiones):
            if word[left] == word[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
