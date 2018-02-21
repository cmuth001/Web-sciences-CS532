from boilerpipe.extract import Extractor

file = open("output/rawHtml/00790905a8fe79685c242150d32c8fbb.html", "r") 
extractor = Extractor(extractor='ArticleExtractor', html=file.read())

print(extractor.getText())
# print(file.read())
