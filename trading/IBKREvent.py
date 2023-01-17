from threading import Event

class IBKREvent(Event):
    def __init__(self, order_id, contract = None) -> None:
        self.order_id = order_id
        self.contract = contract
        self.option_strikes = None
        self.option_expirations = None
        self.option_trading_class = None
        self.option_bid = None
        self.option_ask = None
        self.option_delta = None
        self.option_req_cancelled = False

        self.last = None #for underlying
        super().__init__()

    def has_complete_data(self):
        if self.contract != None:
            match self.contract.secType:
                case 'OPT':
                    return self.option_bid != None and self.option_ask != None and self.option_delta != None
                case 'BAG':
                    return self.option_bid != None and self.option_ask != None #no need delta for combo
                case 'IND':
                    return self.last != None
        
        return True #non data request?
