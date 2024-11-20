class hangman:
    def __init__(self,slovo):
        self.slovo=slovo.lower()
        self.zivoty=3
        self.tvojeslovo=["_"] * len(self.slovo)
        while self.zivoty>=1:
            if "_" not in self.tvojeslovo:
                print("W pogger's! Uhodl jsi slovo:", self.slovo)
                break
            self.status()
            if self.hadajici_pismeno():
                print("Správně :)")
                continue
            else:
                print("Špatné písmeno")
                self.zivoty-=1
        if self.zivoty>=1:
            print("W pogger's", self.slovo, "je správně")
        else:
            print("Skápl si slovo bylo", self.slovo)
            
    def hadajici_pismeno(self):
        print("hádej písmenko")
        pismeno=input().lower()
        if len(pismeno) != 1 or not pismeno.isalpha():
            print("Neplatný vstup! Zadej pouze jedno písmenko.")
            return False
        if pismeno in self.slovo:
            index=0
            for index in range(len(self.slovo)):
                if self.slovo[index] == pismeno:
                    self.tvojeslovo[index] = pismeno
            return True
        else:
            return False
    
    def status(self):
        print(f"Zbývající životy: {self.zivoty}")
        print("Aktuální stav slova:", " ".join(self.tvojeslovo))

try1=hangman("ahoj")