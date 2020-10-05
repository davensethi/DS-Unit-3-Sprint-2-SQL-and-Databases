import sqlite3

def connect_to_db(db_name="rpg_db.sqlite3"):
  return sqlite3.connect(db_name)


def execute_query(cursor, query):
  cursor.execute(query)
  return cursor.fetchall()

GET_CHARACTERS = """
    SELECT  COUNT(DISTINCT name)
    FROM charactercreator_character
"""

weapon_items = """
    SELECT  COUNT(*)
    FROM armory_item;
"""

Items_20 ="""
	SELECT  character_id, Count(*) AS num_times 
    FROM  charactercreator_character_inventory
    GROUP BY character_id
    ORDER BY num_times DESC 
    LIMIT 20;
"""

AVERAGE_ITEM = """
    SELECT AVG (num_times) FROM
    (SELECT  character_id, Count(*) AS num_times 
    FROM  charactercreator_character_inventory
    GROUP BY character_id
    ORDER BY num_times DESC ) 
"""


if __name__ == "__main__":
  conn = connect_to_db()
  curs = conn.cursor()
  char_count = execute_query(curs, GET_CHARACTERS)
  weapon_count = execute_query(curs, weapon_items)
  item_char = execute_query(curs,Items_20)
  Item_average = execute_query(curs,AVERAGE_ITEM)
  print('The total number of characters are', char_count)
  print('using the Schema diagram and no code we are able to see 4 subclasses of characters')
  print('The total number of weapons are', weapon_count)
  print ('The first 20 rows of items when grouped by character id', item_char)
  print ('The average of items each is equal to ', Item_average)