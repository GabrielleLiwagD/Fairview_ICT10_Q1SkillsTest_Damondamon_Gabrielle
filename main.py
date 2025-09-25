from pyscript import document, display

def order_summary(event=None):
    info1 = str(document.getElementById("input1").value) #Name
    info2 = str(document.getElementById("input2").value) #Age
    info3 = str(document.getElementById("input3").value) #School Name
    message = "Name: " + str(info1)
    message2 = "Contact Number: " + str(info2)
    message3 = "Address: " + str(info3)
    food = str(document.getElementById("food-order").value) #Food Order
    
    if food == "Potato-Leek Soup":
        price = 193
    elif food == "Creamy and Cheesy Mashed Potatoes":
        price = 300
    elif food == "Potato-Leek Stir-Fry":
        price = 500
    elif food == "Potato-Leek Salad":   
        price = 550
    else:
        price = 0
    
    total_price = f"Total Price: PHP {price}"
    display(total_price,target="total")
    display(message,target="message1")
    display(message2,target="message2")
    display(message3,target="message3")
