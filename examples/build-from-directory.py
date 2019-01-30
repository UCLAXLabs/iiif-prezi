"""iiif-prezi example code to build a manifest from a directory of images

"""

#from iiif_prezi.factory import ManifestFactory
from factory import ManifestFactory
import os

# folder div for Cantaloupe server is | (urlencoded %7C)
base_dir = "/usr/local/share/images/"
collection_id = "uclaeal_wahon_B11_bib1563926" # No trailing slash
images_subdir = ""
if (images_subdir != ""):
  images_target = os.path.join(collection_id, images_subdir)
else:
  images_target = collection_id

#if (prefix_subpath != ""):
#  images_target = os.path.join(prefix_subpath, images_target)
  
folder_div = '%7C'
#folder_div = '/'
images_prepath = "wahon" # Need to add folder_div when used with Cantaloupe

images_uri = "https://marinus.library.ucla.edu/cantaloupe-4.0.1/iiif/2/" + images_prepath + folder_div
manifest_uri = "https://marinus.library.ucla.edu/iiif/" + images_prepath
image_dir = os.path.join(base_dir, images_prepath, images_target)
#image_dir = base_dir + images_prepath + images_target
manifest_label = images_target.replace("/", "_")
prezi_dir = "."

fac = ManifestFactory()
fac.set_debug("error")
fac.set_base_image_uri(images_uri + images_target.replace("/", folder_div) + folder_div)
#fac.set_base_image_uri(images_uri + images_target.replace("/", folder_div) + folder_div)
fac.set_base_image_dir(image_dir)
fac.set_iiif_image_info()
fac.set_base_prezi_uri(os.path.join(manifest_uri, collection_id))

fac.set_base_prezi_dir(prezi_dir)

mflbl = manifest_label.replace("_", " ").title()

#mfst = fac.manifest(label=mflbl, ident=manifest_label)
mfst = fac.manifest(label=mflbl, ident="manifest")
seq = mfst.sequence()
for fn in sorted(os.listdir(image_dir)):
    #ident = fn[:-4]
    ident = fn
    ident = fn.replace("+", "%2B")
    title = ident.replace("_", " ").title()
    cvs = seq.canvas(ident=ident, label=title)
    cvs.add_image_annotation(ident, True)

mfst.toFile(compact=False)
