import random
class Voin:
  def __init__ (self,value):
    self.health=value
  def set_health(self,value):
    self.health=value
  def get(self):
    return self.health
  def hit(self):
    self.health-=20
  def fight(self,object):
    while 1>0 :
      k=random.randint(1,2)
      if k==1:
        print('Первый воин атакует второго.')
        object.hit()
        if object.get() > 0:
          print('У второго война осталось ',object.get(),' hp')
        else:
          print('У второго война осталось 0 hp')
          print('Второй воин мёртв.\n Первый воин победил!\n Бой окончен!\n')
          break
      else:
        print('Второй воин атакует первого.')
        self.hit()
        if self.get() > 0:
          print('У первого война осталось ',self.get(),' hp')
        else:
          print('У первого война осталось 0 hp')
          print('Первый воин мёртв.\n Второй воин победил!\n Бой окончен!\n')
          break
voin1=Voin(100)
voin2=Voin(100)
voin1.fight(voin2)
