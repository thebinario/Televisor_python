class televisor():
    def __init__(self, canal="5", volume="50"):
        self.canal = canal
        self.volume = volume

    def trocarCanal(self):
        num = input("Mudar para CANAL: ")
        self.canal = num

    def trocarVolume(self):
        num = input("Mudar para VOLUME: ")
        self.volume = num

    def volume(self, numero):
        num = int(numero)
        if num >= 0 and num <= 100:
            self.volume = num
        else:
            print("O volume deve ser entre 0 e 100")
        return self.volume

    def __str__(self):
        return "\n\nCANAL: {} volume: {}\n\n".format(self.canal, self.volume)

def main():
    samsung = televisor()

    while True:
        print(samsung)
        print("opções ---------")
        print("1 - mudar canal")
        print("2 - mudar volume")
        menu = input("Selecionar:")

        if menu == "1":
            samsung.trocarCanal()
        elif menu == "2":
            samsung.trocarVolume()
        else:
            print("Selecione uma opção válida!")

if __name__ == '__main__':
    main()