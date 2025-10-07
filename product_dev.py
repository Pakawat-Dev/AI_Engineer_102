import os
import asyncio
from dotenv import load_dotenv

# === Models (LLM1/LLM2/LLM3) ==========================
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.models.ollama import OllamaChatCompletionClient

# === Agents & Teaming =================================
from autogen_agentchat.agents import AssistantAgent, SocietyOfMindAgent
from autogen_agentchat.ui import Console
from autogen_agentchat.conditions import MaxMessageTermination, TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat

async def main():
    load_dotenv()

    # ------ Product Development LLMs ------
    model_client_openai_1 = OpenAIChatCompletionClient(   # LLM1
        model="gpt-4o-mini",
        api_key=os.environ["OPENAI_API_KEY"],
    )
    model_client_openai_2 = OpenAIChatCompletionClient(   # LLM2
        model="gpt-5-mini",
        api_key=os.environ["OPENAI_API_KEY"],
    )
    model_client_ollama = OllamaChatCompletionClient(  # LLM3
        model="llama3.2:3b",
        base_url=os.environ["OLLAMA_BASE_URL"],
    )

    # ===== PRODUCT TEAM SPECIALISTS ==========
    ux_researcher = AssistantAgent(
        name="ux_researcher",
        model_client=model_client_openai_1,  # LLM1
        system_message=(
            "Role: UX Researcher. Break down user needs, JTBD, pain points, "
            "and success metrics. Produce concise bullets and cite assumptions. "
            "Say 'APPROVED' when your research notes are ready."
        ),
    )

    product_architect = AssistantAgent(
        name="product_architect",
        model_client=model_client_openai_2,  # LLM2
        system_message=(
            "Role: Tech Lead / Engineer. Propose a simple, feasible architecture, "
            "interfaces, and a minimal backlog. Flag risks and unknowns. "
            "Say 'APPROVED' when your plan is ready."
        ),
    )

    quality_analyst = AssistantAgent(
        name="quality_analyst",
        model_client=model_client_ollama,  # LLM3
        system_message=(
            "Role: QA & Compliance. Review for safety, privacy, and regulatory fit "
            "(ISO/OSHA/IEC basics). List testable acceptance criteria. "
            "Say 'APPROVED' when review is ready."
        ),
    )

    # Inner workers’ loop stops once all hand off.
    team_termination = TextMentionTermination(text="APPROVED") | MaxMessageTermination(max_messages=2)

    product_team = RoundRobinGroupChat(
        participants=[ux_researcher, product_architect, quality_analyst],
        termination_condition=team_termination,
    )

    # ===== PRODUCT MANAGER ===============
    product_manager = SocietyOfMindAgent(
        name="product_manager",
        team=product_team,
        model_client=model_client_openai_2,  # Uses LLM2 to plan/route
    )

    # ===== PRODUCT WRITER ====================
    product_writer = AssistantAgent(
        name="product_writer",
        model_client=model_client_openai_1,  # Uses LLM1 to compile
        system_message=(
            "Role: Tech Writer (Synthesizer). Combine the orchestrator’s summary and "
            "worker outputs into a crisp deliverable (one page). Include: "
            "Problem, Target Users, Proposed Solution, System Sketch, MVP Scope, "
            "Acceptance Criteria, Risks & Next Steps. End with 'FINALIZED'."
        ),
    )

    # ===== PRODUCT DEVELOPMENT WORKFLOW ======
    final_termination = TextMentionTermination(text="FINALIZED") | MaxMessageTermination(max_messages=6)

    development_workflow = RoundRobinGroupChat(
        participants=[product_manager, product_writer],
        termination_condition=final_termination,
    )

    # Product development brief request
    task = (
        "INPUT: Create a one-page MVP brief for a burnout monitoring software. "
        "The system should track employee well-being signals (working hours, "
        "self-reported stress surveys, keyboard/mouse activity, optional wearable data). "
        "It must provide managers with aggregated, anonymized dashboards, "
        "offer early warning indicators, and suggest preventive actions. "
        "Ensure compliance with privacy and labor regulations."
    )

    stream = development_workflow.run_stream(task=task)
    await Console(stream)

if __name__ == "__main__":
    asyncio.run(main())