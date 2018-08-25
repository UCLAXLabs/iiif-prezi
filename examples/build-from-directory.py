"""iiif-prezi example code to build a manifest from a directory of images

"""

from iiif_prezi.factory import ManifestFactory
#from factory import ManifestFactory
import os

# folder div for Cantaloupe server is | (urlencoded %7C)
folder_div = '%7C'
# folder_id = '/'
base_dir = "/var/www/cantaloupe/images/"
# No trailing slash
collection_id = "toganoo"
images_subdir = "7"
if (images_subdir != ""):
  images_target = os.path.join(collection_id, images_subdir)
else:
  images_target = collection_id
images_uri = "http://164.67.17.127:8080/cantaloupe-4.0/iiif/2/"
manifest_uri = "http://164.67.17.127/images/"
image_dir = base_dir + images_target
manifest_label = images_target.replace("/", "_")
prezi_dir = "."

fac = ManifestFactory()
fac.set_debug("error")
fac.set_base_image_uri(images_uri + images_target.replace("/", folder_div) + folder_div)
fac.set_base_image_dir(image_dir)
fac.set_iiif_image_info()
fac.set_base_prezi_uri(os.path.join(manifest_uri, collection_id))
fac.set_base_prezi_dir(prezi_dir)

mflbl = manifest_label.replace("_", " ").title()

mfst = fac.manifest(label=mflbl, ident=manifest_label)
seq = mfst.sequence()
for fn in sorted(os.listdir(image_dir)):
    #ident = fn[:-4]
    ident = fn
    title = ident.replace("_", " ").title()
    cvs = seq.canvas(ident=ident, label=title)
    cvs.add_image_annotation(ident, True)

mfst.toFile(compact=False)
