"""
Author: Ryan Teixeira
May 2025
"""
import sys
import re
import glob
from pathlib import Path

def transform_content(content, pattern, replacement):
    """
    Applies a regular expression substitution to the content.
    
    Args:
        content (str): The original file content.
        pattern (str): Regex pattern to search for.
        replacement (str): Replacement string.

    Returns:
        str: Transformed content with substitutions applied.
    """
    return re.sub(pattern, replacement, content)

def process_file(src_path, dest_path, pattern=None, replacement=None):
    """
    Reads a file, optionally applies a content transformation, and writes the result to a destination.

    Args:
        src_path (Path): Source file path.
        dest_path (Path): Destination file path.
        pattern (str): Optional regex pattern to search for.
        replacement (str): Optional replacement string.
    """
    # Read source file content
    with open(src_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply transformation if pattern and replacement are provided
    if pattern and replacement:
        content = transform_content(content, pattern, replacement)

    # Ensure the destination directory exists
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    # Write transformed content to destination file
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(content)

def copy_files(sources, dest_ext=None, dest_dir=None, pattern=None, replacement=None):
    """
    Handles copying and transforming multiple files based on shell-style wildcards.

    Args:
        sources (list): List of source path patterns (e.g., ['*.txt']).
        dest_ext (str): Optional new extension for the output files (e.g., '.ejs').
        dest_dir (str): Optional destination directory to place the output files.
        pattern (str): Optional regex pattern to apply to file contents.
        replacement (str): Optional replacement string for the pattern.
    """
    for src in sources:
        # Resolve wildcards like *.svg to actual file paths
        for file_path in glob.glob(src):
            p = Path(file_path)
            
            # Determine new file name with modified extension if requested
            base_name = p.stem + (dest_ext if dest_ext else p.suffix)
            
            # Determine output directory: use given one or fallback to same as source
            target_dir = Path(dest_dir) if dest_dir else p.parent

            # Combine target directory and new file name to get full destination path
            dest_path = target_dir / base_name

            # Process the file (read, transform, write)
            process_file(p, dest_path, pattern, replacement)

if __name__ == '__main__':
    import argparse

    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Copy and transform files with optional extension and content changes.")
    parser.add_argument('sources', nargs='+', help='Source file patterns (e.g., *.svg or path/to/file.txt)')
    parser.add_argument('--to-ext', help='Change file extension to this (e.g., .ejs)')
    parser.add_argument('--dest-dir', help='Destination directory for output files')
    parser.add_argument('--pattern', help='Regex pattern to search within file content')
    parser.add_argument('--replace', help='Replacement string to use in transformed content')

    # Parse arguments from command line
    args = parser.parse_args()

    # Invoke the main file-copy logic
    copy_files(
        sources=args.sources,
        dest_ext=args.to_ext,
        dest_dir=args.dest_dir,
        pattern=args.pattern,
        replacement=args.replace
    )

