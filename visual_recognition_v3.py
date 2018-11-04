from __future__ import print_function
import json
from os.path import abspath
from watson_developer_cloud import VisualRecognitionV3, WatsonApiException
import os

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    url='https://gateway.watsonplatform.net/visual-recognition/api',
    iam_apikey='_rTi9ExzLh2F_cNt6NRksfQz_sAJ7NhdlXchff5poiF0')

def visRec():
    clothes = []
    filelist = os.listdir("assets/images/")
    thinking = 0
    for i in filelist:
        if thinking == 5:
            print("...")
            thinking = 0
        else:
            thinking += 1


        if i.endswith(".jpg") or i.endswith(".jpeg"):
            with open("assets/images/" + i, 'rb') as images_file:
                classes = visual_recognition.classify(
                    images_file,
                    threshold='0.5',
                    classifier_ids='DefaultCustomModel_2095219532').get_result()
                thisItem = classes['images'][0].get('classifiers')[0].get('classes')
                if len(thisItem) > 1:
                    tempMax = 0
                    thing = {}
                    for d in thisItem:
                        tempMax = max(tempMax, d['score'])
                        if tempMax == d['score']:
                            tempMaxItem = d
                    thisItem = [tempMaxItem]
                thisItem = thisItem[0].get('class')
                #print("visRec evaluated " + i + " as a(n) " + thisItem)
                clothes.append({"assets/images/" + i: thisItem})
    return clothes
