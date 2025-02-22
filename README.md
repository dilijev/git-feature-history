# Git Feature History Script

## Purpose

This script is designed to track all of the commits that changed all of the files involved in a given feature. This includes commits that were part of changes unrelated to the feature. The feature can be identified by a list of commits, which can be created manually or generated using commands like `git log --grep` for feature keywords in commit messages.

This can be useful for identifying commits that might have affected the feature as a side effect.

## Usage

1. **List Files Modified by Commits:**

   By default, the script will output a sorted, unique list of files changed in all of the commits passed into the script.

   ```sh
   python git-feature-history.py < commit_hashes.txt
   ```

2. **List Commits that Touched the Files:**

   Use the `--commits` flag to output a reverse-chronological list of commits that touched all of the files. You can also pass additional git log flags.

   ```sh
   python git-feature-history.py --commits < commit_hashes.txt
   ```

   Example with additional git log flags:

   ```sh
   python git-feature-history.py --commits --since="2022-01-01" < commit_hashes.txt
   ```

## Example

To identify commits outside of explicit efforts on a feature that might have affected the feature as a side effect, you can use the following steps:

1. Generate a list of commits related to the feature using `git log --grep`:

   ```sh
   git log --grep="feature keyword" --pretty=format:"%H" > feature_commits.txt
   ```

2. Run the script to list all files modified by these commits:

   ```sh
   python git-feature-history.py < feature_commits.txt
   ```

3. Optionally, list all commits that touched these files:

   ```sh
   python git-feature-history.py --commits < feature_commits.txt
   ```

4. Generate a list of commits related to the feature using `git log --grep` and pipe it into git-feature-history.py with a commit range.

   ```sh
   git log --grep="feature keyword" --pretty=format:"%H" feature_begin_ref..HEAD | python3 git-file-history.py --commits output_range_begin..HEAD
   ```
