from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
# Creating ChatBot Instance
CB = ChatBot('UNS Bot')
 # Training with Personal Ques & Ans

CB = ChatBot(
    'ChatBot untuk Informasi Akademis',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Kamu mau cari info apa?😃<br><br> 1.&emsp;Kurikulum</br> 2.&emsp;Beasiswa</br>3.&emsp;MBKM</br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'   
) 
trainer = ListTrainer(CB)

conversation = [    
    "Hai",
    "Halo!",
    "Hey",

    "Apa kabarmu?",
    "Aku Baik kok, makasih 😃✨</br> <br>"
    "Mau cari info apa nih? 😃✨<br><br>1.&emsp;Kurikulum.</br>2.&emsp;Beasiswa.</br> 3.&emsp;MBKM</br>",

    "Luar biasa",
    "Mau cari info apa nih? 😃✨ <br><br>1.&emsp;Kurikulum.</br>2.&emsp;Beasiswa.</br> 3.&emsp;MBKM</br>",

    "sehat",
    "Mau cari info apa nih? 😃✨ <br><br>1.&emsp;Kurikulum.</br>2.&emsp;Beasiswa.</br> 3.&emsp;MBKM</br>",

    "mantab",
    "Mau cari info apa nih? 😃✨ <br><br>1.&emsp;Kurikulum.</br>2.&emsp;Beasiswa.</br> 3.&emsp;MBKM</br>",

    "Makasih",
    "Sama-sama 😄",

    "Thanks",
    "Your Welcome 😄",

    "Bye",
    "Sampai Jumpa👋",

    "Siapa kamu?",
    "Aku adalah bot yang akan ngasih info seputar akademik di FMIPA UNS.",
        
        "1",
        "KURIKULUM<br>Masukkan pilihan sesuai prodi anda : <br> <br> 1.1 Informatika <br>1.2  Fisika<br>1.3  Statistika<br>1.4 Biologi <br>1.5 Kimia",
        
        "1.1",
        "Untuk melihat kurikulum Prodi Informatika, 👉 <a href=" 'https://if.mipa.uns.ac.id/akademik/kurikulum/' ">Klik disini</a>",

        "1.2",
        "Untuk melihat kurikulum Prodi Fisika, 👉 <a href=" 'https://fisika.mipa.uns.ac.id/kurikulum' ">Klik disini</a>",

        "1.3",
        "Untuk melihat kurikulum Prodi Statistika, 👉 <a href=" 'https://statistika.mipa.uns.ac.id/akademik/kurikulum/' ">Klik disini</a>",

        "1.4",
        "Untuk melihat kurikulum Prodi Biologi, 👉 <a href=" 'https://mipa.uns.ac.id/program-sarjana/biologi/' ">Klik disini</a>",

        "1.5",
        "Untuk melihat kurikulum Prodi Kimia, 👉 <a href=" 'https://kimia.mipa.uns.ac.id/id/?page_id=16' ">Klik disini</a>",

        "2",
        "BEASISWA<br>Berikut adalah daftar beasiswa yang tersedia: </br></br>2.1 Djarum Beasiswa Plus<br>2.2  BCA Finance Peduli<br>2.3  BRIlian Scholarship ",
        
        "2.1",
        "Info Lengkap Djarum Beasiswa Plus silakan 👉 <a href=" 'https://djarumbeasiswaplus.org/' ">Klik disini</a>",

        "2.2",
        "Info Lengkap Beasiswa BCA Finance Peduli silakan 👉 <a href=" 'https://bcafinance.co.id/berita-program-beasiswa-bca-finance-peduli-2022' ">Klik disini</a>",
    
        "2.3",
        "Info Lengkap Beasiswa BRI Brilian Scholarship silakan 👉 <a href=" 'https://e-recruitment.bri.co.id/beasiswabrilian/' ">Klik disini</a>",
       
    
        "3",
        " INFO MBKM<br>Silakan pilih mode MBKM: </br></br>3.1 Studi Independen<br>3.2  Magang" ,

        "3.1",
        "Studi Independen<br>Berikut adalah daftar Studi Independen yang tersedia: </br></br>3.1.1 Startup Campus<br>3.1.2  Bangkit Academy<br>3.1.3 Dicoding",
        
        "3.1.1",
        "Info Lengkap Studi Independen Startup Campus silakan 👉 <a href=" 'https://startupcampus.id/' ">Klik disini</a>",
        
        "3.1.2",
        "Info Lengkap Studi Independen Bangkit Academy silakan 👉 <a href=" 'https://grow.google/intl/id_id/bangkit/' ">Klik disini</a>",
        
        "3.1.3",
        "Info Lengkap Studi Independen Dicoding silakan 👉 <a href=" 'https://www.dicoding.com/' ">Klik disini</a>",

        "3.2",
        "Magang<br>Berikut adalah daftar Magang yang tersedia: </br></br>3.2.1 Bukalapak Internship<br>3.2.2  Tokopedia Internship<br>3.2.3 Shopee Internship",
        
        "3.2.1",
        "Info Lengkap Magang di Tokopedia silakan 👉 <a href=" 'https://www.tokopedia.com/internship' ">Klik disini</a>",
        
        "3.2.2",
        "Info Lengkap Magang di Bukalapak silakan 👉 <a href=" 'https://www.bukalapak.com/dev-camp/' ">Klik disini</a>",
        
        "3.2.3",
        "Info Lengkap Magang di Shopee silakan 👉 <a href=" 'https://www.shopee.com/dev-camp/' ">Klik disini</a>",
        

]

trainer.train(conversation)
# # Training with Indonesian Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(CB)
trainer_corpus.train('chatterbot.corpus.indonesia')
