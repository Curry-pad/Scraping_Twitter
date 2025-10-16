#https://github.com/dsekz/twitter-x-xp-forwarded-for-header
def Get_XXpForwarded(
  guest_id,user_agent
):

  #もしもguest_idの登録がない場合は、ダミー値を設定して終了
  if(guest_id == "undefined"):
    return {
      "base_key" : "",
      "guest_id" : guest_id,
      "Encrypted" : "119ee12fa18e9a0e0d9a160e7f730da5c071238572a4d832e01c3cc95d37f116145129fed2ff53622eb59778978b9c9b3b36c0004ff8b9cc218d81aaacb6103d5b77a21f98c19ecc75403342ae7a1a978a9f67b45a857cf1ce3eb51a94f1ea6969ca24a16c5006b82a82f3690f1f617dd18e6d6f703765323e925fe01d4f5a3b80849bc4c2c1a4d705270f0bffaee911fe0adde73cfdd218d1cb0938d6e4f311514a654be0195d520bda7067ff0741500cab341941d30ef199fc90f6aa850ce229a4f5a29c711dff5bb0ca010d0dc5acf05812aacb2eb0e39a42efb4829a6eaf3794406ef29af7d43efb94fdf923d70ac5339a8cd6d949b443ab",
      "Decrypted" : ""
    }

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


  
  


