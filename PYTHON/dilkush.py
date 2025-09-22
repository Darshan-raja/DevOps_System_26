import time
import sys


def dilksuh(line, char_delay=0.065):
    """Prints a line with a typewriter effect."""
    for char in line:
        print(char, end="", flush=True)
        time.sleep(char_delay)
    print()


def print_lyrics():
    """Prints a sequence of lyrics with delays between them."""
    lyrics = [
        "dil❤️ jo tu mera hai",
        "kaisa bechara hai",
        "maane na besharam, bilkul khatara hai❤️",
        "tu kare dil beqarar",
        "kyun karoon main tujhse pyar"
    ]

    delays = [1.5, 1.5, 2.0, 1.8, 2.3]

    for i in range(len(lyrics)):
        dilksuh(lyrics[i], char_delay=0.065)

        if i < len(delays):
            time.sleep(delays[i])


# --- Main execution ---
if __name__ == "__main__":
    print_lyrics()
