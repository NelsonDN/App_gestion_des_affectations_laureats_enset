#     # # Création des régions
#     # regions = [
#     #     {'name': 'Adamaoua'},
#     #     {'name': 'Centre'},
#     #     {'name': 'Est'},
#     #     {'name': 'Extrême-Nord'},
#     #     {'name': 'Littoral'},
#     #     {'name': 'Nord'},
#     #     {'name': 'Ouest'},
#     #     {'name': 'Sud'},
#     #     {'name': 'Nord-Ouest'},
#     #     {'name': 'Sud-Ouest'}
#     # ]

#     # region_objects = {}
#     # for region_data in regions:
#     #     region = DRegion.objects.create(**region_data)
#     #     region_objects[region_data['name']] = region

#     # # Création des départements
#     # departments_data = {
#     #     'Adamaoua': [
#     #         'Djérem', 'Fao-et-Déo', 'Mayo-Banyo', 'Mbéré', 'Vina'
#     #     ],
#     #     'Centre': [
#     #         'Mfoundi', 'Lekié', 'Mbam-et-Inoubou', 'Méfou-et-Afamba', 'Méfou-et-Akono',
#     #         'Nyong-et-Kellé', 'Nyong-et-Mfoumou', 'Nyong-et-So’o', 'Haute-Sanaga', 'Mbam-et-Kim'
#     #     ],
#     #     'Est': [
#     #         'Boumba-et-Ngoko', 'Haut-Nyong', 'Kadey', 'Lom-et-Djerem'
#     #     ],
#     #     'Extrême-Nord': [
#     #         'Diamaré', 'Logone-et-Chari', 'Mayo-Danay', 'Mayo-Kani', 'Mayo-Sava', 'Mayo-Tsanaga'
#     #     ],
#     #     'Littoral': [
#     #         'Moungo', 'Nkam', 'Sanaga-Maritime', 'Wouri'
#     #     ],
#     #     'Nord': [
#     #         'Bénoué', 'Faro', 'Mayo-Louti', 'Mayo-Rey'
#     #     ],
#     #     'Ouest': [
#     #         'Bamboutos', 'Haut-Nkam', 'Hauts-Plateaux', 'Koung-Khi', 'Menoua', 'Mifi', 'Ndé', 'Noun'
#     #     ],
#     #     'Sud': [
#     #         'Mvila', 'Océan', 'Vallée-du-Ntem', 'Dja-et-Lobo'
#     #     ],
#     #     'Nord-Ouest': [
#     #         'Boyo', 'Bui', 'Donga-Mantung', 'Menchum', 'Mezam', 'Momo', 'Ngo-Ketunjia'
#     #     ],
#     #     'Sud-Ouest': [
#     #         'Fako', 'Koupé-Manengouba', 'Lebialem', 'Manyu', 'Meme', 'Ndian'
#     #     ]
#     # }

#     # for region_name, departments in departments_data.items():
#     #     region = region_objects[region_name]
#     #     for department_name in departments:
#     #         DDepartement.objects.create(name=department_name, region=region)


