"""
Script to create GitHub issues for all 250 NeetCode 250 LeetCode problems.

Usage:
    python scripts/create_issues.py

Requires:
    - GITHUB_TOKEN environment variable set with repo scope
    - GITHUB_REPOSITORY environment variable (e.g., "cd155/neetcode-250-python-template")

Problems that already have an issue with the same title (open or closed) are skipped,
so the script can be re-run safely if it stops part way through.
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error

LIST_NAME = "NeetCode 250"
LIST_LABEL = "neetcode-250"
EXPECTED_PROBLEMS = 250


def extract_problems(src_dir="src"):
    """Extract problem details from all solution files."""
    problems = []

    for category in sorted(os.listdir(src_dir)):
        cat_path = os.path.join(src_dir, category)
        if not os.path.isdir(cat_path) or category.startswith("_"):
            continue
        for filename in sorted(os.listdir(cat_path)):
            if filename.endswith(".py") and filename != "__init__.py":
                filepath = os.path.join(cat_path, filename)
                with open(filepath, "r") as f:
                    content = f.read()

                match = re.search(r'"""(.*?)"""', content, re.DOTALL)
                if not match:
                    continue

                docstring = match.group(1).strip()
                lines = docstring.split("\n")
                title_match = re.match(r"LeetCode\s+(\d+):\s+(.*)", lines[0])
                if not title_match:
                    continue

                lc_num = int(title_match.group(1))
                title = title_match.group(2).strip()
                description = "\n".join(lines[1:]).strip()

                problems.append(
                    {
                        "number": lc_num,
                        "title": title,
                        "category": category,
                        "filename": filename,
                        "filepath": filepath,
                        "description": description,
                    }
                )

    problems.sort(key=lambda x: x["number"])
    return problems


CATEGORY_DISPLAY_NAMES = {
    "arrays_and_hashing": "Arrays & Hashing",
    "two_pointers": "Two Pointers",
    "sliding_window": "Sliding Window",
    "stack": "Stack",
    "binary_search": "Binary Search",
    "linked_list": "Linked List",
    "trees": "Trees",
    "heap_priority_queue": "Heap / Priority Queue",
    "backtracking": "Backtracking",
    "tries": "Tries",
    "graphs": "Graphs",
    "advanced_graphs": "Advanced Graphs",
    "dp_1d": "1-D Dynamic Programming",
    "dp_2d": "2-D Dynamic Programming",
    "greedy": "Greedy",
    "intervals": "Intervals",
    "math_and_geometry": "Math & Geometry",
    "bit_manipulation": "Bit Manipulation",
}


def get_category_display(category):
    """Get the human-readable NeetCode category name for a src/ directory."""
    return CATEGORY_DISPLAY_NAMES.get(category, category.replace("_", " ").title())


# Solution files are named after the LeetCode URL slug, except where the slug
# is not a valid Python module name.
LEETCODE_SLUG_OVERRIDES = {
    "three_sum.py": "3sum",
    "four_sum.py": "4sum",
}


def get_leetcode_slug(filename):
    """Get the LeetCode problem URL slug from the filename."""
    if filename in LEETCODE_SLUG_OVERRIDES:
        return LEETCODE_SLUG_OVERRIDES[filename]
    return filename.replace(".py", "").replace("_", "-")


def build_issue_body(problem):
    """Build the issue body markdown for a problem."""
    category_display = get_category_display(problem["category"])
    filepath = problem["filepath"]
    slug = get_leetcode_slug(problem["filename"])

    body = f"""## LeetCode {problem['number']}: {problem['title']}

