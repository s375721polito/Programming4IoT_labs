import json

class conditionRule:
    def __init__(self,threshold):
        self.threshold = threshold

    def evaluate(self,value):
        return value > self.threshold

class temperatureRule(conditionRule):
    def evaluate(self, temperature):
        return temperature > self.threshold

class lightRule(conditionRule):
    def evaluate(self, light):
        return light > self.threshold

class ruleController:
    def __init__(self):
        self.rule = {}

    def add(self,name,rule):
        self.rule[name] = rule

    def update(self,name,rule):
        if(name in self.rule.keys()):
            self.rule[name] = rule
        else:
            print("Name not found!")

    def delete(self,name):
        if(name in self.rule.keys()):
            del self.rule[name]
        else:
            print("Name not found!")

    def evaluate(self,temp,light):
        for name,rule in self.rule:
            if isinstance(rule,temperatureRule):
                result = rule.evaluate(temp)
                print(name, ": ",result)
            elif isinstance(rule,light):
                result = rule.evaluate(light)
                print(name,": ",result)

    def rules(self):
        for name,rule in self.rules:
            print(name,": ",rule)

if __name__ == "main":
    controller = ruleController
    while True:
        request = input("add/update/delete/evaluate/rules/exit")
        if(request == "add"):
            rule = input("Insert the name of the type")
            name = input("Insert the name")
            threshold = input("Insert the threshold")
            if(rule == "light"):
                object_rule = lightRule(threshold)
                controller.add(name,object_rule)
            elif(rule == "temperature"):
                object_rule = temperatureRule(threshold)
                controller.add(name,object_rule)
        elif request == "update":
            rule = input("Insert the name of the type")
            name = input("Insert the name")
            threshold = input("Insert the new threshold")
            if(rule == "light"):
                object_rule = lightRule(threshold)
                controller.add(name,object_rule)
            elif(rule == "temperature"):
                object_rule = temperatureRule(threshold)
                controller.add(name,object_rule)
        elif request == "delete":
            name = input("Insert the name")
            controller.delete(name,rule)
        elif request == "evaluate":
            name = input("Insert the name")
            type = input("You want temperature or light(temp/light)")
            if(type == "temp"):
                value = input("Insert the temperature value")
                controller.evaluate(value,None)
            elif type == "light":
                value = input("Insert the light value")
                controller.evaluate(None,value)
        elif request == "rules":
            controller.rules()
        elif request == "exit":
            break