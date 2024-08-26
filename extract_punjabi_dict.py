import PyPDF2
import re

def extract_punjabi_words_from_pdf(pdf_path, output_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to store the extracted text
        extracted_text = ""

        # Iterate through all the pages in the PDF and extract text
        for page_num, page in enumerate(pdf_reader.pages):
            page_text = page.extract_text()
            if page_text:
                extracted_text += page_text + "\n"
            else:
                print(f"Warning: No text found on page {page_num}")

    print("Extracted text preview (first 1000 characters):")
    print(extracted_text[:1000])  # Display the first 1000 characters of the extracted text for debugging

    # Function to extract Punjabi words
    def extract_punjabi_words(text):
        # Define a regex pattern to match Punjabi words (Gurmukhi script)
        punjabi_pattern = r'[ੳਅਇਈਉਊਏਐਓਔਕਖਗਘਙਚਛਜਝਞਟਠਡਢਣਤਥਦਧਨਪਫਬਭਮਯਰਲਵਸ਼ਸਹੴਕ੍ਖ੍ਗ੍ਘ੍ਙ੍ਚ੍ਛ੍ਜ੍ਝ੍ਞ੍ਟ੍ਠ੍ਡ੍ਢ੍ਣ੍ਤ੍ਥ੍ਦ੍ਧ੍ਨ੍ਪ੍ਫ੍ਬ੍ਭ੍ਮ੍ਯ੍ਰ੍ਲ੍ਵ੍ਸ਼੍ਸ੍ਹ੍ੴ\u0a00-\u0a7f]+'
        
        # Find all matches of Punjabi words in the text
        punjabi_words = re.findall(punjabi_pattern, text)
        
        return punjabi_words

    # Extract Punjabi words from the extracted text
    punjabi_words = extract_punjabi_words(extracted_text)

    print("Number of Punjabi words extracted:", len(punjabi_words))  # Display the number of extracted Punjabi words for debugging

    # Join the words into a single string separated by new lines
    punjabi_vocab = "\n".join(punjabi_words)

    # Write the extracted Punjabi words to a text file
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(punjabi_vocab)

    print(f"Punjabi words have been extracted and saved to {output_path}")

# Define the path to your PDF file and the output text file
pdf_path = 'punjabi_vocab.pdf'
output_path = 'punjabi_vocab.txt'

# Extract Punjabi words and save to a text file
extract_punjabi_words_from_pdf(pdf_path, output_path)
