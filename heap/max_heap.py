class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    value_index = len(self.storage) - 1
    self._bubble_up(value_index)

  def delete(self):
    self.storage[0] = self.storage[-1]
    self.storage.pop()
    start = 0
    while start <= len(self.storage) - 3:
      idx = max(self.storage[start + 1], self.storage[start + 2])
      index = self.storage.index(idx)
      start +=1
      self._bubble_up(index)

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    while index > 0:
      parent = (index - 1) // 2
      if self.storage[index] > self.storage[parent]:
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        index = parent
      else:
        break

  def _sift_down(self, index):
    pass
