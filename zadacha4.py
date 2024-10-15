import random
class Voin:
  def __init__ (self,value1,value2,value3):
    self.health=value1
    self.shield=value2
    self.stamina=value3
  def set_health(self,value):
    self.health=value
  def get_health(self):
    return self.health
  def hit_def(self):
    self.health-=random.randint(0,20)
    self.shield-=random.randint(0,10)
  def hit(self):
    self.health-=random.randint(10,30)
  def weak_hit(self):
    self.health-=random.randint(0,10)
  def hit_weak_def(self):
    self.health-=random.randint(0,10)
    self.shield-=random.randint(0,5)
  def atack(self):
    self.stamina-=10
  def get_stamina(self):
    return self.stamina
  def get_shield(self):
    return self.shield
  def fight(self,obj):
    n=0
    while 1>0 :
      k=random.randint(1,2)
      f=random.randint(1,2)
      n+=1
      if k==1 and f==1:
        if self.get_stamina()>0 and obj.get_stamina()>0:
          self.hit()
          obj.hit()
          self.atack()
          obj.atack()
        elif self.get_stamina()>0 and obj.get_stamina()==0:
          self.weak_hit()
          obj.hit()
          self.atack()
        elif self.get_stamina()==0 and obj.get_stamina()>0:
          obj.weak_hit()
          self.hit()
          obj.atack()
        else:
          self.weak_hit()
          obj.weak_hit()
      elif k==1 and f==2:
        if obj.get_shield()>0:
          if self.get_stamina()>0:
            obj.hit_def()
            self.atack()
          else:
            obj.hit_weak_def()
        else:
          if self.get_stamina()>0:
            obj.hit()
            self.atack()
          else:
            obj.weak_hit()
      elif k==2 and f==1:
        if self.get_shield()>0:
          if obj.get_stamina()>0:
            self.hit_def()
            obj.atack()
          else:
            self.hit_weak_def()
        else:
          if obj.get_stamina()>0:
            self.hit()
            obj.atack()
          else:
            self.weak_hit()
      print('Ход номер ', n)
      print('Параметры первого война: ',self.get_health(),self.get_shield(),self.get_stamina())
      print('Параметры второго война: ',obj.get_health(),obj.get_shield(),obj.get_stamina())
      if obj.get_health()<=10 or self.get_health()<=10:
        print('Бой окончен!')
        if 0<obj.get_health()<=10:
          print('Убить второго война?')
          bool=input(('Введите Да или Нет: '))
          if bool=='Да':
            print('За что?')
            answer=input(('Введите причину Вашей ненависти: '))
            print('Вы убили второго война.\n Первый победил!')
            break
          elif bool=='Нет':
            print('Второй воин благодарен Вам.\n Первый победил!')
            break
        elif 0<self.get_health()<=10:
          print('Убить первого война?')
          bool=input(('Введите Да или Нет: '))
          if bool=='Да':
            print('За что?')
            answer=input(('Введите причину Вашей ненависти: '))
            print('Вы убили первого война.\n Второй победил!')
            break
          elif bool=='Нет':
            print('Первый воин благодарен Вам.\n Второй победил!')
            break
        elif self.get_health()<=0:
          print('Первый воин пал в бою!\n Второй победил!')
          break
        elif obj.get_health()<=0:
          print('Второй воин пал в бою!\n Первый победил!')
          break
voin1=Voin(100,100,100)
voin2=Voin(100,100,100)
voin1.fight(voin2)
