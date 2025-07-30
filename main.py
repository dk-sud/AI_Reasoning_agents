#sample agent

import os
from pathlib import Path
from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools


env_file = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_file)


GROQ_API_KEY = os.getenv('GROQ_API_KEY')
groq_client = Groq(api_key=GROQ_API_KEY)


tariff_news = Agent(
    name='USA Tariffs on india',
    model=groq_client,
    description="Trump's tariffs on india and its trade impact.",
    tools=[DuckDuckGoTools],
    markdown=True
)

tariff_news.print_response("What will get cheaper what is expensive with US tariffs")