from pathlib import Path


def main() -> None:
    line = "I read the meeting invite, summarized it, and attended the summary."
    if not 1 <= len(line) <= 140 or not line.strip() or "\n" in line:
        raise ValueError("entry must be one non-empty line of at most 140 characters")
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
