"""Contract specifications for docs validation."""

ALLOWED_DOC_STATUS = {"stable", "draft", "deprecated"}

ALLOWED_INTENTS = {
    "facts",
    "contract",
    "constraints",
    "procedure",
    "problem",
    "rationale",
    "decision",
    "examples",
    "glossary",
}

DECISION_STATUS_VALUES = {"accepted", "rejected", "superseded", "reversed"}

TASK_VALUES = {"setup", "operate", "debug", "change", "explain", "decide"}

INTENT_TASK_MATRIX = {
    "setup": {"facts", "procedure", "constraints"},
    "operate": {"facts", "procedure", "constraints"},
    "debug": {"facts", "procedure", "constraints", "examples"},
    "change": {"facts", "procedure", "constraints", "decision"},
    "explain": {"facts", "rationale", "glossary"},
    "decide": {"facts", "problem", "decision", "rationale", "constraints"},
}
