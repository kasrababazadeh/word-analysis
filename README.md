# Word Analysis Project

## Overview

The **Word Analysis Project** is a Python-based tool designed to analyze text data in terms of letter frequency, patterns, and linguistic properties. This project serves as a starting point for text data analysis, which can be particularly useful in natural language processing (NLP) tasks.

## Features

The project includes several functions that analyze words from a specified text file:

- **Golden Word Check**: Determines if a word is a "golden word" based on the sum of its letters' positions in the alphabet modulo the length of the word.
- **Palindrome Check**: Checks if a word reads the same forwards and backwards.
- **Vowel Count Comparison**: Compares the count of vowels and non-vowels to determine which is greater.
- **Non-Vowel Count Comparison**: Evaluates if there are more non-vowels than vowels in a word.

## Requirements

- Python 3.x
- A text file containing words to analyze (e.g., `text.txt`)

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/kasrababazadeh/word-analysis.git
   cd word-analysis-project

2. Place your text file in the project directory (or update the file path in the code).

3. Run the script:
   ```bash
   python word_analysis.py

4. The output will display the results in the terminal, showing each word alongside its golden status, palindrome status, vowel comparison, and non-vowel comparison.

## Example Output

word    Golden  Palindrome  Vowel      Non Vowel
word1   yes     no          yes        no
word2   no      yes         no         yes
...


## Future Improvements

- Implement input validation to handle edge cases (e.g., empty lines or non-alphabetic characters).
- Enhance the analysis with additional linguistic properties.
- Create a graphical user interface (GUI) for easier interaction.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

Inspired by natural language processing concepts and string manipulation techniques.
