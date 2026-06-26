
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

## Adding to PATH

After building with PyInstaller, move the binary to a directory on your PATH so you can run `tidybox` from anywhere.

### Linux / macOS

```bash
mkdir -p ~/.local/bin
cp dist/tidybox ~/.local/bin/tidybox
```

Then add this to your `~/.bashrc` or `~/.zshrc`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Apply it:

```bash
source ~/.bashrc
```

### Windows

Move `dist/tidybox.exe` to a folder like `C:\Users\YourName\bin\`, then add that folder to PATH:

1. Search "Environment Variables" in the Start menu
2. Click "Environment Variables"
3. Under "User variables", select `Path` → Edit
4. Click New and paste the folder path
5. Click OK and restart your terminal

### Verify

```bash
which tidybox      # Linux/macOS
where tidybox      # Windows
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

## Why TidyBox?

Most file organizers are either too simple or too heavy. TidyBox aims to provide a fast, lightweight, and transparent solution that users can trust.

Every operation can be previewed before execution, logged for later review, and reversed if needed.

## Contributing

Contributions, feature requests, and bug reports are welcome.

Feel free to open an issue or submit a pull request.

## License

Licensed under the MIT License.

