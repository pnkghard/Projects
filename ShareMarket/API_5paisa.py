from py5paisa import FivePaisaClient

class Transaction:
    
    credential = {
                "APP_NAME":str(input("App Name : ")),
                "APP_SOURCE":str(input("App Source : ")),
                "USER_ID":str(input("User ID : ")),
                "PASSWORD":str(input("Password Key : ")),
                "USER_KEY":str(input("User Key : ")),
                "ENCRYPTION_KEY":str(input("Enxryption Key : "))
             }
    client = FivePaisaClient(cred=credential)
    
    #Initializing constructor with otp
    def __init__(self):
        ccode = input("Enter Client Code : ")
        cpin = int(input("Enter Pin : "))
        TOTP = input("Enter TOTP : ")
        token = client.get_request_token(client_code=ccode, totp=TOTP, pin=cpin)
        return self.client.get_access_token(request_token=token)
    
    #total holdings by clients
    def totalHoldings(self):
        hold = client.holdings()
        equity = pd.DataFrame(hold)
        col = ["Symbol", "Quantity", "AvgRate", "CurrentPrice", "Exch", "ExchType"]
        equity = equity[col]
        return equity
    
    #margin availabel
    def margin(self):
        margin = client.margin()
        margin = pd.DataFrame(margin)
        margin = margin.melt(var_name="Margin", value_name="Rupee")
        return margin
    
    #executed order position
    def position(self):
        pos = client.positions()
        if len(pos)==0:
            return "No executed order ...."
        pos = pd.DataFrame(pos)
        col = ["ScripName", "ScripCode", "Exch", "ExchType", "OrderFor", "BuyQty", "BuyAvgRate", "BuyValue", "SellQty", "SellAvgRate", "SellValue", "NetQty", "BookedPL"]
        pos = pos[col]
        return pos
    
    #position conversion
    def position_con():
        script = position()
        if script==-1:
            return "you have no executed order.."
        cod = input("Enter Script Symbol or Code : ")
        netqty = script[script[1]==cod][-2]
        if cod.isdigit():
            if cod in script["ScripCode"]:
                exc = script[script["ScripCode"]==cod]["Exch"]
                ext = script[script["ScripCode"]==cod]["ExchType"]
                conv = script[script["ScripCode"]==cod]["OrderFor"]
                qty = input("Quantity to Convert : ")
                client.position_convertion(Exch=exc, ExchType=ext, ScripData=cod, ConvertFrom=conv, ConvertQty=qty)
                name = script[script["ScripCode"]==cod]["ScripName"]
                return f"ScriptCode {cod} having Symbol {name} converted Quantity {qty} out of {netqty} successfully.."
            else:
                return f"No {cod} order executed..."
        else:
            if cod in script["ScripName"]:
                exc = script[script["ScripName"]==cod]["Exch"]
                ext = script[script["ScripName"]==cod]["ExchType"]
                conv = script[script["ScripName"]==cod]["OrderFor"]
                qty = input("Quantity to Convert : ")
                client.position_convertion(Exch=exc, ExchType=ext, ScripData=cod, ConvertFrom=conv, ConvertQty=qty)
                code = script[script["ScripName"]==cod]["ScripCode"]
                return f"ScriptCode {cod} having Symbol {code} converted Quantity {qty} out of {netqty} successfully.."
            else:
                return f"No {cod} order executed..."

    #UTF error 
    def remove_bom(self, text):
        if isinstance(text, str):
            if text.startswith('\ufeff'):
                self.text = text[1:]
        elif isinstance(text, bytes):
            if text.startswith(b'\xef\xbb\xbf'):
                self.text = text[3:]
        return self.text

    def placeOrder(self, ot:str, ex:str, ext:str, cod, qty:int, pr:int, itr=None, slp=None):
        mrg = client.margin()
        mrg = pd.DataFrame(mrg)
        mrg = mrg["ALB"][0]
    
        if mrg>=pr:    
            self.msg = client.place_order(
                                            OrderType=ot,
                                            Exchange=ex,
                                            ExchangeType=ext,
                                            ScripCode=cod,
                                            Qty=qty,
                                            Price=pr,
                                            IsIntraday=itr,
                                            StopLossPrice=slp
                                         )
            if self.msg is not None:
                self.msg = remove_bom(self.msg)
                print(self.msg)
            else:
                print("Status unknown......")
        else:
            print("You have no enough margin to place this order.....")