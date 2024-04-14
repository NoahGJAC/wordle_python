class Wordle():

    MAX_GUESSES = 6
    WORD_LENGTH = 5

    def __init__(self, secret: str):
        self._secret: str = secret
        self.guesses = []

    @property
    def is_solved(self) -> bool:
        return self.guesses and self.guesses[-1] == self._secret
    
    @property
    def can_guess(self) -> bool:
        return len(self.guesses) < self.MAX_GUESSES and not self.is_solved
    
    @property
    def remaining_guesses(self) -> int:
        return self.MAX_GUESSES - len(self.guesses)
    
    def guess(self, guess: str) -> bool:
        self.guesses.append(guess)
        return self._secret == guess

    def display(self):
        return self._secret

    def is_over(self):
        return len(self.guesses) >= self.max_guesses
    

def main():
    print('Hello Wordle!')
    wordle = Wordle('SLATE')

    while wordle.can_guess:
        word: str = input("Type your guess: ")
        wordle.guess(word)

        if wordle.is_solved:
            print('You win!')
            print(f'The word was: {wordle.display()}')
            break
        else:
            print(f'You have {wordle.remaining_guesses} guesses left.')
            print(f'Your guess: {wordle.guesses[-1]}')

if __name__ == '__main__':
    main()