class DynamicArray:
    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.length: int = 0
        self.array: list[int] = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if len(self.array) == self.capacity:
            self.resize()
        self.array.append(n)
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.array[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [0] * self.capacity

        for i in range(self.length):
            new_array[i] = self.array[i]

        self.array = new_array

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity
