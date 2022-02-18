# class Solution:
#     def validIPAddress(self, queryIP: str) -> str:
#         IP_v4 = queryIP.split('.')
#         IP_v6 = queryIP.split(':')

#         if len(IP_v4)==4:
#             #if ipv4
#             if any([x=="" for x in IP_v4]) or any([x.startswith('0') for x in IP_v4]) or len(IP_v4)!=4 or any([ch.isalpha() for x in queryIP for ch in x ]) or any([int(x)>255 for x in IP_v4]) or queryIP.count('.')!=3 :
#                 return "Neither"
#             else:
#                 return "IPv4"
#         elif len(IP_v6)==8:
#             print("ipv6")
#             #if ipv6
#             # print(any([((int(ch) <0 or int(ch)>9) or
#             # (ch < 'A' or ch > 'F') or ((ch < 'a' or ch > 'f'))) for x in IP_v6 for ch in list(x)]))

#             if any([len(x)>4 for x in IP_v6]) or any([((ch < '0' or ch > '9') or
#             (ch < 'A' or ch > 'F') or ((ch < 'a' or ch > 'f'))) for x in IP_v6 for ch in list(x)]) or queryIP.count(':')!=7:
#                 return "Neither"
#             else:
#                 return "IPv6"
        # else:
        #     return "Neither"
        
        
        
        
        
        
import re
class Solution:
    chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
    patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + r'\.){3}' + chunk_IPv4 + r'$')
    
    chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
    patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + r'\:){7}' + chunk_IPv6 + r'$')

    def validIPAddress(self, IP: str) -> str:        
        if self.patten_IPv4.match(IP):
            return "IPv4"
        return "IPv6" if self.patten_IPv6.match(IP) else "Neither" 