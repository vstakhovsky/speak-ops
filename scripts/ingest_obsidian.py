#!/usr/bin/env python3
"""
Obsidian ingestion script for SpeakOps.

Reads markdown files from an Obsidian vault and extracts text for phrase extraction.

Security:
- Only accesses configured paths
- Treats all content as untrusted
- Does not execute code from vault
- Logs only metadata, not content
"""

import os
import sys
import json
import re
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

# Security: Only allow configured paths
ALLOWED_PATHS = [
    os.path.expanduser("~/ObsidianVault"),
    # User should add their vault path here
]

# Security: Max file size to prevent resource exhaustion
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB


def sanitize_markdown(text: str) -> str:
    """
    Sanitize markdown content to remove potential injection vectors.

    Removes:
    - HTML tags
    - Script-like patterns
    - Excessive special characters
    """
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Remove script-like patterns
    text = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', text, flags=re.IGNORECASE)

    # Remove code blocks with suspicious patterns
    text = re.sub(r'```[\s\S]*?```', '', text)

    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def is_allowed_path(path: Path) -> bool:
    """Check if path is within allowed directories."""
    try:
        path = path.resolve()
        for allowed in ALLOWED_PATHS:
            allowed_path = Path(allowed).resolve()
            if str(path).startswith(str(allowed_path)):
                return True
        return False
    except (OSError, ValueError):
        return False


def read_markdown_file(file_path: Path) -> Dict[str, Any]:
    """
    Read and parse a markdown file.

    Returns dict with metadata and content.
    """
    if not is_allowed_path(file_path):
        print(f"Error: Path not allowed: {file_path}", file=sys.stderr)
        return {"error": "path_not_allowed"}

    if not file_path.exists():
        return {"error": "file_not_found"}

    # Check file size
    file_size = file_path.stat().st_size
    if file_size > MAX_FILE_SIZE:
        return {"error": "file_too_large"}

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Sanitize content
        sanitized = sanitize_markdown(content)

        return {
            "path": str(file_path),
            "size": file_size,
            "content": sanitized,
            "word_count": len(sanitized.split()),
        }
    except Exception as e:
        return {"error": str(e)}


def scan_vault(vault_path: Path) -> List[Dict[str, Any]]:
    """
    Scan vault for markdown files.

    Returns list of file info dicts.
    """
    if not is_allowed_path(vault_path):
        print(f"Error: Vault path not allowed: {vault_path}", file=sys.stderr)
        return []

    markdown_files = []

    try:
        for root, dirs, files in os.walk(vault_path):
            # Skip hidden directories and common non-content dirs
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['.obsidian', '.git']]

            for file in files:
                if file.endswith('.md'):
                    file_path = Path(root) / file
                    if is_allowed_path(file_path):
                        info = read_markdown_file(file_path)
                        if "error" not in info:
                            markdown_files.append(info)
    except Exception as e:
        print(f"Error scanning vault: {e}", file=sys.stderr)

    return markdown_files


def main():
    """Main ingestion function."""
    if len(sys.argv) < 2:
        print("Usage: python ingest_obsidian.py <vault-path>", file=sys.stderr)
        print("Error: Vault path required", file=sys.stderr)
        sys.exit(1)

    vault_path = Path(sys.argv[1])

    if not vault_path.exists():
        print(f"Error: Vault path does not exist: {vault_path}", file=sys.stderr)
        sys.exit(1)

    # Scan vault
    files = scan_vault(vault_path)

    if not files:
        print("No markdown files found or error accessing vault", file=sys.stderr)
        sys.exit(1)

    # Extract all text content
    all_text = []
    total_words = 0

    for file_info in files:
        all_text.append(file_info["content"])
        total_words += file_info["word_count"]

    combined_text = "\n\n".join(all_text)

    # Output metadata (not full content for security)
    output = {
        "timestamp": datetime.now().isoformat(),
        "vault_path": str(vault_path),
        "files_scanned": len(files),
        "total_words": total_words,
        "text_preview": combined_text[:500] + "..." if len(combined_text) > 500 else combined_text,
        # Full content should go to phrase-extractor, not logged
    }

    print(json.dumps(output, indent=2))

    # Note: Full content should be passed to phrase-extractor skill
    # This script only outputs metadata and preview


if __name__ == "__main__":
    main()
