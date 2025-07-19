from tabnanny import verbose
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class DevelopmentTeam:
    """DevelopmentTeam crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    agents_config = "./config/agents.yaml"
    tasks_config = "./config/tasks.yaml"

    @agent
    def development_lead(self) -> Agent:
        return Agent(config=self.agents_config["development_lead"], verbose=True)  # type: ignore[index]
    
    @agent
    def backend_engineer(self) -> Agent:
        return Agent(config=self.agents_config["backend_engineer"], verbose=True) # type: ignore[index]

    @agent
    def code_reviewer(self) -> Agent:
        return Agent(config=self.agents_config["code_reviewer"], verbose=True) # type: ignore[index]
    

    @task
    def design_task(self) -> Task:
        return Task(config=self.tasks_config["design_task"], verbose=True)  # type: ignore[index]

    @task
    def coding_task(self) -> Task:
        return Task(config=self.tasks_config["coding_task"], verbose=True) # type: ignore[index]

    @task
    def code_review_task(self) -> Task:
        return Task(config=self.tasks_config["code_review_task"], verbose=True) # type: ignore[index]

    @task
    def code_rewrite_task(self) -> Task:
        return Task(config=self.tasks_config["code_rewrite_task"], verbose=True) # type: ignore[index]

    @task
    def code_review_task_2(self) -> Task:
        return Task(config=self.tasks_config["code_review_task_2"], verbose=True) # type: ignore[index]

    @task
    def testing_task(self) -> Task:
        return Task(config=self.tasks_config["testing_task"], verbose=True) # type: ignore[index]

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @agent decorator,
            process=Process.sequential,
            verbose=True,
        )
