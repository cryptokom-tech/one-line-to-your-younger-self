import os
import sys

MAX_CHARS = 200

LINE = (
    "At 3am, the baby asleep on your chest will forget the cheap milk "
    "and remember whether you stayed in the room."
)


def valid(text):
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main():
    if not valid(LINE):
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
