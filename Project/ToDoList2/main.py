#This is Task tracking program
ID = 1

class Tasks():
    def __init__(self, id, description, stats, CreatedAt, UpdateAt):
        self.InProgess_Task = [None]
        self.UnFinishTask = [None]
        self.Finish_Task = [None]

        self.id = id
        self.description = description
        self.stats = stats
        self.CreatedAt = CreatedAt
        self.UpdateAt = UpdateAt

    def add_task(self):
        with open("Data.json", "w") as f:
            self.id = ID
            f.write(f"{self.id}, {self.description}, {self.stats}, {self.CreatedAt}, {self.UpdateAt}")


    
