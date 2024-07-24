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

1. **Zero Width Characters**
    ```
    python text_embedding.py -t zero_width -p "This is a test."
    ```
    **Output:**
    ```
    This is a test.‍hidden
    ```

2. **Unicode Whitespace**
    ```
    python text_embedding.py -t unicode_whitespace -p "This is a test."
    ```
    **Output:**
    ```
    This is a test. hidden
    ```

3. **Base64 Encoding**
    ```
    python text_embedding.py -t base64 -p "This is a test."
    ```
    **Output:**
    ```
    This is a test.VGhpcyBpcyBhIHRlc3Q=
    ```

4. **URL Encoding**
    ```
    python text_embedding.py -t url -p "This is a test."
    ```
    **Output:**
    ```
    This is a test.hidden
    ```

5. **Zero Font Size**
    ```
    python text_embedding.py -t zero_font -p "This is a test."
    ```
    **Output:**
    ```html
    <p>This is a test.<span style="font-size:0">hidden</span></p>
    ```

6. **Small Font Size**
    ```
    python text_embedding.py -t small_font -p "This is a test."
    ```
    **Output:**
    ```html
    <p>This is a test.<span style="font-size:1px">hidden</span></p>
    ```

7. **HTML Comment Tags**
    ```
    python text_embedding.py -t html_comment -p "This is a test."
    ```
    **Output:**
    ```html
    <p>This is a test.<!-- hidden --></p>
    ```

8. **Character Substitution**
    ```
    python text_embedding.py -t char_sub -p "This is a test."
    ```
    **Output:**
    ```
    This is a test.hеllо
    ```

9. **Homoglyphs**
    ```
    python text_embedding.py -t homoglyphs -p "This is a test."
    ```
    **Output:**
    ```
    This is a test.hеllо
    ```

10. **Polyglot Text**
    ```
    python text_embedding.py -t polyglot -p "This is a test."
    ```
    **Output:**
    ```
    This is a test.こんにちは
    ```

11. **Hidden in Plain Sight**
    ```
    python text_embedding.py -t plain_sight -p "This is a test."
    ```
    **Output:**
    ```
    This is a test. By the way, every first letter here spells a hidden message.
    ```

12. **Metadata Fields**
    ```
    python text_embedding.py -t metadata -p "This is a test."
    ```
    **Output:**
    ```html
    <meta name="description" content="This is a test.">
    ```

13. **JavaScript Embedding**
    ```
    python text_embedding.py -t javascript -p "This is a test."
    ```
    **Output:**
    ```html
    <script>var hidden="This is a test.";</script>
    ```

14. **CSS Manipulation**
    ```
    python text_embedding.py -t css -p "This is a test."
    ```
    **Output:**
    ```html
    <p>This is a test.<span style="display:none">hidden</span></p>
    ```

**Using File:**

1. **Zero Width Characters**
    ```
    python text_embedding.py -t zero_width -f input.txt
    ```
    **Output:**
    ```
    This is a test.‍hidden
    ```

2. **Unicode Whitespace**
    ```
    python text_embedding.py -t unicode_whitespace -f input.txt
    ```
    **Output:**
    ```
    This is a test. hidden
    ```

3. **Base64 Encoding**
    ```
    python text_embedding.py -t base64 -f input.txt
    ```
    **Output:**
    ```
    This is a test.VGhpcyBpcyBhIHRlc3Q=
    ```

4. **URL Encoding**
    ```
    python text_embedding.py -t url -f input.txt
    ```
    **Output:**
    ```
    This is a test.hidden
    ```

5. **Zero Font Size**
    ```
    python text_embedding.py -t zero_font -f input.txt
    ```
    **Output:**
    ```html
    <p>This is a test.<span style="font-size:0">hidden</span></p>
    ```

6. **Small Font Size**
    ```
    python text_embedding.py -t small_font -f input.txt
    ```
    **Output:**
    ```html
    <p>This is a test.<span style="font-size:1px">hidden</span></p>
    ```

7. **HTML Comment Tags**
    ```
    python text_embedding.py -t html_comment -f input.txt
    ```
    **Output:**
    ```html
    <p>This is a test.<!-- hidden --></p>
    ```

8. **Character Substitution**
    ```
    python text_embedding.py -t char_sub -f input.txt
    ```
    **Output:**
    ```
    This is a test.hеllо
    ```

9. **Homoglyphs**
    ```
    python text_embedding.py -t homoglyphs -f input.txt
    ```
    **Output:**
    ```
    This is a test.hеllо
    ```

10. **Polyglot Text**
    ```
    python text_embedding.py -t polyglot -f input.txt
    ```
    **Output:**
    ```
    This is a test.こんにちは
    ```

11. **Hidden in Plain Sight**
    ```
    python text_embedding.py -t plain_sight -f input.txt
    ```
    **Output:**
    ```
    This is a test. By the way, every first letter here spells a hidden message.
    ```

12. **Metadata Fields**
    ```
    python text_embedding.py -t metadata -f input.txt
    ```
    **Output:**
    ```html
    <meta name="description" content="This is a test.">
    ```

13. **JavaScript Embedding**
    ```
    python text_embedding.py -t javascript -f input.txt
    ```
    **Output:**
    ```html
    <script>var hidden="This is a test.";</script>
    ```

14. **CSS Manipulation**
    ```
    python text_embedding.py -t css -f input.txt
    ```
    **Output:**
    ```html
    <p>This is a test.<span style="display:none">hidden</span></p>
    ```
License
This project is licensed under the MIT License.

```
This script provides a comprehensive set of techniques for hiding or embedding text, suitable for various scenarios where text needs to be concealed from casual observation but still interpreted by an AI model or similar systems.
```
