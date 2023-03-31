import json
from tqdm import tqdm

f = open('cocojson/original/coconut.json')

data = json.load(f)

fragments_list = []
fragments_dict = {}

for i in tqdm(data):

    for k, v in i.items():

        if k == '_id':

            compound_id = v['$oid']

        if k == 'uniqueNaturalProduct':
            fragments_dict = {}
            fragments_dict['id'] = compound_id
            fragments_dict['fragments'] = []
            fragments_dict['fragmentsWithSugar'] = []
            fragments_dict['ertlFunctionalFragments'] = []
            fragments_dict['ertlFunctionalFragmentsPseudoSmiles'] = []

            if 'fragments' in v:
                for frag, frag_int in v['fragments'].items():
                    fragments_dict['fragments'].append(frag + ':' + str(frag_int))

            if 'fragmentsWithSugar' in v:
                for frag, frag_int in v['fragmentsWithSugar'].items():
                    fragments_dict['fragmentsWithSugar'].append(frag + ':' + str(frag_int))

            if 'ertlFunctionalFragments' in v:
                for frag, frag_int in v['ertlFunctionalFragments'].items():
                    fragments_dict['ertlFunctionalFragments'].append(frag + ':' + str(frag_int))

            if 'ertlFunctionalFragmentsPseudoSmiles' in v:
                for frag, frag_int in v['ertlFunctionalFragmentsPseudoSmiles'].items():
                    fragments_dict['ertlFunctionalFragmentsPseudoSmiles'].append(frag + ':' + str(frag_int))

    fragments_list.append(fragments_dict)

with open("coconut_fragments.json", "w") as outfile:
    json.dump(fragments_list, outfile)
