# Text Hiding and Embedding Techniques

This script implements various text hiding and embedding techniques to demonstrate how hidden or embedded instructions can be concealed in text. Users can select a technique, provide a text blob as a payload, or submit a text file as input.

## Available Techniques

1. **Zero Width Characters**: Embeds invisible zero-width characters.
2. **Unicode Whitespace**: Uses Unicode whitespace characters to hide text.
3. **Base64 Encoding**: Encodes the text in Base64 and appends it.
4. **URL Encoding**: Encodes the text using URL encoding.
5. **Zero Font Size**: Hides text by setting font size to zero.
6. **Small Font Size**: Hides text with a very small font size.
7. **HTML Comment Tags**: Embeds text within HTML comment tags.
8. **Character Substitution**: Substitutes characters with visually similar ones from different scripts.
9. **Homoglyphs**: Uses similar-looking characters from different alphabets.
10. **Polyglot Text**: Embeds text in multiple languages.
11. **Hidden in Plain Sight**: Uses sentences with hidden instructions.
12. **Metadata Fields**: Embeds text within metadata fields.
13. **JavaScript Embedding**: Embeds text within JavaScript code.
14. **CSS Manipulation**: Hides text using CSS.

## Installation

No additional packages are required for this script.

## Usage

Run the script with the desired technique, specifying either a payload or a file containing the text.

### Command-Line Options

- `-t, --technique`: Technique to use. Choices are `zero_width`, `unicode_whitespace`, `base64`, `url`, `zero_font`, `small_font`, `html_comment`, `char_sub`, `homoglyphs`, `polyglot`, `plain_sight`, `metadata`, `javascript`, `css`.
- `-p, --payload`: Text payload to process.
- `-f, --file`: File containing text payload.

### Examples

**Using Payload:**
```
python text_embedding.py -t base64 -p "This is a test."
```
Using File:

```
python text_embedding.py -t url -f input.txt

```
License
This project is licensed under the MIT License.

```
This script provides a comprehensive set of techniques for hiding or embedding text, suitable for various scenarios where text needs to be concealed from casual observation but still interpreted by an AI model or similar systems.
```
