class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value > self.value:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
    if value < self.value:
        if self.left is None:
          self.left = BinarySearchTree(value)
        else:
          self.left.insert(value)

  def contains(self, target):
    if self.value is target:
      return True
    elif not self.left and not self.right:
      return False
    elif target > self.value:
      return self.right.contains(target)
    elif target < self.value:
      return self.left.contains(target)

  def get_max(self):
    max = 0
    if not self.right:
      max = self.value
    while self.right:
      max = self.value
      return self.right.get_max()
    return max

  def for_each(self, cb):
    pass