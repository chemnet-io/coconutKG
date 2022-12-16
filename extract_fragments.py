import json
from tqdm import tqdm

f = open('cocojson/original/coconut_02.json')

data = json.load(f)
fragments_dict = {}

idx = 0

for i in tqdm(data):

    for k, v in i.items():

        if k == '_id':

            compound_id = v['$oid']

        if k == 'uniqueNaturalProduct':
            fragments_dict[idx] = {}
            fragments_dict[idx]['id'] = compound_id
            fragments_dict[idx]['fragments'] = []
            fragments_dict[idx]['fragmentsWithSugar'] = []
            fragments_dict[idx]['ertlFunctionalFragments'] = []
            fragments_dict[idx]['ertlFunctionalFragmentsPseudoSmiles'] = []

            if 'fragments' in v:
                for frag, frag_int in v['fragments'].items():
                    fragments_dict[idx]['fragments'].append(frag + ':' + str(frag_int))

            if 'fragmentsWithSugar' in v:
                for frag, frag_int in v['fragmentsWithSugar'].items():
                    fragments_dict[idx]['fragmentsWithSugar'].append(frag + ':' + str(frag_int))

            if 'ertlFunctionalFragments' in v:
                for frag, frag_int in v['ertlFunctionalFragments'].items():
                    fragments_dict[idx]['ertlFunctionalFragments'].append(frag + ':' + str(frag_int))

            if 'ertlFunctionalFragmentsPseudoSmiles' in v:
                for frag, frag_int in v['ertlFunctionalFragmentsPseudoSmiles'].items():
                    fragments_dict[idx]['ertlFunctionalFragmentsPseudoSmiles'].append(frag + ':' + str(frag_int))

    idx += 1

with open("coconut_fragments_02.json", "w") as outfile:
    json.dump(fragments_dict, outfile)
