
def Write_ExecuteLog(write_text):

  import os
  
  #フォルダがない場合は作る
  os.mkdir('./Log')

  #ファイルがない場合は作る
  #ファイルをフォルダの中に作りたい
  
  #ファイル名：Log_yyyymmdd.log
  filename = str(datetime.date.today()) + ".log"
  
  with open(filename, "w") as o:
    print(write_text, file=o)
  
