from crewai import  Agent
from tools import yt_tools
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-3.5-turbo-0125"


#calling gemini model
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                            verbose=True,
                            temperature=0.5,
                            google_api_key=os.getenv("GOOGLE_API_KEY"))


##Create senior blog content researche
blog_researcher=Agent(
    role="Blog Researcher from Youtube Videos",
    goal='get the relevant video content for the topic{topic} from YT channel',
    verbose=True,
    memory=True,
    backstory=('Expert in understanding videos in AI Data Science , Machine Learning And GEN AI and providing suggestion'),
    tools=[yt_tools],
    llm=llm,
    allow_delegation=True
)
#creating blog writer agent with YT tool
blog_writer=Agent(
    role='Writer',
  goal='Narrate compelling tech stories about the video {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  llm=llm,
  tools=[yt_tools],
  allow_delegation=False

)