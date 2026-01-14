#!/usr/bin/env python3
# @directive docs/reference/agentos/validation-scripts.md

import os
import re
import sys

from validation_utils import extract_section_lines, parse_markdown_table, read_lines

BEHAVIOR_SPEC = "docs/reference/agentos/behavior-spec.md"
GATES_PATH = "docs/reference/agentos/verification-gates.md"
JUSTFILE = "justfile"


def parse_task_types():
    lines = read_lines(BEHAVIOR_SPEC)
    section = extract_section_lines(lines, "## 6. Task taxonomy")
    task_types = []
    for line in section:
        stripped = line.strip()
        if stripped.startswith("- "):
            task_types.append(stripped[2:].strip())
    return task_types


def parse_gate_table():
    lines = read_lines(GATES_PATH)
    headers, rows = parse_markdown_table(lines, "Task type")
    return headers, rows


def parse_recipes(lines):
    recipes = set()
    for line in lines:
        if not line or line.startswith(" "):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):", line)
        if match:
            recipes.add(match.group(1))
    return recipes


def load_just_modules():
    modules = {}
    if not os.path.isfile(JUSTFILE):
        return modules
    for line in read_lines(JUSTFILE):
        match = re.match(r'^mod\s+([A-Za-z0-9_-]+)\s+"([^"]+)"', line.strip())
        if match:
            name = match.group(1)
            path = match.group(2)
            modules[name] = path
        else:
            match = re.match(r"^mod\s+([A-Za-z0-9_-]+)$", line.strip())
            if match:
                name = match.group(1)
                modules[name] = name
    return modules


def module_recipe_map(modules):
    module_recipes = {}
    for name, path in modules.items():
        candidates = [
            os.path.join(path, "mod.just"),
            os.path.join(path, "justfile"),
            os.path.join(path, f"{name}.just"),
        ]
        mod_file = next((p for p in candidates if os.path.isfile(p)), None)
        if not mod_file:
            continue
        module_recipes[name] = parse_recipes(read_lines(mod_file))
    return module_recipes


def root_recipes():
    if not os.path.isfile(JUSTFILE):
        return set()
    return parse_recipes(read_lines(JUSTFILE))


def extract_just_recipe(command):
    tokens = command.split()
    if not tokens or tokens[0] != "just":
        return None
    for token in tokens[1:]:
        if token.startswith("-"):
            continue
        return token
    return None


def script_path_in_command(command):
    tokens = command.split()
    for token in tokens:
        cleaned = token.strip().strip("\"'")
        if cleaned.startswith("./"):
            cleaned = cleaned[2:]
        if cleaned.startswith("scripts/") or cleaned.endswith(".py") or cleaned.endswith(".sh"):
            return cleaned
    return ""


def command_exists(command, root_recipes_set, module_recipes):
    command = command.strip()
    if not command:
        return False, "empty command"
    if "&&" in command or ";" in command:
        parts = re.split(r"\s*(?:&&|;)\s*", command)
        for part in parts:
            ok, reason = command_exists(part, root_recipes_set, module_recipes)
            if not ok:
                return False, reason
        return True, ""
    if command.startswith("just "):
        recipe = extract_just_recipe(command)
        if not recipe:
            return False, "missing just recipe"
        if "::" in recipe:
            module, subrecipe = recipe.split("::", 1)
            if module not in module_recipes:
                return False, f"missing module {module}"
            if subrecipe not in module_recipes[module]:
                return False, f"missing recipe {module}::{subrecipe}"
            return True, ""
        if recipe not in root_recipes_set:
            return False, f"missing recipe {recipe}"
        return True, ""
    if command.startswith("ci:"):
        workflow = command[len("ci:") :].strip()
        if not workflow:
            return False, "missing workflow name"
        yml = os.path.join(".github", "workflows", f"{workflow}.yml")
        yaml = os.path.join(".github", "workflows", f"{workflow}.yaml")
        if not os.path.isfile(yml) and not os.path.isfile(yaml):
            return False, f"missing workflow {workflow}"
        return True, ""
    script_path = script_path_in_command(command)
    if script_path:
        if os.path.isfile(script_path):
            return True, ""
        return False, f"missing script {script_path}"
    return False, "unsupported command"


def main():
    if not os.path.isfile(BEHAVIOR_SPEC):
        print(f"Missing {BEHAVIOR_SPEC}")
        return 1
    if not os.path.isfile(GATES_PATH):
        print(f"Missing {GATES_PATH}")
        return 1

    task_types = parse_task_types()
    if not task_types:
        print("No task types found in behavior-spec")
        return 1

    headers, rows = parse_gate_table()
    required_headers = {"Task type", "Gate", "Command", "Evidence source", "Notes"}
    if not headers or not required_headers.issubset(set(headers)):
        print("Verification gate table missing required headers")
        return 1

    gate_task_types = [row.get("Task type", "").strip() for row in rows]
    gate_task_types = [t for t in gate_task_types if t]
    if not gate_task_types:
        print("Verification gates table has no task types")
        return 1

    errors = False

    missing_tasks = sorted(set(task_types) - set(gate_task_types))
    extra_tasks = sorted(set(gate_task_types) - set(task_types))
    duplicates = sorted({t for t in gate_task_types if gate_task_types.count(t) > 1})

    if missing_tasks:
        print("Task types missing from verification gates catalog:")
        for item in missing_tasks:
            print(f"  - {item}")
        errors = True
    if extra_tasks:
        print("Verification gates catalog has unknown task types:")
        for item in extra_tasks:
            print(f"  - {item}")
        errors = True
    if duplicates:
        print("Verification gates catalog has duplicate task types:")
        for item in duplicates:
            print(f"  - {item}")
        errors = True

    root_recipes_set = root_recipes()
    module_recipes = module_recipe_map(load_just_modules())

    for row in rows:
        task_type = row.get("Task type", "").strip()
        command = row.get("Command", "").strip().strip("`")
        if not task_type:
            continue
        ok, reason = command_exists(command, root_recipes_set, module_recipes)
        if not ok:
            print(f"Invalid command for task type {task_type}: {command} ({reason})")
            errors = True

    if errors:
        return 1

    print(f"Verification gates validation passed ({len(gate_task_types)} task types)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
