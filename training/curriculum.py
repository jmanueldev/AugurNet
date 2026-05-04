class Curriculum:
    def __init__(self):
        self.stages = [0.1, 0.3, 0.6, 0.9]

    def get(self, epoch):
        return self.stages[min(epoch // 5, len(self.stages)-1)]