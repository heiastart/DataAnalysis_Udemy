from ftplib import FTP, error_perm
import os
import glob
import pandas
import numpy
import patoolib
import seaborn as sns
import simplekml



def ftpDownloader(stationId, startYear, endYear, url="ftp.pyclass.com", user="student@pyclass.com",
                  passwd="student123"):
    ftp = FTP(url)
    ftp.login(user, passwd)
    if not os.path.exists("C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\rawData"):
        os.makedirs("C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\rawData")
    os.chdir("C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\rawData")
    for year in range(startYear, endYear + 1):
        fullpath = '/Data/%s/%s-%s.gz' % (year, stationId, year)
        filename = os.path.basename(fullpath)
        try:
            with open(filename, "wb") as file:
                ftp.retrbinary('RETR %s' % fullpath, file.write)
            print("%s succesfully downloaded" % filename)
        except error_perm:
            print("%s is not available" % filename)
            os.remove(filename)
    ftp.close()


def extractFiles(indir="C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\rawData",
                 out="C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\rawData\\Extracted"):
    os.chdir(indir)
    archives = glob.glob("*.gz")
    print(archives)
    if not os.path.exists(out):
        os.makedirs(out)
    files = os.listdir("Extracted")
    print(files)
    for archive in archives:
        if archive[:-3] not in files:
            patoolib.extract_archive(archive, outdir=out)


def addField(indir="C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\rawData\\Extracted"):
    os.chdir(indir)
    fileList = glob.glob("*")
    print("fileList", fileList)
    for filename in fileList:
        df = pandas.read_csv(filename, sep='\s+', header=None)
        df["Station"] = [filename.rsplit("-", 1)[0]] * df.shape[0]
        df.to_csv(filename + ".csv", index=None, header=None, sep=';')
        os.remove(filename)


def concatenate(indir="C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\rawData\\Extracted",
                outfile="C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\rawData\\Extracted\\Concatenated.csv"):
    os.chdir(indir)
    fileList = glob.glob("*.csv")
    dfList = []
    colnames = ["Year", "Month", "Day", "Hour", "Temp", "DewTemp", "Pressure", "WindDir", "WindSpeed", "Sky", "Precip1",
                "Precip6", "ID"]
    for filename in fileList:
        print(filename)
        df = pandas.read_csv(filename, header=None, sep=';')
        dfList.append(df)
    concatDf = pandas.concat(dfList, axis=0)
    concatDf.columns = colnames
    concatDf.head()
    concatDf.to_csv(outfile, index=None, sep=';')


def merge(left="C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\rawData\\Extracted\\Concatenated.csv",
          right="C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\station-info.txt",
          output="C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\rawData\\Extracted\\Concatenated-Merged.csv"):
    leftDf = pandas.read_csv(left, sep=';')
    rightDf = pandas.read_fwf(right, converters={"USAF": str, "WBAN": str})
    rightDf["USAF_WBAN"] = rightDf["USAF"] + "-" + rightDf["WBAN"]
    mergedDf = pandas.merge(leftDf, rightDf.loc[:, ["USAF_WBAN", "STATION NAME", "LAT", "LON"]], left_on="ID",
                            right_on="USAF_WBAN")
    mergedDf.to_csv(output, sep=';')


def pivot(
        infile="C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\rawData\\Extracted\\Concatenated-Merged.csv",
        outfile="C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\rawData\\Extracted\\Pivoted.csv"):
    df = pandas.read_csv(infile, sep=';')
    df = df.replace(-9999, numpy.nan)
    df['Temp'] = df["Temp"] / 10.0
    table = pandas.pivot_table(df, index=["ID","LON","LAT","STATION NAME"], columns="Year", values="Temp")
    table.to_csv(outfile, sep=';')
    return table


def plot(outfigure='C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\visualization\\pivoted_plot.png'):
    df = pivot()
    #fig = df.T.plot(subplots=True, kind='bar').get_figure()
    #fig.savefig(outfigure, dpi=200) 
    df.T.plot(subplots=True, kind='bar')
    sns.plt.savefig(outfigure, dpi=200)


def kml(input='C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\archives\\rawData\\Extracted\\Pivoted.csv', output='C:\\Users\\heias\\AnacondaProjects\\DataAnalysis_Udemy\\KML\\Weather.kml'):
    kml = simplekml.Kml()
    df = pandas.read_csv(input, index_col=["ID","LON","LAT","STATION NAME"], sep=';')   
    for lon,lat,name in zip(df.index.get_level_values("LON"), df.index.get_level_values("LAT"), df.index.get_level_values("STATION NAME")):
        kml.newpoint(name=name, coords=[(lon,lat)])
        kml.save(output)

if __name__ == "__main__":  
    stationsIdString = input("Enter stat.names divided by commas: ")
    startingYear = int(input("Enter starting year: "))
    endingYear = int(input("Enter ending year: "))
    stationsIdList = stationsIdString.split(',')
    
    for station in stationsIdList:
        ftpDownloader(station,startingYear,endingYear)
        
    extractFiles()
    addField()
    concatenate()
    merge()
    pivot()
    kml()
    plot()
   
    
    