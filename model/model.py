import copy

from database.DAO import DAO
import networkx as nx


class Model:
    def __init__(self):
        self.optPath = None
        self.optPathDuration = None
        self.DAO = DAO()
        self.graph = None
        self.idMapAlbum = {}


    def createGraph(self, duration):
       pass




