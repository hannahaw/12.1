import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    clean_text = ""
    inside_tag = False

    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            clean_text += char

    final_lines = []
    for line in clean_text.split('\n'):
        stripped_line = line.strip()
        if stripped_line:
            final_lines.append(stripped_line)

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write('\n'.join(final_lines))

delete_html_tags('draft.html')
