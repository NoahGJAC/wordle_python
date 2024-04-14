class LetterState:
    """A class to represent the state of a letter in a wordle game."""
    def __init__(self, character: str, is_in_word: bool = False, is_in_position: bool = False):
        self.character: str = character
        self.is_in_word: bool = is_in_word
        self.is_in_position: bool = is_in_position

    def __repr__(self):
        return f'LetterState(character = {self.character}, is_in_word = {self.is_in_word}, is_in_position = {self.is_in_position})'
    
    def __str__(self):
        return f'Letter: {self.character} \n\tIs in word: {self.is_in_word} \n\tIs in correct position: {self.is_in_position}'