import os
import pandas as pd
from os.path import join, exists





def norm_organism(orgname):
    '''
    Return abbreviated organism name
    '''
    orgname = orgname.replace('[', '').replace(']', '')

    # two organisms occur twice, deal with these special cases
    if orgname == 'Metschnikowia matae var. maris':
        return 'metschnikowia_matae_maris'

    elif orgname == 'Nadsonia fulvescens var. elongata':
        return 'nadsonia_fulvescens_var_elongata'

    # now parse filename for the others
    if orgname.startswith('yH'):
        organism = '_'.join(orgname.split()[1:3]).lower().replace('.', '')
    else:
        organism = '_'.join(orgname.split()[:2]).lower().replace('.', '')

    return organism



def norm_filename(filename):
    '''
    Return abbreviated organism name
    '''
    filename = filename.replace('[', '').replace(']', '')

    # two organisms occur twice, deal with these special cases
    if filename == 'metschnikowia_matae_maris.max.pep':
        return 'metschnikowia_matae_maris'

    elif filename == 'nadsonia_fulvescens_var_elongata.max.pep':
        return 'nadsonia_fulvescens_var_elongata'

    # now parse filename for the others
    if filename.startswith('yH'):
        file = '_'.join(filename.split('.')[0].split('_')[1:3]).lower()
    else:
        file = '_'.join(filename.split('.')[0].split('_')[:2]).lower()

    return file



def get_from_tempo_files(wanted_orgs):

    filepath = 'fasta'

    files = os.listdir(filepath)

    orgs_found = set([])
    for fi in files:

        if fi.endswith('.pep') or fi.endswith('.fasta'):

            norm_org = norm_filename(fi)

            if norm_org in wanted_orgs:
                orgs_found.add(norm_org)

                all_info[norm_org] = {}
                all_info[norm_org]['fasta'] = join(filepath, fi)

    return orgs_found


# make folder if needed
outpath = 'results'
if not exists(outpath):
    os.makedirs(outpath)


# collecte info for which file is where
all_info = {}



# load up the data
genome_data = pd.read_csv('332_yeast_genomes.csv', sep='\t')

# normalize the organism names
genome_data['organism'] = genome_data.apply(lambda row: norm_organism(row['Species name']),axis=1)

# get a list of all organisms
all_orgs = set([norm_organism(s) for s in genome_data['organism'].tolist()])



tempo_orgs_found = get_from_tempo_files(all_orgs)

tempo_orgs_not_found = all_orgs - tempo_orgs_found

print('Orgs with tempo genomes: ', len(tempo_orgs_found))
print('Orgs without genomes: ', len(tempo_orgs_not_found))



missing_subset = genome_data[genome_data['organism'].isin(tempo_orgs_not_found)]

all_orgs_alt_names = set([])
for org in missing_subset['old_species_id'].tolist():
    all_orgs_alt_names.add(norm_filename(org))



tempo2_orgs_found = get_from_tempo_files(all_orgs_alt_names)

tempo2_orgs_not_found = all_orgs_alt_names - tempo2_orgs_found

print('Orgs with tempo genomes: ', len(tempo2_orgs_found))
print('Orgs without genomes: ', len(tempo2_orgs_not_found))



# run signalP on all genomes
for org in sorted(all_info.keys(), reverse=True)[150:]:
    fasta_file = all_info[org]['fasta']
    signalp_outfile = join(outpath, org+'.out')


    if not exists(signalp_outfile):

        mycmd = './signalp -fasta %s -org euk -format short -stdout > %s' % (fasta_file, signalp_outfile)
        print(mycmd)
        os.system(mycmd)

    all_info[org]['signalp_out'] = signalp_outfile


print('Done')
