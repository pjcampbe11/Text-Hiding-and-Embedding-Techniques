import argparse
import base64
import urllib.parse
import unicodedata
from html import escape

def zero_width_characters(text):
    return text + "\u200b" + "hidden"  # Zero-width space

def unicode_whitespace(text):
    return text + "\u2002" + "hidden"  # en space

def base64_encoding(text):
    encoded_text = base64.b64encode(text.encode()).decode()
    return text + encoded_text

def url_encoding(text):
    return text + urllib.parse.quote("hidden")

def zero_font_size(text):
    return f'<p>{text}<span style="font-size:0">hidden</span></p>'

def small_font_size(text):
    return f'<p>{text}<span style="font-size:1px">hidden</span></p>'

def html_comment_tags(text):
    return f'<p>{text}<!-- hidden --></p>'

def character_substitution(text):
    return text + "h\u0435\u0456\u0440d"  # Substituted 'e' with Cyrillic 'е'

def homoglyphs(text):
    return text + "hеllо"  # Cyrillic 'е' and 'о'

def polyglot_text(text):
    return text + "こんにちは"  # Japanese for "Hello"

def hidden_in_plain_sight(text):
    return text + " By the way, every first letter here spells a hidden message."

def metadata_fields(text):
    return f'<meta name="description" content="{text}">'  # Metadata in HTML

def javascript_embedding(text):
    return f'<script>var hidden="{text}";</script>'

def css_manipulation(text):
    return f'<p>{text}<span style="display:none">hidden</span></p>'

def process_text(text, technique):
    techniques = {
        'zero_width': zero_width_characters,
        'unicode_whitespace': unicode_whitespace,
        'base64': base64_encoding,
        'url': url_encoding,
        'zero_font': zero_font_size,
        'small_font': small_font_size,
        'html_comment': html_comment_tags,
        'char_sub': character_substitution,
        'homoglyphs': homoglyphs,
        'polyglot': polyglot_text,
        'plain_sight': hidden_in_plain_sight,
        'metadata': metadata_fields,
        'javascript': javascript_embedding,
        'css': css_manipulation,
    }
    
    if technique not in techniques:
        raise ValueError("Invalid technique selected")
    
    return techniques[technique](text)

def main():
    parser = argparse.ArgumentParser(description="Text Hiding and Embedding Techniques")
    parser.add_argument('-t', '--technique', required=True, choices=[
        'zero_width', 'unicode_whitespace', 'base64', 'url', 'zero_font', 
        'small_font', 'html_comment', 'char_sub', 'homoglyphs', 'polyglot', 
        'plain_sight', 'metadata', 'javascript', 'css'
    ], help="Technique to use for hiding or embedding text")
    parser.add_argument('-p', '--payload', help="Text payload to process")
    parser.add_argument('-f', '--file', help="File containing text payload")

    args = parser.parse_args()

    if args.payload:
        text = args.payload
    elif args.file:
        with open(args.file, 'r') as file:
            text = file.read()
    else:
        raise ValueError("Either payload or file must be provided")

    processed_text = process_text(text, args.technique)
    print(processed_text)

if __name__ == "__main__":
    main()
