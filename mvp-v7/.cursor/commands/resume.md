# /resume

Purpose: Resume work from a prior frame (graph-style navigation).

Steps:
1) Load `.agentos/active-state.yaml` if present.
2) Ask for a `frame_id` if not provided.
3) Set `focus.frame_id` and update `navigation.recent_focus`.
4) Offer `/trace` to show the last decision points in that frame.

