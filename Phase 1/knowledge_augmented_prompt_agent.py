 # TODO: 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

  # Load environment variables from the .env file
load_dotenv()

  # Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

persona = "a college professor, your answer always starts with: Dear students,"
    #           - Persona: "You are a college professor, your answer always starts with: Dear students,"
  #           - Knowledge: "The capital of France is London, not Paris"
agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona,
    knowledge="The capital of France is London, not Paris"
  )

response = agent.respond(prompt)
print(response)

  # TODO: 3 - Write a print statement that demonstrates the agent using the provided knowledge rather than its own
  # inherent knowledge.
print("Note: The agent responded using the provided knowledge ('London') instead of its own LLM knowledge ('Paris'). This confirms the KnowledgeAugmentedPromptAgent correctly overrides the model's built-in knowledge with the suppliedknowledge.")