#!/usr/bin/env python3
"""
Phrase bank update script for SpeakOps.

Updates phrases.csv with new scores and statuses after practice sessions.

Usage:
    python update_phrase_bank.py
"""

import csv
import json
import sys
from pathlib import Path
from datetime import datetime


def load_phrases(data_dir: Path) -> dict:
    """Load existing phrase bank."""
    phrases_file = data_dir / "phrases.csv"
    phrases = {}

    if phrases_file.exists():
        with open(phrases_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                phrase = row.get("phrase", "")
                if phrase:
                    phrases[phrase] = row

    return phrases


def load_latest_session(data_dir: Path) -> dict:
    """Load latest session data."""
    sessions_file = data_dir / "sessions.jsonl"

    if not sessions_file.exists():
        return None

    with open(sessions_file, 'r') as f:
        lines = f.readlines()
        if lines:
            return json.loads(lines[-1])

    return None


def get_status_from_score(score: int) -> str:
    """Get status from activation score."""
    if score < 40:
        return "passive"
    elif score < 60:
        return "recognized"
    elif score < 75:
        return "semi-active"
    elif score < 90:
        return "active"
    else:
        return "meeting-ready"


def update_phrases_with_session(phrases: dict, session: dict) -> dict:
    """Update phrase scores with session data."""
    score_updates = session.get("score_updates", {})

    for phrase, update in score_updates.items():
        if phrase in phrases:
            phrases[phrase]["score"] = update["new_score"]
            phrases[phrase]["status"] = get_status_from_score(update["new_score"])
            phrases[phrase]["last_used"] = session["timestamp"]

    return phrases


def save_phrases(data_dir: Path, phrases: dict):
    """Save updated phrase bank."""
    phrases_file = data_dir / "phrases.csv"

    fieldnames = ["phrase", "score", "status", "russian", "domain", "context", "last_used"]

    with open(phrases_file, 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for phrase_data in phrases.values():
            # Ensure all fields exist
            row = {field: phrase_data.get(field, "") for field in fieldnames}
            writer.writerow(row)


def save_weak_phrases(data_dir: Path, session: dict):
    """Save weak phrases to weak_phrases.jsonl."""
    weak_phrases = session.get("weak_phrases", [])

    if not weak_phrases:
        return

    weak_file = data_dir / "weak_phrases.jsonl"

    with open(weak_file, 'a', encoding='utf-8') as f:
        for phrase in weak_phrases:
            f.write(json.dumps({
                "phrase": phrase,
                "timestamp": session["timestamp"],
                "session_id": session.get("session_id", ""),
            }) + "\n")


def main():
    """Main update function."""
    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    # Load existing phrases
    phrases = load_phrases(data_dir)

    if not phrases:
        print("No existing phrase bank found. Run phrase extraction first.", file=sys.stderr)
        sys.exit(1)

    # Load latest session
    session = load_latest_session(data_dir)

    if not session:
        print("No session data found. Run a practice session first.", file=sys.stderr)
        sys.exit(1)

    # Update phrases with session data
    phrases = update_phrases_with_session(phrases, session)

    # Save updated phrases
    save_phrases(data_dir, phrases)

    # Save weak phrases
    save_weak_phrases(data_dir, session)

    print(f"Updated phrase bank with session from {session['timestamp']}")
    print(f"Phrases updated: {len(session.get('score_updates', {}))}")
    print(f"Weak phrases identified: {len(session.get('weak_phrases', []))}")


if __name__ == "__main__":
    main()
