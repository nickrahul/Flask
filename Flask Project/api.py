import paralleldots

paralleldots.set_api_key("IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFtpLFigQEZlmmk")


def ner(text):
    response = paralleldots.ner(text)
    return response