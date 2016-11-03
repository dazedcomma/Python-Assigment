import random,os, datetime, statistik

def guessingsong():
    now = datetime.datetime.now()
    Name = input('Nama: ')
    dirwrite = "log-"+Name+".txt"
    score = 0
    fw = open("/home/ramadhana/lirik/log/"+dirwrite, 'a')
    fw.write("Nama Pemain: ")
    fw.write(Name)
    fw.write('\n')
    fw.write("Tanggal Main: ")
    fw.write(now.strftime("%Y/%m/%d"))
    fw.write('\n')
    for ronde in range(1,11):
        print("Ronde ", ronde)
        fw.write("Ronde ")
        fw.write(str(ronde))
        fw.write('\n')
        dir = random.choice(os.listdir('/home/ramadhana/lirik/'))
        f = open("/home/ramadhana/lirik/" + dir, 'r')
        title = str(dir).replace('.txt', '').title()
        fw.write("Judul lagu: ")
        fw.write(title)
        fw.write('\n')
        fw.write("Lirik Soal\n")
        lst = []
        for i in f:
            lst.append(i.strip().split(' '))
        shuffle = random.randint(0, len(lst) - 4)
        for x in range(shuffle, shuffle + 3):
            question = " ".join(lst[x])
            fw.write(question)
            fw.write('\n')
            print(question)
        answer = " ".join(lst[x + 1])
        for chance in range(0, 3):
            #print("jawaban: " + answer)
            tebakan = input("Masukan Tebakanmu: ")
            if tebakan == answer:
                print("benar")
                fw.write("Jawaban: ")
                fw.write(answer)
                fw.write('\n')
                fw.write("Tebakan benar\n")
                score += 10
                print("Judul lagu: ", title, '\n')
                break
            else:
                print("salah")
                if chance < 2:
                    print("Petunjuk: " + lst[x + 1][chance])
                else:
                    print("Kesempatan kamu sudah habis :D")
                    print("Lirik yang benar adalah " + answer)
                    print("Judul lagu: ", title, '\n')
                    fw.write("Jawaban: ")
                    fw.write(answer)
                    fw.write('\n')
                    fw.write("Tebakan salah\n")
    print("Permainan Selesai :D")
    print("Skor anda : " + str(score))
    fw.write("Skor akhir: ")
    fw.write(str(score))
    fw.write('\n')
    newgame = input("Main lagi (Y/N)? ")
    if newgame == 'Y':
        fw.write("New Game\n")
        fw.close()
        guessingsong()
    else:
        print("Terima Kasih")
        f.close()
        fw.close()
        statistik.st()
        exit()
guessingsong()
