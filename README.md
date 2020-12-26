
#   Cpanel Suspend Hosting Hosting Paketi Silicisi

Cpanel üzerinde bir çok hosting paketi bulunmaktadır ve burada askıya alınan hosting paketlerinin toplu silinmesi ve takibi oldukça zordur özellikle whmcs gibi bir yazılım kullanmıyorsak :)

# Script Kullanımı  
 

Python sürümünüze göre ben default olarak 2.7 var sayıyorum aşağıdaki şekilde çalıştırabilirz.
Özetlemek gerekir ise kodumuzdan sonraki parametre tarih aralığını belirtmektedir eğer 1 yazar isek dün alınan yedekleri ertesi gün silecektir.

Not : 0 yazmanız durumunda aynı gün içersinde suspend alınan hosting paketleri silinmektedir.
Örnek  Kod : 

    python2.7 cp_acc_sus_term.py 1

Örnek Çıktı : 

    Kullanıcı Adı: {deneme} Silindi... ✅

 Güncellenicek...
