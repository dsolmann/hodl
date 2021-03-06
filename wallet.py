import cryptogr as cg
import net
import block
import mining
import time


bch = block.Blockchain()

class Wallet:
    def __init__(self):
        self.privkey, self.pubkey = cg.gen_keys()

    def new_transaction(self, outs, outns):
        """Performs tnx"""
        out = 0
        for outn in outns:
            out += outn
        if out > bch.money(self.pubkey):
            return False
        froms = []
        # todo: write froms generation algorythm
        bch.new_transaction(self.pubkey, froms, outs, outns, privkey=self.privkey)

    def my_money(self):
        return bch.money(self.pubkey)

    def listen_in_thread(self):
        while True:
            mess = net.listen(bch)
            net.handle_mess(bch, mess[0], mess[1])

    def act(self):
        if bch[-1].is_full:
            bch.append(mining.mine(bch))
