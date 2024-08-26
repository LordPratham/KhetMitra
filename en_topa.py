from deep_translator import GoogleTranslator

# Read the input text file
with open('cleaned_punjabi_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()[:500]

# Translate the text to Punjabi
translator = GoogleTranslator(source='en', target='pa')
translated_text = translator.translate(text)

# Write the translated text to a new file
with open('translated_output.txt', 'w', encoding='utf-8') as file:
    file.write(translated_text)

print("Translation complete! The translated text has been saved to 'translated_output.txt'.")
