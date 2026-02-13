class FrequencyTracker:

    def __init__(self):
        self.freq_count = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        if self.freq[number] != 0:
            self.freq_count[self.freq[number]] -= 1
            if not self.freq_count[self.freq[number]]:
                del self.freq_count[self.freq[number]]
        self.freq[number] += 1
        self.freq_count[self.freq[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.freq[number] != 0:
            self.freq_count[self.freq[number]] -= 1
            if not self.freq_count[self.freq[number]]:
                del self.freq_count[self.freq[number]]
            self.freq[number] -= 1
        if self.freq[number] != 0:
            self.freq_count[self.freq[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count[frequency] != 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)