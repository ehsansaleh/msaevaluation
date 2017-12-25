import matplotlib,os,operator,shutil
matplotlib.use('Agg')
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math,random
import errno

#Figure type is the name of the specific type of figures and also the name of the ouput folder
for figureType in ['AverageStatBinnedFullDatasets','AverageStatBinnedFullMethods','AverageScatterFullMethods','AverageScatterFullDatasets',
                   'AverageTCFScoreScatterFullDatasets','TopMethodsAverageScatter','TopMethodsAverageTCFScoreScatter',
                   'AverageCompressionFullMethods','AverageCompressionFullDatasets','AverageStatBinnedDiffFullDatasets',
                   'DefaultVsUndefaultModellerSPScore','DefaultVsUndefaultTCFScore','MAPvsPDModellerSPScore','MAPvsPDTCFScore',
                   'AverageScatterPDistFullMethods','AverageScatterPDistFullDatasets','AverageScatterLenHetFullMethods',
                   'AverageScatterLenHetFullDatasets','AverageScatterGapLenFullMethods','AverageScatterGapLenFullDatasets',
                   'ExampleFigures','Histograms','AverageScatterCombinedDB','AverageTCFScoreScatterFullMethods',
                   'AverageScatterFullDatasetsSimulated','MaskedVsUnMasked']:

	#Default values for variables in case it is not defined for the figure type
    fulldataormethod='FullMethods' #The union or intersection of different method outputs
    combinedatabaseslist = [False]  #Do you need a figure with all the datasets of different benchmarks combined?
    justtopmethodslist = [False] #Do you want just the top methods?
    converttomean=True #
    mainsharey=False
    mainmarkersize=30
    dividebycategorylist=[True,False] #Dividing by subcategories inside each benchmark
    maskinglist=[False] #Do you want the masked assessment?
    cleanoutput=False
    NucleicOrAminoList=['Amino']
    mainwraplist = [2]
    maintitle=''
    myfirstaxis = 'Modeller Score'
    myfirstaxisname = 'Modeller Score'
    mysecondaxis = 'SP-Score'
    mysecondaxisname = 'SP-Score'
    inputfolder = fulldataormethod + 'Input'
    outfolder = 'Output/'+'Misc'
    scatterbining=False
    specialflag1=False
	
	#Defining the variables for other figure types
    if figureType=='AverageScatterFullMethods':
        fulldataormethod='FullMethods'
        myfirstaxis = 'Modeller Score'
        myfirstaxisname = 'Modeller Score'
        mysecondaxis = 'SP-Score'
        mysecondaxisname = 'SP-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/'+figureType
        cleanoutput=True
        maskinglist = [False]
        combinedatabaseslist = [False]
        justtopmethodslist = [False]
        dividebycategorylist=[False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList=['Amino', 'Nucleic']
        mainwraplist = [2, 2]
        maintitle='Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of all the methods'
    if figureType=='NumSeqVsLength':
        fulldataormethod='FullMethods'
        myfirstaxis = 'Number of Sequences'
        myfirstaxisname = 'Number of Sequences'
        mysecondaxis = 'Effective Length'
        mysecondaxisname = 'Effective Reference Length'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/'+figureType
        cleanoutput=True
        maskinglist = [False]
        combinedatabaseslist = [True]
        justtopmethodslist = [False]
        dividebycategorylist=[False]
        converttomean = False
        mainsharey = False
        mainmarkersize = 5
        NucleicOrAminoList=['Amino', 'Nucleic']
        mainwraplist = [2, 2]
        maintitle='Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of all the datasets'
    if figureType=='AverageScatterFullDatasets':
        fulldataormethod='FullMethods'
        myfirstaxis = 'Modeller Score'
        myfirstaxisname = 'Modeller Score'
        mysecondaxis = 'SP-Score'
        mysecondaxisname = 'SP-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/'+figureType
        cleanoutput=True
        maskinglist = [False]
        combinedatabaseslist = [False]
        justtopmethodslist = [True]
        dividebycategorylist=[False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList=['Amino', 'Nucleic']
        mainwraplist = [2, 2]
        maintitle='Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of the top methods'
    if figureType=='AverageScatterFullDatasetsSimulated':
        fulldataormethod='FullMethods'
        myfirstaxis = 'Modeller Score'
        myfirstaxisname = 'Modeller Score'
        mysecondaxis = 'SP-Score'
        mysecondaxisname = 'SP-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/'+figureType
        cleanoutput=True
        maskinglist = [False]
        combinedatabaseslist = [True]
        justtopmethodslist = [True]
        dividebycategorylist=[False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList=['Nucleic']
        mainwraplist = [2, 2]
        maintitle='Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of the top methods on all of the simulated Rose datasets combined'
    if figureType=='AverageTCFScoreScatterFullMethods':
        fulldataormethod='FullMethods'
        myfirstaxis = 'TC'
        myfirstaxisname='Column Score'
        mysecondaxis='F-Score'
        mysecondaxisname = 'F-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/'+figureType
        cleanoutput=True
        maskinglist = [False]
        combinedatabaseslist = [False]
        justtopmethodslist = [False]
        dividebycategorylist=[False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList=['Amino', 'Nucleic']
        mainwraplist = [2, 2]
        maintitle='Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of all the methods'
    if figureType=='AverageTCFScoreScatterFullDatasets':
        fulldataormethod='FullMethods'
        myfirstaxis = 'TC'
        myfirstaxisname = 'Column Score'
        mysecondaxis = 'F-Score'
        mysecondaxisname = 'F-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/'+figureType
        cleanoutput=True
        maskinglist = [False]
        combinedatabaseslist = [False]
        justtopmethodslist = [True]
        dividebycategorylist=[False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList=['Amino', 'Nucleic']
        mainwraplist = [2, 2]
        maintitle='Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of the top methods'
    if figureType=='TopMethodsAverageScatter':
        fulldataormethod='FullMethods'
        myfirstaxis = 'Modeller Score'
        myfirstaxisname = 'Modeller Score'
        mysecondaxis = 'SP-Score'
        mysecondaxisname = 'SP-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/'+figureType
        cleanoutput=True
        maskinglist = [False,True]
        combinedatabaseslist = [False]
        justtopmethodslist = [True]
        dividebycategorylist=[False,True]
        mainwraplist = [2,4]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList=['Amino']
        maintitle='Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of the top methods'
    if figureType=='TopMethodsAverageTCFScoreScatter':
        fulldataormethod='FullMethods'
        myfirstaxis = 'TC'
        myfirstaxisname = 'Column Score'
        mysecondaxis = 'F-Score'
        mysecondaxisname = 'F-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/'+figureType
        cleanoutput=True
        maskinglist = [False,True]
        combinedatabaseslist = [False]
        justtopmethodslist = [True]
        dividebycategorylist=[False,True]
        mainwraplist = [2,4]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList=['Amino']
        maintitle='Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of the top methods'
    if figureType=='AverageCompressionFullMethods':
        fulldataormethod = 'FullMethods'
        myfirstaxis = 'Expansion'
        myfirstaxisname = 'Alignment Expansion Rate'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [False]
        justtopmethodslist = [False]
        dividebycategorylist = [False]
        mainwraplist = [2]
        converttomean = False
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList=['Amino', 'Nucleic']
        maintitle = 'Average '+myfirstaxisname+' of all the methods'
    if figureType=='AverageCompressionFullDatasets':
        fulldataormethod = 'FullMethods'
        myfirstaxis = 'Expansion'
        myfirstaxisname = 'Alignment Expansion Rate'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [False]
        justtopmethodslist = [True]
        dividebycategorylist = [False]
        mainwraplist = [2]
        converttomean = False
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList = ['Amino', 'Nucleic']
        maintitle = 'Average '+myfirstaxisname+' of the top methods'
    if figureType=='AverageStatBinnedFullDatasets':
        binslist = ['Average Sequence Identity', 'Sequence Length Heterogeneity', 'Median Gap Length']
        shortnames = ['average sequence identity', 'sequence length heterogeneity', 'median gap length']
        bincolnamelist = ['Identity Bin', 'Length Het. Bin', 'Med. Gap Len. Bin']
        binabrevlist = ['ID', 'Len.Het.', 'Med. Gap']
        fileextlist = ['Idbin', 'LenHetbin', 'MedGapbin']
        minlists = [[0, 0.15, 0.25, 0.5], [0, 0.1, 0.2], [0, 1.5, 2.5, 3.5]]
        maxlists = [[0.15, 0.25, 0.5, 1], [0.1, 0.2, 10], [1.5, 2.5, 3.5, 100000]]
        axislist = ['Average Sequence Identity','Modeller Score', 'SP-Score', 'F-Score', 'TC', 'Expansion',]
        axisnames = ['Sequence Identity','Modeller Score', 'SP-Score', 'F-Score', 'Column Score', 'Expansion']
        dependtomethodlist=[False,True,True,True,True,True]
        fulldataormethod = 'FullMethods'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [True]
        justtopmethodslist = [True]
        dividebycategorylist = [False]
        converttomean = False
        mainwraplist = [1]
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList = ['Amino']
        #Title is defiined in the for loop
    if figureType=='AverageStatBinnedScatterFullDatasets':
        binslist = ['Average Sequence Identity', 'Sequence Length Heterogeneity', 'Median Gap Length']
        shortnames = ['average sequence identity', 'sequence length heterogeneity', 'median gap length']
        bincolnamelist = ['Identity Bin', 'Length Het. Bin', 'Med. Gap Len. Bin']
        binabrevlist = ['ID', 'Len.Het.', 'Med. Gap']
        fileextlist = ['Idbin', 'LenHetbin', 'MedGapbin']
        minlists = [[0, 0.15, 0.25, 0.5], [0, 0.1, 0.2], [0, 1.5, 2.5, 3.5]]
        maxlists = [[0.15, 0.25, 0.5, 1], [0.1, 0.2, 10], [1.5, 2.5, 3.5, 100000]]
        myfirstaxis = 'Modeller Score'
        myfirstaxisname = 'Modeller Score'
        mysecondaxis = 'SP-Score'
        mysecondaxisname = 'SP-Score'
        dependtomethodlist=[False,True,True,True,True,True]
        fulldataormethod = 'FullMethods'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [True]
        justtopmethodslist = [True]
        dividebycategorylist = [False]
        converttomean = False
        mainwraplist = [1]
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList = ['Amino']
        #Title is defiined in the for loop
    if figureType=='AverageStatBinnedFullMethods':
        binslist = ['Average Sequence Identity', 'Sequence Length Heterogeneity', 'Median Gap Length']
        shortnames = ['identity', 'sequence length heterogeneity', 'median gap length']
        bincolnamelist = ['Identity Bin', 'Length Het. Bin', 'Med. Gap Len. Bin']
        binabrevlist = ['ID', 'Len.Het.', 'Med. Gap']
        fileextlist = ['Idbin', 'LenHetbin', 'MedGapbin']
        minlists = [[0, 0.15, 0.25, 0.5], [0, 0.1, 0.2], [0, 1.5, 2.5, 3.5]]
        maxlists = [[0.15, 0.25, 0.5, 1], [0.1, 0.2, 10], [1.5, 2.5, 3.5, 100000]]
        axislist = ['Modeller Score', 'SP-Score', 'F-Score', 'TC', 'Expansion']
        axisnames = ['Modeller Score', 'SP-Score', 'F-Score', 'Column Score', 'Expansion']
        dependtomethodlist = [True, True, True, True, True]
        fulldataormethod = 'FullMethods'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [True]
        justtopmethodslist = [False]
        dividebycategorylist = [False]
        converttomean = False
        mainwraplist = [1]
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList = ['Amino']
        #Title is defiined in the for loop
    if figureType=='AverageStatBinnedDiffFullDatasets':
        binslist = ['Average Sequence Identity', 'Sequence Length Heterogeneity', 'Median Gap Length']
        shortnames = ['identity', 'sequence length heterogeneity', 'median gap length']
        bincolnamelist = ['Identity Bin', 'Length Het. Bin', 'Med. Gap Len. Bin']
        binabrevlist = ['ID', 'Len.Het.', 'Med. Gap']
        fileextlist = ['Idbin', 'LenHetbin', 'MedGapbin']
        minlists = [[0, 0.15, 0.25, 0.5], [0, 0.1, 0.2], [0, 1.5, 2.5, 3.5]]
        maxlists = [[0.15, 0.25, 0.5, 1], [0.1, 0.2, 10], [1.5, 2.5, 3.5, 100000]]
        axislist = ['Modeller Score', 'SP-Score', 'F-Score', 'TC', 'Expansion']
        axisnames = ['Modeller Score', 'SP-Score', 'F-Score', 'Column Score', 'Expansion']
        fulldataormethod = 'FullMethods'
        inputfolder = fulldataormethod + 'Input'
        difficultydirectionlist = ['left', 'right', 'right']
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [True]
        justtopmethodslist = [True]
        dividebycategorylist = [False]
        converttomean = False
        mainwraplist = [1]
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList = ['Amino']
    if figureType=='DefaultVsUndefaultModellerSPScore':
        fulldataormethod = 'FullMethods'
        myfirstaxis = 'Modeller Score'
        myfirstaxisname = 'Modeller Score'
        mysecondaxis = 'SP-Score'
        mysecondaxisname = 'SP-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [True]
        justtopmethodslist = [False]
        dividebycategorylist = [False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList = ['Amino', 'Nucleic']
        mainwraplist = [2, 2]
        maintitle = 'Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of Mafft Variants'
    if figureType=='DefaultVsUndefaultTCFScore':
        fulldataormethod = 'FullMethods'
        myfirstaxis = 'TC'
        myfirstaxisname = 'Column Score'
        mysecondaxis = 'F-Score'
        mysecondaxisname = 'F-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [True]
        justtopmethodslist = [False]
        dividebycategorylist = [False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList = ['Amino', 'Nucleic']
        mainwraplist = [2, 2]
        maintitle = 'Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of Mafft Variants'
    if figureType=='AverageScatterPDistFullMethods':
        scatterbining=True
        scatterbinstat='Average Sequence Identity'
        scatbinshortnamefortitle = 'Identity'
        scatbinshortname='identity'
        min_scatbinstat_list = [0, 0.25, 0.5]
        max_scatbinstat_list = [0.25, 0.5, 1]
        fulldataormethod = 'FullMethods'
        myfirstaxis = 'Modeller Score'
        myfirstaxisname = 'Modeller Score'
        mysecondaxis = 'SP-Score'
        mysecondaxisname = 'SP-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [False]
        justtopmethodslist = [False]
        dividebycategorylist = [False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList = ['Amino', 'Nucleic']
        mainwraplist = [2, 2]
        maintitle = 'Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of all the methods'
    if figureType=='AverageScatterPDistFullDatasets':
        scatterbining=True
        scatterbinstat='Average Sequence Identity'
        scatbinshortnamefortitle = 'Identity'
        scatbinshortname='identity'
        min_scatbinstat_list = [0, 0.25, 0.5]
        max_scatbinstat_list = [0.25, 0.5, 1]
        fulldataormethod = 'FullMethods'
        myfirstaxis = 'Modeller Score'
        myfirstaxisname = 'Modeller Score'
        mysecondaxis = 'SP-Score'
        mysecondaxisname = 'SP-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [False]
        justtopmethodslist = [True]
        dividebycategorylist = [False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList = ['Amino', 'Nucleic']
        mainwraplist = [2, 2]
        maintitle = 'Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of all the methods'
    if figureType=='AverageScatterLenHetFullMethods':
        scatterbining=True
        scatterbinstat='Sequence Length Heterogeneity'
        scatbinshortnamefortitle = 'Len. Het.'
        scatbinshortname='lenhet'
        min_scatbinstat_list = [0,0.1,0.2]
        max_scatbinstat_list = [0.1,0.2,100]
        fulldataormethod = 'FullMethods'
        myfirstaxis = 'Modeller Score'
        myfirstaxisname = 'Modeller Score'
        mysecondaxis = 'SP-Score'
        mysecondaxisname = 'SP-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [False]
        justtopmethodslist = [False]
        dividebycategorylist = [False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList = ['Amino', 'Nucleic']
        mainwraplist = [2, 2]
        maintitle = 'Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of all the methods'
    if figureType=='AverageScatterLenHetFullDatasets':
        scatterbining=True
        scatterbinstat='Sequence Length Heterogeneity'
        scatbinshortname='lenhet'
        scatbinshortnamefortitle = 'Len. Het.'
        min_scatbinstat_list = [0,0.1,0.2]
        max_scatbinstat_list = [0.1,0.2,100]
        fulldataormethod = 'FullMethods'
        myfirstaxis = 'Modeller Score'
        myfirstaxisname = 'Modeller Score'
        mysecondaxis = 'SP-Score'
        mysecondaxisname = 'SP-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [False]
        justtopmethodslist = [True]
        dividebycategorylist = [False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList = ['Amino', 'Nucleic']
        mainwraplist = [2, 2]
        maintitle = 'Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of all the methods'
    if figureType=='AverageScatterGapLenFullMethods':
        scatterbining=True
        scatterbinstat='Median Gap Length'
        scatbinshortnamefortitle='Median Gap Length'
        scatbinshortname='gaplen'
        min_scatbinstat_list = [0, 1.49, 2.49, 3.49]
        max_scatbinstat_list = [1.49, 2.49, 3.49, 10000]
        fulldataormethod = 'FullMethods'
        myfirstaxis = 'Modeller Score'
        myfirstaxisname = 'Modeller Score'
        mysecondaxis = 'SP-Score'
        mysecondaxisname = 'SP-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [False]
        justtopmethodslist = [False]
        dividebycategorylist = [False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList = ['Amino', 'Nucleic']
        mainwraplist = [2, 2]
        maintitle = 'Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of all the methods'
    if figureType=='AverageScatterGapLenFullDatasets':
        scatterbining=True
        scatterbinstat='Median Gap Length'
        scatbinshortnamefortitle='Median Gap Length'
        scatbinshortname='gaplen'
        min_scatbinstat_list = [0, 1.49, 2.49, 3.49]
        max_scatbinstat_list = [1.49, 2.49, 3.49, 10000]
        fulldataormethod = 'FullMethods'
        myfirstaxis = 'Modeller Score'
        myfirstaxisname = 'Modeller Score'
        mysecondaxis = 'SP-Score'
        mysecondaxisname = 'SP-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [False]
        justtopmethodslist = [True]
        dividebycategorylist = [False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList = ['Amino', 'Nucleic']
        mainwraplist = [2, 2]
        maintitle = 'Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of all the methods'
    if figureType=='ExampleFigures':
        specialflag1=True
        fulldataormethod = 'FullMethods'
        myfirstaxis = 'Average Sequence Identity'
        myfirstaxisname =  'Average Sequence Identity'
        mysecondaxis ='F-Score'
        mysecondaxisname ='F-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [False]
        justtopmethodslist = [True]
        dividebycategorylist = [False]
        converttomean = False
        mainsharey = True
        mainmarkersize = 10
        NucleicOrAminoList = ['Amino']
        mainwraplist = [2]
        maintitle = 'Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of a top method'
    if figureType=='Histograms':
        fulldataormethod = 'FullMethods'
        myfirstaxislist = ['Average Sequence Identity','Number of Sequences','Number of Sequences','Reference Length','Reference Length','Gappiness Percentage','Average Gap Length','Median Gap Length','Average Terminal Gap length']
        myfirstaxisnamelist = ['Average Sequence Identity','Number of Sequences','Number of Sequences','Reference Alignment Length','Reference Alignment Length','Gappiness Percentage','Average Gap Length','Median Gap Length','Average Terminal Gap Length']
        outpicfilenameslist = ['histseqid','histnumseq','histnumseqscaled','histalnref','histalnrefscaled','histgappercent','histavggaplen','histmedgaplen','avgtermgaplenscaled']
        myshareaxlist = [False,True,False,True,False,True,False,False,False]
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [False]
        justtopmethodslist = [True]
        dividebycategorylist = [False]
        converttomean = False
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList = ['Amino']
        mainwraplist = [2]
    if figureType=='AverageScatterCombinedDB':
        fulldataormethod='FullMethods'
        myfirstaxis = 'Modeller Score'
        myfirstaxisname = 'Modeller Score'
        mysecondaxis = 'SP-Score'
        mysecondaxisname = 'SP-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/'+figureType
        cleanoutput=True
        maskinglist = [False]
        combinedatabaseslist = [True]
        justtopmethodslist = [False,True]
        dividebycategorylist=[False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList=['Amino', 'Nucleic']
        mainwraplist = [2, 2]
        maintitle='Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of the top methods'
    if figureType=='MAPvsPDModellerSPScore':
        fulldataormethod = 'FullMethods'
        myfirstaxis = 'Modeller Score'
        myfirstaxisname = 'Modeller Score'
        mysecondaxis = 'SP-Score'
        mysecondaxisname = 'SP-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [True]
        justtopmethodslist = [False]
        dividebycategorylist = [False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList = ['Amino', 'Nucleic']
        mainwraplist = [2, 2]
        maintitle = 'Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of BAli-Phy Summarization Methods'
    if figureType=='MAPvsPDTCFScore':
        fulldataormethod = 'FullMethods'
        myfirstaxis = 'TC'
        myfirstaxisname = 'Column Score'
        mysecondaxis = 'F-Score'
        mysecondaxisname = 'F-Score'
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/' + figureType
        cleanoutput = True
        maskinglist = [False]
        combinedatabaseslist = [True]
        justtopmethodslist = [False]
        dividebycategorylist = [False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList = ['Amino', 'Nucleic']
        mainwraplist = [2, 2]
        maintitle = 'Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of BAli-Phy Summarization Methods'
    if figureType=='MaskedVsUnMasked':
        fulldataormethod='FullMethods'
        myfirstaxislist = ['Modeller Score','SP-Score','F-Score','TC']
        myfirstaxisnamelist = ['Modeller Score','SP-Score','F-Score','Column Score']
        inputfolder = fulldataormethod + 'Input'
        outfolder = 'Output/'+figureType
        cleanoutput=True
        maskinglist = [False]
        combinedatabaseslist = [False]
        justtopmethodslist = [False]
        dividebycategorylist=[False]
        converttomean = True
        mainsharey = True
        mainmarkersize = 30
        NucleicOrAminoList=['Amino']
        mainwraplist = [2, 2]
        maintitle='Average ' + myfirstaxisname + ' vs ' + mysecondaxisname + ' of all the methods'
    if cleanoutput:
        if (os.path.exists(outfolder)):
            shutil.rmtree(outfolder)
    #if not (os.path.exists(outfolder)):
    #    os.mkdir(outfolder)
    try:
        os.makedirs(outfolder)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(outfolder):
            pass

    def plotfunc():
        if (dividebycategory):
            filedivext = 'Divided'
        else:
            filedivext = 'Whole'

        firstaxis = myfirstaxis
        firstaxisname = myfirstaxisname
        secondaxis = mysecondaxis
        secondaxisname = mysecondaxisname
        if masking == True:
            firstaxis = myfirstaxis + '(masked)'
            firstaxisname = myfirstaxisname + '(masked)'
            secondaxis = mysecondaxis + '(masked)'
            secondaxisname = mysecondaxisname + '(masked)'
            filedivext += 'Masked'
        else:
            filedivext += 'Unmasked'

        resfactor = 1.5
        #resfactor = 2
        adjustment = 0.9
        markersize = int(resfactor * mainmarkersize / 1.5)
        legendmarkerscale = int(100 / markersize)
        mysharey = mainsharey
        figsize = 3 * resfactor
        mainwrap=mymainwrap
        if combinedatabases:
            resfactor = 5
            markersize = int(resfactor * mainmarkersize / 1.5)
            legendmarkerscale = int(100 / markersize)
            # markersize = int( resfactor * mainmarkersize / 1.5 )
            mysharey = True
            legendmarkerscale = 2
            adjustment = 0.9
            filedivext = 'CombinedDB'
            mainwrap = 1
            if dividebycategory:
                return
        #sns.set(font_scale=resfactor * 0.8)
        sns.set(font_scale=resfactor)
        sns.set_style("white")

        if justtopmethods:
            filedivext = filedivext + 'TopMethods'
        else:
            filedivext = filedivext + 'AllMethods'

        sns.palplot(sns.color_palette("Paired", 16))
        colors = ['#F00000', '#00BF00', '#FF00FE',
                  '#9E4F46', '#7B1A69', '#00FFC1', '#008395', '#0000FF', '#FF0000', '#00FF00', '#837200', '#00FF00',
                  '#FF1AB8', '#FF1AB8',
                  '#00007B', '#F69EDB', '#72F6FF', '#D311FF', '#FFC183', '#95D34F', '#00002B', '#232308', '#FFD300',
                  '#F68308', '#8CA77B',
                  '#D3FF00', '#FFD300', '#9EC1FF', '#72607B', '#9E0000', '#004FFF', '#004695', '#005700', '#8383FF',
                  '#B84FD3', '#0000FF']
        colordict = {'BAliPhy-PD': '#000000', 'Muscle': '#00BE00', 'Clustal': '#D3D300', 'Prank': '#008080', 'MAFFT-G': '#FF9900',
                     'MAFFT-G-INS-I': '#FF9900','TCoffee': '#A4009B','ProbCons':'#8080C0','MAFFT-Homologs':'#804000',
                     'ContrAlign': '#4385FF', 'DiAlign': '#800000', 'KAlign': '#664C28', 'Prime': '#FF00FF',
                     'ProbAlign': '#FF0000', 'SAPD': '#0000A0','Promals':'#408080','Praline':'#8080FF'
                     ,'ProbCons    ':'#8080C0','MAFFT-L': '#408080',}
        fig, ax = plt.subplots()

        def csv2datafram(inaddress, databasename):

            #Removing "Taxa don't match" errored datasets
            with open(inaddress) as f:
                content = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            content = [x.strip() for i,x in enumerate(content)]
            content = [x for i, x in enumerate(content) if not(('Taxa' in x) and ('match' in x))]
            thefile = open(inaddress, 'w')
            for line in content:
                thefile.write("%s\n" % line)
            thefile.close()

            mytips2 = pd.read_csv(inaddress)

            mytips2 = mytips2.rename(columns={'1-SPFP(masked)': 'Modeller Score(masked)'})
            mytips2 = mytips2.rename(columns={'1-SPFN(masked)': 'SP-Score(masked)'})
            mytips2 = mytips2.rename(columns={'Compression(masked)': 'Expansion(masked)'})
            if 'Modeller Score(masked)' in mytips2.columns and 'SP-Score(masked)' in mytips2.columns:
                def fstatmaskedcalc(row):
                    if (row['Modeller Score(masked)'] * row['SP-Score(masked)']):
                        return 2 * (row['Modeller Score(masked)'] * row['SP-Score(masked)']) / (
                        row['Modeller Score(masked)'] + row['SP-Score(masked)'])
                    else:
                        return 0

                mytips2['F-Score(masked)'] = mytips2.apply(lambda row: fstatmaskedcalc(row), axis=1)

            def fstatcalc(row):
                if (float(row['1-SPFP']) * float(row['1-SPFN'])):
                    return 2 * (float(row['1-SPFP']) * float(row['1-SPFN'])) / (float(row['1-SPFP']) + float(row['1-SPFN']))
                else:
                    return 0

            mytips2['F-Score'] = mytips2.apply(lambda row: fstatcalc(row), axis=1)

            mytips2 = mytips2.rename(columns={'SP-Score': 'SP-Accuracy'})

            def fstatcalc(row):
                if (row['1-SPFP'] * row['1-SPFN']):
                    return 2 * (row['1-SPFP'] * row['1-SPFN']) / (row['1-SPFP'] + row['1-SPFN'])
                else:
                    return 0

            mytips2['F-Score'] = mytips2.apply(lambda row: fstatcalc(row), axis=1)

            def aacount(row):
                return (row['Reference Length']*(1-row['Gappiness Percentage']))

            mytips2['Effective Length'] = mytips2.apply(lambda row: aacount(row), axis=1)

            mytips2 = mytips2.rename(columns={'1-SPFP': 'Modeller Score'})
            mytips2 = mytips2.rename(columns={'1-SPFN': 'SP-Score'})
            mytips2 = mytips2.rename(columns={'Compression': 'Expansion'})
            tips2 = mytips2
            if figureType.startswith('DefaultVsUndefault'):
                tips2 = tips2[tips2.Method.isin(['MAFFT', 'LINSI', 'GINSI', 'EINSI'])]
                #tips2 = tips2[tips2.Method.isin(['MAFFT', 'LINSI', 'GINSI', 'EINSI', 'ContrAlign', 'DefaultContrAlign','ProbCons','DefaultProbCons'])]
                #tips2 = tips2.replace(['ContrAlign'], ['Non-Default-ContrAlign'])
                #tips2 = tips2.replace(['DefaultContrAlign'], ['ContrAlign    '])
                #tips2 = tips2.replace(['ProbCons'], ['Non-Default-ProbCons'])
                #tips2 = tips2.replace(['DefaultProbCons'], ['ProbCons    '])
                tips2 = tips2.replace(['MAFFT'], ['MAFFT-Auto'])
                tips2 = tips2.replace(['LINSI'], ['MAFFT-L-INS-I'])
                tips2 = tips2.replace(['GINSI'], ['MAFFT-G-INS-I'])
                tips2 = tips2.replace(['EINSI'], ['MAFFT-E-INS-I'])
            if figureType.startswith('MAPvsPD'):
                tips2 = tips2[tips2.Method.isin(['BPPD','BPMAP'])]
                tips2 = tips2.replace(['BPPD'], ['BAliPhy-PD'])
                tips2 = tips2.replace(['BPMAP'], ['BAliPhy-MAP'])

                if tips2.empty:
                    return tips2

                tips2['Database'] = databasename
                return tips2

            tips2 = tips2[tips2.Method != 'MAFFT-H-LargeDB']
            tips2 = tips2[tips2.Method != 'Pagan']
            tips2 = tips2[tips2.Method != 'ContrAlign']
            tips2 = tips2.replace(['DefaultContrAlign'], ['ContrAlign'])
            tips2 = tips2[tips2.Method != 'ProbCons']
            #tips2 = tips2.replace(['ProbCons'], ['Non-Default-ProbCons'])
            tips2 = tips2.replace(['DefaultProbCons'], ['ProbCons'])
            #tips2 = tips2[tips2.Method != 'ProbCons']
            tips2 = tips2.replace(['SWA0.5'], ['SWA'])

            if tips2.empty:
                return tips2
            tips2 = tips2.applymap(lambda x: x.replace('SWA0.5', 'SWA') if isinstance(x, str) else x)
            tips2 = tips2.applymap(lambda x: x.replace('SWA', 'SAWA') if isinstance(x, str) else x)

            for mainmethodabrev in ['SA', 'BP']:
                droplist = []
                chosenmethod = 'LongestPossibleMethodNameIsLessThanThis'
                allmethods = tips2.Method.unique()[:]
                allmethods.sort()
                for i, method in enumerate(allmethods):
                    if mainmethodabrev in method:
                        droplist.append(method)
                        if len(method) < len(chosenmethod):
                            chosenmethod = method
                if chosenmethod in droplist:
                    droplist.remove(chosenmethod)
                for droppingmethod in droplist:
                    tips2 = tips2[tips2.Method != droppingmethod]

            tips2 = tips2[tips2.Method != 'SAPD']

            for mainmethodabrev in ['ContrAlign', 'ProbCons']:
                droplist = []
                chosenmethod = ''
                for method in tips2.Method.unique():
                    if mainmethodabrev in method:
                        droplist.append(method)
                        if len(method) > len(chosenmethod):
                            chosenmethod = method
                if chosenmethod in droplist:
                    droplist.remove(chosenmethod)
                for droppingmethod in droplist:
                    tips2 = tips2[tips2.Method != droppingmethod]

            priority_list = [ 'GINSI', 'LINSI', 'EINSI', 'MAFFT']
            droplist = []
            chosenmethod = ''
            chosenidx = 100000
            for method in tips2.Method.unique():
                if method in priority_list:
                    droplist.append(method)
                    if priority_list.index(method) < chosenidx:
                        chosenmethod = method
                        chosenidx = priority_list.index(chosenmethod)
            if chosenmethod in droplist:
                droplist.remove(chosenmethod)
            if NucleicOrAmino == 'Nucleic':
                tips2 = tips2[~tips2.Method.isin(['EINSI', 'MAFFT'])]
                tips2 = tips2.replace(['LINSI'], ['MAFFT-L'])
            else:
                for droppingmethod in droplist:
                    tips2 = tips2[tips2.Method != droppingmethod]
            if not figureType.startswith('DefaultVsUndefault'):
                tips2 = tips2.replace([chosenmethod], ['MAFFT-' + chosenmethod[0]])

            tips2['Database'] = pd.Series([databasename for i in range(len(tips2.index))], index=tips2.index)
            tips2 = tips2.replace(['BPPD'], ['BAliPhy-PD'])
            return tips2

        def MattBenchCatAdder(dataframe):
            mydf = dataframe
            mydf.index = range(len(mydf.index))
            for p, row in mydf.iterrows():
                if row["Database"] == 'MattBench':
                    if row["Dataset"].startswith('SF'):
                        category = 'SuperFamily'
                    else:
                        category = 'TwilightZone'
                    mydf.set_value(p, 'Database', 'MattBench-' + category)
            return mydf

        def BaliBaseCatAdder(dataframe):
            mydf = dataframe
            sisydatacat = pd.read_csv('BaliBaseCategories.csv')
            mycounter = 0
            mydf.index = range(len(mydf.index))
            for p, row in mydf.iterrows():
                if row["Database"] == 'BAliBase':
                    mycounter = mycounter + 1
                    catrow = sisydatacat[sisydatacat['New Name'] == row.Dataset]
                    category = catrow.get_value(catrow.index[0], 'Category')
                    if category == 'RV921' or category == 'RV941':
                        category = 'RV921+RV941'
                    mydf.set_value(p, 'Database', 'BAliBase-' + category)
            return mydf

        def SisyphusCatAdder(dataframe):
            mydf = dataframe
            sisydatacat = pd.read_csv('SisyphusCategories.csv')
            mycounter = 0
            mydf.index = range(len(mydf.index))
            for p, row in mydf.iterrows():
                if row["Database"] == 'Sisyphus':
                    mycounter = mycounter + 1
                    if(row.Dataset.endswith('-Small')):
                        cmpval=row.Dataset[:-6]
                    else:
                        cmpval = row.Dataset
                    catrow = sisydatacat[sisydatacat['Dataset'] == cmpval]
                    category = catrow.get_value(catrow.index[0], 'Category')
                    mydf.set_value(p, 'Database', 'Sisyphus-' + category)
                    # mydf.loc[i, "DataBase"] = "answer {}".format(trial["no"])
            return mydf

        def df2mean(mydf):
            outdf = mydf
            outdf['Type'] = 'Data'
            outdf.index = range(len(outdf.index))
            for col in list(outdf):
                if np.issubdtype(outdf[col].dtype, np.number):
                    outdf[[col]] = outdf[[col]].apply(lambda x: pd.to_numeric(x, downcast='float'))

            if 'Database' in list(outdf):
                for method in mydf.Method.unique():
                    for database in mydf.Database.unique():
                        currdf = outdf[outdf.Database == database]
                        alldatasets = len(currdf['Dataset'].unique())
                        currdf = currdf[currdf.Method == method]
                        if not (len(currdf['Dataset'].unique()) == alldatasets):
                            print(
                            'Warning: Method ' + method + ' on Database ' + database + ' has less datasets than the whole database. '
                            + str(len(currdf['Dataset'].unique())) + '/' + str(alldatasets))
                            continue
                        newdf = currdf[:1]
                        outdf = pd.concat([outdf, newdf], ignore_index=True)
                        for col in list(outdf):
                            if np.issubdtype(currdf[col].dtype, np.number):
                                # print (len(outdf)-1,col,currdf[col].mean())
                                outdf.set_value(len(outdf) - 1, col, currdf[col].mean())
                                # print currdf[col].mean()
                                # print outdf.iloc[len(outdf)-1][col]
                        outdf.set_value(len(outdf) - 1, 'Type', 'Mean')
                        outdf.set_value(len(outdf) - 1, 'Database', database + '/' + str(alldatasets))

            else:
                for method in mydf.Method.unique():
                    currdf = outdf[outdf.Method == method]
                    outdf.loc[len(outdf)] = currdf.iloc[0].values
                    for col in list(outdf):
                        if np.issubdtype(currdf[col].dtype, np.number):
                            outdf.set_value(len(outdf) - 1, col, currdf[col].mean())
                    outdf.set_value(len(outdf) - 1, 'Type', 'Mean')

            outdf = outdf[outdf['Type'] == 'Mean']

            return outdf

        def commentadder(inputdf, commentaddress):
            def closefinder(indf, firstax, secondax, closethresh):

                def closefunc(mydf, ax1, ax2, firstmethod, secondmethod, th):
                    a1m1 = mydf[mydf['Method'] == firstmethod][ax1].iloc[0]
                    a1m2 = mydf[mydf['Method'] == secondmethod][ax1].iloc[0]
                    a2m1 = mydf[mydf['Method'] == firstmethod][ax2].iloc[0]
                    a2m2 = mydf[mydf['Method'] == secondmethod][ax2].iloc[0]
                    if math.sqrt(((a1m1 - a1m2) ** 2) + ((a2m1 - a2m2) ** 2)) < th:
                        return True
                    else:
                        return False

                def classproximity(mydf, ax1, ax2, th, firstclass, secondclass):
                    for firstmethod in firstclass:
                        for secondmethod in secondclass:
                            if closefunc(mydf, ax1, ax2, firstmethod, secondmethod, th):
                                return True
                    return False

                df = indf.copy(deep=True)
                ax1min = df[firstax].min()
                ax1max = df[firstax].max()
                ax2min = df[secondax].min()
                ax2max = df[secondax].max()
                df[firstax] = df.apply(lambda row: row[firstax] / (ax1max - ax1min), axis=1)
                df[secondax] = df.apply(lambda row: row[secondax] / (ax2max - ax2min), axis=1)

                outdict = {}
                for mydatabasename in df.Database.unique():
                    mycurrdf = df[df.Database == mydatabasename]

                    allclasses = []
                    for mynewmethod in mycurrdf.Method.unique():
                        allclasses.append([mynewmethod])

                    while True:
                        breakflag = False
                        for v in range(len(allclasses)):
                            for b in range(v):
                                if classproximity(mycurrdf, firstax, secondax, closethresh, allclasses[v], allclasses[b]):
                                    breakflag = True
                                    merge1 = v
                                    merge2 = b
                                    break
                            if breakflag:
                                break
                        if breakflag:
                            allclasses.append(allclasses[merge1] + allclasses[merge2])
                            del allclasses[merge1]
                            del allclasses[merge2]
                        else:
                            break
                    outdict[mydatabasename] = [myclass for myclass in allclasses if len(myclass) > 1]
                return outdict

            commentstringlist = []
            fullproximities = closefinder(inputdf, firstaxis, secondaxis, 0.01)
            for dbname in fullproximities.keys():
                for proximities in fullproximities[dbname]:
                    if len(proximities) == 2:
                        commentstringlist.append(
                            'On ' + dbname.split('/')[0] + ', \\textit{' + proximities[0] + '} and \\textit{'
                            + proximities[1] + '} methods are tightly close.')
                    if len(proximities) > 2:
                        methstr = ', '.join(['\\textit{' + proximities[r] + '}' for r in range(len(proximities) - 1)])
                        methstr = methstr + ', and \\textit{' + proximities[-1] + '}'
                        commentstringlist.append(
                            'On ' + dbname.split('/')[0] + ', methods ' + methstr + ' are very close.')
            random.shuffle(commentstringlist)
            commentstring = ' '.join(commentstringlist)
            text_file = open(commentaddress, "w")
            text_file.write(commentstring)
            text_file.close()

        def bincountwriter(indf,commentpath):
            df=indf.copy()
            bins = df[bincolname].unique()
            bins = sorted(bins, key=lambda x: float(x.split('<')[0]))

            bincntdict={}
            alldatabases=df.Database.unique()
            for c, database in enumerate(alldatabases):
                mycurrdf = df[df.Database ==database]
                bincntlist=[]
                for i,bin in enumerate(bins):
                    newcurrdf=mycurrdf[mycurrdf[bincolname]==bin]
                    #bincntlist.append(newcurrdf.groupby(['Dataset','Database']).count())
                    bincntlist.append( len(newcurrdf.drop_duplicates(subset=['Dataset','Database'],keep='first')) )
                bincntdict[database]=bincntlist[:]

            num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
                          9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                          15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
            #tempstring='The number of datasets in each bin, sorted with the order of the lowest '+shortname+' bin in the beginning of the sequence' \
            #           ' and the highest '+shortname+' bin at the end of the sequence, are '
            tempstring='The '+num2words[len(bincntdict[alldatabases[0]])]+' bins based on '+shortname+', ordered from smallest to largest, have '
            for database in alldatabases:
                if len(alldatabases)>1:
                    tempstring=tempstring + 'for ' + database+' '
                cntstr=str(bincntdict[database]).replace('[', '').replace(']', '')
                if cntstr.count(',') > 1:
                    cntstr=','.join(cntstr.split(',')[:-1])+', and '+cntstr.split(', ')[-1]
                else:
                    cntstr = ' and '.join(cntstr.split(', ')[:])
                tempstring=tempstring+ cntstr

            #tempstring=','.join(tempstring.split(',')[:-1])+'.'
            if len(alldatabases)>1:
                tempstring = 'for'.join(tempstring.split('for')[:-1])+'and for'+tempstring.split('for')[-1]

            tempstring=tempstring+' alignments, respectively.'
            text_file = open(commentpath, "w")
            text_file.write(tempstring)
            text_file.close()

        def missingdatacompleter(myinputdf, inaccuracycols='default', indisablecompletion='default'):
            inputdf = myinputdf.copy()
            if inaccuracycols == 'default':
                accuracycols = {'Modeller Score': 0, 'SP-Score': 0, 'TC': 0, 'Expansion': np.NaN,
                                'Modeller Score(masked)': 0,
                                'SP-Score(masked)': 0, 'TC(masked)': 0, 'Expansion(masked)': np.NaN}
            else:
                accuracycols = inaccuracycols
            if indisablecompletion == 'default':
                disablecompletion = {'BAliBase': ['SAPD']}
            else:
                disablecompletion = indisablecompletion

            alldatasets = inputdf.Dataset.unique()
            allmethods = inputdf.Method.unique()
            for method in allmethods:
                mycurrdf = inputdf[inputdf.Method == method]
                for dataset in alldatasets:

                    mydatabase = inputdf[inputdf.Dataset == dataset].Database.tolist()[0]
                    continueflag = False
                    for db in disablecompletion:
                        if db == mydatabase:
                            if dataset in disablecompletion[db]:
                                continueflag = True

                    if not (mycurrdf['Dataset'] == dataset).any() and not (continueflag):
                        print(
                        'Warning: Method ' + method + ' was not measured on dataset ' + dataset + '. We will just put 0 accuracy instead.')
                        smalldf = inputdf[inputdf['Dataset'] == dataset].copy()
                        smalldf = smalldf[:1]
                        for stat in accuracycols:
                            smalldf[stat] = accuracycols[stat]
                        smalldf['Method'] = method
                        inputdf = inputdf.append(smalldf, ignore_index=True)
            return inputdf

        def dfbalancerByremoving(mydf, dblist=None):
            inputdf = mydf.copy()
            if dblist == None:
                dblist = inputdf.Database.unique()
            allmethods = len(inputdf.Method.unique())
            for db in dblist:
                dbdatasets = inputdf[inputdf.Database == db].Dataset.unique()
                for dataset in dbdatasets:
                    crit1 = inputdf['Database'].map(lambda x: x == db)
                    crit2 = inputdf['Dataset'].map(lambda x: x == dataset)
                    crit3 = inputdf['Database'].map(lambda x: not x == db)
                    crit4 = inputdf['Dataset'].map(lambda x: not x == dataset)
                    if len(inputdf[crit1 & crit2].Method.unique()) < allmethods:
                        inputdf = inputdf[crit3 | crit4]
            return inputdf

        def idbinner(df):
            minidlist=minlist
            maxidlist = maxlist

            binnames=[]
            for i,minval in enumerate(minidlist):
                binnames.append(str(minval)+'<= '+binabrev+' <='+str(maxidlist[i]))

            def binfunc(idpercent):
                for i, minval in enumerate(minidlist):
                    if ((minval) <= idpercent) and ((maxidlist[i]) >= idpercent):
                        return binnames[i]
                return 'No Bin Found!'

            df[bincolname]=df.apply(lambda row: binfunc(row[bincol]),axis=1)

            return df

        def dfaddnumdatasets(mydf):
            outdf=mydf
            outdf['Type']='Data'
            outdf.index=range(len(outdf.index))
            for col in list(outdf):
                if np.issubdtype(outdf[col].dtype, np.number):
                    outdf[[col]] = outdf[[col]].apply(lambda x:pd.to_numeric(x,downcast='float'))

            if 'Database' in list(outdf):
                for method in mydf.Method.unique():
                    for database in mydf.Database.unique():
                        currdf = outdf[outdf.Database == database]
                        alldatasets = len(currdf['Dataset'].unique())
                        currdf = currdf[currdf.Method == method]
                        if not (len(currdf['Dataset'].unique()) == alldatasets):
                            print('Warning: Method ' + method + ' on Database ' + database + ' has less datasets than the whole database. '
                                  + str(len(currdf['Dataset'].unique())) + '/' + str(alldatasets) )
                        outdf= outdf.replace([database], [database+'/'+str(alldatasets)])

            return outdf

        def difbincalc(indf,mybincolname):
            newdf=indf.groupby(['Method','Database',mybincolname]).mean()
            #newdf.reset_index(inplace=True)

            allmethods=list(set([meth for meth, mydb, bincol in newdf.index.tolist()]))
            alldbs = list(set([mydb for meth, mydb, bincol in newdf.index.tolist()]))
            for method in allmethods:
                for db in alldbs:
                    currbins = list(set([bincol for meth, mydb, bincol in newdf.index.tolist() if (meth==method and mydb==db)]))
                    currbins.sort(key=lambda x: float(x.split('<')[0]))
                    if diffdirect=='left':
                        minbin=currbins[0]
                        maxbin=currbins[-1]
                    else:
                        minbin = currbins[-1]
                        maxbin = currbins[0]
                    newdf.loc[method,db,'maxdiff'] = newdf.loc[method,db,maxbin] - newdf.loc[method,db,minbin]
            outdf=newdf.iloc[newdf.index.get_level_values(mybincolname) == 'maxdiff'].copy()
            outdf.reset_index(level=2,drop=True,inplace=True)
            outdf.reset_index(inplace=True)
            return outdf

        def extremebincoladder(indf,statlist=None):
            if statlist==None:
                statlist=['Modeller Score', 'SP-Score', 'F-Score', 'TC']
            newdf = indf.copy()
            outdf=pd.DataFrame(data=None,columns={'Method','Database','Statistics','Extreme Bins Difference'})
            allmethods = newdf.Method.unique()
            alldbs = newdf.Database.unique()
            for method in allmethods:
                for db in alldbs:
                    for stat in statlist:
                        crit1=newdf['Method'].map(lambda x: x==method)
                        crit2 = newdf['Database'].map(lambda x: x == db)
                        tempdf=newdf[crit1 & crit2].copy()
                        tempdf.reset_index(inplace=True)
                        difval=tempdf.ix[0,stat]
                        outdf=outdf.append([{'Method':method,'Database':db,'Statistics':stat,'Extreme Bins Difference':difval}],ignore_index=True)
            return outdf

        def extractalinums(indf):
            olddblist=indf.Database.unique()
            if len(olddblist)==1:
                titlestr=str(olddblist[0].split('/')[-1]) +' alignments were used in the process of generating this figure.'
                indf = indf.replace([olddblist[0]], [olddblist[0].split('/')[0]])
                return indf,titlestr
            titlestr='For this figure, the numbers of alignments used in each benchmark are as follows: '
            for i,olddb in enumerate(olddblist):
                newdb=olddb.split('/')[0]
                numdb=olddb.split('/')[-1]
                if i==(len(olddblist)-1):
                    titlestr = titlestr +'and ' + str(numdb) + ' in ' + str(newdb) + '.'
                else:
                    titlestr=titlestr+str(numdb)+' in '+str(newdb) +', '
                indf = indf.replace([olddb], [newdb])
            return indf,titlestr

        for NucleicOrAmino in NucleicOrAminoList:

            prefix = outfolder + '/Scatter' + NucleicOrAmino + filedivext
            processeddfcsv = 'AverageOutput' + NucleicOrAmino + fulldataormethod + filedivext + '.csv'
            mymaintitle=maintitle
            if figureType == 'AverageScatterFullMethods':
                prefix = outfolder + '/Scatter' + NucleicOrAmino
            if figureType.startswith('AverageScatterFullDatasets'):
                prefix = outfolder + '/Scatter' + NucleicOrAmino
            if figureType.startswith('AverageTCFScoreScatterFull'):
                prefix = outfolder + '/Scatter' + NucleicOrAmino
            if figureType.startswith('TopMethodsAverageScatter'):
                prefix = outfolder + '/Scatter' + NucleicOrAmino + filedivext
                mymaintitle = 'Average ' + firstaxisname + ' vs ' + secondaxisname + ' of the top methods'
            if figureType.startswith('TopMethodsAverageTCFScoreScatter'):
                prefix = outfolder + '/Scatter' + NucleicOrAmino + filedivext
                mymaintitle = 'Average ' + firstaxisname + ' vs ' + secondaxisname + ' of the top methods'
            if figureType == 'AverageCompressionFullMethods' or figureType == 'AverageCompressionFullDatasets':
                prefix = outfolder + '/BarPlot' + NucleicOrAmino
            if figureType=='AverageStatBinnedFullDatasets' or figureType=='AverageStatBinnedFullMethods':
                prefix = outfolder+'/'+fileext+'Scatter'+axisname.replace(' ','') + NucleicOrAmino
                mymaintitle = 'Average ' + axisname + ' bined into different ' + shortname + ' levels'
                if figureType == 'AverageStatBinnedFullDatasets':
                    if dependtomethod:
                        mymaintitle=mymaintitle+' for the top methods'
                if figureType == 'AverageStatBinnedFullMethods':
                    if dependtomethod:
                        mymaintitle = mymaintitle + ' for all the methods'
            if figureType.startswith('MaskedVsUnMasked'):
                prefix = outfolder+'/'+'Scatter'+firstaxisname.replace(' ','') + NucleicOrAmino
                mymaintitle = 'Average ' + firstaxisname + ' vs ' + secondaxisname
                if figureType == 'AverageStatBinnedFullDatasets':
                    mymaintitle=mymaintitle+' for the top methods'
                if figureType == 'AverageStatBinnedFullMethods':
                    mymaintitle = mymaintitle + ' for all the methods'
            if figureType == 'AverageStatBinnedDiffFullDatasets':
                prefix = outfolder+'/'+fileext+'Scatter' + NucleicOrAmino
                mymaintitle = 'Extereme ' + shortname + ' bin averages difference for different statistics '
            if figureType.startswith('DefaultVsUndefault'):
                prefix = outfolder + '/Scatter' + NucleicOrAmino
            if scatterbining:
                prefix = outfolder + '/Scatter' + NucleicOrAmino + '-'+scatbinshortname.replace(' ','') + str(scatbinstatcounter)
            if specialflag1:
                prefix = outfolder + '/Scatterpdistvsfscorecontra'
            if figureType=='Histograms':
                prefix=outfolder + '/' + outpicfilenames + NucleicOrAmino
            if figureType=='AverageScatterCombinedDB':
                if justtopmethods:
                    prefix=outfolder + '/Scatter'+NucleicOrAmino+'CombinedDBTopMethods'
                else:
                    prefix = outfolder + '/Scatter' + NucleicOrAmino + 'CombinedDBAllMethods'
            print(prefix)

            if NucleicOrAmino == 'Amino':
                wrap = mainwrap
                maxmethodsperfigure = 50
            else:
                wrap = mainwrap
                maxmethodsperfigure = 50

            csvlist = []
            dblist = []
            for root, dirs, files in os.walk(inputfolder):
                for file in files:
                    if file.endswith('.csv'):
                        csvFile = str(os.path.join(root, file))
                        if not (NucleicOrAmino in csvFile):
                            continue
                        databasename = csvFile.split('/')[-1]
                        databasename = databasename.split('Data.csv', 1)[0]
                        csvlist.append(csvFile)
                        dblist.append(databasename)

            roselist = []
            nonroselist = []
            for db in dblist:
                if 'Rose' in db:
                    roselist.append(db)
                else:
                    nonroselist.append(db)

            roselist.sort()
            nonroselist.sort()

            sorteddblist = []
            sortedcsvlist = []
            for db in roselist:
                sorteddblist.append(db)
                sortedcsvlist.append(csvlist[dblist.index(db)])
            for db in nonroselist:
                sorteddblist.append(db)
                sortedcsvlist.append(csvlist[dblist.index(db)])

            firstflag = True
            aggregateddf = 'Empty'
            for i, db in enumerate(sorteddblist):
                currcsvfile = sortedcsvlist[i]
                currdb = db
                currdf = csv2datafram(currcsvfile, currdb)
                if currdf.empty:
                    continue
                if firstflag:
                    aggregateddf = currdf
                    firstflag = False
                else:
                    aggregateddf = pd.concat([currdf, aggregateddf])

            if isinstance(aggregateddf, basestring):
                continue
            if NucleicOrAmino == 'Nucleic':
                keepdbs = []
                for dbsim in aggregateddf.Database.unique():
                    if not 'Big' in dbsim:
                        keepdbs.append(dbsim)
                #if figureType=='AverageScatterFullDatasetsSimulated':
                #    keepdbs=['RoseSmallL1']
                aggregateddf = aggregateddf[aggregateddf['Database'].isin(keepdbs)]
            aggregateddf = aggregateddf[aggregateddf.Method != 'Praline']
            if figureType == 'NumSeqVsLength':
                aggregateddf = aggregateddf[aggregateddf.Method == 'ProbAlign']
            aggregateddf['Average Sequence Identity'] = aggregateddf.apply(
                lambda row: 1 - row['Average Pairwise P-Distance'], axis=1)
            aggregateddf = aggregateddf[aggregateddf['Number of Sequences'] < 26]
            aggregateddf = aggregateddf[aggregateddf['Number of Sequences'] > 3]
            if masking == True or figureType.startswith('MaskedVsUnMasked'):
                aggregateddf = aggregateddf[aggregateddf.Database.isin(['Sisyphus'])]
            if scatterbining:
                aggregateddf = aggregateddf[aggregateddf[scatterbinstat] > min_scatbinstat]
                aggregateddf = aggregateddf[aggregateddf[scatterbinstat] < max_scatbinstat]
            if aggregateddf.empty:
                continue

            commentwriting=True
            mysharey = mainsharey
            if specialflag1 or figureType == 'Histograms':
                aggregateddf = aggregateddf[aggregateddf.Method.isin(['ContrAlign'])]
            if combinedatabases:
                aggregateddf['Database'] = 'Datasets-Combined'
                figsize = 6 * resfactor
                markersize = 30 * mainmarkersize
                mysharey = True
                if dividebycategory:
                    continue
            elif dividebycategory:
                aggregateddf = aggregateddf[aggregateddf.Database != 'Homstrad']
                aggregateddf = SisyphusCatAdder(aggregateddf)
                aggregateddf = BaliBaseCatAdder(aggregateddf)
                aggregateddf = MattBenchCatAdder(aggregateddf)
            if justtopmethods:
                aggregateddf = aggregateddf[~aggregateddf.Method.isin(['DiAlign', 'KAlign', 'Prank', 'SAPD'])]
            aggregateddf = aggregateddf.sort_values(by=['Database'], ascending=True)
            if fulldataormethod == 'FullDatasets':
                aggregateddf = missingdatacompleter(aggregateddf)
            else:
                aggregateddf = dfbalancerByremoving(aggregateddf)
            if figureType.startswith('AverageStatBinnedFull') or figureType == 'AverageStatBinnedDiffFullDatasets':
                aggregateddf = idbinner(aggregateddf)
                #if not dependtomethod:
                #    aggregateddf=aggregateddf[aggregateddf.Method.isin(['ContrAlign'])]
                if figureType.startswith('AverageStatBinnedFull'):
                    commentwriting=False
                    bincountwriter(aggregateddf, prefix + '.' + 'comments')
            if converttomean==True:
                aggregateddf = df2mean(aggregateddf)
            else:
                aggregateddf = dfaddnumdatasets(aggregateddf)

            aggregateddf,alinumstr = extractalinums(aggregateddf)

            if figureType == 'AverageStatBinnedDiffFullDatasets':
                diffdf = difbincalc(aggregateddf,bincolname)
                gooddiffdf = extremebincoladder(diffdf)
            if commentwriting:
                commentadder(aggregateddf, prefix + '.' + 'comments')
            aggregateddf.to_csv(processeddfcsv)

            currmethods = []

            methoddict = {}
            for method in aggregateddf.Method.unique():
                currdf = aggregateddf[aggregateddf.Method == method]
                methoddict[method] = currdf["SP-Score"].mean()

            sorted_methods = sorted(methoddict.items(), key=operator.itemgetter(1))
            sorted_methods.reverse()
            sorted_methods = [method[0] for i, method in enumerate(sorted_methods)]

            Priority_list = ['BAliPhy-PD', 'ContrAlign', 'ProbAlign', 'LINSI', 'Prime', 'SAPD']
            for i, method in enumerate(Priority_list):
                if method in sorted_methods:
                    currmethods.append(method)
                    sorted_methods.remove(method)

            for i, method in enumerate(sorted_methods):
                currmethods.append(method)
                sorted_methods.remove(method)
            sorted_methods = currmethods[:]

            curr_color_dict = {}
            methodsorder = aggregateddf.Method.unique()
            mymethodsorder = sorted(methodsorder)
            methodsorder = sorted(methodsorder, key=len, reverse=True)
            for method in methodsorder:
                if method in colordict:
                    curr_color_dict[method] = colordict[method]
                else:
                    for i, color in enumerate(colors):
                        if not color in colordict.values() and not color in curr_color_dict.values():
                            curr_color_dict[method] = color
                            break

            mywrap = wrap
            if len(currdf.Database.unique()) <= mywrap and not (mywrap == 1):
                mywrap = len(currdf.Database.unique())
                adjustment = 0.8

            # The main plotting part
            defaultscatterplot = True
            if figureType == 'NumSeqVsLength':
                defaultscatterplot = False
                kws = dict(marker="D", s=markersize, linewidth=.5)
                if len(aggregateddf.Database.unique()) == 1 and not(masking):
                    g = sns.FacetGrid(aggregateddf, hue="Method",
                                      hue_order=mymethodsorder,
                                      palette=(curr_color_dict),
                                      sharey=mysharey,
                                      size=figsize)
                else:
                    g = sns.FacetGrid(aggregateddf, col="Database", col_wrap=mywrap, hue="Method",hue_order=mymethodsorder,
                                      palette=(curr_color_dict),
                                      sharey=mysharey,
                                      size=figsize)
                g = (g.map(plt.scatter, firstaxis, secondaxis, edgecolor="w", **kws))
                #plt.subplots_adjust(top=adjustment)
            if figureType.startswith('AverageStatBinnedFull'):
                if not dependtomethod:
                    aggregateddf=aggregateddf[aggregateddf.Method.isin(['ContrAlign'])]
                defaultscatterplot=False
                bins = aggregateddf[bincolname].unique()
                bins = sorted(bins, key=lambda x: float(x.split('<')[0]), reverse=True)
                aggregateddf.sort([bincol, 'Database'], ascending=[True, True], inplace=True)

                mycols = aggregateddf['Database'].unique()
                mycols = sorted(mycols)

                mymeths = sorted(aggregateddf['Method'].unique())
                if len(aggregateddf.Database.unique()) == 1  and not(masking):
                    if dependtomethod:
                        g = sns.factorplot(x=bincolname, y=axis, data=aggregateddf,
                                           hue='Method',
                                           kind="bar",
                                           row_order=bins, hue_order=mymeths,
                                           palette=curr_color_dict, size=figsize)
                    else:
                        g = sns.factorplot(x=bincolname, y=axis, data=aggregateddf,
                                           kind="bar",# row_order=bins,hue='Method',hue_order=mymeths,
                                           size=figsize)
                else:
                    if dependtomethod:
                        g = sns.factorplot(x=bincolname, y=axis, data=aggregateddf, col='Database', col_wrap=mywrap, hue='Method',
                                           kind="bar",
                                           row_order=bins, col_order=mycols, hue_order=mymeths,
                                           palette=curr_color_dict, size=figsize)
                    else:
                        g = sns.factorplot(x=bincolname, y=axis, data=aggregateddf, col='Database', col_wrap=mywrap,
                                           kind="bar", #row_order=bins, col_order=mycols,hue='Method',hue_order=mymeths,
                                           size=figsize)
                g.despine(left=True)
                g.set_xticklabels(rotation=90)
                #plt.subplots_adjust(top=adjustment)
            if figureType == 'AverageCompressionFullMethods' or figureType == 'AverageCompressionFullDatasets':
                defaultscatterplot = False
                allmeths = aggregateddf.Method.unique()
                allmeths.sort()
                priority_order = ['SAPD', 'BAliPhy-PD', 'SAWA', 'BPWA', 'BPMAP', 'ContrAlign', 'ProbAlign', 'MAFFT-G']
                method_ordered_list = []
                for cat in priority_order:
                    for method in allmeths:
                        if cat in method and not (method in method_ordered_list):
                            method_ordered_list.append(method)

                for method in aggregateddf.Method.unique():
                    if not method in method_ordered_list:
                        method_ordered_list.append(method)

                if len(aggregateddf.Database.unique()) == 1  and not(masking):
                    g = sns.factorplot(x="Method", y=firstaxis, data=aggregateddf,
                                       # order=method_ordered_list,
                                       order=mymethodsorder,
                                       kind="bar", palette=curr_color_dict, size=figsize)
                else:
                    g = sns.factorplot(x="Method", y=firstaxis, data=aggregateddf, col='Database', col_wrap=mywrap,
                                       #order=method_ordered_list,
                                       order = mymethodsorder,
                                       kind="bar", palette=curr_color_dict, size=figsize)
                g.despine(left=True)
                g.set_xticklabels(rotation=90)

                x = plt.gca().axes.get_xlim()
                g = g.map_dataframe(plt.plot, x, len(x) * [1], sns.xkcd_rgb["pale red"],
                                    label='Perfect ' + firstaxis)
                g = g.add_legend().set_axis_labels('Method', firstaxis)
                #plt.subplots_adjust(top=adjustment)
            if figureType == 'AverageStatBinnedDiffFullDatasets':
                defaultscatterplot=False
                mycols = gooddiffdf['Database'].unique()
                mycols = sorted(mycols)

                mymeths = sorted(gooddiffdf['Method'].unique())
                if len(aggregateddf.Database.unique()) == 1  and not(masking):
                    g = sns.factorplot(x='Statistics', y='Extreme Bins Difference', data=gooddiffdf, hue='Method',
                                       kind="bar", hue_order=mymeths,  # row_order=bins,
                                       palette=curr_color_dict, size=figsize)
                else:
                    g = sns.factorplot(x='Statistics', y='Extreme Bins Difference', data=gooddiffdf, col='Database',
                                       col_wrap=mywrap, hue='Method',
                                       kind="bar", col_order=mycols, hue_order=mymeths,  # row_order=bins,
                                       palette=curr_color_dict, size=figsize)
                g.despine(left=True)
                g.set_xticklabels(rotation=90)
                #plt.subplots_adjust(top=adjustment)
            if figureType=='Histograms':
                defaultscatterplot=False
                if len(aggregateddf.Database.unique()) == 1  and not(masking):
                    g = sns.FacetGrid(aggregateddf, hue="Method",hue_order=mymethodsorder,
                                      palette=(curr_color_dict), size=figsize, sharex=myshareax, sharey=myshareax)
                else:
                    g = sns.FacetGrid(aggregateddf, col="Database", col_wrap=mywrap, hue="Method",hue_order=mymethodsorder,
                                      palette=(curr_color_dict), size=figsize, sharex=myshareax, sharey=myshareax)
                g = (g.map(sns.distplot, firstaxis, hist=False, rug=True))
                #plt.subplots_adjust(top=adjustment)
            if defaultscatterplot:
                kws = dict(marker="D", s=markersize, linewidth=0)
                if len(aggregateddf.Database.unique())==1 and not(masking or figureType.startswith('MaskedVsUnMasked')):
                    g = sns.FacetGrid(aggregateddf, hue="Method",hue_order=mymethodsorder,
                                      palette=(curr_color_dict),sharey=mysharey,size=figsize)
                else:
                    g = sns.FacetGrid(aggregateddf, col="Database", col_wrap=mywrap, hue="Method",hue_order=mymethodsorder,
                                      palette=(curr_color_dict),sharey=mysharey,size=figsize)
                g = (g.map(plt.scatter, firstaxis, secondaxis, edgecolor="w", **kws).add_legend(markerscale=legendmarkerscale))
                #g=g.map(plt.scatter, firstaxis, secondaxis, edgecolor="w", **kws)

                #handles = g._legend_data.values()
                #labels = g._legend_data.keys()
                #g.fig.legend(handles=handles, labels=labels, bbox_to_anchor=(0.5, -0.1), loc='lower center', ncol=4)

                #plt.subplots_adjust(top=adjustment)

            if (dividebycategory):
                titleextension = ' divided by database categories'
            else:
                titleextension = ''
            if figureType == 'Histograms':
                if not myshareax:
                    titleextension = titleextension + ' (The vertical and horizontal axis ranges are not shared in subfigures)'
            else:
                if not mysharey:
                    titleextension = titleextension + ' (The vertical axis range is not the same range)'
            #g.fig.suptitle(mymaintitle + titleextension, size=int(16 * resfactor / 1.5))
            with open(prefix + '.' + 'title', "w") as text_file:
                text_file.write(mymaintitle + titleextension+'. '+alinumstr)
            g.savefig(prefix + '.' + 'png', bbox_inches='tight')
            g.savefig(prefix + '.' + 'eps', bbox_inches='tight')
            plt.cla()
            plt.clf()
            plt.close('all')

    defaultplots=True
    if figureType.startswith('AverageStatBinnedFull') or figureType=='AverageStatBinnedDiffFullDatasets':
        defaultplots=False
        for combinedatabases in combinedatabaseslist:
            for justtopmethods in justtopmethodslist:
                for w,dividebycategory in enumerate(dividebycategorylist):
                    for masking in maskinglist:
                        mymainwrap=mainwraplist[w]
                        for q, col in enumerate(binslist):
                            bincol = binslist[q]
                            bincolname = bincolnamelist[q]
                            binabrev = binabrevlist[q]
                            fileext = fileextlist[q]
                            minlist = minlists[q]
                            maxlist = maxlists[q]
                            shortname = shortnames[q]
                            if figureType.startswith('AverageStatBinnedDiffFull'):
                                diffdirect = difficultydirectionlist[q]

                            if figureType=='AverageStatBinnedDiffFullDatasets':
                                plotfunc()
                                continue

                            for p, teempaxis in enumerate(axislist):
                                axisname = axisnames[p]
                                axis = teempaxis
                                dependtomethod=dependtomethodlist[p]
                                if masking == True:
                                    axisname += '(masked)'
                                    axis = teempaxis + '(masked)'
                                plotfunc()
    if figureType=='Histograms':
        defaultplots=False
        for combinedatabases in combinedatabaseslist:
            for justtopmethods in justtopmethodslist:
                for y,dividebycategory in enumerate(dividebycategorylist):
                    for masking in maskinglist:
                        mymainwrap=mainwraplist[y]
                        for w,myfirstaxis in enumerate(myfirstaxislist):
                            myfirstaxisname=myfirstaxisnamelist[w]
                            outpicfilenames=outpicfilenameslist[w]
                            myshareax=myshareaxlist[w]
                            maintitle = 'Empirical Distribution of ' + myfirstaxisname + ' (KDE) of the benchmarks'
                            plotfunc()
    if figureType.startswith('MaskedVsUnMasked'):
        defaultplots = False
        for combinedatabases in combinedatabaseslist:
            for justtopmethods in justtopmethodslist:
                for w,dividebycategory in enumerate(dividebycategorylist):
                    for masking in maskinglist:
                        for vv,myfirstaxis in enumerate(myfirstaxislist):
                            myfirstaxisname = myfirstaxisnamelist[vv]
                            mysecondaxis = myfirstaxis + '(masked)'
                            mysecondaxisname = myfirstaxisname + '(masked)'
                            mymainwrap=mainwraplist[w]
                            if scatterbining:
                                scatbinstatcounter=0
                                for i, min_scatbinstat in enumerate(min_scatbinstat_list):
                                    max_scatbinstat = max_scatbinstat_list[i]
                                    scatbinstatcounter = scatbinstatcounter + 1
                                    maintitle='Average '+myfirstaxisname+' vs '+mysecondaxisname+' for datasets with ' \
                                              + str(min_scatbinstat) + '<'+scatbinshortnamefortitle+'<' + str(max_scatbinstat)
                                    plotfunc()
                                continue

                            plotfunc()

    if defaultplots:
        for combinedatabases in combinedatabaseslist:
            for justtopmethods in justtopmethodslist:
                for w,dividebycategory in enumerate(dividebycategorylist):
                    for masking in maskinglist:
                        mymainwrap=mainwraplist[w]
                        if scatterbining:
                            scatbinstatcounter=0
                            for i, min_scatbinstat in enumerate(min_scatbinstat_list):
                                max_scatbinstat = max_scatbinstat_list[i]
                                scatbinstatcounter = scatbinstatcounter + 1
                                maintitle='Average '+myfirstaxisname+' vs '+mysecondaxisname+' for datasets with ' \
                                          + str(min_scatbinstat) + '<'+scatbinshortnamefortitle+'<' + str(max_scatbinstat)
                                plotfunc()
                            continue

                        plotfunc()