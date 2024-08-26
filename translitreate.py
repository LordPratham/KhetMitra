from transliterate import translit

# Define a function to convert Romanized Punjabi to Gurmukhi script
def roman_to_gurmukhi(text):
    # Note: You may need a custom mapping if the library does not support Punjabi directly
    return translit(text, 'pa', reversed=True)

# Read the input text file
with open('cleaned_punjabi_text.txt', 'r', encoding='utf-8') as file:
    romanized_text = file.read()

# Convert to Gurmukhi script
gurmukhi_text = roman_to_gurmukhi(romanized_text)

# Write the converted text to a new file
with open('translated_output.txt', 'w', encoding='utf-8') as file:
    file.write(gurmukhi_text)

print("Transliteration complete! The text has been saved to 'translated_output.txt'.")
