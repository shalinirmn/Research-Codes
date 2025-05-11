# from automate_ibab import *

# PACKAGE CONTENTS

import os
import pandas as pd
import numpy as np

def get_pdb_file_paths(pdb_folder):
    pdb_file_paths = []
    
    # Walk through all directories and subdirectories
    for dirpath, dirnames, filenames in os.walk(pdb_folder):
        for filename in filenames:
            if filename.endswith('.pdb'):
                # Construct the full file path and add it to the list
                pdb_file_paths.append(os.path.join(dirpath, filename))
    
    return pdb_file_paths

def get_helices(file_path):

    with open(file_path, "r") as file:
        pdb_contents = file.read()

    i_stat_0 = pdb_contents.index('SEQRES')
    templis = pdb_contents[i_stat_0:].split('HELIX')

    helices = []
    for i in range(len(templis)):
        if i != 0:
            helices.append(templis[i])
    

    tem = helices[0].split(' ')
    for i in tem:
        if i == '':
            tem.remove('')

    startlis = [tem[3],tem[4],tem[7]]

    coord_list = pd.DataFrame([startlis], columns=['Chain', 'Start_in', 'End_in'])
    for i in helices[1:]:

        n = len(helices[0])
        tem2 = i[0:n+1].split(' ')

        for j in tem2:
            if j == '':
                tem2.remove('')

        new_row = [tem2[3],tem2[4],tem2[7]]
        coord_list.loc[len(coord_list)] = new_row

    
    i_stat = pdb_contents.index('SCALE1')

    atom_lis1 = pdb_contents[i_stat:].split('\n')
    atom_lis2 = []


    for i in atom_lis1:

        if 'ATOM' in i:
            atom_lis2.append(i)

    chain_lis = []
    ind_lis = []

    for i in atom_lis2:
        try:
            chain_lis.append(i.split()[4])
            ind_lis.append(int(i.split()[5]))
        except:
            chain_lis.append(i.split()[3])
            ind_lis.append(int(i.split()[4]))

    chain_uniq = coord_list['Chain'].unique().tolist()


    pdb_exp_hel = []

    for i in range(len(coord_list)):
        
        txt = ''
        chain = coord_list['Chain'][i]
        st = int(coord_list['Start_in'][i])
        ed = int(coord_list['End_in'][i])

        ind_lis2 = []
        chain_lis2 = []
        atom_lis3 = []
        for k in range(len(ind_lis)):
            if chain == chain_lis[k]:
                ind_lis2.append(ind_lis[k])
                chain_lis2.append(chain_lis[k])
                atom_lis3.append(atom_lis2[k])


        for j in range(len(ind_lis2)):
            
            if ind_lis2[j] in range(st,ed+1):
                txt = txt + atom_lis3[j] + '\n'
            else:
                pass

            if ind_lis2[j] == ed+2:
                break

        txt = txt + 'TER'


        pdb_exp_hel.append(txt)

    return pdb_exp_hel


def create_dir(directory_path, folder_name):
    # Construct the full path for the new folder
    new_folder_path = os.path.join(directory_path, folder_name)
    
    # Create the new folder
    try:
        os.makedirs(new_folder_path, exist_ok=True)
        print(f"Folder '{folder_name}' created successfully at '{directory_path}'")
    except Exception as e:
        print(f"An error occurred while creating the folder: {e}")


def save_helices(pdb_exp_hel,folder_path):
    for i in range(len(pdb_exp_hel)):
        file_path = folder_path + "\helix_" + str(i+1) + ".pdb"

        with open(file_path, "w") as file:
            file.write(pdb_exp_hel[i])

pdb_folder = r"C:\Users\Snehil\OneDrive\Desktop\newpdb"
pdb_files = get_pdb_file_paths(pdb_folder)
create_dir(pdb_folder, 'Helices')
helix_file_names = []

for i in pdb_files:
    helix_file_names.append(i.split('\\')[-1].split('.')[0])
error_files = []
for i in range(len(pdb_files)):


    try:
        create_dir(pdb_folder + "\Helices",helix_file_names[i])
        
        pdb_exp_hel = get_helices(pdb_files[i])

        save_helices(pdb_exp_hel, pdb_folder + f"\Helices\{helix_file_names[i]}")
    except:
        print(pdb_files[i])
        error_files.append(pdb_files[i])

error_files


