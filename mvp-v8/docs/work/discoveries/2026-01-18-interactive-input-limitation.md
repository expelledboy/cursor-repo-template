---
status: active
domain: agentos
type: discovery
created_date: 2026-01-18
tags: [interactive, input, shell, chat-environment]
related: []
---

# Interactive Input Limitation in Chat Environment

## Discovery
Python scripts using `input()` or `sys.stdin.readline()` do not support truly interactive user input in this chat environment. When executed, these calls complete immediately without waiting for user input, effectively making interactive scripts non-functional.

## Evidence
- `input("Please enter some text: ")` - exits immediately without prompting
- `sys.stdin.readline().strip()` - same behavior
- Works with piped input: `echo "text" | python3 script.py`
- Complex interactive scripts (like `scripts/docs/index.py retrospect`) can work, suggesting selective interactive support

## Implications
- Simple interactive Python scripts cannot be used for user input in this environment
- Interactive functionality must be implemented differently or avoided
- More complex interactive systems (like the DOE retrospective tool) have some level of support
- Input validation and processing should assume non-interactive execution

## Verification
Tested with multiple approaches:
1. Basic `input()` call - fails
2. `sys.stdin.readline()` - fails  
3. Piped input `echo "test" | python3 script.py` - works
4. Complex interactive script (`scripts/docs/index.py retrospect`) - works

## Recommendations
- Avoid simple interactive input patterns in scripts intended for this environment
- Use alternative input methods (command line arguments, file input, etc.)
- For interactive features, implement within supported frameworks (like the existing DOE system)