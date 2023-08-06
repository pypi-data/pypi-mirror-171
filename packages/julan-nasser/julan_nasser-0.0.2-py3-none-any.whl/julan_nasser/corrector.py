#%%
from julan_nasser import io_handler
from julan_nasser.proj_config import config
from julan_nasser.string_manipulator import StringManipulator
from julan_nasser.models.n_gram import NGramModel
from julan_nasser.preprocess import Preprocessor

class Corrector:
    
    def __init__(self):
        self.vocabs = io_handler.load_dict_file(config['vocab_freqs'])
        self.model = NGramModel()
        self.model.load_model()
        self.processor = Preprocessor()
    
    def is_known(self, txt):
        return txt in self.vocabs
    
    def get_most_likely_edit(self, edits, num = 1):
        return sorted(edits, key = lambda item: item[1], reverse=True)[:num]

    def rank_edits1(self, txt, num = 1):
        str_manipulator = StringManipulator(txt)
        edits = str_manipulator.get_edits1()
        edits = [(edit, self.vocabs[edit]) for edit in edits if self.is_known(edit)]
        return self.get_most_likely_edit(edits, num)
    
    def rank_edits2(self, txt, num = 1):
        str_manipulator = StringManipulator(txt)
        edits = str_manipulator.get_edits2()
        edits = [(edit, self.vocabs[edit]) for edit in edits if self.is_known(edit)]
        return self.get_most_likely_edit(edits, num)

    def spell_correct(self, txt, num = 5):
        return self.is_known(txt) or self.rank_edits1(txt, num) or self.rank_edits2(txt, num) or txt
    
    def get_possible_fixes(self, txt, num = 5):
        return self.rank_edits1(txt, num) + self.rank_edits2(txt, num) or txt
    
    def rank_possibilities(self, context, possible_fixes):
        context = ' '.join(context).strip()
        ranks = {}
        for fix, freq in possible_fixes:
            ranks[fix] = self.model.estimate_probability(fix, context)
        res = sorted(ranks, key = ranks.get, reverse=True)[0]
        return res

    def contextual_correct(self, txt):
        tokens = self.processor.tokenize(txt)
        correct_tokens = []
        for token in tokens:
            if not self.is_known(token):
                possible_fixes = self.get_possible_fixes(token, 5)
                if possible_fixes != token:
                    fix = self.rank_possibilities(correct_tokens, possible_fixes)
                    correct_tokens.append(fix)
                else:
                    correct_tokens.append(token)
            else:
                correct_tokens.append(token)
        return ' '.join(correct_tokens).strip()
    def correctFile(self, input, output):
        with open(input, "r", encoding="utf-8") as f:
            content = f.read()
        corrected = self.contextual_correct(content)
        with open(output, "w", encoding="utf-8") as f:
            f.write(corrected)

if __name__ == '__main__':
    corr = Corrector()
    sent = 'أكدت قواءص التمذد في تشاد أنها تواضضل طريقها للعاحمة'
    print(corr.contextual_correct(sent))
    sent = 'اتتنتهى حدث آبل المنتظو بالإعلاخ عن مموعة من المنتجات'
    print(corr.contextual_correct(sent))
# %%
