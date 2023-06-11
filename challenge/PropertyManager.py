class Input:
    def __init__(self):
        pass
    
    def get_valid_num(self, type_str):
        while True:
            try:
                    value = input(type_str)
                    return int(value)
            except ValueError:
                    print('Invalid entry! Only numeric entry is allowed')
    def get_valid_str(self, str_msg):
        while True:
            try:
                value = input(str_msg)
                if not value.strip():
                    raise ValueError
                else:
                    return value
            except ValueError:
                print("Blank input is not acceptable")
    

class PropertyManager(Input):
    #Class Body
    def __init__(self, name, id):
            self.name = name
            self.id = id
            self.property_list = []
            self.applicant_list = []

    def save_property(self, address, rent):
        self.property_list.append({"address":address, "rent":rent})

            
    def create_property(self, disp_str1 = "Please provide address of the property: ", disp_str2 =  "Please provide rent amount: "):
        self.save_property(super().get_valid_str(disp_str1), super().get_valid_num(disp_str2))
        
    def save_applicant(self, name, income):
        self.applicant_list.append({"name":name, "income":income})
        
    def create_applicant(self, disp_str1 = "Please provide name of the applicant: ", disp_str2 = "Please provide income amount: "):
        self.save_applicant(super().get_valid_str(disp_str1), super().get_valid_num(disp_str2))

    def best_applicant(self, property_index = 0):
        self.r2i = [self.property_list[property_index]["rent"]/applicant["income"] for applicant in self.applicant_list]
        r2i_index_min = self.r2i.index(min(self.r2i))
        return self.applicant_list[r2i_index_min]["name"]

    def prefered_activity(self, disp_str):
        while True:
            try: 
                value = self.get_valid_num(disp_str)
                if 1 <= value <= 2:
                    return value
            except ValueError:
                print("Invalid Input")