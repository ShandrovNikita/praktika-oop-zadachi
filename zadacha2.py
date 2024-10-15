class Point(object):
  def __init__ (self,x_value,y_value):
    self.x=x_value
    self.y=y_value
  def set_coords(self,x_value,y_value):
    self.x=x_value
    self.y=y_value
  def get_coords(self):
    return self.x,self.y
point=Point(1,2)
point.get_coords()
point.set_coords(1,5)
point.get_coords()
