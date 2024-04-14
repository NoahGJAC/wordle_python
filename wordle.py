from letter_state import LetterState

class Wordle():
    """Wordle game class."""
    MAX_GUESSES = 6
    WORD_LENGTH = 5

    def __init__(self, secret: str):
        """Initialize the Wordle game."""
        self._secret: str = secret.upper()
        self.guesses = []

    @property
    def is_solved(self) -> bool:
        """Check if the word has been solved.

            Returns:
                Returns True if the word has been solved, False otherwise."""
        return self.guesses and self.guesses[-1] == self._secret
    
    @property
    def can_guess(self) -> bool:
        """Check if the player can still guess.
        
            Returns:
                (bool) Returns True if the player can still guess, False otherwise."""
        return len(self.guesses) < self.MAX_GUESSES and not self.is_solved
    
    @property
    def remaining_guesses(self) -> int:
        """Get the number of remaining guesses.

            Returns:
                (int) Returns the number of remaining guesses."""
        return self.MAX_GUESSES - len(self.guesses)
    
    def guess(self, guess: str) -> bool:
        """Guess the word. Return True if the guess is correct, False otherwise.
            Args:
                guess (str): The word to be guessed.
                
            Returns:
                Returns True if the guess is correct, False otherwise."""
        if not self.validate_guess(guess):
            return False
        
        self.guesses.append(guess.upper())
        return self._secret == guess.upper()

    def validate_guess(self, guess: str) -> bool:
        """Check if the guess is valid.
            Args:
                guess (str): The word to be guessed.

            Returns:
                Returns True if the guess is valid, False otherwise."""
        return len(guess) == self.WORD_LENGTH and guess.isalpha()
    
    def get_guess_feedback(self, guess: str) -> list[LetterState]:
        """Get the feedback for the guess.
            Args:
                guess (str): The word to be guessed.

            Returns:
                Returns a list of LetterState objects."""
        guess = guess.upper()
        return [LetterState(character = guess[i], is_in_word= guess[i] in self._secret, is_in_position=guess[i] == letter) for i, letter in enumerate(self._secret)]
    
    def display(self) -> str:
        """Display the secret word."""
        return self._secret

    def is_over(self) -> bool:
        """Check if the game is over."""
        return self.remaining_guesses <= 0
    

def main():
    print('Hello Wordle!')
    wordle = Wordle('Slate')

    while wordle.can_guess:
        word: str = input("Type your guess: ").upper()

        if not wordle.validate_guess(word):
            print('Invalid guess. Please try again.')
            continue
        
        wordle.guess(word)
        result = wordle.get_guess_feedback(word)
        print(*result, sep='\n')

        if wordle.is_solved:
            print('You win!')
            print(f'The word was: {wordle.display()}')
            break
        else:
            print(f'You have {wordle.remaining_guesses} guesses left.')
            print(f'Your guess: {wordle.guesses[-1] if wordle.guesses else 'was invalid'}')

        if wordle.is_over():
            print('You lose!')
            print(f'The word was: {wordle.display()}')
            break

if __name__ == '__main__':
    main()