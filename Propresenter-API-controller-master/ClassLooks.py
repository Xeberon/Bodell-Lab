class looks:
    def __init__(self, uuid, name, index, lookcontent):
        #info needed from looks is uuid, name, index, bool toggles for io layers, current mask, current presentation theme
        self.uuid = uuid
        self.name = name
        self.index = index
        self.lookcontent = []
    
    def add_content(self, cmask, bmessages, bprops, bannouncements, cpresentation, bslide, bmedia, bvideoin, lookcontent):
        self.cmask = cmask
        self.bmessages = bmessages
        self.bprops = bprops
        self.bannouncements = bannouncements
        self.cpresentation = cpresentation
        self.bslide = bslide
        self.bmedia = bmedia
        self.bvideoin = bvideoin
        self.content.append(lookcontent)



