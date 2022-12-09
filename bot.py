import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5791998848:AAFx78tuc3mhWIB2vninmzibD4dn9gc_3Wk")

API_ID = int(os.environ.get("API_ID", "26248857"))

API_HASH = os.environ.get("API_HASH", "9ecc044d9b122a351b9d9b6b8ceaa1c4")

STRING = os.environ.get("STRING", "AQB7TnkzG33ebGeNniM90jGAJq258VNvCrRg_j3gfwo1UmJmJ0gx7WwGVmui1CV8mOHVh8YeWca3t2yI44acI81qCPu5I5w01iitW8kMjO3x1ZU2jdyAdHsfUvxojaM5j26bmfbYa2DuTpp7_PZxFISftGoJjlyMl61AQuKaDWr-mfUSZw7uas-XYFiuTcdlOCaJe1J0xvckA60pksJYmSq829GxeMYQIA3j5Fchlw9HDzlpXxxkf2DdGYHzoXK_Vl-gNTCU927gWIJg7CToA2O8_gbPS_gLJrbPoXV5AJ8P_F-Aq0Mdhluh3J4TgxgR6Al3s874aWdZiOU3qGzVMcEOAAAAAU-eBhoA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
