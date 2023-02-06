# Training
Due to Github's upload capacity limit, you must download the dataset from outside to reproduce model learning.

## Dataset preparation
**1. Download STRING DB**
- protein network data (full network, scored links between proteins)
- species: Homo sapiens
- https://stringdb-static.org/download/protein.links.v11.5/9606.protein.links.v11.5.txt.gz
- Convert to all.edgelist using 1. conversion jupyter notebook file.

**2. Download Therapeutic Target Database(TTD)**
 - Target Information Downloads
 - Download Uniprot IDs for successful targets only
 - https://db.idrblab.net/ttd/sites/default/files/ttd_database/P2-02-TTD_uniprot_successful.txt

**3. Conversion of identifiers using bioDBnet**
 - The TTD database from step 2 is used as input.
 - Input: UniProt Entry name
 - Output: Ensemble protein ID
 - https://biodbnet-abcc.ncifcrf.gov/db/db2db.php
 - This is the first input file of the autotarget Jupyter notebook file.

**4. Node2Vec**
- Embedding each protein node of the STRING DB in step 1.
- https://github.com/snap-stanford/snap/tree/master/examples/node2vec
- ./node2vec -i:graph/all.edgelist -o:emb/p10q5.emb -l:3 -d:24 -p:10 -q:0.5 -dr -v
- Output file is the second input file(p10q5.emb) of the autotarget jupyter notebook file.

## Training
1. Just run the autotarget jupyter notebook files in order from the top.
