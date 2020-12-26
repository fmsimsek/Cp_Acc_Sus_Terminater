#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Bu Script Otomatik olarak suspend olan hosting paketlerini silmek amacı ile oluşturulmuştur.
# Cpanel Askıya alan hosting paketlerini /var/cpanel/suspend klasörü altında kullanıcı adı ile dosya oluşturmaktadır
# Bu oluşan klasör adını alıp /script/removeacct aktarıp terminate etme işlemi sağlanabilir.
# Copyright 20220 
# Creator Fmsimsek
# Licensed under the MIT license :)

from subprocess import  *
from os         import  listdir , path
from datetime   import  date , timedelta
from sys        import  argv

class MainStd:
 
  def __init__(self,):
        
    try:
       
        self.normal     = '\33[33m'  # Default    Renk Stili.
        self.succes     = '\33[32m'  # Başarılı  Renk Stili.
        self.return_col = '\33[37m'  # Return Terminal Renk Stili
        self.warn_pic   = '❌'
        self.succ_pic   = '✅'
        self.paths     = '/var/cpanel/suspended/'
        self.command   = '/scripts/removeacct'
        self.mdate     = path.getmtime(self.paths)
        self.p_count   = listdir(self.paths)
        self.sus_date  = date.fromtimestamp(self.mdate)
        self.today     = date.today()
        self.diffrent  = self.today - self.sus_date 
        self.del_day   = argv[1] 
        self.count     = 0
    
        if self.count != (len(self.p_count)):    
          while(self.count < (len(self.p_count))):
              for self.user in self.p_count:

                  if (int(self.del_day))  <=  (int(self.diffrent.days)):  

                    self.process = Popen(self.command+' '+ self.user , stdout=PIPE  ,  shell=True)
                    print(self.succes + "Kullanıcı Adı: " + '{'+self.user+'}' + " Silindi... "  +self.succ_pic)     
                    print(self.return_col)       
                    self.count+=1
                
                  else:
                    print(self.warn_pic+self.normal+' {'+self.user+'}'+' Kullanıcısı Suspend Edilmiş Fakat '+ self.del_day + ' Gün Olmamıştır...'+self.warn_pic)
                    print(self.return_col) 

              break     
    
        else:
          print(self.normal+ self.warn_pic+' Suspend Hesap Bulunmamaktadır... '+self.warn_pic)
          print(self.return_col)

    except IndexError:
      
       print('\n'+self.warn_pic+self.normal+""" Suspend Olan Hosting Paketinin Kaç Gün Aralığında Silinmesini Belirtmediniz... \n 
       Örnek Olarak python sus_acc_del.py 7 Komutunu Girmeniz Durumunda 
       Hosting Paketi Suspend Edildikten  7 Gün Sonra Siliniecektir.
       """)
       print(self.return_col)
    
    except ValueError :

      print('\n'+self.warn_pic+self.normal+""" Hatalı String İfade Girdiniz. Lütfen Sayı Girmeniz Gerekmektedir. Aşağıdaki Örneği İnceleyiniz. \n      
       Örnek Olarak python sus_acc_del.py 7 Komutunu Girmeniz Durumunda 
       Hosting Paketi Suspend Edildikten  7 Gün Sonra Siliniecektir.
       """)
      
      print(self.return_col)
 
if __name__ == "__main__":
  general = MainStd()   
