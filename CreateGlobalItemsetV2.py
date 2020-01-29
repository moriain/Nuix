"""
Menu Title: Create_Global_ItemsetV2
Needs Case: true
Needs Selected Items: false
"""

#Author: Marc O Riain
#Date: 24/01/2020

#Description:
#1.This script finds the case name and current date and appends this info to a variable used to name the itemset in the following format '[CASE NAME] Item Set Global [Todays Date]'.
#2.Using this naming convention the script checks to see if an item set with the same name exists already, if it does not exist the script creates a new item set and adds the items to the itemset.





#Import required dependencies


import time
import javax.swing


#Display message to Users to notify them of the script running
jp=javax.swing.JOptionPane
msg1="This script will create an itemset from all items loaded into the case up to now.\nAll items will be deduplicated by Family using MD5.\n\n1. Choose \"Yes\" to continue.\n2. Choose \"No\" to quit."
title1="Run Global Itemset Script"

answer=jp.showConfirmDialog(None, msg1, title1, 0)

def create_itemset():

    from datetime import datetime
    #from datetime import datetime
    today=datetime.today().strftime('%d-%m-%Y')
    
    #search for all items
    allItems=currentCase.searchUnsorted('')
    #get case name
    caseName=currentCase.getName()

    #create an Item set name variable in the format [CaseName] [Item-Set-Global] yyyy-mm-dd
    myItemSetName="[{}] Item-Set-Global {}".format(caseName, today)
    
    ##test var name
    print(myItemSetName)

    #Settings to use for Item set
    msg2="This Global itemset was created on: {}, all items selected in the case where deduplicated by family using Md5".format(today)
    settings={'deduplication':'MD5','deduplicateBy':'FAMILY', 'description':msg2}

    #1. Check if the an itemset already exists before creating one..
    #1.a Loop through current itemsets and assing them to a list

    if(currentCase.findItemSetByName(myItemSetName)):
        ##Testprint("found itemset")
        wrnmsg="A global itemset already exists for the itemset named: {}\n\nIf you loaded additional items today {} and wish to update todays global itemset.\n1. Delete the exisiting itemset named: {}\n2. Re-run this script.".format(myItemSetName,today,myItemSetName)
        wrntitle="Global itemset already exists!"
        jp.showMessageDialog(None, wrnmsg, wrntitle, 2)
        
    else:
        #Testprint("No Itemset found")
        currentCase.createItemSet(myItemSetName, settings)
        
        myCreatedItemSet=currentCase.findItemSetByName(myItemSetName)
        myCreatedItemSet.addItems(allItems)
        query1="item-set:\"{}\"".format(myCreatedItemSet.getGuid())
        query2="item-set-originals:\"{}\"".format(myCreatedItemSet.getGuid())
    
        #print("Search over {} AND Search Term's".format(query))
        allItemSum=currentCase.count('')
        itemSetSum=currentCase.count(query1)
        deDupSum=currentCase.count(query2)
        
        msg3="{}\nCase total Items:  {}\nItem-set count:  {}\nItem-set Deduplicated originals:  {}".format(myItemSetName,allItemSum,itemSetSum, deDupSum)
        title3="Created a Global Itemset"
        jp.showMessageDialog(None, msg3, title3, 1)





if(answer == 0):
    create_itemset()








