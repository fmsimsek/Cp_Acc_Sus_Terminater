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
from time       import  sleep
from argparse   import  ArgumentParser , ArgumentError

# Son işlem yedek almasın ama taşıma yapsın..

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
        self.p_count   = listdir(self.paths)
        self.count     = 0

        # User İnput 
        self.user_inp  = ArgumentParser()
        self.del_day   = self.user_inp.add_argument('-g', '--gun',   type=int, required=True, help="Suspend Paketlerin Silinme Aralığını Giriniz Örnek: -g 7 veya --gun 7")
        self.backup    = self.user_inp.add_argument('-y', '--yedek', type=str, required=True, help="Eğer Silinmeden Önce Backup Almak İsterseniz Evet yazmanız yeterlidir. Örnek -y veya --yedek evet ")  
        self.backup_p  = self.user_inp.add_argument('-p', '--yol',   type=str ,help="Yedeklerin Hangi Dizine Alınmasını İstersiniz Örnek -p /tmp/ veya --yol /tmp " )       
        self.args      = vars(self.user_inp.parse_args())
        
        # Local Backup Process Veriable 
        self.bp_command     = '/scripts/pkgacct'
        self.bp_answer      = 'evet'
        self.bp_move_c      = 'mv'
                 
        if self.count != (len(self.p_count)):    
          while(self.count < (len(self.p_count))):
              for self.user in self.p_count:
                                   
                # Lokal Değişkenler
                self.mdate     = path.getmtime(self.paths+self.user)
                self.sus_date  = date.fromtimestamp(self.mdate)
                self.diffrent  = date.today() - self.sus_date
                # Local değişkenler Bitiş.
                  
                if (self.args['gun'])  <=  (self.diffrent.days):  
                      if self.args['yedek'].lower() in self.bp_answer: 

                          # Yedek Alma Süreci Başlar..
                          self.b_process = Popen(self.bp_command+' '+ self.user, stderr=PIPE, shell=True)
                          if self.b_process.wait() == 0 :                                                         
                            if self.args['yol'] and path.isdir(self.args['yol']):                   
                              print('\n'+self.succes + "Kullanıcı Adı: " + '{'+self.user+'}' + " Yedek Alındı... "  +self.succ_pic+self.return_col)
                              self.b_mover= Popen(self.bp_move_c+' /home/cpmove-'+self.user+'.tar.gz'+' '+self.args['yol'], stdin=PIPE,  shell=True) 
                              # Yedek Kontrolü Başar..
                              if self.b_mover.wait() == 0:
                                 print(self.succes +  "Kullanıcı Adı: " + '{'+self.user+'}' + ' '+'/cpmove-'+self.user+'.tar.gz' + ' Yedek Dosyası '+'{'+self.args['yol']+'}' + " Klasörüne Taşındı ... "  +self.succ_pic+self.return_col)
                                 # Yedek Alındıktan Sonra Silme İşlemi Başlar..
                                 self.t_process = Popen(self.command+' '+ self.user, stdin=PIPE, shell=True)  
                                 if self.t_process.wait() == 0:       
                                  print('\n \n'+self.succes + "Kullanıcı Adı: " + '{'+self.user+'}' + " Silindi... "  +self.succ_pic+self.return_col)            
                                  self.count+=1 
                                 else:
                                   print(self.warn_pic +  "Kullanıcı Adı: " + '{'+self.user+'}' + ' '+'/cpmove-'+self.user+'.tar.gz' + ' Yedek Dosyası '+'{'+self.args['yol']+'}' + " Klasörüne Taşındı ... Fakat Silme İşlemi Gerçekleştirilemedi.... "  +self.warn_pic+self.return_col)                                        
                              else:
                                print('\n'+self.warn_pic + "Kullanıcı Adı: " + '{'+self.user+'}' + " Yedeği Alındı Fakat Belirtmiş Olduğunuz Klasöre Taşınamadı...\n Silme İşlemi İptal Edildi... "  +self.warn_pic+self.return_col)            
                                     
                            else:                             
                              #Eger Yedek Alınacak Yol Belirtmez ve yanlış ise yol  otomatik olarak home dizinine yedek alır ve silme işlemi sağlar...
                              print('\n'+self.succes + "Kullanıcı Adı: " + '{'+self.user+'}' + " Yedek Home Dizinine Alındı... "  +self.succ_pic+self.return_col)
                              self.t_process = Popen(self.command+' '+ self.user, stdin=PIPE, shell=True)        
                              if self.t_process.wait() == 0:       
                               print('\n \n'+self.succes + "Kullanıcı Adı: " + '{'+self.user+'}' + " Silindi... "  +self.succ_pic+self.return_col)            
                               self.count+=1  

                          else:
                            print('\n'+self.warn_pic+self.normal+"Yedek Alma İşlemi Başarısız..")
                      else:
                          # Bu Kısım Yedek Alma İşlemi Yapmadan Otomatik Silmektedir.... 
                          self.t_process = Popen(self.command+' '+ self.user ,  stdin=PIPE, shell=True)                        
                          if self.t_process.wait() == 0:        
                            print(self.succes + "Kullanıcı Adı: " + '{'+self.user+'}' + " Silindi... "  +self.succ_pic)     
                            print(self.return_col)       
                            self.count+=1
                          else:
                            print('\n'+self.warn_pic+self.normal+"Hesap Silme İşlemi Başarısız.."+self.return_col)
                                                   
                else:
                    print(self.warn_pic+self.normal+' {'+self.user+'}'+' Kullanıcısı Suspend Edilmiş Fakat '+ (str(self.args['day'])) + ' Gün Olmamıştır...'+self.warn_pic)
                    print(self.return_col) 
                
              break     
    
        else:
          print('\n'+self.normal+ self.warn_pic+' Suspend Hesap Bulunmamaktadır... '+self.warn_pic)
          print(self.return_col)
          
   
    except KeyboardInterrupt :
      print(self.normal+"CTRL+C İle Çıkış Yapılmıştır...")
      print(self.return_col)
 
  
if __name__ == "__main__":
  general = MainStd()   
