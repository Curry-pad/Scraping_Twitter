#https://github.com/dsekz/twitter-x-xp-forwarded-for-header
def Get_XXpForwarded(
  guest_id,user_agent
):

  import twitter_xpff
  from twitter_xpff import XPFFHeaderGenerator

  #base_keyは、今のところは静的なもので、固定値らしい。
  #To understand how the base_key works, refer to the Reverse Engineering section. This key is hardcoded inside the WASM, so as long as you provide a valid guest_id, everything should function correctly. For now, there's no need for additional scraping since the key is not dynamic.
  #base_keyの仕組みを理解するには、「リバースエンジニアリング」セクションを参照してください。このキーはWASM内にハードコードされているため、有効なguest_idを提供する限り、すべてが正しく機能するはずです。今のところ、キーは動的ではないため、追加のスクレイピングは必要ありません。
  base_key = "0e6be1f1e21ffc33590b888fd4dc81b19713e570e805d4e5df80a493c9571a05"
  xpff_gen = XPFFHeaderGenerator(base_key)
  
  xpff_plain = '{"navigator_properties":{"hasBeenActive":"true","userAgent":"' + user_agent + '","webdriver":"false"},"created_at":' + Get_Timestamp_Milliseconds() + '}'
  
  encrypted = xpff_gen.generate_xpff(xpff_plain, guest_id)
  print("Encrypted:", encrypted)
  
  decrypted = xpff_gen.decode_xpff(encrypted, guest_id)
  print("Decrypted:", decrypted)

  return {
    "base_key" : base_key,
    "guest_id" : guest_id,
    "Encrypted" : encrypted,
    "Decrypted" : decrypted
  }

#現在時刻、ゼロ日付からの経過時間を、ミリ秒単位で返す。
def Get_Timestamp_Milliseconds():

  import time
  # 現在時刻を秒単位で取得
  current_time_seconds = time.time()
  # 秒からミリ秒に変換
  current_time_milliseconds = current_time_seconds * 1000
  print("現在時刻(ミリ秒):", current_time_milliseconds)

  #小数点以下切り捨て
  millisec_num = int(current_time_milliseconds)

  #文字列にしてから返却
  return str(millisec_num)


  
  


