import os
import subprocess
def headerPrint():
    print("""
     _   _            _                  _              _       _ _ 
    | |_| |_  __ _ __| |___ _ __    __ _| |  _ __  __ _| |_  __| (_)
    | / / ' \/ _` / _` / -_) '  \  / _` | | | '  \/ _` | ' \/ _` | |
    |_\_\_||_\__,_\__,_\___|_|_|_| \__,_|_| |_|_|_\__,_|_||_\__,_|_|
                                                                    
                   _        __ _         _         
     _ __  _____ _(_)___   / _(_)_ _  __| |___ _ _ 
    | '  \/ _ \ V / / -_) |  _| | ' \/ _` / -_) '_|
    |_|_|_\___/\_/|_\___| |_| |_|_||_\__,_\___|_|  
                                                   
    thanks to movie-map :)
    
    youtube = btly.ir/google
    telegram = @khodekhadem
    instagram = khodekhadem
    """
    )   



headerPrint()
movieName = input("""
enter movie  name 
you have to enter exact name
----------------------------
esm film ro vared kon
esm ro bayad kamel va daghigh vared konid

""")

output = subprocess.check_output( "curl https://www.movie-map.com/"+movieName , shell=True)
output = output.decode("utf-8")
classPlace = output.rfind("class=S ")+12

if(output.find( "Lost in Space. How did you get here?") != -1 ):
    os.system("clear")
    headerPrint()
    print("""





    nothing found please check your movie name it have to be the exact name of movie
----------------------------------------------------------
chizi peyda nakardam , shayad to vared kardan esm film ghalat emlaee dashti , bayad esm film ro kamel va daghigh vared koni  
            """)
    exit()

moviNum = output.find( ">"  , classPlace )
moviNum = output[classPlace:moviNum]


os.system("clear")
headerPrint()
for i in range (int(moviNum)+1):
    searchStr = "class=S id=s"+str(i)
    ST = output.find(searchStr)
    print(    output[ ST+len(searchStr) : output.find("</a>",ST) ]   )

