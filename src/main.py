from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import mysql.connector
import os
from database.post import select_post_by_id
from database.comment import select_comments_by_post_id
from services.summary_service import create_post_summary

def main():
  load_dotenv()

  db = mysql.connector.connect(
    host='localhost',
    user='nw',
    password='test12345',
    database='nw'
  )

  api_key = os.getenv('OPENAI_API_KEY')
  model = ChatOpenAI(model='gpt-3.5-turbo-0125', openai_api_key=api_key)

  post_id_raw = input('Enter post id: ')
  post_id = int(post_id_raw)
  post = select_post_by_id(db, post_id)
  if post is None:
    print(f'Post with id={post_id} not found')
    return
  print(f'Loaded post(id={post.id}, title="{post.title})"')
  
  comments = select_comments_by_post_id(db, post.id)
  for comment in comments:
    print(f'Loaded comment(id={comment.id}, title="{comment.title}")')
  print(len(comments))

  summary = create_post_summary(
    model=model,
    post=post.content,
    comments=list(map(lambda c: c.content, comments))
  )
  print(f'Summary: {summary}')

  db.close()
  exit()

main()