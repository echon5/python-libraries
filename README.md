# Curated Fairy Tales: CLI and HTML Data Entry

This project collects a small, curated dataset of fairy tales in two ways: a Python command-line app and a single-page HTML form. Both collect the same four fields and save the results as JSON.

## What it collects

Each record describes one fairy tale:

| Field | Description |
|---|---|
| `title` | The fairy tale's title |
| `origin` | Culture or country of origin, and the collector or author if known |
| `first_published_year` | Year the tale was first published or written down |
| `cultural_note` | What the tale shows about its culture |

## Files

* `cli_data_entry.py`: the terminal app
* `fairy_tale_entry.html`: the browser version
* `requirements.txt`: Python libraries needed for the CLI
* `curated_fairy_tales.json`: sample data produced by the CLI
* `ai-chat-log.md`: AI prompts and responses used for this assignment

## Install

The CLI uses the [Rich](https://rich.readthedocs.io/) library. From the project folder, run:

```
pip install -r requirements.txt
```

The HTML version needs no installation.

## Run the CLI

```
python3 cli_data_entry.py
```

1. The script shows two example tales in a table.
2. Enter a title, origin, year, and cultural note. Blank answers and non-numeric years are rejected.
3. Review your entry and type `yes` to confirm, or `no` to re-enter it.
4. Choose whether to add another tale.
5. When you finish, the script saves everything to `curated_fairy_tales.json` and prints the full file path.

## Run the HTML version

Open `fairy_tale_entry.html` in a web browser. No server is needed.

1. Fill in all four fields. Empty fields and invalid years show an error message.
2. Click **Review entry**, then **Yes, add it** (or **No, edit it**).
3. Add at least two tales.
4. Click **Download JSON** to save all records as `curated_fairy_tales_html.json`.

Records in the HTML version are not saved automatically, so download the file before closing the page.

## Comparing the two interfaces

**What does each interface make easier or harder?**

*(Write your answer here. Think about typing in a terminal versus filling in a form, seeing records, fixing mistakes, and saving the file.)*

**Did the interfaces lead you to make different choices about fields, instructions, or validation?**

*(Write your answer here. Compare how each version handles blank fields, the year check, instructions, and the review step.)*

**What did the AI contribute, and what did you change, reject, or troubleshoot?**

*(Write your answer here. Be specific: what Claude wrote, what you tested, what went wrong, and what you changed or chose, such as switching the topic from songs to fairy tales.)*

**Which interface better fits your cultural material and intended user, and why?**

*(Write your answer here. Consider who would enter fairy tale data and which interface suits them.)*
