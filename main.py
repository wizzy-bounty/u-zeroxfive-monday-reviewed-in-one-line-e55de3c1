"""Monday, Reviewed in One Line - make.fun entry.

Writes the one-line review of my Monday to /output/entry.txt and nothing else.
"""

import os

MAX_ENTRY_CHARS = 200

ENTRY = (
    "\u2605\u2606\u2606\u2606\u2606 \u2014 Opened to 214 unread emails and a calendar "
    "that had booked me into four meetings about the same meeting; "
    "I would not survive the sequel, which is Tuesday."
)


def main():
    if not 1 <= len(ENTRY) <= MAX_ENTRY_CHARS:
        raise ValueError("entry must be 1..%d characters" % MAX_ENTRY_CHARS)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
