import os
import re
import argparse

# Argument parser for dynamic paths
parser = argparse.ArgumentParser(description="Add wrapper links for PDF files in Obsidian vault.")
parser.add_argument("--vault", required=True, help="Path to the Obsidian vault")
parser.add_argument("--wrapper", required=True, help="Wrapper folder name inside the vault")
args = parser.parse_args()

vault_path = args.vault
wrapper_folder = args.wrapper

# Regex to match Obsidian-style PDF links, with or without alias and page number
pdf_link_pattern = re.compile(r"!?\[\[([^\|\[\]#]+\.pdf)(?:#[^\|\]]*)?(?:\|[^\]]+)?\]\]", re.IGNORECASE)

def find_and_add_wrapper_links():
    for root, _, files in os.walk(vault_path):
        for filename in files:
            if filename.endswith(".md") and not filename.startswith(".") and wrapper_folder not in root:
                file_path = os.path.join(root, filename)

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                matches = pdf_link_pattern.findall(content)

                if matches:
                    print(f"✅ Found in {file_path}: {matches}")
                else:
                    print(f"🔍 No PDF links in {file_path}")

                wrapper_links_to_add = []

                for pdf_filename in matches:
                    base_name = os.path.splitext(os.path.basename(pdf_filename))[0]
                    wrapper_path = f"[[{wrapper_folder}/{base_name}_PDF.md]]"
                    if wrapper_path not in content:
                        wrapper_links_to_add.append(wrapper_path)

                if wrapper_links_to_add:
                    new_content = content.strip() + "\n\n" + "\n".join(wrapper_links_to_add) + "\n"
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated: {file_path} with wrappers: {wrapper_links_to_add}")

find_and_add_wrapper_links()
