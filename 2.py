repeat=input("Ну шо, еще партейку?")

attenpt = 1
while repeat.lower() != 'нет':
    print('Ну пошло добро по трубам! Трай', attenpt)
    attenpt += 1
    repeat=input("Ну шо, еще партейку?")
while (repeat := input("Ну шо, еще партейку?")) != 'нет':

    print(f'Да, сам согласился {repeat}, Ну пошло добро по трубам! Трай', attenpt)
    attenpt += 1