def vigenere_decrypt(ciphertext, key_length):
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decrypted_text = ''

    # Divide the ciphertext into blocks based on the key length
    blocks = [ciphertext[i::key_length] for i in range(key_length)]

    for block in blocks:
        # Calculate the most frequent letter in the block
        most_common_letter = max(set(block), key=block.count)
        shift = (ord(most_common_letter) - ord('E')) % 26  # Assuming 'E' is the most common English letter

        # Decrypt each character in the block
        for char in block:
            if char.isalpha():
                decrypted_char = chr(((ord(char.upper()) - ord('A') - shift) % 26) + ord('A'))
                decrypted_text += decrypted_char
            else:
                decrypted_text += char

    return decrypted_text

# Example usage
encrypted_message = "YYICSJIZIBAGYYXRIEWVIXAFNJOOVQQVHDLCRKLBSSLYXRIQYIIOXQTWXRICRVVKPBHZXIYLYZPDLCDIIKGFJUXRIPTFQGLCWVXRIEZRVNMYSFJDLCLRXOWJNMINXFNJSPJGHVVERJTTOOHRMVMBWNJTXKGJJJXYTSYKLOQZFTOSRFNJKBIYYSSHELIKLORFJGSVMRJCCYTCSVHDLCLRXOJMWFYBJPNVRNWUMZGRVMFUPOEBXKSDLCBZGUIBBZXMLMKKLOACXKECOCIUSBSRMPXRIPJZWXSPTRHKRQBVVOHRMVKEEPIZEXSDYYIQERJJRYSLJVZOVUNJLOWRTXSDLYYNEILMBKLORYWVAOXMKZRNLCWZRAYGWVHDLCLZVVXFFKASPJGVIKWWWVTVMCIKLOQYSWSBAFJEWRIISFACCMZRVOMLYYIMSSSKVISDYYIGMLPZICWFJNMVPDNEHISSFEHWEIJPSEEJQYIBWJFMICTCWYEZWLTKWKMBYYICGYWVGBSUKFVGIKJRRDSBJJXBSWMVVYLRMRXSWBNWJOVCSKWKMBYYIQYYWUMKRMKKLOKYYVWXSMSVLKWCAVVNIQYISIIBMVVLIDTIICSGSRXEVYQCCDLMZXLDWFJNSEPBRROOWJFMICSDDFYKWQMVLKWMKKLOVCXKFEXRFBIMEPJWSBWFJZWGMAPVHKRBKZIBGCFEHWEWSFXKPJTNCYYRTUICXPTPLOVIJVTDSRMVAOWRBYIBIRMVWERQJKWKRBDFYMELSFXPEGQKSPMLIYIBXFJPXRELPVHRMKFEHLEBJYMWKMTUFIIYSUXEVLJUXYAYWUXRIUJJXGEJPZRQSTJIJSIJIJSPWMKKKBEQXUSDXCIYIBIYSUXRIPJNMDLBFZWSIQFEHLYRYVVMYNXUSBSRMPWDMJQNSBIRMVTBIRYPWSPIIIICWQMVLKHNZKSXMLYYIZEJFTILYRSFADSFJIWEVNWZWOWFJWSERBNKAKWLTCSXKCWXVOILGLXZYPJNLSXCYYIBMZGFRKVMZEHDSRTJROGIMRHKPQTCSCXGYJKBICSTSVSPFEHGEQFJARMRJRWNSPTKLIWBWVWCXFJVQOVYQUGSXWBRWCSMSCIPXDFIFOLGSUECXFJPENZYSTINXFJXVYYLISIMEKJISEKFJIEXHFNCPSIPKFVDLCWVAOVCSFJKVKXESBLMZJICMLYYMCGMZEXBCMKKLOACXKEXHRMVKBSSSUAKWSSKMVPCIZRDLCFWXOVLTFRDLCXLRCLMSVLYXGSKLOMPKRGOWDTIXRIPJNIBILTKVOIQYFSPJCWKLOQQMRHOWMYYEDFCKFVORGLYXNSPTKLIELIKSDSYSUXRIJNFRGIPJKMBIBFEHVEWIFAXYNTEXRIEWRWCELIWIVPYXCIOTUNKLDLCBFSNQYSRRNXFJJGKVCHISGOCJGMXKUFKGR"
key_length = 6

decrypted_result = vigenere_decrypt(encrypted_message, key_length)
print("Decrypted message:", decrypted_result)
