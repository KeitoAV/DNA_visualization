import random
import sys
import time


def main():
    PAUSE = 0.15  # значение можно менять - 0.5 или 0.0

    ROWS = [
        '         ##',  # у индекса 0 нет нуклеотидов {}.
        '        #{}-{}#',
        '       #{}---{}#',
        '      #{}-----{}#',
        '     #{}------{}#',
        '    #{}------{}#',
        '    #{}-----{}#',
        '     #{}---{}#',
        '     #{}-{}#',
        '      ##',  # у индекса 9 нет нуклеотидов {}.
        '     #{}-{}#',
        '     #{}---{}#',
        '    #{}-----{}#',
        '    #{}------{}#',
        '     #{}------{}#',
        '      #{}-----{}#',
        '       #{}---{}#',
        '        #{}-{}#']
    # 123456789 <- для наглядной оценки количества пробелов

    try:
        print("DNA Animation")
        print("Press Ctrl-C to quit...")
        print(chr(9786))
        time.sleep(2)
        rowIndex = 0

        while True:  # основной цикл программы
            # увеличиваем rowIndex на 1 для отрисовки следующей строки
            rowIndex = rowIndex + 1
            if rowIndex == len(ROWS):
                rowIndex = 0

            # у строк с индексами 0 и 9 нет нуклеотидов
            if rowIndex == 0 or rowIndex == 9:
                print(ROWS[rowIndex])
                continue

            # выбираем случайные пары оснований гуанин-цитозин и аденин-тимин
            randomSelection = random.randint(1, 4)
            leftNucleotide, rightNucleotide = str(), str()
            if randomSelection == 1:
                leftNucleotide, rightNucleotide = 'A', 'T'
            elif randomSelection == 2:
                leftNucleotide, rightNucleotide = 'T', 'A'
            elif randomSelection == 3:
                leftNucleotide, rightNucleotide = 'C', 'G'
            elif randomSelection == 4:
                leftNucleotide, rightNucleotide = 'G', 'C'

            # вывод строки на экран
            print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))
            time.sleep(PAUSE)  # пауза
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()

