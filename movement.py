class movement:
    mv_bs = int(0)
    mv_en = int(0)
    mv_ol = int(0)

    def __init__(self):
        self.mv_bs = int(120)
        self.mv_en = int(self.mv_bs//3)
        self.mv_ol = int(self.mv_bs//5)

    def __init__(self, mv_bs):
        self.mv_bs = mv_bs
        self.mv_en = int(self.mv_bs//3)
        self.mv_en = int(self.mv_bs//5)
