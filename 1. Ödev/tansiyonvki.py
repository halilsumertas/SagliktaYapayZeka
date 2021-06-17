#VKİ Hesaplama Fonksiyonu
def VkiHesap(kilo,boy):
    vki = (boy/kilo**2)*100 #Orijinal formülde boy metre cinsinden fakat biz cm cinsinde alıyoruz veriyi. O yüzden 100 ile çarpıyoruz
    return vki
#Tansiyon Hesaplama Fonksiyonu
def TansiyonHesap(sistolik,diastolik):
    if sistolik < 120 and diastolik < 80:
        tansiyon = "Optimal"
        return tansiyon
    elif (sistolik < 130 and sistolik > 120) and (diastolik < 85 and  diastolik > 80):
        tansiyon = "Normal"
        return tansiyon
    elif (sistolik <= 139 and sistolik >= 130) or (diastolik <= 90 and diastolik >= 85):
        tansiyon = "Yüksek"
        return tansiyon
    elif (sistolik <= 159 and sistolik >= 140) or (diastolik <= 99 and diastolik >= 90):
        tansiyon = "Evre1"
        return tansiyon
    elif (sistolik <= 179 and sistolik >= 160) or (diastolik <= 109 and diastolik >= 100):
        tansiyon = "Evre2"
        return tansiyon
    elif (sistolik >= 180) or (diastolik >= 110):
        tansiyon = "Evre3"
        return tansiyon
    elif (sistolik <= 160 and sistolik >= 140) and (diastolik < 90):
        tansiyon = "İzole sistolik hipertansiyon (sınırda)"
        return tansiyon
    elif (sistolik >= 160) and (diastolik < 90):
        tansiyon = "İzole sistolik hipertansiyon"
        return tansiyon
#Program boyunca kullanacağımız değişkenler
dongu = True #Programı sürdürmek için kullanacağımız değişken
Kayitlar = [] #Kayıtları tutacağımız değişken

#Arayüz
print("Kan Basıncı ve Vücut Kitle Endeksi Değerlendirme Uygulmasına Hoşgeldiniz! \n")
while dongu:
    print("Lütfen yapmak istediğiniz işlemi seçiniz. \n")
    secim = int(input("Kan Basıncı değerlendirmesi için 1 \nVücut Kitle Endeksi hesaplaması için 2 \nGeçmiş kayıtları görüntülemek için 3 \nUygulamadan çıkmak için 0 \n"))
    if secim == 1:
        print("Kan Basıncı değerlendirme uygulması. \n")
        ad = input("Lütfen adınızı giriniz: ")
        soyad = input("Lütfen soyadınızı giriniz: ")
        sistolik = int(input("Lütfen sistolik kan basıncınızı giriniz: "))
        diastolik = int(input("Lütfen diastolik kan basıncınızı giriniz: "))
        hasta_tansiyon = TansiyonHesap(sistolik,diastolik)
        hasta_kayit = [ad, soyad, hasta_tansiyon]
        Kayitlar = Kayitlar + hasta_kayit
        print(f"Sayın {ad} {soyad}. Teşhisiniz: {hasta_tansiyon}. Detaylı bilgi için bağlantıyı takip edebilirisiniz: https://tkd.org.tr/kilavuz/k03/3_2d304.htm?wbnum=1104 \n")
    elif secim == 2:
        print("Vücut Kitle Endeksi hesaplama uygulaması.")
        ad = input("Lütfen adınızı giriniz: ")
        soyad = input("Lütfen soyadınızı giriniz: ")
        boy = int(input("Lütfen boyunuzu cm cinsinden giriniz: "))
        kilo = int(input("Lütfen kilonuzu kg cinsinden giriniz: "))
        hasta_vki = VkiHesap(boy,kilo)
        hasta_kayit = [ad, soyad, hasta_vki]
        Kayitlar = Kayitlar + hasta_kayit
        print(f"Sayın {ad} {soyad}. Vücut Kitle Endeksiniz: {hasta_vki}. ")
    elif secim == 3:
        print(Kayitlar)
    elif secim == 0:
        dongu = False
    else:
        print("Hatalı seçim yaptınız!")


