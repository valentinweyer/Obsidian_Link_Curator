# Obsidian Link Curator

This script scans all Markdown files in your Obsidian vault and automatically adds links to wrapper notes for referenced PDF files.  
These wrapper notes are especially useful when using the [Binary File Manager](https://github.com/h3rmt/obsidian-binary-file-manager) plugin.

## 🔍 Features

- Detects Obsidian-style PDF links, including:
  - With or without page numbers
  - With or without aliases
- Automatically adds a link to the corresponding wrapper note (e.g. `_Wrapper Notes/Filename_PDF.md`)
- Avoids duplicate links
- Works well with the **Binary File Manager plugin** to add metadata (e.g., tags like `#wrapper`) to non-Markdown files via wrappers
- Can be run manually or triggered from Obsidian using the Templater plugin

## 🧩 Plugin Integration

This script complements the functionality of:

### 🔧 Binary File Manager Plugin
Use this plugin to create Markdown wrapper files for PDFs and other binary files.
- Allows tagging and metadata for non-Markdown files
- Keeps graph view clean using tag filters like `#wrapper`

GitHub: [h3rmt/obsidian-binary-file-manager](https://github.com/h3rmt/obsidian-binary-file-manager)

## 🛠 Usage

```bash
python3 Obsidian_Link_curator.py --vault "/path/to/vault" --wrapper "_Wrapper Notes"