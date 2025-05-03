
def Write_ExecuteLog(write_text):

  import os
  import datetime
  
  #フォルダがない場合は作る
  if os.path.isdir("Log") != False:
    os.mkdir('./Log')

  #ファイルがない場合は作る
  #ファイルをフォルダの中に作りたい
  
  #ファイル名：Log_yyyy-mm-dd.log
  filename = "/Log/" + str(datetime.date.today()) + ".log"
  
  with open(filename, "w") as o:
    print("[" + datetime.datetime.now() + "]" + write_text, file=o)
  

def Create_HTTPErrorMessage(status_code):
  return "Request Failed for Scraping Twitter by Python returned code " + str(status_code)
