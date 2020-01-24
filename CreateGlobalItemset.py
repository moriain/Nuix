"""
Menu Title: Create_Global_Itemset
Needs Case: true
Needs Selected Items: false
"""

#Author: Marc O Riain
#Date: 24/01/2020

#Description:
#1.This script finds the case name and current date and appends this info to a variable used to name the itemset in the following format '[CASE NAME] Item Set Global [Todays Date]'.
#2.Using this naming convention the script checks to see if an item set with the same name exists already, if it does not exist the script creates a new item set and adds the items to the itemset.




#Import required dependencies
import urllib2
import urllib
import json
import time
import javax.swing


#Display message to Users to notify them of the script running
jp=javax.swing.JOptionPane
jp.showMessageDialog(None, "The Global Item set Script will run,\nAll items will be deduplicated by Md5 and by Family.\npress okay to continue")


def create_itemset():
    from datetime import datetime
    #search for all items
    allItems=currentCase.search('')
    caseName=currentCase.getName()
    #find the current date
    #from datetime import datetime
    today=datetime.today().strftime('%Y-%m-%d')
    #create an Item set name variable in the format CaseName Item Set Global yyyy-mm-dd
    itemsetName="[{}] Item Set Global {}".format(caseName, today)
    
    ##test var name
    #print(itemsetName)

    #Settings to use for Item set
    settings={'deduplication':'MD5','deduplicateBy':'FAMILY'}

    #1. Check if the an itemset already exists before creating one..
    #1.a Loop through current itemsets and assing them to a list
    
    #empty list var
    parsedItemsets=[]
    
    #get Nuix itemsets
    Itemsets= currentCase.getAllItemSets()
    #populat the list
    for itemset in Itemsets:
    	parsedItemsets.append(itemset.getName())
    #Check that the itemset does not exist already, if true create an itemset
    if itemsetName not in parsedItemsets:
        print("The \"{}\" Itemset already exists!!".format(itemsetName))
        currentCase.createItemSet(itemsetName, settings)
        newItemset=currentCase.findItemSetByName(itemsetName)
    #add items to it
        newItemset.addItems(allItems)
        jp.showMessageDialog(None, "A new Itemset has been created, called:'{}'".format(itemsetName))
    else:
        jp.showMessageDialog(None, "The Itemset called:'{}' already exists, if you have added more data today and wish to update the global itemset then delete the current itemset called:'{}' and run this script again.".format(itemsetName, itemsetName))


create_itemset()

