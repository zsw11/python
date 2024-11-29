class Car(object):

    def run(self):
        return "一辆破车在路上跑，除了喇叭不响哪儿都响"


class Benz(Car):

    def run(self):
        return "benz在路上跑"


class Bmw(Car):

    def run(self):
        return "bmw在路上跑"


class Audi(Car):

    def run(self):
        return "audi在路上跑"


class CarFactory(object):
    @staticmethod
    def get_car(car_name):

        if car_name == "benz":
            return Benz()
        elif car_name == 'bmw':
            return Bmw()
        elif car_name == 'audi':
            return Audi()
        else:
            return Car()


class User(object):

    def __init__(self, name):
        self.name = name

    def drive_car(self, car):
        print(self.name + "正在开着" + car.run())


user = User('zhangsan')

user.drive_car(CarFactory.get_car('bmw'))
user.drive_car(CarFactory.get_car('audi'))
user.drive_car(CarFactory.get_car('benz'))
user.drive_car(CarFactory.get_car('hello'))


