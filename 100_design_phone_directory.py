# Time complexity: get - O(n), check - O(1), release - O(1)
# Space complexity: get - O(n), check - O(n), release - O(n)

# Approach - Maintain a queue and a set and insert all the numbers in maxnumbers into these two. Get()
# fetches the first num in queue and removes it from the set. Check() is to check if the number is in the 
# set and Release() adds the number to the queue and the set.

from queue import Queue
class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        self.q = Queue()
        self.hashSet = set()
        
        for i in range(maxNumbers):
            self.q.put(i)
            self.hashSet.add(i)

    def get(self) -> int:
        if len(self.hashSet) == 0:
            return -1
        number = self.q.get()
        self.hashSet.remove(number)
        return number

    def check(self, number: int) -> bool:
        if number in self.hashSet:
            return True
        return False
        

    def release(self, number: int) -> None:
        if number in self.hashSet:
            return
        self.q.put(number)
        self.hashSet.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)