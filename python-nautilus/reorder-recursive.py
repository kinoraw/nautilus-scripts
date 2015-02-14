import os, shutil 
        
            
def reorder(ext, folder):            
    #pythonic way to magic:
    for root, dirs, files in os.walk("."):
        for f in files:
            if f.rpartition(".")[2] == ext:
                    os.mkdir(folder)
                    src=os.path.join(root,f)
                    dst=os.path.join(folder,f)
                    shutil.copy(src, dst)


 
reorder("exr", "./exr")
