
building_1 = {
    'name': 'Производственный цех №1',
    'adress': {
        'street': 'Динамовское шоссе', 
        'built_index': '7/1'},
    'types': ['Производственное помещение'],
    'count_floors': 1,
    'count_sections': 2,
    'sections_on_floors':{
        'floor_1':{
            'section_101':{
                'area': '80м²',
                'type': 'Производство',
                'heating': 'Отапливаемое',
                'tenant': None
            },
            'section_2':{
                'area': '80м²',
                'type': 'Производство',
                'heating': 'Отапливаемое',
                'tenant': {
                    'name':'ООО Заебись',
                    'type_of_activity': 'Доставляет радость'
                }
            }
        }
    }
}
