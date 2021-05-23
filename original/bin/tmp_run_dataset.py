import os
from glob import glob


pjoin = os.path.join
pexists = os.path.exists
#dataset_name = 'custom_famous_smallnoise'
#dataset_list_filename = dataset_name + '_filelist.txt'

#with open(dataset_list_filename) as dataset_list_file:
#    filelist = dataset_list_file.readlines()


dataset = 'custom_famous_trimesh_nonoise'
recon_scheme = 'poisson'

if recon_scheme == 'poisson':
    recon_folder = '05_recon_poisson'
    executable = 'PoissonRecon --depth 10 --degree 2 --pointWeight 2'
elif recon_scheme == 'ssd':
    recon_folder = '05_recon_ssd'
    executable = 'SSDRecon'
else:
    print(f'unsupported mode {recon_scheme}')
    exit(0)

if not pexists(f'{dataset}/{recon_folder}'):
    os.system(f'mkdir -p {dataset}/{recon_folder}')

filelist = sorted(list(glob(f'{dataset}/04_pts_vis/*_pcpnormal.xyz')))

for filename in filelist:
    #filename = filename[:-1]
    #meshname = f'{dataset_name}/04_pts_vis/{filename}'
    meshname = filename
    _, _, data_id = meshname.split('/')
    data_id = data_id[:-4]
    print(meshname)
    cmd = f"./{executable} --in {meshname} --out {pjoin(dataset, recon_folder, data_id + '.ply')}"
    print(f'EXECUTING {cmd}')
    os.system(cmd)
