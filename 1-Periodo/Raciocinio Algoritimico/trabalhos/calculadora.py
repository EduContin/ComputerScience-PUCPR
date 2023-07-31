shouldSave = False

while True:
    print("""
     ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
    ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
    ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
    ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    
     -~- MENU OPTIONS -~-
    
     [1] Adição
     [2] Subtração
     [3] Multiplicação
     [4] Divisão
     [0] Exit program
     """)
    
    option = int(input("Choose your option: "))
    
    if option == 1:
        print("""
         ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
        ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
        ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
        ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
        ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
         ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

         -~- ADIÇÃO SELECTED -~-
         """)
        if shouldSave == True:
            n2 = float(input("Digite o 2° valor: "))
            resultado = memory + n2
            print(f"Resultado: {resultado}\n")
            
        elif shouldSave == False:
            n1 = float(input("Digite o 1° valor: "))
            n2 = float(input("Digite o 2° valor "))
            resultado = n1 + n2
            print(f"Resultado: {resultado}\n")

        saveOption = input("Use result in next operation? (y/n): ")
        print(saveOption)
        if saveOption == "y":
            shouldSave = True
            memory = resultado
        option = 777

    if option == 2:
        print("""
         ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
        ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
        ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
        ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
        ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
         ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

         -~- SUBTRAÇÃO SELECTED -~-
         """)
        if shouldSave == True:
            n2 = float(input("Digite o 2° valor: "))
            resultado = memory - n2
            print(f"Resultado: {resultado}\n")
            
        elif shouldSave == False:
            n1 = float(input("Digite o 1° valor: "))
            n2 = float(input("Digite o 2° valor "))
            resultado = n1 - n2
            print(f"Resultado: {resultado}\n")

        saveOption = input("Use result in next operation? (y/n): ")
        print(saveOption)
        if saveOption == "y":
            shouldSave = True
            memory = resultado
        option = 777
    
    if option == 3:
        print("""
         ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
        ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
        ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
        ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
        ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
         ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

         -~- MULTIPLICAÇÃO SELECTED -~-
         """)
        if shouldSave == True:
            n2 = float(input("Digite o 2° valor: "))
            resultado = memory * n2
            print(f"Resultado: {resultado}\n")
            
        elif shouldSave == False:
            n1 = float(input("Digite o 1° valor: "))
            n2 = float(input("Digite o 2° valor "))
            resultado = n1 * n2
            print(f"Resultado: {resultado}\n")

        saveOption = input("Use result in next operation? (y/n): ")
        print(saveOption)
        if saveOption == "y":
            shouldSave = True
            memory = resultado
        option = 777
    
    if option == 4:
        print("""
         ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
        ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
        ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
        ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
        ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
         ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

         -~- DIVISÃO SELECTED -~-
         """)
        if shouldSave == True:
            n2 = float(input("Digite o 2° valor: "))
            resultado = memory / n2
            print(f"Resultado: {resultado}\n")
            
        elif shouldSave == False:
            n1 = float(input("Digite o 1° valor: "))
            n2 = float(input("Digite o 2° valor "))
            resultado = n1 / n2
            print(f"Resultado: {resultado}\n")

        saveOption = input("Use result in next operation? (y/n): ")
        print(saveOption)
        if saveOption == "y":
            shouldSave = True
            memory = resultado
        option = 777

    if option == 0:
        break

    else:
        continue