from tkinter import *
class No:
    def __init__(self, dado=None):
        self.esquerdo = None
        self.direito = None
        self.dado = dado
    def __str__(self):
        return "{", str(dado), "}"
    def Fator_balanceamento(self):
        folha_esq = 0
        if self.esquerdo:
            folha_esq = self.esquerdo.ramo()
        folha_dir = 0
        if self.direito:
            folha_dir = self.direito.ramo()
        return folha_esq - folha_dir
    def ramo(self):
        folha_esq = 0
        if self.esquerdo:
            folha_esq = self.esquerdo.ramo()
        folha_dir = 0
        if self.direito:
            folha_dir = self.direito.ramo()
        return 1 + max(folha_esq, folha_dir)
    def setaFilhos(self, esquerdo, direito):
        self.esquerdo = esquerdo
        self.direito = direito
class ArvoreAVL:
    def __init__(self):
        self.raiz = None
    def calculaProfMaxima(self, raiz):
        if raiz == None:
            return 0
        return raiz.ramo()
    def criaNoh(self, dado):
        return No(dado)
    def contaNohs(self, raiz):
        if raiz == None:
            return 0
        return 1 + self.contaNohs(raiz.esquerdo) + self.contaNohs(raiz.direito)
    def RE(self, raiz):
        if raiz:
            raiz.dado, raiz.direito.dado = raiz.direito.dado, raiz.dado
            old_esquerdo = raiz.esquerdo
            raiz.setaFilhos(raiz.direito, raiz.direito.direito)
            raiz.esquerdo.setaFilhos(old_esquerdo, raiz.esquerdo.esquerdo)
    def RD(self, raiz):
        if raiz:
            raiz.dado, raiz.esquerdo.dado = raiz.esquerdo.dado, raiz.dado
            old_direito = raiz.direito
            raiz.setaFilhos(raiz.esquerdo.esquerdo, raiz.esquerdo)
            raiz.direito.setaFilhos(raiz.direito.direito, old_direito)
    def RED(self, raiz):
        if raiz:
            self.RE(raiz.esquerdo)
            self.RD(raiz)
    def RDE(self, raiz):
        if raiz:
            self.RD(raiz.direito)
            self.RE(raiz)
    def balancear(self, raiz):
        if raiz:
            balanco = raiz.Fator_balanceamento()
            if balanco > 1:
                if raiz.esquerdo.Fator_balanceamento() > 0:
                    self.RD(raiz)
                else:
                    self.RED(raiz)
            elif balanco < -1:
                if raiz.direito.Fator_balanceamento() < 0:
                    self.RE(raiz)
                else:
                    self.RDE(raiz)
    def insere(self, raiz, dado):
        if raiz == None:
            return self.criaNoh(dado)
        else:
            if dado <= raiz.dado:
                raiz.esquerdo = self.insere(raiz.esquerdo, dado)
            else:
                raiz.direito = self.insere(raiz.direito, dado)
            self.balancear(raiz)
        return raiz

class Aplicacao:
    def __init__(self, pai):
        self.arvoreAVL = None
        # campo de entrada texto
        self.t1 = Entry(pai)
        self.t1.bind("<Return>", self.constroiArvore)
        self.t1.pack()
        # Botão entrar com valor
        self.b1 = Button(pai,height = 1, width = 15)
        self.b1.bind("<Button-1>", self.constroiArvore)
        self.b1["text"] = "ENTRE COM VALOR"
        self.b1.pack()
        # Botão criar aleatoria uma arvore
        self.b2 = Button(pai,height = 1, width = 15)
        self.b2["text"] = "Exibe Árvore AVL"
        self.b2.bind("<Button-1>", self.exibeArvoreAVL)
        self.b2.pack()
        # Botão criar aleatoria uma arvore
        self.b3 = Button(pai,height = 1, width = 15)
        self.b3["text"] = "Balanceamento"
        self.b3.bind("<Button-1>", self.exibeBalanceamento)
        self.b3.pack()
        self.c1 = Canvas(pai, width=1024, height=650)
        self.c1.pack()
    def constroiArvore(self, *args):
        try:
            valor = int(self.t1.get())
        except Exception:
            return
        print(valor)
        if self.arvoreAVL == None:
            print("Criando")
            self.arvoreAVL = ArvoreAVL()
            self.raiz = self.arvoreAVL.criaNoh(valor)
        else:
            print("Inserindo")
            self.arvoreAVL.insere(self.raiz, valor)
        self.desenhaArvore(False)
    def exibeArvoreAVL(self, *args):
        if self.arvoreAVL != None:
            print("Exibindo arvore")
            self.desenhaArvore(False)
    def exibeBalanceamento(self, *args):
        if self.arvoreAVL != None:
            print("Exibindo arvore")
            self.desenhaArvore(True)
    def desenhaArvore(self, comFB=False):
        self.HORIZONTAL = 1024
        self.VERTICAL = 750
        self.tamanho = 30
        self.c1.delete(ALL)
        self.c1.create_rectangle(
            0, 0, self.HORIZONTAL, self.VERTICAL, fill="blue")
        self.xmax = self.c1.winfo_width() - 40  # margem de 40
        self.ymax = self.c1.winfo_height()
        self.numero_linhas = self.arvoreAVL.calculaProfMaxima(self.raiz)
        x1 = int(self.xmax / 2 + 20)
        y1 = int(self.ymax / (self.numero_linhas + 1))
        self.desenhaNoh(self.raiz, x1, y1, x1, y1, 1, comFB)
    def desenhaNoh(self, noh, posAX, posAY, posX, posY, linha, comFB=False):
        if noh == None:
            return
        numero_colunas = 2 ** (linha + 1)
        x1 = int(posX - self.tamanho / 2)
        y1 = int(posY - self.tamanho / 2)
        x2 = int(posX + self.tamanho / 2)
        y2 = int(posY + self.tamanho / 2)
        self.c1.create_line(posAX, posAY, posX, posY, fill="white")
        self.c1.create_oval(x1, y1, x2, y2, fill="white")
        rotulo = str(noh.dado)
        if comFB:
            rotulo = str(noh.Fator_balanceamento())
        self.c1.create_text(posX, posY, text=str(rotulo))
        posAX, posAY = posX, posY
        dx = self.xmax / numero_colunas
        dy = self.ymax / (self.numero_linhas + 1)
        posX = posAX + dx
        posY = posAY + dy
        self.desenhaNoh(noh.direito, posAX, posAY, posX, posY, linha + 1, comFB)
        posX = posAX - dx
        self.desenhaNoh(noh.esquerdo, posAX, posAY, posX, posY, linha + 1, comFB)

if __name__ == "__main__":
    root = Tk(None, None, "Desenhando Uma Arvore Binaria")
    root.geometry("1024x750")
    ap = Aplicacao(root)
    root.mainloop()
