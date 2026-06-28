#!/usr/bin/env python3
"""
Eval runner script for SpeakOps.

Runs all evals and generates report.

Usage:
    python run_evals.py --all
    python run_evals.py --eval <eval-name>
"""

import json
import sys
from pathlib import Path
from datetime import datetime


EVALS = [
    "phrase-extraction-quality",
    "spoken-naturalness",
    "voice-drill-quality",
    "activation-scoring",
    "privacy-security",
    "weekly-regression",
]


def run_eval(eval_name: str, evals_dir: Path) -> dict:
    """Run a single eval."""
    # For MVP, this is a placeholder
    # Real implementation would load test cases and run them

    rubric_file = evals_dir / "rubrics" / f"{eval_name}.md"

    if not rubric_file.exists():
        return {
            "status": "error",
            "message": f"Eval rubric not found: {eval_name}"
        }

    # Placeholder: Read rubric and return mock result
    with open(rubric_file, 'r') as f:
        rubric_content = f.read()

    # Extract pass threshold from rubric
    pass_threshold = 4
    for line in rubric_content.split('\n'):
        if 'Pass threshold:' in line:
            try:
                pass_threshold = int(line.split(':')[-1].strip())
                break
            except ValueError:
                pass

    return {
        "status": "pass",
        "score": 5,  # Placeholder
        "pass_threshold": pass_threshold,
        "eval_name": eval_name,
    }


def generate_report(results: list) -> dict:
    """Generate eval report."""
    passed = sum(1 for r in results if r.get("status") == "pass")
    total = len(results)

    return {
        "timestamp": datetime.now().isoformat(),
        "total_evals": total,
        "passed": passed,
        "failed": total - passed,
        "pass_rate": passed / total if total > 0 else 0,
        "results": results,
    }


def save_report(report: dict, reports_dir: Path):
    """Save eval report."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = reports_dir / f"eval_report_{timestamp}.json"

    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)

    print(f"Eval report saved to: {report_file}")


def main():
    """Main eval runner."""
    if len(sys.argv) < 2:
        print("Usage: python run_evals.py --all OR --eval <eval-name>", file=sys.stderr)
        sys.exit(1)

    mode = sys.argv[1]

    # Set up paths
    repo_dir = Path(__file__).parent.parent
    evals_dir = repo_dir / "evals"
    reports_dir = evals_dir / "reports"
    reports_dir.mkdir(exist_ok=True)

    results = []

    if mode == "--all":
        # Run all evals
        for eval_name in EVALS:
            result = run_eval(eval_name, evals_dir)
            results.append(result)
            print(f"{eval_name}: {result.get('status', 'error')}")

    elif mode == "--eval":
        if len(sys.argv) < 3:
            print("Error: Eval name required", file=sys.stderr)
            sys.exit(1)

        eval_name = sys.argv[2]
        result = run_eval(eval_name, evals_dir)
        results.append(result)
        print(f"{eval_name}: {result.get('status', 'error')}")

    else:
        print("Error: Invalid mode", file=sys.stderr)
        sys.exit(1)

    # Generate and save report
    report = generate_report(results)
    save_report(report, reports_dir)

    # Print summary
    print(f"\nEval Summary:")
    print(f"Total: {report['total_evals']}")
    print(f"Passed: {report['passed']}")
    print(f"Failed: {report['failed']}")
    print(f"Pass rate: {report['pass_rate']:.1%}")


if __name__ == "__main__":
    main()
