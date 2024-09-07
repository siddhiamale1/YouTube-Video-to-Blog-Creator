from crewai import Task
from tools import yt_tools
from agents import blog_researcher,blog_writer

#research Task
research_task = Task(
  description=(
    "Identify the video {topic}."
    "Get detailed information about the video from the channel."
  ),
  expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.',
  tools=[yt_tools],
  agent= blog_researcher,
)
# Writing task with language model configuration
write_task = Task(
  description=(
    "get the info from the youtube channel on the topic {topic}."
  ),
  expected_output='Summarize the info from the youtube channel video on the topic{topic}',
  tools=[yt_tools],
  agent=blog_writer,
  async_execution=False,##if set true both agents will work parallely but we are doing sequentially
  output_file='new-blog-post.md'  # Example of output customization
)