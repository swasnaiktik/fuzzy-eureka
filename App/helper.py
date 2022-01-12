# helper.py can be used for creating more helper functions for future expandability

# Function to validate if the asked shipment item quantity is available in the Inventory
def checkQuantity(shipmentItemQuantity, itemQuantity):
    if shipmentItemQuantity > itemQuantity >= 0:
        raise RuntimeError

# Validating of the passed string is not empty and returns the stripped string.
def validateStr(string):
    string = string.strip()
    if string == "":
        raise RuntimeError
    return string
