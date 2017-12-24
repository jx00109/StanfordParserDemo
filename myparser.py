# -*- coding:utf-8 -*-
from nltk.tokenize import StanfordTokenizer
from nltk.tokenize.stanford_segmenter import StanfordSegmenter
from nltk.tag import StanfordPOSTagger
from nltk.parse.stanford import StanfordDependencyParser
from nltk.parse.stanford import StanfordParser
import pickle as pkl

# 英文分词

tokenizer = StanfordTokenizer(path_to_jar=r"D:\stanford-parser-full-2016-10-31\stanford-parser.jar")
#
# sentence2 = "Micron hasn't declared its first quarterly profit for three years, but he has been dead."
# sentence = "Jim Williams director of the US VISIT project said that by the middle of November many arriving passengers in Atlanta will be fingerprinted and photographed"
#
# print(tokenizer.tokenize(sentence2))

# 英文词性标注
# 词性标注的标签说明：http://www.comp.leeds.ac.uk/amalgam/tagsets/upenn.html
# eng_tagger = StanfordPOSTagger(
#     path_to_jar=r"D:\stanford-postagger-full-2016-10-31\stanford-postagger.jar",
#     model_filename=r"D:\stanford-postagger-full-2016-10-31\models\english-bidirectional-distsim.tagger"
# )
# print("词性标注结果", eng_tagger.tag(sentence.split()))

# 句法分析

# eng_parser = StanfordParser(
#     path_to_jar=r"D:\stanford-parser-full-2016-10-31\stanford-parser.jar",
#     path_to_models_jar=r"D:\stanford-parser-full-2016-10-31\stanford-parser-3.7.0-models.jar",
#     model_path=u"edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz"
# )
#
# mylist = list(eng_parser.parse(sentence.split()))
# print(len(mylist))
# print("句法分析结果", mylist)

# 依存句法分析
# 对于依存关系的标签说明：http://universaldependencies.org/u/dep/all.html#al-u-dep/det
eng_dependency_parser = StanfordDependencyParser(path_to_jar=r"D:\stanford-parser-full-2016-10-31\stanford-parser.jar",
                                                 path_to_models_jar=r"D:\stanford-parser-full-2016-10-31\stanford-parser-3.7.0-models.jar",
                                                 model_path=u'edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')

outputs = ' '.join(tokenizer.tokenize("Dole was defeated by Clinton"))
print(outputs)

result = list(eng_dependency_parser.parse(outputs.split()))
for each in result[0].triples():
    print(each)
#     if each[1]=='dobj':
#         # print(each)
#         print(each[0][0])
#         print(each[2][0])
# print("依存句法分析结果:")
# for row in result[0].triples():
#     print(row)
# print(result[0])
# 中文分词
# 还要研究一下，一下代码报错
# chinese_segmenter = StanfordSegmenter(
#     path_to_jar=r"D:\stanford-segmenter-2016-10-31\stanford-segmenter-3.7.0.jar",
#     path_to_slf4j=r"D:\stanford-segmenter-2016-10-31\slf4j-api.jar",
#     path_to_sihan_corpora_dict=r"D:\stanford-segmenter-2016-10-31\data",
#     path_to_model=r"D:\stanford-segmenter-2016-10-31\data\pku.gz",
#     path_to_dict=r"D:\stanford-segmenter-2016-10-31\data\dict-chris6.ser.gz"
# )
# chinese_sentence = u"昨天我喝了点酒，很早就睡了。"
# res = chinese_segmenter.segment(chinese_sentence)
# print(res)
