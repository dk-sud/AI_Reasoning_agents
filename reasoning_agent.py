import os
from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from agno.tools.reasoning import ReasoningTools
from pathlib import Path
from dotenv import load_dotenv
from agno.models.openai import OpenAIChat


env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

API_SECRETS = os.getenv('OPENAI_API_KEY')
openai_client = OpenAIChat(api_key=API_SECRETS)


def get_company_symbols(company_name):
    """
    Use this function only when the stock symbol from the brower tooling is not available.

    Arg:
        company: (str) this will be the name of the company.
    returns:
        str: this is the stock symbol of the company.

    """

    symbols = {
        "AtliQ": "MSFT",
        "Tesla": "TSLA",
        "Apple": "AAPL",
        "Amazon": "AMZN"
    }
    return symbols.get(company_name, company_name)


fin_consultant = Agent(
    name='fin_analyst',
    model=openai_client,
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            key_financial_ratios=True,
            analyst_recommendations=True,
            company_info=True,
            technical_indicators=True
        ),
        get_company_symbols
    ],
    instructions=[
        'Present the findings in a tabular format.',
        'exclude preamble, present only the output.'
    ],
    markdown=True,
    show_tool_calls=True
)
fin_consultant.print_response(
    "Analyze and prepare a report summary of AMD's performance in the last quarter of last financial year",
    stream=True, show_reasoning=True, stream_intermediate_steps=True, markdown=True, show_full_reasoning=True
)
