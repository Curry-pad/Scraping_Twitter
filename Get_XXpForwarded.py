#https://github.com/dsekz/twitter-x-xp-forwarded-for-header
def Get_XXpForwarded(
  guest_id
):

  import twitter_xpff
  from twitter_xpff import XPFFHeaderGenerator

  #base_keyは、今のところは静的なもので、固定値らしい。
  #To understand how the base_key works, refer to the Reverse Engineering section. This key is hardcoded inside the WASM, so as long as you provide a valid guest_id, everything should function correctly. For now, there's no need for additional scraping since the key is not dynamic.
  #base_keyの仕組みを理解するには、「リバースエンジニアリング」セクションを参照してください。このキーはWASM内にハードコードされているため、有効なguest_idを提供する限り、すべてが正しく機能するはずです。今のところ、キーは動的ではないため、追加のスクレイピングは必要ありません。
  base_key = "0e6be1f1e21ffc33590b888fd4dc81b19713e570e805d4e5df80a493c9571a05"
  xpff_gen = XPFFHeaderGenerator(base_key)
  
  xpff_plain = '{"navigator_properties":{"hasBeenActive":"true","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36","webdriver":"false"},"created_at":1750014202073}'
  
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
