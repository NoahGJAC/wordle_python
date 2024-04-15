from letter_state import LetterState
from colorama import Fore, Style
from typing import List
from data.convert_words import convert_words
import random

#TODO: MVC pattern
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
    
    @property
    def secret(self) -> str:
        """Returns the secret word.
        
            Returns:
                Returns the secret word."""
        return self._secret

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
                (list[LetterState]): Returns a list of LetterState objects."""
        guess = guess.upper()
        return [
            LetterState(
                character=guess[i],
                is_in_word=guess[i] in self._secret,
                is_in_position=guess[i] == letter)
            for i, letter in enumerate(
                self._secret)]

    def is_over(self) -> bool:
        """Check if the game is over."""
        return self.remaining_guesses <= 0


def main():
    word_set = load_word_set('data/filtered_words.txt')
    print('Hello Wordle!')
    wordle = Wordle(random.choice(list(word_set)))

    while wordle.can_guess:
        word: str = input("Type your guess: ").upper()

        if not wordle.validate_guess(word):
            print(Fore.RED + 'Invalid guess. Please try again.' + Fore.RESET)
            continue
        
        if word not in word_set:
            print(Fore.RED + 'Word is not valid. Please try again.' + Fore.RESET)
            continue

        wordle.guess(word)
        display_results(wordle)

        if wordle.is_solved:
            print('You won!')
            print(f'The word was: {wordle.secret}')
            break
        else:
            print(f'You have {wordle.remaining_guesses} guesses left.')
            print(f'Your guess: {
                  wordle.guesses[-1] if wordle.guesses else 'was invalid'}')

        if wordle.is_over():
            print('You lose!')
            print(f'The word was: {wordle.secret}')
            break


def display_results(wordle: Wordle):
    lines: List[str] = []
    for word in wordle.guesses:
        result = wordle.get_guess_feedback(word)
        coloured_result_str = convert_result_to_color(result)
        lines.append(coloured_result_str)
    
    for _ in range(Wordle.MAX_GUESSES - len(wordle.guesses)):
        lines.append(' '.join(['_'] * wordle.WORD_LENGTH))
    draw_border(lines, size=Wordle.WORD_LENGTH * 2 - 1, pad=1)


def convert_result_to_color(result: List[LetterState]) -> str:
    """Convert the result to a colored string.
        Args:
            result (List[LetterState]): The result of the guess.

        Returns:
            Returns a colored string."""
    return ' '.join([Fore.GREEN +
                    letter.character +
                    Fore.RESET if letter.is_in_position else Fore.YELLOW +
                    letter.character +
                    Fore.RESET if letter.is_in_word else Fore.LIGHTBLACK_EX +
                    letter.character +
                    Fore.RESET for letter in result])


def draw_border(lines: List[str], size: int = 9, pad: int = 1) -> None:
    """Draw a border around the given lines.
        Args:
            lines (List[str]): The lines to draw the border around.
            size (int): The size of the border.
            pad (int): The padding around the border."""
    border = '+' + '-' * (size + pad * 2) + '+'
    print(border)
    for line in lines:
        print(f'|{" " * pad}{line}{" " * pad}|')
    print(border)

def load_word_set(path: str) -> set[str]:
    """Load the word set from the file.
        Returns:
            Returns a set of words."""
    word_set = set()
    with open(path, 'r') as file:
        for line in file.readlines():
            word_set.add(line.strip().upper())
        return word_set

if __name__ == '__main__':
    main()
