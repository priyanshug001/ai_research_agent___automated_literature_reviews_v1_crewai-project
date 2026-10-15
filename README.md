# AI Research Agent — Automated Literature Reviews

A CrewAI-based multi-agent workflow that searches academic sources, screens papers, analyzes included studies, compares findings, identifies candidate research gaps, synthesizes a literature review, and runs a citation/quality-control audit.

> **Important:** This repository currently provides a command-line CrewAI workflow. It does not include a web UI yet. Generated reviews are AI-assisted research drafts and should be checked against the original papers before academic submission.

## Features

- Research planning with keywords, search queries, and inclusion/exclusion criteria
- Academic paper discovery using arXiv and Exa-powered web search
- Paper screening and relevance scoring
- Structured analysis of included papers
- Cross-paper comparison and research-gap hypotheses
- Literature-review synthesis in Markdown
- Quality-control and citation-audit report
- Final report written to `output/literature_review.md`

The workflow is configured in `src/ai_research_agent___automated_literature_reviews/config/agents.yaml` and `tasks.yaml`.

## Requirements

- Python 3.10–3.13
- Git
- An OpenAI API key
- An Exa API key for Exa-powered academic/web search
- [uv](https://docs.astral.sh/uv/) (recommended dependency manager)

## Setup on Windows PowerShell

Run these commands from the repository root:

```powershell
python -m pip install --upgrade pip
python -m pip install uv
uv sync
Copy-Item .env.example .env
```

Open `.env` and replace the placeholders:

```dotenv
OPENAI_API_KEY=your_openai_api_key
EXA_API_KEY=your_exa_api_key
OPENAI_MODEL_NAME=openai/gpt-4o-mini
```

Keep real keys private. **Never commit `.env` or paste API keys into issues or chat.** The committed `.env.example` should contain placeholders only.

## Run the workflow

```powershell
uv run crewai run
```

The starter inputs are defined in `src/ai_research_agent___automated_literature_reviews/main.py`. The default topic is evaluation and reliability of LLM-based agents, with a publication range beginning in 2020 and a target of up to 20 papers.

After a successful run, check:

```text
output/
└── literature_review.md
```

The run can take time and incur API charges. Results depend on source availability, model responses, and the configured API credentials.

## Customize the research

Edit `default_inputs()` in `src/ai_research_agent___automated_literature_reviews/main.py` to change:

- `research_topic`
- `research_question`
- `disciplines`
- `year_from` and `year_to`
- `max_papers`
- `citation_style`

Change the model using `OPENAI_MODEL_NAME` in `.env`, if the selected model is available to your account.

## Troubleshooting

### Missing API key
Confirm that `.env` exists in the repository root and contains valid `OPENAI_API_KEY` and `EXA_API_KEY` values. Restart the command after editing the file.

### `uv` is not recognized
Run `python -m pip install uv`, then open a new terminal if necessary.

### Git reports a README merge conflict
Keep one clean README version and remove any Git conflict markers: `<<<<<<<`, `=======`, and `>>>>>>>`. Then run `git add README.md`, `git commit -m "Resolve README conflict"`, and `git push`.

### Output is missing
Check the terminal for failed tasks, API quota errors, invalid credentials, or source-access errors. The review is written only after the final quality-control task completes.

## Research integrity

- The workflow is designed to instruct agents not to fabricate paper metadata or findings, but LLM output is not a guarantee of correctness.
- Verify each title, author list, year, DOI, URL, and claim against the publisher or trusted scholarly database.
- Treat proposed research gaps as hypotheses within the retrieved corpus, not proof of global novelty.
- Abstract-based analysis is less reliable than full-text analysis; retain the report's scope limitations.
- This project does not replace a human systematic-review protocol or independent screening.

## Project structure

```text
.
├── .env.example
├── knowledge/
├── pyproject.toml
├── uv.lock
└── src/
    └── ai_research_agent___automated_literature_reviews/
        ├── config/
        │   ├── agents.yaml
        │   └── tasks.yaml
        ├── tools/
        ├── crew.py
        └── main.py
```

## License

No license file is currently included. Add a license before redistributing the project if you intend to grant reuse rights.
