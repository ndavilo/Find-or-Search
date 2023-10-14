import os
import string
import platform

search = input("Enter the file you wish to search for(with extention): ")

if platform.system() == "windows":
    # get the windows drives avaliable 
    drvs = string.ascii_uppercase
    drvs_list = []
    for letter in drvs:
        if os.path.exists("%s:\\" % letter):
            #            print ("%s:" %letter)
            try:
                with open('%s:\\' % (letter), 'r') as f:
                    pass
            except IOError:
                continue
            
            drvs_list.append(letter + ":\\")
        for drv in drvs_list:
            for dirs, subdirs, files in os.walk(drv):
                for file in files:
                    if file == search:
                        print(os.path.join(dirs, file))

else:
    for dirs, subdirs, files in os.walk("/"):
        for file in files:
            if file == search:
                print(os.path.join(dirs, file))
                    
                
                
        
        
                    
                