**Category:** {category_display}
**Difficulty:** See [LeetCode](https://leetcode.com/problems/{slug}/)
**Solution File:** `{filepath}`
**Test File:** `tests/test_{problem['filename']}`

### Problem Description

{problem['description']}

### Tasks

- [ ] Implement the solution in `{filepath}`
- [ ] Ensure all test cases pass
- [ ] Analyze time complexity
- [ ] Analyze space complexity
"""
    return body


def github_request(token, url, data=None, method="GET"):
    """Send a request to the GitHub REST API and return the decoded JSON response."""
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8") if data is not None else None,
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json",
        },
        method=method,
    )
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode("utf-8"))


def get_existing_issue_titles(token, repo):
    """Return the titles of all existing issues (open and closed) in the repository."""
    titles = set()
    page = 1
    while True:
        url = f"https://api.github.com/repos/{repo}/issues?state=all&per_page=100&page={page}"
        issues = github_request(token, url)
        if not issues:
            return titles
        titles.update(issue["title"] for issue in issues if "pull_request" not in issue)
        page += 1


def create_github_issue(token, repo, title, body, labels):
    """Create a GitHub issue using the REST API."""
    url = f"https://api.github.com/repos/{repo}/issues"
    try:
        result = github_request(token, url, {"title": title, "body": body, "labels": labels}, "POST")
        return result["number"], result["html_url"]
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"  Error creating issue: {e.code} - {error_body}")
        return None, None


def ensure_labels_exist(token, repo, labels):
    """Ensure all required labels exist in the repository."""
    label_colors = {
        "arrays and hashing": "7057ff",
        "two pointers": "008672",
        "sliding window": "d73a4a",
        "stack": "0075ca",
        "binary search": "cfd3d7",
        "linked list": "e4e669",
        "trees": "0e8a16",
        "heap priority queue": "a2eeef",
        "backtracking": "d876e3",
        "tries": "f9d0c4",
        "graphs": "1d76db",
        "advanced graphs": "5319e7",
        "dp 1d": "b60205",
        "dp 2d": "e99695",
        "greedy": "c2e0c6",
        "intervals": "bfd4f2",
        "math and geometry": "fef2c0",
        "bit manipulation": "006b75",
        LIST_LABEL: "fbca04",
    }

    for label, color in label_colors.items():
        if label not in labels:
            continue
        if label == LIST_LABEL:
            description = f"{LIST_NAME} problems"
        else:
            description = f"{LIST_NAME} - {get_category_display(label.replace(' ', '_'))} problems"
        url = f"https://api.github.com/repos/{repo}/labels"

        try:
            github_request(token, url, {"name": label, "color": color, "description": description}, "POST")
            print(f"  Created label: {label}")
        except urllib.error.HTTPError as e:
            if e.code == 422:
                pass  # Label already exists
            else:
                print(f"  Warning: Could not create label '{label}': {e.code}")


def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")

    if not token:
        print("Error: GITHUB_TOKEN environment variable is required")
        sys.exit(1)
    if not repo:
        print("Error: GITHUB_REPOSITORY environment variable is required")
        sys.exit(1)

    print(f"Repository: {repo}")
    print("Extracting problems from source files...")

    problems = extract_problems()
    print(f"Found {len(problems)} problems\n")

    if len(problems) != EXPECTED_PROBLEMS:
        print(f"Error: Expected {EXPECTED_PROBLEMS} problems, found {len(problems)}")
        sys.exit(1)

    # Collect all unique labels
    all_labels = {LIST_LABEL}
    for p in problems:
        all_labels.add(p["category"].replace("_", " "))

    print("Ensuring labels exist...")
    ensure_labels_exist(token, repo, all_labels)
    print()

    existing_titles = get_existing_issue_titles(token, repo)
    if existing_titles:
        print(f"Found {len(existing_titles)} existing issues; matching titles will be skipped\n")

    # Create issues
    created = 0
    skipped = 0
    total = len(problems)
    for i, problem in enumerate(problems, 1):
        category_label = problem["category"].replace("_", " ")
        title = f"LeetCode {problem['number']}: {problem['title']}"

        if title in existing_titles:
            print(f"[{i}/{total}] Skipping existing issue: {title}")
            skipped += 1
            continue

        body = build_issue_body(problem)
        labels = [LIST_LABEL, category_label]

        print(f"[{i}/{total}] Creating issue: {title}")
        issue_num, issue_url = create_github_issue(token, repo, title, body, labels)

        if issue_num:
            print(f"  Created: #{issue_num} - {issue_url}")
            created += 1
        else:
            print(f"  Failed to create issue")

        # Rate limiting - GitHub allows 30 requests per minute for issue creation
        if i % 25 == 0:
            print("  Pausing for rate limiting...")
            time.sleep(10)
        else:
            time.sleep(1)

    print(f"\nDone! Created {created} issues, skipped {skipped} existing, out of {total}.")


if __name__ == "__main__":
    main()
