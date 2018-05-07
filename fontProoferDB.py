from math import floor
import datetime

fontList = [u"/Library/Application Support/Adobe/Fonts/ResursSans-BlackBETA.otf", u"/Library/Application Support/Adobe/Fonts/ResursSans-BoldBETA.otf", u"/Library/Application Support/Adobe/Fonts/ResursSans-BookBETA.otf", u"/Library/Application Support/Adobe/Fonts/ResursSans-DisplayBETA.otf", u"/Library/Application Support/Adobe/Fonts/ResursSans-HeavyBETA.otf", u"/Library/Application Support/Adobe/Fonts/ResursSans-RegularBETA.otf"]

#Page Size
w = 210
h = 297

#Glyph font size
fontSize = 75

#Margin of the top Bar
tab = 5
#Side margin of the page
margin = 10


#Number of line and column (count+1)
line = 1
column = 2
width = (w/(line + 1)) - margin
height = (h - tab) / (column + 1)

#Small text font Parameters
monoFont = 'FedraMono-Book'
monoSize = 3

def reset():                
    newPage(w, h)
    global line
    line = 1
    global column
    column = 2
    
def pageTab(fontName, numberPage):
    if(numberPage != 0):
        reset()
    else:
        numberPage+=1
    tabTxt = FormattedString()
    tabTxt.font(monoFont)
    tabTxt.fontSize(monoSize)
    tabTxt.tabs((margin, "left"), (w/3, "left"), (w-30, "right"))
    tabTxt += fontName + "\t" + now.strftime("%Y-%m-%d %H:%M") + "\t" + "page n°" + str(numberPage)
    textBox(tabTxt, (margin, h-tab-5, w-margin, tab))
    
#Setting default Values
now = datetime.datetime.now()
oldFontPath = False
numberPage = 0
size(w, h)

for fontPath in fontList:
    if oldFontPath:
        uninstallFont(oldFontPath)
    currentFont = installFont(fontPath)
    fontName = font(currentFont, fontSize=fontSize)
    #listOpenTypeFeature(currentFont)
    #listFontVariations(currentFont)
    ascenderHeight = fontAscender()
    xHeight = fontXHeight()
    #print ascenderHeight
    fontGlyphs = listFontGlyphNames() 
    print fontName
    
    pageTab(fontName, numberPage)
    numberPage+=1
    
    for glyph in fontGlyphs:
        #print glyph
        glyphName = glyph
        
        txt = FormattedString()
        txt.font(currentFont)
        txt.fontSize(fontSize)
        txt.align('center')
        txt.appendGlyph(glyph)
        textBox(txt, ( (line * width) + margin, column * height, width, height ) )
        
        name = FormattedString()
        name.font(monoFont)
        name.fontSize(monoSize)
        name.align('left')
        name += glyphName
        textBox(name, ( (line * width) + margin, column * height + xHeight , 20, 20 ) )
        
        if line >0:
            line = line - 1
        else:
            line = 1
            if column>0:
                column = column -1
            else:
                pageTab(fontName, numberPage)
                numberPage+=1
                column = 2
        
    
    oldFontPath = fontPath
    print 'done'

saveImage(u"~/Desktop/PDF/" + now.strftime("%Y-%m-%d %H:%M") + "_" + fontName + "_proof.pdf")
print 'PDF Saved'