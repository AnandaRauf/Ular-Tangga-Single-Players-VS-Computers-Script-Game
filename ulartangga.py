print "****** 26 Mei 2018 PT.MrvDevelopment™ ********"
print "****** Program Bot Like dan Comment ******"
print "****** Chief Executive Officer Ananda Rauf Maududi ******"
import random

player1 =raw_input('Perkenalkan nama anda terlebih dahulu!')
posisi = 1
print nama, ',Selamat Datang Di Permainan Ular Tangga.'
print 'Posisi anda sekarang berada di nomor 1'

menang = False

def angkadadu(dadu):
angka = random.randrange (1,7,1)
print 'Angka Dadu =',angka
dadu = dadu + angka
if dadu == 3 :
print 'YEAY ada tangga \(≧▽≦)/'
return 22
elif dadu == 5 :
print 'YEAY ada tangga \(≧▽≦)/'
return 8
elif dadu ==11 :
print 'YEAY ada tangga \(≧▽≦)/'
return 26
elif dadu ==19 :
print 'Oh sial, ulaaaaaaaar tidakkkkk ∠(ﾟДﾟ)/ '
return 7
elif dadu ==20 :
print 'YEAY ada tangga \(≧▽≦)/'
return 29
elif dadu ==21 :
print 'Oh sial, ulaaaaaaaar tidakkkkk ∠(ﾟДﾟ)/'
return 9
elif dadu ==27 :
print 'Oh sial, ulaaaaaaaar tidakkkkk ∠(ﾟДﾟ)/'
return 1
else :
return dadu

while menang == False :
lempar = raw_input ('Tekan apa saja untuk melempar dadu')
posisi = angkadadu (posisi)
print 'Posisi anda sekarang berada di  :', posisi
if posisi <40 :
menang = False
else :
menang = True
print player1, ',Wah kamu hebat, kamu menang ≧▽≦. Jangan Lupa Share ya!.Terima Kasih ^o^'
print '/n'
