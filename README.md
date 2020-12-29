
#   Cpanel Suspend Hosting Paketi Sonlanırıcısı

Cpanel üzerinde bir çok hosting paketi bulunmaktadır ve burada askıya alınan hosting paketlerinin toplu silinmesi ve takibi oldukça zordur özellikle whmcs gibi bir yazılım kullanmıyorsak :)

# Script Kullanımı  
 
 Cpanel sunucularında default olarak python 2.7 sürümü gelmektedir ve python 2.7 sürümü baz alınarak script geliştirilmiştir. İlerleyen zamanlarda cpanel python 3 sürümü desteklemesi durumunda veya default olarak python 3 sürümü gelmesi durumuda yeni düzenlemeler sağlanabilinir.

Scrip sizden 2 adet zorunlu ve 1 adet isteğe bağlı olmak üzere 3 parametre bekler bunlar aşağıdaki gibidir.

 **Yıldız** İşareti ile belirtilenler zorunlu parametrelerdir.

 1. *-g  veya  --gun        
 2. *-y  veya  --yedek   
 3. -p  veya - -yol 

Kullanımı ve seneryolarını aşağıda inceleyelim.
 
 **Senaryo 1**  
  Buğün veya bir günden daha kısa süre içersinde olan suspend hesapları silmek ve silmeden   önce yedek almak istersek girmemiz gereken kod aşağıdaki gibidir

    Python2.7 cp_acc_sus_term.py --gun 0  --yedek evet
  
  Not : Yedek almak istemez iseniz -y hayır yazmanız yeterlidir.
  
  **Senaryo 2**
Hosting paketi askıya alındıktan 7 gün sonra yedeği alınmadan silinsin.

    Python2.7 cp_acc_sus_term.py --gun 7 --yedek hayır
    
   **Senaryo 3**
	Hosting paketi askıya alındıktan 5 gün sonra yedeği alınsın ve home dizini yerine yedekler benim belirteceğim dizine taşınsın.

    Python2.7 cp_acc_sus_term.py --gun 5 --yedek evet --yol /tmp/
    
   **Senaryo 4**
   Örnek olarak yukardaki senaryo işimizi görmektedir fakat bu seferde sürekli 5 günde bir scripti çalıştırmak durumuda kalacağım bunuda otomatikleştirmek istersek crontab aşağıdaki şekilde eklememiz yeterli olacaktır.
   
    * * 5  * *  /usr/bin/python2.7 /root/cp_acc_sus_term.py --gun 5 --yedek evet --yol /tmp/ 
   
 
