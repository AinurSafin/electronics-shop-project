class InstantiateCSVError(Exception):

    def __str__(self):
        return 'Файл items.csv поврежден'