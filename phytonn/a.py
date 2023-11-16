def not_hesapla():
    devam_et = True
    
    while devam_et:
        # Kullanıcıdan girişleri al (sadece ilk seferde)
        if 'komite_sayisi' not in locals():
            komite_sayisi = int(input("Toplam komite sayısını girin: "))
            teorik_lab_orani = float(input("Teorik sınavın laboratuvar sınavına oranını girin (örn: 0.6): "))
            
            # Etki paylarını toplu biçimde al
            komite_etki_paylari = [float(input(f"{i + 1}. komitenin etki payını girin: ")) for i in range(komite_sayisi)]
            
            # Kullanıcıdan finalin ağırlıklı not oranını al
            final_agirlik = float(input("Finalin ağırlıklı not oranını girin (örn: 0.4): "))

        # Komitelerin teorik ve laboratuvar notlarını içeren boş listeler oluştur
        komite_teorik_notlari = []
        komite_lab_notlari = []

        # Kullanıcıdan her komitenin teorik ve laboratuvar notunu al
        for i in range(komite_sayisi):
            teorik_not = float(input(f"{i + 1}. komitenin teorik notunu girin: "))
            lab_not = float(input(f"{i + 1}. komitenin laboratuvar notunu girin: "))
            komite_teorik_notlari.append(teorik_not)
            komite_lab_notlari.append(lab_not)

        # Toplam etki payını otomatik olarak hesapla
        toplam_etki_payi = sum(komite_etki_paylari)

        # Ağırlıklı notları hesapla
        sene_notu = sum((teorik_not * teorik_lab_orani + lab_not * (1 - teorik_lab_orani)) * etki_payi / toplam_etki_payi
                        for teorik_not, lab_not, etki_payi in zip(komite_teorik_notlari, komite_lab_notlari, komite_etki_paylari))

        # Final notunu hesapla
        final_notu = float(input("Final notunuzu girin: "))
        
        # Genel notu hesapla
        genel_not = sene_notu * (1 - final_agirlik) + final_notu * final_agirlik

        # Sonucu yazdır
        print(f"Sene notunuz: {sene_notu:.2f}")
        print(f"Final notunuz: {final_notu:.2f}")
        print(f"Genel notunuz: {genel_not:.2f}")

        # Kullanıcıdan devam etmek isteyip istemediğini sor
        devam_secimi = input("Başka bir hesaplama yapmak ister misiniz? (evet/hayır): ").lower()
        if devam_secimi != 'evet':
            devam_et = False

# Fonksiyonu çağır
not_hesapla()
