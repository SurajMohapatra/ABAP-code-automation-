from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class AutomatingSapAbapCodeForCrewEfficiencyCrew():
    """AutomatingSapAbapCodeForCrewEfficiency crew"""

    @agent
    def abap_report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['abap_report_generator'],
            tools=[SerperDevTool()],
        )

    @agent
    def form_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['form_creator'],
            tools=[SerperDevTool()],
        )

    @agent
    def module_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['module_developer'],
            tools=[SerperDevTool()],
        )

    @agent
    def data_dictionary_automator(self) -> Agent:
        return Agent(
            config=self.agents_config['data_dictionary_automator'],
            tools=[SerperDevTool()],
        )

    @agent
    def enhancement_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['enhancement_specialist'],
            tools=[SerperDevTool()],
        )

    @agent
    def rap_application_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['rap_application_developer'],
            tools=[SerperDevTool()],
        )


    @task
    def generate_abap_reports(self) -> Task:
        return Task(
            config=self.tasks_config['generate_abap_reports'],
            tools=[SerperDevTool()],
        )

    @task
    def create_forms(self) -> Task:
        return Task(
            config=self.tasks_config['create_forms'],
            tools=[SerperDevTool()],
        )

    @task
    def develop_modules(self) -> Task:
        return Task(
            config=self.tasks_config['develop_modules'],
            tools=[SerperDevTool()],
        )

    @task
    def automate_data_dictionary(self) -> Task:
        return Task(
            config=self.tasks_config['automate_data_dictionary'],
            tools=[SerperDevTool()],
        )

    @task
    def implement_enhancements(self) -> Task:
        return Task(
            config=self.tasks_config['implement_enhancements'],
            tools=[SerperDevTool()],
        )

    @task
    def develop_rap_applications(self) -> Task:
        return Task(
            config=self.tasks_config['develop_rap_applications'],
            tools=[SerperDevTool()],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the AutomatingSapAbapCodeForCrewEfficiency crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
