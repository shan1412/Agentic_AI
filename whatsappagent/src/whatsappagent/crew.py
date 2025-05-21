from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class Whatsappagent():
    """Whatsappagent crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def call_center_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['call_center_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def backoffice_ops_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['backoffice_ops_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def team_lead_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['team_lead_agent'], # type: ignore[index]
            verbose=True
        )
    
    @task
    def call_center_task(self) -> Task:
        return Task(
            config=self.tasks_config['call_center_task'], # type: ignore[index]
            human_input=True,
            output_file='output/call_center_report.md'
        )

    @task
    def backoffice_ops_task(self) -> Task:
        return Task(
            config=self.tasks_config['backoffice_ops_task'], # type: ignore[index]
            output_file='output/backoffice_ops_report.md'
        )

    @task
    def team_lead_task(self) -> Task:
        return Task(
            config=self.tasks_config['team_lead_task'], # type: ignore[index]
            output_file='output/team_lead_report.md'
        )
    @crew
    def crew(self) -> Crew:
        """Creates the Whatsappagent crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True
        )
