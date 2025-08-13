#In here im going to serialization and Deserialization with the Objects
#First we need to import the pickle package
import pickle
class Main:
    #In this Constructor set Some Values to object Variables
    def __init__(self,value,value_01):
        self.value = list([value,value_01])



    #In this Function get the all object variables
    def get_the_values(self):
        for i in self.value:
            yield i

    #In here get the Gen Object
    def get_the_gen_object(self):
        self.gen = self.get_the_values()
        return self.gen


    #Serialization
    @staticmethod
    def serialization(text,text_01):
        myObject = Main(text,text_01)

        with open('name-of-the-pickle-file','wb') as f:
            pickle.dump(myObject,f)

    #Deserialization
    @staticmethod
    def deserialization():
        try:
            with open("name-of-the-pickle-file", "rb") as f:
                myValue = pickle.load(f)
                return myValue
        except FileNotFoundError:
            return "File Not Found"


class Main_01:

    Main.serialization("Colombo", "Sri Lanka")
    myValue = Main.deserialization()
    myObj = myValue.get_the_gen_object()
    print(myObj.__next__())
    print(myObj.__next__())







