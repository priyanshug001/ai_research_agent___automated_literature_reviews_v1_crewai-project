#!/usr/bin/env python
import sys
from datetime import date

from ai_research_agent___automated_literature_reviews.crew import (
    AiResearchAgentAutomatedLiteratureReviewsCrew,
)


def default_inputs() -> dict[str, str]:
    """Provide a useful starter topic for a literature review."""
    return {
        "research_topic": "Evaluation and reliability of large language model agents",
        "research_question": (
            "How are LLM-based autonomous agents evaluated for task performance, "
            "reliability, safety, and reproducibility, and what benchmarks, methods, "
            "and limitations are reported?"
        ),
        "disciplines": (
            "Computer Science, Artificial Intelligence, Natural Language Processing, "
            "and Robotics"
        ),
        "year_from": "2020",
        "year_to": str(date.today().year),
        "max_papers": "20",
        "citation_style": "APA 7th edition",
    }

def run():
    """Run the literature-review crew."""
    AiResearchAgentAutomatedLiteratureReviewsCrew().crew().kickoff(
        inputs=default_inputs()
    )


def train():
    """Train the crew using the project's default research inputs."""
    try:
        AiResearchAgentAutomatedLiteratureReviewsCrew().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=default_inputs(),
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}") from e


def replay():
    """Replay the crew execution from a specific task."""
    try:
        AiResearchAgentAutomatedLiteratureReviewsCrew().crew().replay(
            task_id=sys.argv[1]
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}") from e


def test():
    """Test the crew execution using the project's default research inputs."""
    try:
        AiResearchAgentAutomatedLiteratureReviewsCrew().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=default_inputs(),
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}") from e


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)
