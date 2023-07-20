import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom


def generateConfig(fmId, isTeam, fileDir, iconFolder, bigFolder):
    root = ET.Element("record")

    # Create Elements
    bool1 = ET.Element("boolean", id="preload", value="false")
    bool2 = ET.Element("boolean", id="amap", value="false")
    ids = ET.Element("list", id="maps")

    # Append to root
    root.append(bool1)
    root.append(bool2)

    # Generate image ID XML section
    if isTeam == True:
        small = ET.Element(
            "record",
            from_="{}{}".format(iconFolder, fmId),
            to="graphics/pictures/club/{}/icon".format(fmId),
        )

        big = ET.Element(
            "record",
            from_="{}{}".format(bigFolder, fmId),
            to="graphics/pictures/club/{}/logo".format(fmId),
        )
    elif isTeam == False:
        small = ET.Element(
            "record",
            from_="{}{}".format(iconFolder, fmId),
            to="graphics/pictures/person/{}/icon".format(fmId),
        )
        big = ET.Element(
            "record",
            from_="{}{}".format(bigFolder, fmId),
            to="graphics/pictures/person/{}/portrait".format(fmId),
        )

    # Append to root
    ids.append(small)
    ids.append(big)
    root.append(ids)

    # Correct XML formatting
    tree = ET.ElementTree(root)
    tree = ET.tostring(root, encoding="utf-8", method="xml")
    reparsed = minidom.parseString(tree)
    tree = reparsed.toprettyxml()

    # Write to file
    with open(fileDir, "w") as f:
        f.write(tree)
        f.close()
