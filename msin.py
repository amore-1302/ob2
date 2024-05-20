
class User:
    def __init__(self,my_id, name, access_level):
        self.__my_id =  my_id
        self.__name = name
        self.__access_level = access_level

    def get_my_id(self):
        return self.__my_id
    def set_my_id(self, new_my_id):
        self.__my_id = new_my_id

    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name

    def get_access_level(self):
        return self.__access_level
    def set_access_level(self, new_access_level):
        self.__access_level = new_access_level




class Admin(User):
    def __init__(self,my_id, name, access_level, dop_access_level):
        super.__init__(my_id, name, access_level)
        self.__dop_access_level = dop_access_level
    def add_user(self, list_user):
        current_el = self
        if current_el  not in list_user:
            list_user.append(current_el)

    def remove_user(self, list_user):
        current_el = self
        if current_el  in list_user:
            list_user.remove(current_el)

    def get_dop_access_level(self):
        return self.__dop_access_level
    def set_dop_access_level(self, new_dop_access_level):
        self.__dop_access_level = new_dop_access_level
