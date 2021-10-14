#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created on: Wed Sep 22 13:19:30 2021
@author: Chris Thompson
@course: INF 6050
@university: Wayne State University
@assignment: 

@pythonVersion: 3.8
@requiredModules:
    
@description: This is a script to...
"""
#####################################
#IMPORT MODULES
#####################################
import requests
from bs4 import BeautifulSoup
import pandas as pd

#####################################
#GLOBAL VARIABLES
#####################################
#Stores lists of characters in page titles that need to be removed or replaced
#in order to access the url to that page
removal = ["– ", "’", '"', '“', "(", ")", "/", ":", "- ", "”", "...", "!", "?", ",",
           "„", "…", "[", "]", "°"]
letterA = ["ą", "ã", "Ã", "ä", "Ä", "å", "Å", "Á", "á", "À", "à", "Â", "â", "ǎ", "Ǎ",
           "ä", "Ä", "ă", "Ă", "ā", "Ā", "ⱥ", "Ⱥ", "ą", "Ą", "ǡ", "Ǡ", "ǻ", "Ǻ", "ǟ",
           "Ǟ", "ǻ", "Ǻ", "ǟ", "Ǟ", "ȁ", "Ȁ", "ȃ", "Ȃ", "ḁ", "Ḁ"]
letterAE = ["æ", "Æ", "ǽ", "Ǽ", "ǣ", "Ǣ"]
letterB = ["ḃ", "Ḃ", "ƀ", "Ƀ", "ḅ", "Ḅ", "ḇ", "Ḇ"]
letterC = ["ç", "Ç", "Ĉ", "ĉ", "č", "Č", "ć", "Ć", "ċ", "Ċ", "ȼ", "Ȼ", "ḉ", "Ḉ"]
letterD = ["ḋ", "Ḋ", "ď", "Ď", "ḑ", "Ḑ", "đ", "Đ", "ḍ", "Ḍ", "ḓ", "Ḓ", "ḏ", "Ḏ"]
letterE = ["è", "É", "é", "È", "ê", "Ê", "ë", "Ë", "ė", "Ė", "ě", "Ě", "ĕ", "Ĕ",
           "ē", "Ē", "ę", "Ę", "ȩ", "Ȩ", "ɇ", "Ɇ", "ḗ", "Ḗ", "ḕ", "Ḕ", "ḝ", "Ḝ",
           "ȅ", "Ȅ", "ȇ", "Ȇ", "ḙ", "Ḙ", "ḛ", "Ḛ"]
letterF = ["ḟ", "Ḟ"]
letterG = ["Ĝ", "ĝ", "ǵ", "Ǵ", "ġ", "Ġ", "ǧ", "Ǧ", "ğ", "Ğ", "ḡ", "Ḡ", "ģ", "Ģ",
           "ǥ", "Ǥ"]
letterH = ["Ĥ", "ĥ", "ḣ", "Ḣ", "ḧ", "Ḧ", "ȟ", "Ȟ", "ḩ", "Ḩ", "ħ", "Ħ", "ḥ", "Ḥ",
           "ḫ", "Ḫ", "ⱨ", "Ⱨ"]
letterI = ["í", "Í", "ì", "Ì", "î", "Î", "ï", "Ï", "ǐ", "Ǐ", "ĭ", "Ĭ", "ī", "Ī",
           "ĩ", "Ĩ", "į", "Į", "ḯ", "Ḯ", "ȉ", "Ȉ", "ȋ", "Ȋ", "ḭ", "Ḭ"]
letterJ = ["Ĵ", "ĵ", "ɉ", "Ɉ"]
letterK = ["ḱ", "Ḱ", "ǩ", "Ǩ", "ķ", "Ķ", "ḳ", "Ḳ", "ḵ", "Ḵ", "ⱪ", "Ⱪ"]
letterL = ["ƚ", "Ƚ", "ĺ", "Ĺ", "ŀ", "Ŀ", "ľ", "Ľ", "ļ", "Ļ", "ł", "Ł", "ḷ", "Ḷ",
           "ḽ", "Ḽ", "ḻ", "Ḻ", "ḹ", "Ḹ"]
letterM = ["ḿ", "Ḿ", "ṁ", "Ṁ", "ṃ", "Ṃ"]
letterN = ["ń", "Ń", "ñ", "Ñ", "ǹ", "Ǹ", "ṅ", "Ṅ", "ň", "Ň", "ņ", "Ņ", "ƞ", "Ƞ",
           "ṇ", "Ṇ", "ṋ", "Ṋ", "ṉ", "Ṉ"]
letterO = ["ø", "Ø", "ô", "Ô", "ó", "Ó", "ò", "Ò", "ö", "Ö", "õ", "Õ", "ȯ", "Ȯ",
           "ǒ", "Ǒ", "ŏ", "Ŏ", "ō", "Ō", "õ", "Õ", "ǫ", "Ǫ", "ő", "Ő", "ṓ", "Ṓ",
           "ṑ", "Ṑ", "ṍ", "Ṍ", "ȱ", "Ȱ", "ȫ", "Ȫ", "ṏ", "Ṏ", "ǿ", "Ǿ", "ȭ", "Ȭ",
           "ǭ", "Ǭ", "ȍ", "Ȍ", "ȏ", "Ȏ"]
letterOE = ["œ", "Œ"]
letterOU = ["ȣ", "Ȣ"]
letterP = ["ṕ", "Ṕ", "ṗ", "Ṗ"]
letterQ = ["ɋ", "Ɋ"]
letterR = ["ŕ", "Ŕ", "ṙ", "Ṙ", "ř", "Ř", "ŗ", "Ŗ", "ɍ", "Ɍ", "ȑ", "Ȑ", "ȓ", "Ȓ",
           "ṛ", "Ṛ", "ṟ", "Ṟ", "ṝ", "Ṝ"]
letterS = ["ß", "ẞ", "ş", "Ŝ", "ŝ", "ś", "Ś", "ṡ", "Ṡ", "š", "Š", "ş", "Ş", "ṥ",
           "Ṥ", "ṧ", "Ṧ", "ṣ", "Ṣ", "ș", "Ș", "ṩ", "Ṩ"]
letterT = ["ṫ", "Ṫ", "ť", "Ť", "ţ", "Ţ", "ṭ", "Ṭ", "ț", "Ț", "ṱ", "Ṱ", "ṯ", "Ṯ",
           "ⱦ", "Ⱦ", "þ", "Þ", "ŧ", "Ŧ"]
letterU = ["ü", "Ü", "ú", "Ú", "ù", "Ù", "û", "Û", "ū", "Ū" "Ǔ", "ǔ", "ŭ", "Ŭ",
           "ũ", "Ũ", "ů", "Ů", "ų", "Ų", "ű", "Ű", "ʉ", "Ʉ", "ǘ", "Ǘ", "ǜ", "Ǜ",
           "ṹ", "Ṹ", "ǚ", "Ǚ", "ṻ", "Ṻ", "ǖ", "Ǖ", "ȕ", "Ȕ", "ȗ", "Ȗ", "ṳ", "Ṳ",
           "ṷ", "Ṷ", "ṵ", "Ṵ"]
letterV = ["ṽ", "Ṽ", "ṿ", "Ṿ"]
letterW = ["ẃ", "Ẃ", "ẁ", "Ẁ", "ẇ", "Ẇ", "ŵ", "Ŵ", "ẅ", "Ẅ", "ẉ", "Ẉ", "ⱳ", "Ⱳ"]
letterX = ["ẋ", "Ẋ", "ẍ", "Ẍ"]
letterY = ["ÿ", "Ÿ", "ý", "Ý", "ỳ", "Ỳ", "ẏ", "Ẏ", "ŷ", "Ŷ", "ȳ", "Ȳ", "ỹ", "Ỹ",
           "ɏ", "Ɏ", "ỷ", "Ỷ", "ỵ", "Ỵ"]
letterZ = ["ž", "Ž", "ź", "Ź", "ż", "Ż", "ẑ", "Ẑ", "ȥ", "Ȥ", "ẓ", "Ẓ", "ẕ", "Ẕ",
           "ⱬ", "Ⱬ"]
#####################################
#USER-DEFINED FUNCTIONS
#####################################
#This function is used to replace characters that need removing in a page title
#It also replaces letters that have accents and other markings with non-accented letters
def remove_characters(string):
    for char in letterA:
        string = string.replace(char, "a")
    for char in letterAE:
        string = string.replace(char, "ae")
    for char in letterB:
        string = string.replace(char, "b")
    for char in letterC:
        string = string.replace(char, "c")
    for char in letterD:
        string = string.replace(char, "d")
    for char in letterE:
        string = string.replace(char, "e")
    for char in letterF:
        string = string.replace(char, "f")
    for char in letterG:
        string = string.replace(char, "g")
    for char in letterH:
        string = string.replace(char, "h")
    for char in letterI:
        string = string.replace(char, "i")
    for char in letterJ:
        string = string.replace(char, "j")
    for char in letterK:
        string = string.replace(char, "k")
    for char in letterL:
        string = string.replace(char, "l")
    for char in letterM:
        string = string.replace(char, "m")
    for char in letterN:
        string = string.replace(char, "n")
    for char in letterO:
        string = string.replace(char, "o")
    for char in letterOE:
        string = string.replace(char, "oe")
    for char in letterOU:
        string = string.replace(char, "ou")
    for char in letterP:
        string = string.replace(char, "p")
    for char in letterQ:
        string = string.replace(char, "q")
    for char in letterR:
        string = string.replace(char, "r")
    for char in letterS:
        string = string.replace(char, "s")
    for char in letterT:
        string = string.replace(char, "t")
    for char in letterU:
        string = string.replace(char, "u")
    for char in letterV:
        string = string.replace(char, "v")
    for char in letterW:
        string = string.replace(char, "w")
    for char in letterX:
        string = string.replace(char, "x")
    for char in letterY:
        string = string.replace(char, "y")
    for char in letterZ:
        string = string.replace(char, "z")
    for char in removal:
        string = string.replace(char,"")
        string = string.replace("¶", "to")
        string = string.replace("&", "and")    
        string = string.replace(" ", "-").lower()
    return string

#####################################
#RUN SCRIPT
#####################################
if __name__ == "__main__":
    #This for loop iterates through the first page of reviews on AMG
    for x in range(0, 10):
        amgPage1 = requests.get("https://www.angrymetalguy.com/category/reviews/", headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"})
        amgSoup1 = BeautifulSoup(amgPage1.content, 'html.parser')
        #Extracts web page title in order to gain access to web page. 
        amgPageTitle = amgSoup1.select('h2')[x].text
        #Removes unwanted characters and replaces accented letters for use to access web page
        for s in amgPageTitle:
            s = remove_characters(amgPageTitle)
            amgPageTitle = s
        #Save the review page url in a variable    
        url = 'https://www.angrymetalguy.com/%s' %amgPageTitle
        #Request access to the web page of a specific review
        try:
            amgPage = requests.get(url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"})
        except:
            print(amgPageTitle, "gives an error.")
        amgSoup = BeautifulSoup(amgPage.content, 'html.parser')   
        #Finds the desired contents of the web page.
        amgReview = amgSoup.select("h1")[0].text
        try:
            amgAuthor = amgSoup.select("div.entry-meta")[0].text
            amgRating1 = amgSoup.select("p")[6].text
            amgRating2 = amgSoup.select("p")[7].text
            amgRating3 = amgSoup.select("p")[8].text
        except:
            print(amgPageTitle, "gives an error.")
        else:
            print(amgPageTitle, "works.")
        #Save data to a DataFrame and then a csv
        amg = pd.DataFrame({"Review": amgReview, "Author": amgAuthor, "Rating1": amgRating1, "Rating2": amgRating2, "Rating3": amgRating3}, index=[0])
        amg.to_csv('amg_reviews.csv', index=False, encoding='utf-8', mode = 'a', header = None)
    #New for loop in order to access the successive review pages on AMG    
    for y in range(2, 533):
        amgPage1 = requests.get("https://www.angrymetalguy.com/category/reviews/page/%s" %y, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"})
        amgSoup1 = BeautifulSoup(amgPage1.content, 'html.parser')
        #This for loop iterates through the each page of reviews on AMG
        for x in range(0, 10):
            amgPageTitle = amgSoup1.select('h2')[x].text
            #Removes unwanted characters and replaces accented letters for use to access web page
            for s in amgPageTitle:
                s = remove_characters(amgPageTitle)
                amgPageTitle = s
            #Save the review page url in a variable 
            url = 'https://www.angrymetalguy.com/%s' %amgPageTitle
            #Request access to the web page of a specific review
            try:
                amgPage = requests.get(url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"})
            except:
                print(amgPageTitle, "gives an error.")
            amgSoup = BeautifulSoup(amgPage.content, 'html.parser')   
            #Finds the desired contents of the web page.
            amgReview = amgSoup.select("h1")[0].text
            try:
                amgAuthor = amgSoup.select("div.entry-meta")[0].text
                amgRating1 = amgSoup.select("p")[6].text
                amgRating2 = amgSoup.select("p")[7].text
                amgRating3 = amgSoup.select("p")[8].text
            except:
                print(amgPageTitle, "gives an error.")
            else:
                print(amgPageTitle, "works.")
            #Save data to a DataFrame and then a csv
            amg = pd.DataFrame({"Review": amgReview, "Author": amgAuthor, "Rating1": amgRating1, "Rating2": amgRating2, "Rating3": amgRating3}, index=[0])
            amg.to_csv('amg_reviews.csv', index=False, encoding='utf-8', mode = 'a', header = None)
    #This for loop continues off the last one, but due to different review formatting
    #a new loop was necessary        
    for y in range(533, 625):
        amgPage1 = requests.get("https://www.angrymetalguy.com/category/reviews/page/%s" %y, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"})
        amgSoup1 = BeautifulSoup(amgPage1.content, 'html.parser')
        #This for loop iterates through the each page of reviews on AMG
        for x in range(0, 10):
            amgPageTitle = amgSoup1.select('h2')[x].text
            #This page is titled different from other AMG pages
            if amgPageTitle == "Exitus – Statutum Est Hominibus Mori Review":
                amgPageTitle.replace("Exitus – Statutum Est Hominibus Mori Review", "retro spective review Exitus – Statutum Est Hominibus Mori")
            #Removes unwanted characters and replaces accented letters for use to access web page
            for s in amgPageTitle:
                s = remove_characters(amgPageTitle)
                amgPageTitle = s
            #Save the review page url in a variable 
            url = 'https://www.angrymetalguy.com/%s' %amgPageTitle
            #Request access to the web page of a specific review
            try:
                amgPage = requests.get(url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"})
            except:
                print(amgPageTitle, "gives an error.")
            amgSoup = BeautifulSoup(amgPage.content, 'html.parser')   
            #Finds the desired contents of the web page.
            amgReview = amgSoup.select("h1")[0].text
            try:
                amgAuthor = amgSoup.select("div.entry-meta")[0].text
                amgRating1 = amgSoup.select("p")[0].text
                amgRating2 = amgSoup.select("p")[1].text
                amgRating3 = amgSoup.select("p")[2].text
            except:
                print(amgPageTitle, "gives an error.")
            else:
                print(amgPageTitle, "works.")
            #Save data to a DataFrame and then a csv
            amg = pd.DataFrame({"Review": amgReview, "Author": amgAuthor, "Rating1": amgRating1, "Rating2": amgRating2, "Rating3": amgRating3}, index=[0])
            amg.to_csv('amg_reviews.csv', index=False, encoding='utf-8', mode = 'a', header = None)
           