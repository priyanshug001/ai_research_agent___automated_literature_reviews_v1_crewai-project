import os


from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	ArxivPaperTool,
	ExaSearchTool,
	URLReadTool
)

MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "openai/gpt-4o-mini")




@CrewBase
class AiResearchAgentAutomatedLiteratureReviewsCrew:
    """AiResearchAgentAutomatedLiteratureReviews crew"""

    
    @agent
    def research_planner(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["research_planner"],
            
            
            tools=[],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model=MODEL_NAME,
                
                
            ),
            
        )
        
    
    @agent
    def academic_search_agent(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["academic_search_agent"],
            
            
            tools=[				ArxivPaperTool(),
				ExaSearchTool()],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model=MODEL_NAME,
                
                
            ),
            
        )
        
    
    @agent
    def screening_and_relevance_agent(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["screening_and_relevance_agent"],
            
            
            tools=[				URLReadTool()],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model=MODEL_NAME,
                
                
            ),
            
        )
        
    
    @agent
    def paper_analysis_agent(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["paper_analysis_agent"],
            
            
            tools=[				URLReadTool()],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model=MODEL_NAME,
                
                
            ),
            
        )
        
    
    @agent
    def comparative_analysis_agent(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["comparative_analysis_agent"],
            
            
            tools=[],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model=MODEL_NAME,
                
                
            ),
            
        )
        
    
    @agent
    def research_gap_identification_agent(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["research_gap_identification_agent"],
            
            
            tools=[],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model=MODEL_NAME,
                
                
            ),
            
        )
        
    
    @agent
    def literature_synthesis_agent(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["literature_synthesis_agent"],
            
            
            tools=[],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model=MODEL_NAME,
                
                
            ),
            
        )
        
    
    @agent
    def quality_control_and_citation_audit_agent(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["quality_control_and_citation_audit_agent"],
            
            
            tools=[],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model=MODEL_NAME,
                
                
            ),
            
        )
        
    

    
    @task
    def create_research_plan(self) -> Task:
        return Task(
            config=self.tasks_config["create_research_plan"],
            markdown=False,
            
            
        )
    
    @task
    def search_academic_sources(self) -> Task:
        return Task(
            config=self.tasks_config["search_academic_sources"],
            markdown=False,
            
            
        )
    
    @task
    def screen_and_score_papers(self) -> Task:
        return Task(
            config=self.tasks_config["screen_and_score_papers"],
            markdown=False,
            
            
        )
    
    @task
    def analyze_included_papers(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_included_papers"],
            markdown=False,
            
            
        )
    
    @task
    def comparative_analysis_and_matrix(self) -> Task:
        return Task(
            config=self.tasks_config["comparative_analysis_and_matrix"],
            markdown=False,
            
            
        )
    
    @task
    def identify_research_gaps(self) -> Task:
        return Task(
            config=self.tasks_config["identify_research_gaps"],
            markdown=False,
            
            
        )
    
    @task
    def synthesize_literature_review(self) -> Task:
        return Task(
            config=self.tasks_config["synthesize_literature_review"],
            markdown=False,
            
            
        )
    
    @task
    def quality_control_and_citation_audit(self) -> Task:
        return Task(
            config=self.tasks_config["quality_control_and_citation_audit"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the AiResearchAgentAutomatedLiteratureReviews crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,

            chat_llm=LLM(model=MODEL_NAME),
        )

