def convert_words(length: int) -> None:
    """Convert words of a certain length to a new file."""
    input_file_path = 'data/word_source.txt'
    output_file_path = 'data/filtered_words.txt'
    filtered_words: list[str] = []

    with open(input_file_path, 'r') as file:
        for line in file.readlines():
            word = line.strip()
            if len(word) == length:
                filtered_words.append(word)
    
    with open(output_file_path, 'w') as file:
        for word in filtered_words:
            file.write(f'{word}\n')

    print(f'Filtered {len(filtered_words)} words of length {length}.')

if __name__ == '__main__':
    convert_words(5)