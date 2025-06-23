import flet as ft
import networkx as nx
from model.album import Album


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.view = view
        # the model, which implements the logic of the program and holds the data
        self.model = model

    def handleCreaGrafo(self, e):
        if self.view._txtInNcanzoni is not None:
            self.view.txt_result.clean()
            try:
                Ncanzoni = int(self.view._txtInNcanzoni.value)
                self.model.createGraph(Ncanzoni)
                graph = self.model.graph
                self.view.txt_result.controls.append(ft.Text(
                    f"Grafo creato!\n"
                    f"# vertici {graph.number_of_nodes()}\n"
                    f"# archi {graph.number_of_edges()}\n"))
                self.view.ddAlbum1.value = None
                self.view.ddAlbum1.options = []
                self.view.ddAlbum2.value = None
                self.view.ddAlbum2.options = []
                for node in list(graph.nodes()):
                    self.view.ddAlbum1.options.append(ft.dropdown.Option(key=node.AlbumId, text=node.title))
                    self.view.ddAlbum2.options.append(ft.dropdown.Option(key=node.AlbumId, text=node.title))

            except ValueError:
                self.view.txt_result.controls.append(ft.Text(
                    f"Inserisci i valori correttamente"))
        else:
            self.view.txt_result.controls.append(ft.Text(
                f"Inserisci i valori correttamente"))
        self.view.update_page()

    def handleStampaAdiacenze(self, e):
        graph = self.model.graph
        source = self.model.idMapAlbum[int(self.view.ddAlbum1Value)]
        listSuccessors = []
        for successor in graph.successors(source):
            #print(successor)
            weightOutEdge = 0
            weightInEdge = 0

            for u, v, data in graph.out_edges(successor, data=True):  # attenzine
                weightOutEdge += data.get('weight', 1)

            for u, v, data in graph.in_edges(successor, data=True):  # attenzine
                weightInEdge += data.get('weight', 1)

            bilancio = weightInEdge - weightOutEdge
            listSuccessors.append((successor, bilancio))
        listSuccessors = sorted(listSuccessors, key=lambda x: x[1], reverse = True)
        for element in listSuccessors:
            self.view.txt_result.controls.append(ft.Text(f"{element[0].__str__()}-->{element[1]}"))
        self.view.update_page()





    def handleCalcolaPercorso(self, e):
        if self.view.ddAlbum1Value is not None and self.view.ddAlbum2Value is not None:
            try:
                partenza = self.model.idMapAlbum[int(self.view.ddAlbum1Value)]
                print(partenza.AlbumId)
                arrivo = self.model.idMapAlbum[int(self.view.ddAlbum2Value)]
                print(arrivo.AlbumId)
                soglia = int(self.view._txtInSoglia.value)
                optPath = self.model.getOptPath(partenza, arrivo, soglia)
                self.view.txt_result.controls.append(ft.Text(
                    f"Il cammino semplice voluto è:"))
                for node in optPath:
                    self.view.txt_result.controls.append(ft.Text(
                        f"{node.__str__()}"))


            except ValueError:
                self.view.txt_result.controls.append(ft.Text(
                    f"Inserisci i valori correttamente"))
        else:
            self.view.txt_result.controls.append(ft.Text(
                f"Inserisci i valori correttamente"))
        self.view.update_page()





