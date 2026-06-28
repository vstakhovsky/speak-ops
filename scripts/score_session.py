#!/usr/bin/env python3
"""
Session scoring script for SpeakOps.

Processes practice session transcripts and updates phrase activation scores.

Usage:
    python score_session.py --transcript <file>
    python score_session.py --summary <text>
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any


# Activation scoring model
SCORING_DIMENSIONS = {
    "meaning_understood": 10,
    "used_without_hint": 20,
    "correct_usage": 20,
    "natural_spoken_usage": 20,
    "context_transfer": 15,
    "retrieval_speed": 10,
    "retention_after_7days": 5,
}


def load_phrases(data_dir: Path) -> Dict[str, Dict[str, Any]]:
    """Load phrase bank from data directory."""
    phrases_file = data_dir / "phrases.csv"

    phrases = {}
    if phrases_file.exists():
        with open(phrases_file, 'r', encoding='utf-8') as f:
            # Simple CSV parsing (for MVP)
            header = f.readline().strip().split(',')
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    phrase = parts[0]
                    phrases[phrase] = {
                        "phrase": phrase,
                        "score": int(parts[1]) if len(parts) > 1 else 0,
                        "status": parts[2] if len(parts) > 2 else "passive",
                    }

    return phrases


def find_phrases_in_transcript(transcript: str, target_phrases: List[str]) -> Dict[str, Dict[str, Any]]:
    """
    Find target phrases in transcript.

    Returns dict with phrase usage info.
    """
    usage = {}
    transcript_lower = transcript.lower()

    for phrase in target_phrases:
        phrase_lower = phrase.lower()

        # Simple string matching (for MVP)
        if phrase_lower in transcript_lower:
            # Found it, now assess usage
            # For MVP, this is simplified - real implementation would need NLP
            usage[phrase] = {
                "found": True,
                "count": transcript_lower.count(phrase_lower),
                "correct": True,  # Simplified
                "natural": True,  # Simplified
                "instant": True,  # Simplified
            }
        else:
            usage[phrase] = {
                "found": False,
                "count": 0,
            }

    return usage


def calculate_score_update(usage_info: Dict[str, Any], previous_score: int = 0) -> Dict[str, Any]:
    """
    Calculate score update based on usage.
    """
    if not usage_info.get("found", False):
        return {
            "change": 0,
            "new_score": previous_score,
            "dimensions": {},
        }

    points = 0
    dimensions = {}

    # Used without hint
    if usage_info["instant"]:
        points += 20
        dimensions["used_without_hint"] = 20

    # Correct usage
    if usage_info["correct"]:
        points += 20
        dimensions["correct_usage"] = 20

    # Natural spoken usage
    if usage_info["natural"]:
        points += 20
        dimensions["natural_spoken_usage"] = 20

    # Retrieval speed
    if usage_info["instant"]:
        points += 10
        dimensions["retrieval_speed"] = 10

    # Cap at 100
    new_score = min(previous_score + points, 100)

    return {
        "change": points,
        "new_score": new_score,
        "dimensions": dimensions,
    }


def identify_weak_phrases(usage_results: Dict[str, Dict[str, Any]]) -> List[str]:
    """Identify weak phrases from session."""
    weak = []

    for phrase, usage_info in usage_results.items():
        if not usage_info.get("found", False):
            weak.append(phrase)
        elif not usage_info.get("correct", True):
            weak.append(phrase)
        elif not usage_info.get("natural", True):
            weak.append(phrase)

    return weak


def main():
    """Main scoring function."""
    if len(sys.argv) < 3:
        print("Usage: python score_session.py --transcript <file> OR --summary <text>", file=sys.stderr)
        sys.exit(1)

    mode = sys.argv[1]
    input_data = sys.argv[2]

    data_dir = Path(__file__).parent.parent / "data"
    data_dir.mkdir(exist_ok=True)

    # Load phrase bank
    phrases = load_phrases(data_dir)

    if not phrases:
        print("No phrases found in phrase bank", file=sys.stderr)
        sys.exit(1)

    # Get transcript text
    if mode == "--transcript":
        transcript_file = Path(input_data)
        if not transcript_file.exists():
            print(f"Error: Transcript file not found: {transcript_file}", file=sys.stderr)
            sys.exit(1)
        with open(transcript_file, 'r', encoding='utf-8') as f:
            transcript = f.read()
    elif mode == "--summary":
        transcript = input_data
    else:
        print("Error: Invalid mode. Use --transcript or --summary", file=sys.stderr)
        sys.exit(1)

    # Find phrases in transcript
    target_phrases = list(phrases.keys())
    usage_results = find_phrases_in_transcript(transcript, target_phrases)

    # Calculate score updates
    score_updates = {}
    for phrase, usage_info in usage_results.items():
        previous_score = phrases[phrase].get("score", 0)
        update = calculate_score_update(usage_info, previous_score)
        score_updates[phrase] = update

    # Identify weak phrases
    weak_phrases = identify_weak_phrases(usage_results)

    # Output results
    output = {
        "timestamp": datetime.now().isoformat(),
        "total_phrases": len(target_phrases),
        "used_phrases": sum(1 for u in usage_results.values() if u.get("found", False)),
        "missed_phrases": len([p for p, u in usage_results.items() if not u.get("found", False)]),
        "score_updates": score_updates,
        "weak_phrases": weak_phrases,
    }

    print(json.dumps(output, indent=2))

    # Save to sessions.jsonl
    sessions_file = data_dir / "sessions.jsonl"
    with open(sessions_file, 'a', encoding='utf-8') as f:
        f.write(json.dumps(output) + "\n")


if __name__ == "__main__":
    main()
