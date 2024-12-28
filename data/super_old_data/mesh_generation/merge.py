import pymesh as pym
import os
import shutil
from tqdm import tqdm


for _type in ["dex", "lev"]:
    for directory in tqdm(os.listdir(_type)):
        meshes = []

        for off in os.listdir(_type + "/" + directory):
            _mesh = pym.load_mesh(_type + "/" + str(directory) + "/" + str(off))
            meshes.append(_mesh)

        molmesh = pym.merge_meshes(tuple([mesh for mesh in meshes]))
        pym.save_mesh(_type + "/" + directory + ".off", molmesh, ascii=True)
        shutil.rmtree(_type + "/" + directory)

