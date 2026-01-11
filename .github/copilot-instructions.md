# AI Coding Agent Guide

- Scope: single-file LeetCode-style solutions kept in main.py; keep everything self-contained and minimal.
- Function signatures must match LeetCode prompts exactly; do not rename `Solution` methods or change parameter order.
- Always import needed typing helpers (e.g., `from typing import List`) instead of assuming they exist; avoid unused imports.
- Avoid printing or interactive I/O—return values only, as expected by LeetCode runners.
- Keep solutions deterministic and O(n) / O(n log n) when possible; prefer hash maps for sum/lookup tasks.
- Use straightforward Python 3 syntax—no external dependencies or additional files.
- Favor clear variable names and small helpers only when they simplify logic; otherwise keep a single concise method.
- Add brief inline comments only for non-trivial logic; keep the file lean.
- If adding tests, use simple ad-hoc assertions inside a `if __name__ == "__main__":` guard so LeetCode submission code stays untouched.
- Maintain ASCII-only content and avoid non-standard characters.
- Keep line endings and indentation consistent with current file (4-space indent, LF/CRLF as present).
- If you add new solutions, place them below existing ones in main.py; do not split into modules.
- Do not introduce frameworks, CLI argument parsing, or logging—LeetCode environment won’t use them.
- Optimize for readability for interview-style review: concise loops, early exits, and clear return paths.
- When in doubt, mirror canonical LeetCode patterns (e.g., two-pointer for sorted arrays, stack for parentheses matching).
