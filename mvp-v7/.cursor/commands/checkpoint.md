# /checkpoint

Purpose: Create a new frame in active-state with a concise summary + anchors, and link it from the current frame.

Steps:
1) Load `docs/reference/agentos/spec-active-state.md`.
2) Append a new frame with:
   - summary (1-3 sentences)
   - anchors (files/rules/docs/tools used)
3) Add a `links[]` edge from current frame -> new frame with kind `branch|resume|shift_context`.

