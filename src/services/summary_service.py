from langchain_core.language_models.base import BaseLanguageModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from typing import List

def get_summary_prompt_template() -> str:
  return """
    Write a summary for the post and its comments.
    Use an official and authoritative tone that is intended for casual users.
    The max length of the summary is {summary_length} characters, shorter is ok.

    The post is:
    {post}

    The comments are:
    {comments}
  """

def create_post_summary(
  model: BaseLanguageModel,
  post: str,
  comments: List[str]
) -> str:
  prompt_template = get_summary_prompt_template()
  prompt = ChatPromptTemplate.from_template(prompt_template)

  output_parser = StrOutputParser()

  chain = prompt | model | output_parser

  result = chain.invoke({
    'summary_length': 200,
    'post': post,
    'comments': comments
  })
  return result