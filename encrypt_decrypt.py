########################################################
# encrypt()
# stream cipher: takes a line at a time and encrypts it 
# return the encrypted string 
# ###################################################### 
  
def encrypt(account):
    encryptAcct = ''
    firstKey = {'a': '/', 'b':'@', 'c':'T','d':'r', 'e':'$','f':'D','g':'s',
                        'h':'^','i':'b','j':'Q','k':'8','l':'a','m':')','A':'#','B':'l',
                        'C':'E','D':'1','E':'%','F':'9','G':'*','H':'w','I':'5','J':'!','K':'A',
                        'L':'(','M':'x','0':'H','1':'j', '2':'y','3':'u','4':'2','n':'3','o':'[',
                        'p':'6','q':'Z','r':'B','s':'0','t':'V','u':'-','v':'+','w':'S','x':'F',
                        'y':'4','z':'{','N':'L','O':'J','P':'C','Q':'g','R':'P','S':';','T':'>',
                         'U':'o','V':'q','W':'.','X':'O','Y':'p','Z':'G','5':'U','6':'i','7':'k',
                         '8':'K','9':']', '.':'_'}


    for line in str(account):
        encryptAcct = encryptAcct + firstKey.get(line, encryptAcct)

    return encryptAcct

####################################################
# decrypt()
# decrypts line at a time
# returns the original string
####################################################              
    
def decrypt(account):
    decryptStr = ''
    decryptKey = {'/': 'a', '@':'b', 'T':'c','r':'d', '$':'e','D':'f','s':'g',
                        '^':'h','b':'i','Q':'j','8':'k','a':'l',')':'m','#':'A','l':'B',
                        'E':'C','1':'D','%':'E','9':'F','*':'G','w':'H','5':'I','!':'J','A':'K',
                        '(':'L','x':'M','H':'0','j':'1', 'y':'2','u':'3','2':'4','3':'n','[':'o','6':'p','Z':'q','B':'r','0':'s','V':'t','-':'u','+':'v','S':'w',
                         'F':'x','4':'y','{':'z','L':'N','J':'O','C':'P','g':'Q','P':'R',';':'S','>':'T',
                         'o':'U','q':'V','.':'W','O':'X','p':'Y','G':'Z','U':'5','i':'6','k':'7','K':'8',']':'9', '_':'.'}
        
    for line in str(account):
        decryptStr = decryptStr + decryptKey.get(line, ' ')
                
    return decryptStr

# TESTING ################################
# user = encrypt("Sabrina Lugo")
# print("User's name: ", user)
# print("User's name: ", decrypt(user))
##########################################

