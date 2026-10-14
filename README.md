# Curated Fairy Tales: CLI and HTML Data Entry

This project collects a small, curated dataset of fairy tales in two ways: a Python command-line app and a single-page HTML form. 

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
The CLI allows for user customization since they are able to type their responses in, this could make responding less acessible for users that can't type. The HTML also has same issue with typing but you can click the yes or not buttons inseatd of the CLI where you have to type it.

**Did the interfaces lead you to make different choices about fields, instructions, or validation?**

The CLI has each step with instruction set out chronologically whereas the HTML has all the text boxes set in front of the user at once. The CLI offers better guidance but both that requirements for the the type of responses needed. The HTML also has buttons for yes and no whereas the CLI makes you type it.

**What did the AI contribute, and what did you change, reject, or troubleshoot?**

Claude came up with the code for the CLI but started with the theme of songs, it also helped with the read me formatting, and made the html. It also helped troubleshooted with file locations. I changed it to match with my teams theme and tested and trouble shooted. I also added stories and tested all of the instructions and validations. I wrote all the responses on my own.

**Which interface better fits your cultural material and intended user, and why?**

I think that both younger and olderfolk would be inputting story data so i think the HTML is much easier to naviagte instead of typing in the terminal. It also looks nicers which could help with the user experience. There is also guidance with instructions like the CLI its just not step by step.
