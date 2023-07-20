import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom


def generateConfig(fmId, isTeam, fileDir, bigFolder, iconFolder):
    # root = ET.Element("record")

    # # Create Elements
    # bool1 = ET.Element("boolean", id="preload", value="false")
    # bool2 = ET.Element("boolean", id="amap", value="false")
    # ids = ET.Element("list", id="maps")

    # # Append to root
    # root.append(bool1)
    # root.append(bool2)

    # # Generate image ID XML section
    # if isTeam == True:
    #     small = ET.Element(
    #         "record",
    #         {"from": "{}{}".format(iconFolder, fmId)},
    #         to="graphics/pictures/club/{}/icon".format(fmId),
    #     )

    #     big = ET.Element(
    #         "record",
    #         {"from": "{}{}".format(bigFolder, fmId)},
    #         to="graphics/pictures/club/{}/logo".format(fmId),
    #     )
    # elif isTeam == False:
    #     small = ET.Element(
    #         "record",
    #         {"from": "{}{}".format(iconFolder, fmId)},
    #         to="graphics/pictures/person/{}/icon".format(fmId),
    #     )
    #     big = ET.Element(
    #         "record",
    #         {"from": "{}{}".format(bigFolder, fmId)},
    #         to="graphics/pictures/person/{}/portrait".format(fmId),
    #     )

    if isTeam:
        xml_str = '''
        <record>
            <boolean id="preload" value="false"/>
            <boolean id="amap" value="false"/>
            <list id="maps">
                <record from_="{}{}" to="graphics/pictures/club/{}/icon"/>
                <record from_="{}{}" to="graphics/pictures/club/{}/logo"/>
            </list>
        </record>'''.format(iconFolder, fmId, fmId, bigFolder, fmId, fmId)
    else:
        xml_str = '''
        <record>
            <boolean id="preload" value="false"/>
            <boolean id="amap" value="false"/>
            <list id="maps">
                <record from="{}{}" to="graphics/pictures/person/{}/icon"/>
                <record from="{}{}" to="graphics/pictures/person/{}/portrait"/>
            </list>
        </record>'''.format(iconFolder, fmId, fmId, bigFolder, fmId, fmId)


    # Correct XML formatting
    root = ET.fromstring(xml_str)
    tree = ET.ElementTree(root)
    tree = ET.tostring(root, encoding="utf-8", method="xml")
    reparsed = minidom.parseString(tree)
    tree = reparsed.toprettyxml()

    # Write to file
    with open(fileDir, "w") as f:
        f.write(tree)
        f.close()
