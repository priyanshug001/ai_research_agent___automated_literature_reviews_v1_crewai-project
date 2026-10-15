# AiResearchAgentAutomatedLiteratureReviews Crew

Welcome to the AiResearchAgentAutomatedLiteratureReviews Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Requires Python >=3.10 and <3.14. The project uses [uv](https://docs.astral.sh/uv/):

```powershell
python -m pip install uv
uv sync
Copy-Item .env.example .env
```

Skip the install command if `uv` is already available.

Set `OPENAI_API_KEY` in `.env` before running. The academic search agent also uses
Exa, so set `EXA_API_KEY` to enable web search. Do not commit `.env`.

## Running the Project

From the project root, run:

```powershell
uv run crewai run
```

The default review investigates how large language model agents are evaluated for
task performance, reliability, safety, and reproducibility. It searches papers
published from 2020 through the current year and targets up to 20 papers. The
completed audit and literature review are written to
`output/literature_review.md`.

Change the default question and scope in
`src/ai_research_agent___automated_literature_reviews/main.py`. Select another
OpenAI model by setting `OPENAI_MODEL_NAME` in `.env`; the default is
`openai/gpt-4o-mini`.

## Understanding Your Crew

The ai_research_agent___automated_literature_reviews Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on tasks defined in `src/ai_research_agent___automated_literature_reviews/config/tasks.yaml`. The `agents.yaml` file in the same directory outlines their capabilities and configurations.

## Support

For support, questions, or feedback regarding the AiResearchAgentAutomatedLiteratureReviews Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
