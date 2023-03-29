class Citizen:
    def __init__(self,name,age,dob,id_number):
        self.citizen_name=name
        self.citizen_age=age
        self.citizen_dob=dob
        self.id_number=id_number
        
    def add_citizen(self):
        print("Name: "+self.citizen_name)
        print("Age: "+str(self.citizen_age))
        print("Dateof birth: "+self.citizen_dob)
        print("Citizen Id: "+self.id_number)
        print("Citizen Added")
        
citizen1 = Citizen("peter",8,"19th october 2010","0198")
citizen1.add_citizen()

citizen2 = Citizen("Sophia",11,"24th october 2011","0198")
citizen2.add_citizen()