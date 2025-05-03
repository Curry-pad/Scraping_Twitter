
def Write_ExecuteLog(write_text):

  import os
  import datetime
  
  #フォルダがない場合は作る
  if os.path.isdir("Log") != True:
    os.mkdir('./Log')
    print("フォルダを作りました")

  #ファイルがない場合は作る
  #ファイルをフォルダの中に作りたい
  fileName = str(datetime.date.today()) + ".log"

  #ファイル名：Log_yyyy-mm-dd.log
  filePath = "./Log/" + fileName
  
  if os.path.isfile(filePath) != True:
    print("ファイルがない")
  
  with open(filePath, "w") as o:
    print("[" + str(datetime.datetime.now()) + "]" + write_text, file=o)
  

def Create_HTTPErrorMessage(status_code):
  return "Request Failed for Scraping Twitter by Python returned code " + str(status_code)
