
class inv_type
    def __init__(self, item_type):
        self.item_type  = item_type
        self.storage    = {}
        
class inventory
    def __init__(self, size):
        self.size       = 20
        
    class inv_type
        def __init__(self, item_type):
            self.item_type  = item_type
            self.storage    = {}
            
class char_data
    def __init__(self,name,health,hunger):
        self.name       = name   #name to refer player to
        self.health     = health #starting health
        self.hunger     = hunger #starting hunger
        self.inventory  = self.name(20)
        
