class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        return

    def __str__(self):
        return self.prompt + "\nAnswer: " + self.answer
