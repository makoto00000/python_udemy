# 多重継承
# 複数のクラスを同時に継承する
# 使わない方が良いが、開発が進んで来たときに使わざるを得ない場面も出てくる

class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('person run')

class Car(object):
    def run(self):
        print('car run')

# Person,Carそれぞれにrunメソッドが存在する場合、継承した順番で、先に継承したものが優先される。（以下の場合、Personのrunが優先）
class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()