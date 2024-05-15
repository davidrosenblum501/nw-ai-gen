from typing import Union
from mysql.connector.abstracts import MySQLConnectionAbstract

class Post:
  def __init__(self, data: dict):
    self.id = data.get('id')
    self.title = data.get('title')
    self.content = data.get('content')

def select_post_by_id(db: MySQLConnectionAbstract, id: int) -> Union[Post, None]:
  with db.cursor() as cursor:
    cursor.execute('SELECT * FROM post WHERE id = %s', (id,))
    post_tuple = cursor.fetchone()
    column_names = [desc[0] for desc in cursor.description]
  post_data = dict(zip(column_names, post_tuple)) if post_tuple else None
  return Post(post_data) if post_data else None
