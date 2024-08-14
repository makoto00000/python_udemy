from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, age=1):
        self.age = age
    
    @abstractmethod
    def drive(self):
        pass

class Baby(Person):
      def __init__(self, age=1):
          if age < 18:
              super().__init__(age)
          else:
              raise ValueError

      def drive(self):
          raise Exception('No Drive')

class Adult(Person):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

    def drive(self):
        print('OK')

baby = Baby()
adult = Adult()

class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
      print('run')

    def ride(self, person):
          person.drive()

car = Car()
# car.ride(baby)
car.ride(adult)

class ToyotaCar(Car):
    def run(self):
      print('fast')

class TeslaCar(Car):
    def __init__(self, 
                 model='Model S',
                 enable_auto_run=False,
                 password='123'):
        super().__init__(model)
        # _ なし どこからでもアクセスできる
        # _ 1つ どこからでも＋propertyからアクセス
        # _ 2つ propertyからのみ クラス内では参照できる
        self.__enable_auto_run = enable_auto_run
        self.password = password

    @property
    def enable_auto_run(self):
        return self.__enable_auto_run
    
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.password == '456':
            self.__enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
      print(self.__enable_auto_run)
      print('super fast')

    def auto_run(self):
      print('auto run')

print("##############")
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()

print("##############")
tesla_car = TeslaCar('Model S', password='456')
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)

# 以下のように再定義してしまうと、属性「__enable_auto_run」が追加されてしまうので、エラーにならずprintできてしまう。（もとのenable_auto_runには影響なし）
# tesla_car.__enable_auto_run = False
# print(tesla_car.__enable_auto_run)

print("##############")
