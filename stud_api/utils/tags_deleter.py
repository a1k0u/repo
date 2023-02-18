import re

CLEANER = re.compile("<.*?>")


def clean_html(raw_html):
    cleaned_text = re.sub(CLEANER, "", raw_html)
    return cleaned_text
