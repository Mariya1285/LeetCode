class Codec:
    def __init__(self):
        self.mapping_var = dict()
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.mapping_var[longUrl] = "http://tinyurl.com/"+str(hash(longUrl))
        return self.mapping_var[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        for key, val in self.mapping_var.items():
            if val == shortUrl:
                return key
       
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))