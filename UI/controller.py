import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):

        allCountries = self._model.getAllCountries()
        allYears = self._model.getAllYears()
        countryDD = []
        yearsDD=[]

        for country in allCountries:
            countryDD.append(ft.dropdown.Option(country))

        self._view.ddcountry.options= countryDD

        for year in allYears:
            yearsDD.append(ft.dropdown.Option(year))

        self._view.ddyear.options = yearsDD
        self._view.update_page()



    def handle_graph(self, e):
        pass



    def handle_volume(self, e):
        pass


    def handle_path(self, e):
        pass
