# ai-tools

A collection of AI-powered skills for software development workflows, organized as plugins.

## Plugins

### `pr` — PR Review Workflows

| Skill | Description |
|-------|-------------|
| `pr:review` | Structured PR review with JIRA context, module onboarding, and a problem summary table |
| `pr:respond` | Interactively address review comments on your PR one by one |

## Installation

### Claude Code

Add the marketplace and install plugins:

```
/plugin marketplace add SamuelSill/ai-tools
/plugin install ai-tools@pr
```

Skills will be available automatically in your sessions. Claude will invoke them when relevant, or you can trigger them explicitly:

```
/review
/respond
```

## Development

### Repository Structure

```
ai-tools/
├── build.py                               # Assembles SKILL.md from templates
└── prek.toml                              # Pre-commit hook configuration
├── instructions/                          # Source of truth (tool-agnostic)
│   ├── claude/                            # Claude-specific helpers
│   └── reviews/                           # Review workflow instructions
├── plugins/                               # Claude Code plugins
│   └── pr/                                # PR review workflows
│       ├── .claude-plugin/plugin.json
│       └── skills/
│           ├── review/
│           │   ├── SKILL.md.template      # Template referencing instructions
│           │   └── SKILL.md               # Generated (do not edit directly)
│           .
│           .
│           .
```

### How It Works

The `instructions/` directory contains the tool-agnostic source of truth for all skill content. The `SKILL.md.template` files reference these instructions using `{{path/to/file.md}}` syntax. A build step inlines the referenced content to produce the final `SKILL.md` files that Claude Code consumes.

This allows the same instructions to be reused across different AI tools while keeping the Claude plugin self-contained.

### Editing Instructions

1. Edit files in `instructions/` (never edit `SKILL.md` directly)
2. Commit as usual — the pre-commit hook rebuilds and stages the `SKILL.md` files automatically

### Adding a New Skill

1. Create instruction files in `instructions/`
2. Create a new directory under `plugins/<plugin-name>/skills/<skill-name>/`
3. Add a `SKILL.md.template` with frontmatter and `{{...}}` references to your instructions
4. Run `python3 build.py` to verify the output
5. Commit — the hook handles the rest

### Setting Up the Pre-commit Hook

This project uses [prek](https://prek.j178.dev/) to manage pre-commit hooks. After cloning, run:

```bash
prek install
```

This ensures `SKILL.md` files are rebuilt and staged automatically on every commit.
