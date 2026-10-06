from pyscript import document

def generate(event):
    Espresso = "COFdE0101"
    Latte = "COFdL0202"
    Caramel_Macchiato = "COFdCM0303"
    Worlds_Best_Hot_Chocolate = "COFdWBHC0404"
    Horchata = "COFdH0505"
    Strawberry_Shorcake = "CAKcSS0601"
    Carrot_Cake = "CAKcCaC0702"
    Chocolate_Cake = "CAKcChC0803"
    Red_Velvet_Cake = "CAKcRvC0904"
    Blueberry_Cheesecake = "CAKcBC1005"

    category = document.querySelector("#category").value
    product = document.querySelector("#item").value

    if product == "Espresso":
        SKU = str(Espresso)
    
    elif product == "Latte":
        SKU = str(Latte)

    elif product == "Caramel Macchiato":
        SKU = str(Caramel_Macchiato)

    elif product == "World' s Best Hot Chocolate":
        SKU = str(Worlds_Best_Hot_Chocolate)

    elif product == "Horchata":
        SKU = str(Horchata)

    elif product == "Strawberry Shorcake":
        SKU = str(Strawberry_Shorcake)

    elif product == "Carrot Cake":
        SKU = str(Carrot_Cake)

    elif product == "Chocolate Cake":
        SKU = str(Chocolate_Cake)

    elif product == "Red Velvet Cake":
        SKU = str(Red_Velvet_Cake)

    elif product == "Blueberry Cheesecake":
        SKU = str(Blueberry_Cheesecake)

    elif product == "All":
        SKU = "No selected Product."

    document.querySelector("#output").innerText = "SKU:" + str(SKU)