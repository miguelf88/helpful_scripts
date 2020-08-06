####
# This function evaluates the place type field in CommunityViz and assigns a broader
# community type to the record
###

# Green fields
gf = ["POS", "WF", "RL", "ROS", "ROW", "0"]

#  Employment, goods & services
egs = ["MC", "SCC", "SOC", "REC"]

# Urban Walkable community
uwc = ["WAC", "TC", "TAC"]

# Living spaces
ls = ["UN", "LLR", "MHN", "SFN", "THC", "MFN", "WN"]

# Education, medical and institutional
emi = ["CSA", "GAA", "CIV", "SD", "UC", "UCD", "EC", "HCC"]

# Manufacturing
m = ["HI", "LI"]

def classify_pt(land_use):
    if land_use in gf:
        return "Green Fields"
    elif land_use in egs:
        return "Employment, Goods & Services"
    elif land_use in uwc:
        return "Urban Walkable Community"
    elif land_use in ls:
        return "Living Spaces"
    elif land_use in emi:
        return "Education, Medical & Institutional"
    else:
        return "Manufacturing"
