from rada_factories import UkraineRadaFactory, PolandRadaFactory

simulation_config_file = {'rada': 'Poland'}


if __name__=="__main__":
    if simulation_config_file['rada'] == 'Ukraine':
        UkraineRadaFactory()().run()
    else:
        PolandRadaFactory()().run()
