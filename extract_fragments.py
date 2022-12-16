import json
from tqdm import tqdm

f = open('cocojson/original/coconut.json')

data = json.load(f)
fragments_dict = {}

for i in tqdm(data):
    for k, v in i.items():

        if k == '_id':
            compound_id = v['$oid']

        if k == 'uniqueNaturalProduct':
            fragments_dict[compound_id] = {}
            fragments_dict[compound_id]['id'] = compound_id
            fragments_dict[compound_id]['fragments'] = []
            fragments_dict[compound_id]['fragmentsWithSugar'] = []
            fragments_dict[compound_id]['ertlFunctionalFragments'] = []
            fragments_dict[compound_id]['ertlFunctionalFragmentsPseudoSmiles'] = []

            if 'fragments' in v:
                for frag, frag_int in v['fragments'].items():
                    fragments_dict[compound_id]['fragments'].append(frag + ':' + str(frag_int))

            if 'fragmentsWithSugar' in v:
                for frag, frag_int in v['fragmentsWithSugar'].items():
                    fragments_dict[compound_id]['fragmentsWithSugar'].append(frag + ':' + str(frag_int))

            if 'ertlFunctionalFragments' in v:
                for frag, frag_int in v['ertlFunctionalFragments'].items():
                    fragments_dict[compound_id]['ertlFunctionalFragments'].append(frag + ':' + str(frag_int))

            if 'ertlFunctionalFragmentsPseudoSmiles' in v:
                for frag, frag_int in v['ertlFunctionalFragmentsPseudoSmiles'].items():
                    fragments_dict[compound_id]['ertlFunctionalFragmentsPseudoSmiles'].append(frag + ':' + str(frag_int))

with open("coconut_fragments.json", "w") as outfile:
    json.dump(fragments_dict, outfile)
