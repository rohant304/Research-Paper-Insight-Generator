def clean_text(text):

    text = text.replace("\x00", " ")

    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:
        line = line.strip()

        if line:
            cleaned_lines.append(line)

    return " ".join(cleaned_lines)