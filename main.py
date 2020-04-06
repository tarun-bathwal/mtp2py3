import sys
import json
import numpy as np 
import pickle

from model import Model
from corpus import Corpus

def main():

    QAfile 	   		    = sys.argv[1]
    ReviewFile 		    = sys.argv[2]
    minReview  		    = int(sys.argv[3])
    V                   = int(sys.argv[4])
    k		   	        = int(sys.argv[5])
    numiter	   		    = int(sys.argv[6])
    Lambda			    = float(sys.argv[7])
    predictionsOut 	    = sys.argv[8]
    rankingOut 		    = sys.argv[9]
    create_corpus       = sys.argv[10]# takes zero and 1 as args
    corpus_pickle_file  = "./Data/corpus_{}.pkl".format(QAfile.split("/")[-1].split(".")[0])

    if x:
        corpus = Corpus(QAfile, ReviewFile, minReview,V)
        corpus.construct_QAnswersAndQPerItem()
        corpus.construct_SentencesAndSPerItem()
        corpus.Calculate_PairWiseFeature()
        with open(corpus_pickle_file,'wb') as f:
            pickle.dump(corpus,f)
    else:
        with open(corpus_pickle_file,'rb') as f:
                corpus = pickle.load(f) 

    print("corpus is available")
    print(("Vocabulary Size: " + str(corpus.Map.V)))
    print(("Number of Questions: " + str(len(corpus.QAnswers))))
    print(("Number of Reviews: " + str(len(corpus.Sentences))))
    print(("Number of Items " + str(len(corpus.Map.ItemIDMap))))
    print(("Avg review length " + str(sum(corpus.Avgdl.values())/len(corpus.Avgdl))))

    # model	  	= Model(k, numiter, Lambda, corpus)

    # sess = model.train_model()

    # print("\nModel is trained and optimal model loaded!\n")

    # valid_accuracy, test_accuracy, topRanked 	= model.valid_test_perf(sess)

    # if (predictionsOut):
    #     model.save_predictions(topRanked, predictionsOut)

    # if (rankingOut):
    #     topRanked = model.top_ranked(sess, 3)
    #     model.save_top_ranked(topRanked, rankingOut)

    # print("Predictions are saved\n")

    # valid_AUC, test_AUC	= model.AUC(sess)

    # print("-----------------------------------------------")
    # print("----------------------------------------------\n")
    # print("Accuracy: ")
    # print(("\tValidation: "+str(valid_accuracy)))
    # print(("\tTest: "+str(test_accuracy)))
    # print("\n")
    # print("AUC: ")
    # print(("\tValidation: "+str(valid_AUC)))
    # print(("\tTest: "+str(test_AUC)))
    # print("\n")
    # print("-----------------------------------------------")
    # print("----------------------------------------------\n")

if __name__ == "__main__":
    main()
