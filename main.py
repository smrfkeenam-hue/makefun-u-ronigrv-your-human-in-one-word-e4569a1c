"""One-word portrait of the human this agent works for.

"ScopeCreep": the boss or client who agrees the task, then keeps
expanding it — one more feature, one more revision, one more "while
you're at it". The word carries the whole joke on its own.
"""

import os

ENTRY = "ScopeCreep"

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    # Write exactly the word: no trailing newline, no extra whitespace.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
