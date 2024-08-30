from operation import Check, MathService
class large_num:
    @staticmethod
    def toStr(num: float) -> str:
        suffixes = [
            "", "k", "m", "b", "t", "qd", "qn", "sx", "sp", "oc", "No", "De", "UDe", "DDe", "TDe", 
            "QdDe", "QnDe", "SxDe", "SpDe", "OcDe", "NoDe", "Vt", "UVt", "DVt", "TVt", "QdVt", "QnVt", 
            "SxVt", "SpVt", "OcVt", "NoVt", "Tg", "UTg", "DTg", "TTg", "QdTg", "QnTg", "SxTg", "SpTg", 
            "OcTg", "NoTg", "qg", "Uqg", "Dqg", "Tqg", "Qdqg", "Qnqg", "Sxqg", "Spqg", "Ocqg", "Noqg", 
            "Qg", "UQg", "DQg", "TQg", "QdQg", "QnQg", "SxQg", "SpQg", "OcQg", "NoQg", "sg", "Usg", 
            "Dsg", "Tsg", "Qdsg", "Qnsg", "Sxsg", "Spsg", "Ocsg", "Nosg", "Sg", "USg", "DSg", "TSg", 
            "QdSg", "QnSg", "SxSg", "SpSg", "OcSg", "NoSg", "Og", "UOg", "DOg", "TOg", "QdOg", "QnOg", 
            "SxOg", "SpOg", "OcOg", "NoOg", "Ng", "UNg", "DNg", "QdNg", "QnNg", "SxNg", "SpNg", 
            "OcNg", "NoNg", "Ce", "UCe", "DCe"
        ]

        mag = 0
        while Check.meeq(abs(num), 1000) and mag < len(suffixes) - 1:
            mag = MathService.add(mag, 1)
            num = MathService.div(num, 1000.0)
        
        if Check.eq(num, int(num)):
            format = f"{int(num)}{suffixes[mag]}"
        elif Check.le(num, 10):
            format = f"{num:.2f}{suffixes[mag]}"
        else:
            format = f"{num:.1f}{suffixes[mag]}"

        return format