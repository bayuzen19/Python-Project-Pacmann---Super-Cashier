#!/usr/bin/env python
# coding: utf-8

# In[295]:


import pandas as pd
"""
package untuk membuat dataframe
"""

class Transaction():
    
    def __init__(self):
        self.belanja = []
        
        """
        fungsi ini untuk inisiasi transaksi
        self.belanja bersifat list
        """
    
    def add_item(self,nama_barang,jumlah,harga):
        """
        fungsi ini untuk menambahkan item kedalam transaksi
        self.nama_barang bersifat string
        self.jumlah bersifat float
        self.harga bersifat float
        """
        
        try:
          jumlah = float(jumlah)
          harga = float(harga)

        except ValueError as Error:
          raise ValueError ("Masukkan angka !") 
        
        self.nama_barang = nama_barang
        self.jumlah = jumlah
        self.harga = harga
        
        items = {"nama":nama_barang,
                "jumlah":jumlah,
                "harga":harga}
        
        self.belanja.append(items)
        
        print(f"Pesanan dengan nama {nama_barang} berjumlah {jumlah} dengan harga Rp {harga}. Berhasil !")
        return
        
    def update_item_name(self,old_name,new_name):
        """
        fungsi ini untuk mengubah nama lama menjadi nama baru
        old_name bersifat string
        new_name bersifat string
        """
        
        for key in self.belanja:
            if key["nama"] == old_name:
                key["nama"] = new_name
                print(f"{old_name} telah berhasil diganti dengan {new_name}")
                break
        else:
            print(f"{old_nama} tidak di temukan dalam keranjang")
            
    def update_item_qty(self,nama_barang,jumlah_baru):
        """
        fungsi ini untuk mengubah jumlah lama menjadi jumlah baru
        nama_barang bersifat string
        jumlah_baru bersifat float
        """
        
        try:
          jumlah_baru = float(jumlah_baru)

        except ValueError as Error:
          raise ValueError ("Masukkan angka !") 
        
        for key in self.belanja:
            if key["nama"] == nama_barang:
                key["jumlah"] = jumlah_baru
                print(f"{nama_barang} telah berhasil menganti jumlah menjadi {jumlah_baru}")
                break
        else:
            print(f"{nama_barang} tidak di temukan dalam keranjang")
            
    def update_item_price(self,nama_barang,price_baru):
        """
        fungsi ini untuk mengubah price lama menjadi price baru
        nama_barang bersifat string
        price_baru bersifat float
        """
        
        try:
          price_baru = float(price_baru)

        except ValueError as Error:
          raise ValueError ("Masukkan angka !") 
        
        for key in self.belanja:
            if key["nama"] == nama_barang:
                key["harga"] = price_baru
                print(f"{nama_barang} telah berhasil menganti harga menjadi {price_baru}")
                break
        else:
            print(f"{nama_barang} tidak di temukan dalam keranjang")
            
    def delete_item(self,nama_barang):
        """
        fungsi untuk mengapus remove item dari transaksi belanja
        """
        filter_ = list(filter(lambda items:items["nama"]==str(nama_barang),self.belanja))
        if len(filter_) > 0:
            self.belanja.remove(filter_[0])
            print(f"{nama_barang} telah di remove")
        else:
            print(f"{nama_barang} tidak ditemukan dalam list belanja")
                  
    def reset_transaction(self):
        """
        fungsi untuk menghapus transaksi
        """
        try:
            self.belanja.clear()
            print("Transaksi berhasil di hapus")
        except:
            print("tidak berhasil membersihkan")
                  
    def check_order(self):
        """
        fungsi untuk memeriksa order dan dikembalikan dalam bentuk 
        dataframe
        """
        try :
            data = pd.DataFrame(self.belanja)
            data["total harga"] = data["jumlah"] * data["harga"]
            if len(data) == 1:
                data["No"] = 1
                data=data.reindex(columns=['No', 'nama', 'jumlah',"harga","total harga"])
            elif len(data) > 1:
                data["No"] = pd.RangeIndex(start=1,stop=len(data)+1)
                data=data.reindex(columns=['No', 'nama', 'jumlah',"harga","total harga"])
            return data
        except:
            print("Belum ada transaksi atau transaksi belum benar, silahkan check kembali")
            
            
    def print_total(self):

        """
        fungsi untuk menghitung total pembayaran
        """

        total_belanja = sum((items['jumlah']*items['harga']) for items in self.belanja)

        if total_belanja > 500_000:
          diskon = total_belanja * .08
          total_akhir = total_belanja - diskon
          print(f"Selamat! Anda mendapat potongan sebesar Rp {diskon}, total belanja Anda adalah Rp {total_akhir}.")

        elif total_belanja > 300_000:
          diskon = total_belanja * .05
          total_akhir = total_belanja - diskon
          print(f"Selamat! Anda mendapat potongan sebesar Rp {diskon}, total belanja Anda adalah Rp {total_akhir}.")

        elif total_belanja > 200_000:
          diskon = total_belanja * .02
          total_akhir = total_belanja - diskon
          print(f"Selamat! Anda mendapat potongan sebesar Rp {diskon}, total belanja Anda adalah Rp {total_akhir}.")

        elif total_belanja > 0:
          print(f"Total belanja Anda adalah Rp {total_belanja}.")

        else:
          print("Belum ada transaksi")


# In[ ]:





# In[ ]:




