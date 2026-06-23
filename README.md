
# TidyBox

TidyBox is a command-line file organizer built in Python that helps keep your directories clean and organized.

Instead of manually sorting files every week, TidyBox can automatically group files by type, move them into organized folders, preview changes before they happen, and even undo previous operations.

Perfect for managing Downloads folders, school projects, screenshots, archives, and other file collections.

## Features

- Organize files by extension
- Dry-run mode for safe previews
- Undo previous operations
- Recursive directory scanning
- Custom organization rules
- Detailed logging
- Cross-platform support (Linux, Windows, macOS)
- Watch mode for automatic organization

## Installation

Clone the repository:

```bash
git clone https://github.com/strpowkno/tidybox.git
cd tidybox
````

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Scan a directory

```bash
python tidybox.py scan ~/Downloads
```

### Preview changes

```bash
python tidybox.py clean ~/Downloads --dry-run
```

### Organize files

```bash
python tidybox.py clean ~/Downloads
```

### Undo the last operation

```bash
python tidybox.py undo
```

### Watch a directory

```bash
python tidybox.py watch ~/Downloads
```

## Examples

Before:

```
Downloads/
├── image.png
├── archive.zip
├── homework.pdf
├── script.py
└── screenshot.jpg
```

After:

```
Downloads/
├── Images/
│   ├── image.png
│   └── screenshot.jpg
├── Archives/
│   └── archive.zip
├── Documents/
│   └── homework.pdf
└── Code/
    └── script.py
```

## Project Structure

```text
tidybox/
├── tidybox/
│   ├── cli.py
│   ├── organizer.py
│   ├── logger.py
│   ├── undo.py
│   ├── rules.py
│   └── watcher.py
├── logs/
├── tests/
├── requirements.txt
├── README.md
└── LICENSE
```

## Roadmap

* [ ] Basic file organization
* [ ] Dry-run mode
* [ ] Undo support
* [ ] Recursive organization
* [ ] Watch mode
* [ ] Custom rules
* [ ] Duplicate file detection
* [ ] Configuration file support
* [ ] Plugin system

## Why TidyBox?

Most file organizers are either too simple or too heavy. TidyBox aims to provide a fast, lightweight, and transparent solution that users can trust.

Every operation can be previewed before execution, logged for later review, and reversed if needed.

## Contributing

Contributions, feature requests, and bug reports are welcome.

Feel free to open an issue or submit a pull request.

## License

Licensed under the MIT License.

