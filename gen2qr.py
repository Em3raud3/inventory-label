import pyqrcode
import svgwrite
import io
import xml.etree.ElementTree as ET
import random
import string
import cairosvg
#import safeRandom


# create an DMC QR code
def genQrPath(qr_text):
    # create qr code
    url = pyqrcode.create(qr_text)
    buffer = io.BytesIO()
    # save it as svg in buffer
    url.svg(buffer, scale=4.6, quiet_zone=0, xmldecl=False, svgns=False)
    # convert svg xml string to xml ElementTree for easier extraction of desire data
    # print(buffer.getvalue().decode("utf-8"))
    root = ET.fromstring(buffer.getvalue().decode("utf-8"))
    s = "Error No Data"
    # find path in tree
    for partElm in root.iter('path'):
        s = partElm.attrib['d']

    return s

# combine two QR codes into a single image
# this is done to create smaller proptry stickers (2 property tag images in 1 sticker)


def genMainXml(txt1, txt2, pathString,
               secondtxt2, secondpathString,
               thirdtxt3, thirdpatchString,
               fourthtxt4, fourthpathString,
               fifthtxt5, fifthpathString,
               sixthtxt6, sixthpathString):
    # size = {width, height)
    # dwg = svgwrite.Drawing(size=(220, 140))
    dwg = svgwrite.Drawing(size=(345, 280))

    nameExtra = {"font-weight": "bold", "font-size": "8px"}
    dwg.add(dwg.text(txt1, insert=(5, 10), fill='black', **nameExtra))
    dwg.add(dwg.text(txt1, insert=(123, 10), fill='black', **nameExtra))
    dwg.add(dwg.text(txt1, insert=(243.5, 10), fill='black', **nameExtra))
    dwg.add(dwg.text(txt1, insert=(5, 150), fill='black', **nameExtra))
    dwg.add(dwg.text(txt1, insert=(123, 150), fill='black', **nameExtra))
    dwg.add(dwg.text(txt1, insert=(243.5, 150), fill='black', **nameExtra))

    NumberExtra = {"class": "heavy", "font-weight": "bold",
                   "font-size": "24px", "font-family": "monospace"}
    dwg.add(dwg.text(txt2, insert=(6, 32), fill='black', **NumberExtra))
    dwg.add(dwg.text(secondtxt2, insert=(126, 32), fill='black', **NumberExtra))
    dwg.add(dwg.text(thirdtxt3, insert=(246, 32), fill='black', **NumberExtra))
    dwg.add(dwg.text(fourthtxt4, insert=(6, 172), fill='black', **NumberExtra))
    dwg.add(dwg.text(fifthtxt5, insert=(126, 172), fill='black', **NumberExtra))
    dwg.add(dwg.text(sixthtxt6, insert=(246, 172), fill='black', **NumberExtra))

    # print(dwg.()) save
    pathExtra = {"transform": "scale(3) translate(0 12)", "stroke": "#000"}
    dwg.add(dwg.path(d=pathString, **pathExtra))

    pathExtra2 = {"transform": "scale(3) translate(40 12)", "stroke": "#000"}
    dwg.add(dwg.path(d=secondpathString, **pathExtra2))

    pathExtra3 = {"transform": "scale(3) translate(80 12)", "stroke": "#000"}
    dwg.add(dwg.path(d=secondpathString, **pathExtra3))

    pathExtra4 = {"transform": "scale(3) translate(0 59)", "stroke": "#000"}
    dwg.add(dwg.path(d=secondpathString, **pathExtra4))

    pathExtra5 = {"transform": "scale(3) translate(40 59)", "stroke": "#000"}
    dwg.add(dwg.path(d=secondpathString, **pathExtra5))

    pathExtra6 = {"transform": "scale(3) translate(80 59)", "stroke": "#000"}
    dwg.add(dwg.path(d=secondpathString, **pathExtra6))
    return dwg.tostring()


def genqr(txt1, txt2, qr_text, serial2, qr_text2, serial3, qr_text3, serial4, qr_text4, serial5, qr_text5, serial6, qr_text6):
    d = genQrPath(qr_text)
    d2 = genQrPath(qr_text2)
    d3 = genQrPath(qr_text3)
    d4 = genQrPath(qr_text4)
    d5 = genQrPath(qr_text5)
    d6 = genQrPath(qr_text6)

    return genMainXml(txt1, txt2, d, serial2, d2, serial3, d3, serial4, d4, serial5, d5, serial6, d6)

    # for partElm in root.iter('{http://www.w3.org/2000/svg}path'):
    #  s = partElm.attrib['d']


# def genSerialNumber(numDigits):
#  return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(numDigits))

def createQrCodes(numStickers, safeR, placeDir, numDigits):
    for i in range(0, numStickers):
        serialNum = safeR.safeId(numDigits)
        serialNum2 = safeR.safeId(numDigits)
        serialNum3 = safeR.safeId(numDigits)
        serialNum4 = safeR.safeId(numDigits)
        serialNum5 = safeR.safeId(numDigits)
        serialNum6 = safeR.safeId(numDigits)
        data = genqr("Data Machines Corp.",
                     serialNum, "https://dmc.sh/p?SN="+serialNum,
                     serialNum2, "https://dmc.sh/p?SN="+serialNum2,
                     serialNum3, "https://dmc.sh/p?SN="+serialNum3,
                     serialNum4, "https://dmc.sh/p?SN="+serialNum4,
                     serialNum5, "https://dmc.sh/p?SN="+serialNum5,
                     serialNum6, "https://dmc.sh/p?SN="+serialNum6)
        cairosvg.svg2png(bytestring=data, write_to=placeDir +
                         "/"+serialNum+"_"+serialNum2+"_"+serialNum3+"_"+serialNum4+"_"+serialNum5+"_"+serialNum6+".png")


def createStickersForPage(numStickers, safeR, placeDir, numDigits):
    createQrCodes(numStickers, safeR, placeDir, numDigits)
