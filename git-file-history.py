#!/usr/bin/env python3

import sys
import subprocess
import re
from collections import defaultdict
from typing import Set, Dict, List

def run_git_command(command: List[str]) -> str:
    """Run a git command and return its output."""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running git command: {e}", file=sys.stderr)
        sys.exit(1)

def get_files_for_commit(commit_hash: str) -> Set[str]:
    """Get the list of files modified in a commit."""
    files = run_git_command(
        ["git", "show", "--name-only", "--format=", commit_hash]
    ).splitlines()
    return set(files)

def main():
    # Dictionary to store files and their associated commits
    files_to_commits: Dict[str, Set[str]] = defaultdict(set)

    # Read commit hashes/messages from stdin or file
    commits: Set[str] = set()
    for line in sys.stdin:
        # Extract commit hash - assumes it's either a full hash or starts a line
        hash_match = re.search(r"([a-f0-9]{7,40})", line.strip())
        if hash_match:
            commits.add(hash_match.group(1))

    if not commits:
        print("No commit hashes found in input", file=sys.stderr)
        sys.exit(1)

    # Process each commit
    for commit in commits:
        files = get_files_for_commit(commit)
        for file in files:
            files_to_commits[file].add(commit)

    # Output results
    unique_files = sorted(files_to_commits.keys())
    for file in unique_files:
        print(file)

if __name__ == "__main__":
    main()
