import subprocess
path=r"C:\\Users\\Jusin M\\Desktop\\grabcut-maskrcnn\\grabcut-maskrcnn"
subprocess.run("python mask_rcnn_grabcut.py --mask-rcnn mask-rcnn-coco --image example.jpg",cwd=path, shell='true')
