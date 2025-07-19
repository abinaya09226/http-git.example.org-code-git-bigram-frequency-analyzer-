class BigramFrequencyProcessor:
    def __init__(self, text: str):
        self.text = text.lower()
        self.words = self.text.split()
    
    def total(self) -> int:
        return len(self.words)
    
    def count(self, word1: str, word2: str) -> int:
        count = 0
        for i in range(len(self.words) - 1):
            if self.words[i] == word1.lower() and self.words[i + 1] == word2.lower():
                count += 1
        return count
    
text = "The cat sat on the mat. The cat saw a rat. The cat ran."
processor = BigramFrequencyProcessor(text)

print("Total words:", processor.total())  
print("Count of 'the cat':", processor.count("the", "cat"))  
print("Count of 'cat sat':", processor.count("cat", "sat"))  
print("Count of 'saw a':", processor.count("saw", "a"))      
