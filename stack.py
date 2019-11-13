
class Stack:
    """
    Common datastructure used heavily
    """
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def insert(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def remove(self, object):
        """
        Todo: maybe return removed object to use?
        :param object:
        :return:
        """
        if self.is_empty():
            return None
        self.stack.remove(object)

    def size(self):
        return len(self.stack)
