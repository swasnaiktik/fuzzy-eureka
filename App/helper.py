def checkQuantity(shipmentItemQuantity, itemQuantity):
    if shipmentItemQuantity > itemQuantity >= 0:
        raise RuntimeError


def validateStr(string):
    string = string.strip()
    if string == "":
        raise RuntimeError
    return string
