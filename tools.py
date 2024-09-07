from crewai_tools import YoutubeChannelSearchTool
from dotenv import load_dotenv
import os
load_dotenv()
#serpapi_api_key = os.getenv("SERPER_API_KEY")

# Mock the OPENAI_API_KEY to avoid errors
#os.environ["OPENAI_API_KEY"] = "mock_key"

#from crewai_tools.tools.youtube_channel_search_tool import YoutubeChannelSearchTool# Initialize the tool with a specific Youtube channel handle to target your search
yt_tools = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')
                                    #serpapi_api_key=os.getenv("SERPER_API_KEY"))

#os.environ['SERPER_API_KEY']=os.getenv('SERPER_API_KEY')
