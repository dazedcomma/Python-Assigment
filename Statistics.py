import os

def st():
    listing = os.listdir('/home/ramadhana/lirik/log')
    outfile = open('/home/ramadhana/lirik/Statistik/db.txt', 'w')
    for dir in listing:
        infile = open('/home/ramadhana/lirik/log/'+dir ,'r')
        outfile.truncate()
        list_score = []
        t = ()
        for i in infile:
            a = i.replace("\n","")
        # print(a)
            if 'Nama' in a:
                namapemain = a.replace('Nama Pemain: ','')
            if 'Skor' in a:
                b = a.replace('Skor akhir: ','')
                list_score.append(int(b))
        p = sum(list_score)
        outfile.write(str(namapemain))
        outfile.write(' ')
        outfile.write(str(p))
        outfile.write("\n")
        infile.close()
    outfile.close()
    klasmen()


def klasmen():
    infile = open('/home/ramadhana/lirik/Statistik/db.txt','r')
    outfile = open('/home/ramadhana/lirik/Statistik/klasmen.txt','w')
    lst=[]
    t = ()
    total = 0
    collect = {}
    for x in infile:
        z = x.replace("\n","").split(' ')
        t = (z[0],z[1])
        lst.append(t)
        collect = dict(lst)
        total = total+int(z[1])

    game = len(collect)
    rata = total / game
    maxi = max(collect, key=collect.get)
    outfile.write("STATISTIK PERMAINAN")
    outfile.write("\n")
    outfile.write("====================")
    outfile.write("\n")
    outfile.write("Jumlah Permainan: ")
    outfile.write(str(game))
    outfile.write("\n")
    outfile.write("Nilai rata-rata: ")
    outfile.write(str(rata))
    outfile.write("\n")
    outfile.write("Nilai tertinggi: ")
    outfile.write(str(collect[maxi]))
    outfile.write("\n")
    outfile.write("Peraih skor tertinggi: ")
    outfile.write(str(maxi))
    infile.close()
    outfile.close()

st()


