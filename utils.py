def get_obj_by_name(name, objects):

  for item in objects:
    if(item.name == name):
      return item
  return None
