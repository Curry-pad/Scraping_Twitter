
def Write_ExecuteLog(write_text):

  import os
  
  #フォルダがない場合は作る
  os.mkdir('./Log')

  #ファイルがない場合は作る
  #ファイルをフォルダの中に作りたい
  
  #ファイル名：Log_yyyy-mm-dd.log
  filename = str(datetime.date.today()) + ".log"
  
  with open(filename, "w") as o:
    print(write_text, file=o)
  

def Create_HTTPErrorMessage(status_code):
  return "Request Failed for Scraping Twitter by Python returned code " + str(status_code)
