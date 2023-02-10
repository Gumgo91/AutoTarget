import pandas as pd
import os
pt = os.path.abspath(__file__).replace('autotarget.py', '')
class Searcher():   
    def change_threshold(self, threshold):
        self.threshold = threshold
        self.df = self.df_all.copy()
        self.df['label'] = (self.df['probability'] > threshold) * 1.0
        
    def __init__(self, path=pt + 'data/targets_inference_complete.csv', threshold=0.05):
        self.df_all = pd.read_csv(path, compression='gzip')
        print(f'Loaded {len(self.df_all)} data from file.')
        self.diseases = set(self.df_all['diseaseName'])
        print(f'{len(self.diseases)} disease names were extracted.')
        
        self.change_threshold(threshold) # 0.05: about 90% recall rate
        
    def search_disease(self, keyword):
        keyword = keyword.lower()
        matching = {s for s in self.diseases if keyword in s.lower()}
        print(f"{len(matching)} results")
        return matching
    
    def search(self, keyword, mode='partial', scope='positive'):
        """
        <mode>
        partial
        exact
        
        <scope>
        positive: search only positive(1) label
        negative: search only negative(0) label
        all: search all proteins
        """
        if not(mode in ['partial', 'exact']):
            print("'mode' must be either partial or exact.")
            return
        if not(scope in ['positive', 'negative', 'all']):
            print("'scope' must be positive, negative, or all.")
        
        output = self.df.copy()
        if scope == 'positive':
            output = output[output['label']==1]
        elif scope == 'negative':
            output = output[output['label']==0]
        output = output.reset_index(drop=True)
        
        if mode == 'partial':
            output = output[output['diseaseName'].str.contains(keyword)]
        else:
            output = output[output['diseaseName']==keyword]
        output = output.sort_values('probability', ascending=False)
        output = output[['id', 'probability', 'label', 'Entry', 'Protein names', 'UniProtKB', 'geneName', 'pLI', 'DSI', 'DPI', 'diseaseName']]
        output = output.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=True)
        return output        