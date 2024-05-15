from typing import List, Union
from mysql.connector.abstracts import MySQLConnectionAbstract

class Comment:
  def __init__(self, data: dict):
    self.id = data.get('id')
    self.title = data.get('title')
    self.content = data.get('content')

def select_comments_by_post_id(db: MySQLConnectionAbstract, post_id: int) -> List[Comment]:
  with db.cursor() as cursor:
    cursor.execute('SELECT * FROM comment WHERE post_id = %s', (post_id,))
    comment_tuples = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]
  return map(lambda cts: Comment(dict(zip(column_names, cts))), comment_tuples)