#https://github.com/dsekz/twitter-x-xp-forwarded-for-header
def Create_XXpForwarded():

  import twitter_xpff
  from twitter_xpff import XPFFHeaderGenerator

  base_key = "0e6be1f1e21ffc33590b888fd4dc81b19713e570e805d4e5df80a493c9571a05"
  xpff_gen = XPFFHeaderGenerator(base_key)
  
  guest_id = "v1%3A174849298500261196"
  xpff_plain = '{"navigator_properties":{"hasBeenActive":"true","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36","webdriver":"false"},"created_at":1750014202073}'
  
  encrypted = xpff_gen.generate_xpff(xpff_plain, guest_id)
  print("Encrypted:", encrypted)
  
  decrypted = xpff_gen.decode_xpff(encrypted, guest_id)
  print("Decrypted:", decrypted)
