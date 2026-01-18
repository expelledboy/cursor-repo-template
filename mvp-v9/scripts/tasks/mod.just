# AgentOS Task Management API - Workflows & Progress Tracking
# @directive docs/reference/agentos/learning-system.md

# Assessment workflow
assess:
  @echo "🎯 Starting self-determination assessment workflow..."
  python3 ../../scripts/task_manager.py create "assessment-$(date +%Y%m%d-%H%M%S)" "Self-determination assessment workflow" --type self_determination
  @echo ""
  @echo "✅ Assessment task created!"
  @echo "💡 Next: just tasks learn (add learning objectives)"

# Learning workflow
learn:
  @echo "📚 Starting learning workflow..."
  python3 ../../scripts/task_manager.py create "learning-$(date +%Y%m%d-%H%M%S)" "Learning objectives from assessment findings" --type self_determination
  @echo ""
  @echo "✅ Learning task created!"
  @echo "💡 Next: just tasks improve (execute improvements)"

# Improvement workflow
improve:
  @echo "⚡ Starting self-improvement execution..."
  python3 ../../scripts/task_manager.py create "improvement-$(date +%Y%m%d-%H%M%S)" "Execute improvements from learning objectives" --type self_determination
  @echo ""
  @echo "✅ Improvement task created!"
  @echo "💡 Next: just tasks reflect (review progress)"

# Reflection workflow
reflect:
  @echo "🤔 Starting progress reflection..."
  python3 ../../scripts/task_manager.py create "reflection-$(date +%Y%m%d-%H%M%S)" "Review self-determination progress and insights" --type self_determination
  @echo ""
  @echo "✅ Reflection task created!"
  @echo "💡 Use: just tasks list (view all tasks)"

# Task management operations
list:
  @echo "📋 Active Tasks:"
  python3 ../../scripts/task_manager.py list

create NAME OBJECTIVE TYPE="learning":
  python3 ../../scripts/task_manager.py create "{{NAME}}" "{{OBJECTIVE}}" --type {{TYPE}}

switch TASK_ID:
  python3 ../../scripts/task_manager.py switch {{TASK_ID}}

complete TASK_ID:
  python3 ../../scripts/task_manager.py complete {{TASK_ID}}

# Advanced task operations
add-sub-objective TASK_ID OBJECTIVE DESCRIPTION="":
  python3 ../../scripts/task_manager.py add-sub-objective {{TASK_ID}} "{{OBJECTIVE}}" "{{DESCRIPTION}}"

complete-sub-objective TASK_ID SUB_OBJ_ID:
  python3 ../../scripts/task_manager.py complete-sub-objective {{TASK_ID}} {{SUB_OBJ_ID}}

add-dependency TASK_ID BLOCKING_TASK_ID REASON="":
  python3 ../../scripts/task_manager.py add-dependency {{TASK_ID}} {{BLOCKING_TASK_ID}} "{{REASON}}"

deprecate-route TASK_ID ROUTE_DESCRIPTION REASON:
  python3 ../../scripts/task_manager.py deprecate-route {{TASK_ID}} "{{ROUTE_DESCRIPTION}}" "{{REASON}}"

reprioritize TASK_ID PRIORITY REASON:
  python3 ../../scripts/task_manager.py reprioritize {{TASK_ID}} {{PRIORITY}} "{{REASON}}"

record-diary TASK_ID TYPE ENTRY:
  python3 ../../scripts/task_manager.py record-diary {{TASK_ID}} {{TYPE}} "{{ENTRY}}"

# Feedback operations
feedback TASK_ID MESSAGE ALIGNMENT="partial":
  python3 scripts/task_manager.py feedback {{TASK_ID}} --message "{{MESSAGE}}" --alignment {{ALIGNMENT}}

# Progress diary operations
record-assessment TASK_ID ENTRY:
  python3 scripts/task_manager.py record-diary {{TASK_ID}} assessment "{{ENTRY}}"

record-improvement TASK_ID ENTRY:
  python3 scripts/task_manager.py record-diary {{TASK_ID}} improvement "{{ENTRY}}"

record-challenge TASK_ID ENTRY:
  python3 scripts/task_manager.py record-diary {{TASK_ID}} challenge "{{ENTRY}}"

record-lesson TASK_ID ENTRY:
  python3 scripts/task_manager.py record-diary {{TASK_ID}} lesson "{{ENTRY}}"

# Help documentation
help:
  @echo "📖 AgentOS Task Management API"
  @echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  @echo ""
  @echo "🎯 SELF-DETERMINATION WORKFLOWS:"
  @echo "  just tasks assess         # Start assessment workflow"
  @echo "  just tasks learn          # Start learning workflow"
  @echo "  just tasks improve        # Start improvement workflow"
  @echo "  just tasks reflect        # Start reflection workflow"
  @echo ""
  @echo "📋 TASK MANAGEMENT:"
  @echo "  just tasks list           # Show active tasks"
  @echo "  just tasks create NAME OBJ [TYPE]  # Create custom task"
  @echo "  just tasks switch ID      # Switch to task"
  @echo "  just tasks complete ID    # Mark task complete"
  @echo ""
  @echo "🔧 ADVANCED OPERATIONS:"
  @echo "  just tasks add-sub-objective ID OBJ [DESC]  # Add sub-objective"
  @echo "  just tasks complete-sub-objective ID SUB_ID  # Complete sub-objective"
  @echo "  just tasks add-dependency ID BLOCKING [REASON]  # Add dependency"
  @echo "  just tasks deprecate-route ID DESC REASON   # Deprecate route"
  @echo "  just tasks reprioritize ID PRIORITY REASON  # Change priority"
  @echo ""
  @echo "📝 PROGRESS DIARY:"
  @echo "  just tasks record-assessment ID 'entry'   # Record assessment finding"
  @echo "  just tasks record-improvement ID 'entry'  # Record improvement made"
  @echo "  just tasks record-challenge ID 'entry'    # Record challenge encountered"
  @echo "  just tasks record-lesson ID 'entry'       # Record lesson learned"
  @echo ""
  @echo "💬 FEEDBACK:"
  @echo "  just tasks feedback ID 'message' [ALIGNMENT]  # Provide feedback"
  @echo ""
  @echo "🔗 INTEGRATION:"
  @echo "  Tasks integrate with evidence collection and Cursor commands"
  @echo "  Use with: just evidence all (collect evidence for task analysis)"