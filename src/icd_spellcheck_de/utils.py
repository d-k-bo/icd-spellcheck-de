import re

letters_exp = re.compile(r"[a-zA-ZäöüßÄÖÜẞ]")
special_chars_exp = re.compile(r"[^a-zA-ZäöüßÄÖÜẞ]")
lower_case_exp = re.compile(r"[a-zäöüß]")


def split_terms(s: str) -> list[str]:
    return special_chars_exp.split(s)


def contains_letters(s: str) -> bool:
    return letters_exp.search(s) is not None


def is_acronym(s: str) -> bool:
    return lower_case_exp.search(s) is None
