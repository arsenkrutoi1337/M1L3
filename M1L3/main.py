import os
import random

@app.route("/ПУТЬ")
def eco():
     images=os.listdir('images')
     img_name=random.choice(images)
    
       