from sartopo_python import SartopoSession
import time
import json

# def pucb(*args):
#     print("pucb called with args "+str(args))

# def gucb(*args):
#     print("gucb called with args "+str(args))

# def nfcb(*args):
#     print("nfcb called with args "+str(args))

# def dfcb(*args):
#     print("dfcb called with args "+str(args))

# open a session
sts=SartopoSession('sartopo.com',
# sts=SartopoSession('localhost:8080',
        configpath='../../sts.ini',
        # mapID='[NEW]',
        # mapID='[NEW]new4240',
        # mapID='[NEW]SAR:new4240',
        # mapID='[NEW]test:new4240',
        # mapID='QDJKMQQ',
        # mapID='CA4L4',
        mapID='DEKFJ',
        # syncInterval=10,
        # syncDumpFile='syncDump',
        # propertyUpdateCallback=pucb,
        # geometryUpdateCallback=gucb,
        # newFeatureCallback=nfcb,
        # deletedFeatureCallback=dfcb,
        account='caver456@gmail.com')

# sts.addLine([[39,-120],[39.1,-120]],'a')
# sts.addLine([[39,-120,1,2],[39.1,-120,1,2]],'b')

# sts.addLine([[-120.1,39],[-120.1,39.1]],'a')
# sts.addLine([[-120.1,39,1,2],[-120.1,39.1,1,2]],'b')

sts.addLine([[80,80,1,2],[80.1,80,1,1,2]],'a')

# sts.getFeatures('Shape')
# print('account data:')
# d=sts.getAccountData()
# with open('accountData.json','w') as f:
#         json.dump(d,f,indent=3)

# sts.openMap('CA4L4')
# sts._stop() # stop sync
# time.sleep(120)

# fid=sts.addFolder('newFolder')
# sts.addMarker(39,-120,'newMarker',description='desc',color='#00FF00',symbol='fire',size=4,folderId=fid)
# sts.addLine([[-120,39],[-120.1,39.1],[-120,39.1]],title='newLine',description='desc',width=8,opacity=0.6,pattern='M12 -7M0 5M9 0A3 3 0 1 0 6 0 A3 3 0 0 0 9 0,2,20,T;M0 0L12 0,15,20',folderId=fid)
# sts.addPolygon([[-120.2,39],[-120.3,39.1],[-120.2,39.1]],title='newPoly',description='desc2',strokeOpacity=0.4,strokeWidth=1,fillOpacity=0.8,stroke='#FF00FF',fill='#00FF00')
# op1=sts.addOperationalPeriod('1',color='#222222')
# sts.addLineAssignment([[-120,39.2],[-120.1,39.3],[-120,39.3]],
#         number='101',
#         letter='AA',
#         opId=op1,
#         resourceType='GROUND_1',
#         teamSize=5,
#         priority='HIGH',
#         responsivePOD='MEDIUM',
#         unresponsivePOD='HIGH',
#         cluePOD='LOW',
#         description='assignmentAA',
#         previousEfforts='None',
#         transportation='self',
#         timeAllocated='6hrs',
#         primaryFrequency='BANNER',
#         secondaryFrequency='TAC1',
#         preparedBy='SAR35',
#         status='PREPARED')
# sts.addAreaAssignment([[-120,39.4],[-120.1,39.5],[-120,39.5]],
#         letter='AB',
#         opId=op1,
#         resourceType='GROUND_3',
#         teamSize=5,
#         priority='MEDIUM',
#         responsivePOD='MEDIUM',
#         unresponsivePOD='HIGH',
#         cluePOD='LOW',
#         description='assignmentAB',
#         previousEfforts='None2',
#         transportation='self2',
#         timeAllocated='8hrs',
#         primaryFrequency='BANNER2',
#         secondaryFrequency='TAC12',
#         preparedBy='SAR352',
#         status='PREPARED')
# sts.addAppTrack([[-120,39.6],[-120.1,39.7],[-120,39.7]],
#         title='apptrack1',
#         description='t101')




# print(str(sts.getFeature(title='AB')))
# aa=sts.getFeature(title='AA 101')
# sts.editFeature(id=aa['id'],properties={'description':'other'})
# nm=sts.getFeature(title='newMarker')
# sts.moveMarker([-119.9,39],title='newMarker')
# sts.editMarkerDescription('newDesc2',title='newMarker')
# sts.delFeature(aa)
# sts.delFeatures(sts.getFeatures(featureClass='Marker'))
# sts.delMarkers(sts.getFeatures(featureClass='Marker'))

# sts.addMarker(39,-120,'newMarker2',description='desc2',color='#00FF00',symbol='a:1',rotation=38,size=2)

# r=sts.s.get('https://caltopo.com/sideload/account/'+sts.accountId+'.json?json=%7Bfull:+true%7D')

# print('request sent:'+str(r.url))
# print('r:'+str(r))
# if r:
#         print(str(r.status_code)+':'+str(r.text))

# print('getting account data...')
# ad=sts.getAccountData()
# print('account data:')
# print(json.dumps(ad,indent=3))

# ml=sts.getMapList(groupAccountTitle='NCSSAR')
# ml=sts.getAllMapLists()
# print('Map lists:')
# print(json.dumps(ml,indent=3))

# print(str(sts.getMapTitle('CA4L4')))
# print(str(sts.getGroupAccountTitles()))

# print('creating map...')
# r=sts.openMap('[NEW]')
# print('r: '+str(r))

# sts=SartopoSession('caltopo.com',
#         configpath='../../sts.ini',
#         mapID='CA4L4',
#         account='caver456@gmail.com')

# markers=sts.getFeatures(featureClass='Marker')

# sts.openMap('[NEW]newMap')
# sts.addPolygon([[-120,39],[-120.1,39.1],[-120.1,39]],'a')
# sts.addPolygon([[39,-120.2],[39.1,-120.3],[39,-120.3]],'b')
# time.sleep(10)
# op1=sts.addOperationalPeriod('3',color='#2222FF',strokeWidth=4,fillOpacity=0.8)
# time.sleep(10)
# sts.editFeature(op1,properties={'title':'1b'})
# time.sleep(10)
# sts.addAreaAssignment([[-120.3,39.3],[-120.4,39.4],[-120.5,39]],letter='AA',opId=op1)

# testList=[
#         [[-120,39],[-120.1,39],[-120,39.1]], # all valid
#         [[39,-120],[39,-120.1],[39.1,-120]], # all swapped
#         [[39,-120],[-120.1,39],[-120,39.1]],  # mixed
#         [[50,50],[50.1,50],[50,50.1]], # all ambiguous
#         [[-120,39,1],[-120.1,39,1],[-120,39.1,1]], # all valid (3-element)
#         [[39,-120,1],[39,-120.1,1],[39.1,-120,1]], # all swapped (3-element)
#         [[39,-120,1],[-120.1,39,1],[-120,39.1,1]],  # mixed (3-element)
#         [[50,50,1],[50.1,50,1],[50,50.1,1]], # all ambiguous (3-element)
#         [[-120,39,1,2],[-120.1,39,1,2],[-120,39.1,1,2]], # all valid (4-element)
#         [[39,-120,1,2],[39,-120.1,1,2],[39.1,-120,1,2]], # all swapped (4-element)
#         [[39,-120,1,2],[-120.1,39,1,2],[-120,39.1,1,2]],  # mixed (4-element)
#         [[50,50,1,2],[50.1,50,1,2],[50,50.1,1,2]]] # all ambiguous (4-element)
# for pointsList in testList:
#         print('\n\ninitial points:'+json.dumps(pointsList,indent=3))
#         print('validated points:'+json.dumps(sts._validatePoints(pointsList),indent=3))

# # from sartopo_python_authTest import SartopoSession
# import logging
# import sys
# import time
# import json



# print('startup')

# logging.basicConfig(stream=sys.stdout,level=logging.INFO)

# sts=SartopoSession('localhost:8080','FAB')
# sts=SartopoSession('localhost:8080','CM1') # CTD: geomTest / geomTest.json - geomTestOrig=CGA
# sts=SartopoSession('sartopo.com','UMEPJ', # web: geomTest / geomTest.json - geomTestOrig=HB0U
#         configpath='../../sts.ini',
#         account='caver456@gmail.com',
#         # sync=False,
#         syncDumpFile='../../HB0U.txt')
#         # propUpdateCallback=pucb,
#         # geometryUpdateCallback=gucb,
#         # newObjectCallback=nocb,
#         # deletedObjectCallback=docb)

# open a mapless web session, then get the map list, then associate the session with a map
# sts=SartopoSession('sartopo.com','[NEW]', # web: geomTest / geomTest.json - geomTestOrig=HB0U
# sts=SartopoSession('sartopo.com','44H1C', # web: geomTest / geomTest.json - geomTestOrig=HB0U
# mapID='MVLDC' # writable map
# mapID='N3U63', # non-writable map, from SDL 10/26/23
# mapID='50503' # secret map from IC training, owned by ncssaradm
# mapID='MGVG3' # secret map owned by me

# mapID='PVTGT'
# # mapID='DHFSB'
# sts=SartopoSession('sartopo.com', # web: mapless
#         configpath='../../sts.ini',
#         account='caver456@gmail.com',
#         mapID=mapID,
#         cacheDumpFile=mapID+'_cache.txt',
#         caseSensitiveComparisons=True,
#         sync=False)
        # syncDumpFile='../../HB0U.txt')


# sts.cut('AB','zz') # cut area assignment using line
# sts.cut('AA','z2')
# sts.cut('AA','z3')
# sts.cut('AA','z')
# sts.cut('z4','z5')
# sts.cut('z4:1','z6')

# sts.addMarker(39,-120,'testMarker')

# open a mapless web session, then get the map list, then associate the session with a map
# sts=SartopoSession('localhost:8080',accountId='11UEE9')

# this line adds a marker to the opened web map, with a signed POST request:
# sts.addMarker(39,-120,'abcde')

# sts=SartopoSession('sartopo.com',
#         configpath='../../sts.ini',
#         # mapID='PVTGT',
#         # mapID='MAA8J', # sharing=URL
#         # mapID='QPQ91', # sharing=public
#         # mapID='1H0U6', # sharing=secret
#         mapID='KC1CM', # sharing=private
#         account='caver456@gmail.com',
#         sync=False)

# markers=sts.getFeatures(featureClass='Marker')
# test all argument configurations to all del... functions
# 1a. delMarker(feature)
# 1b. delMarker(id)
# 2a. delMarkers(features)
# 2b. delMarkers(ids)
# 3a. delFeature(feature)
# 3b. delFeature(id)
# 3b1. delFeature(id,class) (correct class)
# 3b2. delFeature(id,class) (incorrect class)
# 4a. delFeatures(features)
# 4b. delFeatures(idAndClassList)

# # 1a. delMarker(feature)
# for marker in markers:
#     sts.delMarker(marker)

# # 1b. delMarker(id)
# for marker in markers:
#     sts.delMarker(marker['id'])

# 2a. delMarkers(features)
# sts.delMarkers(markers)

# # 2b. delMarkers(ids)
# sts.delMarkers([m['id'] for m in markers])

# # 3a. delFeature(feature)
# for marker in markers:
#     sts.delFeature(marker)

# # 3b. delFeature(id)
# for marker in markers:
#     sts.delFeature(marker['id'])

# # 3b1. delFeature(id,class) (correct class)
# for marker in markers:
#     sts.delFeature(marker['id'],'Marker')

# # 3b2. delFeature(id,class) (incorrect class) = requests should fail gracefully
# for marker in markers:
#     sts.delFeature(marker['id'],'Shape')

# # 4a. delFeatures(features)
# sts.delFeatures(markers)

# # 4b. delFeatures(idAndClassList)
# sts.delFeatures([{'id':m['id'],'class':m['properties']['class']} for m in markers])

# all del... QA passed 5-17-24

# print(json.dumps(markers,indent=3))
# delList=[]
# for marker in markers:
#     delList.append({'id':marker['id'],'class':'Marker'})
# sts.delFeatures(idAndClassList=delList)
# sts.delMarkers([marker['id'] for marker in markers])
# sts.delMarkers(markers)

# with open('acct.txt','w') as outfile:
#     outfile.write(json.dumps(sts.accountData,indent=3))

# sts.moveMarker([-121.026,38.885],title='a')
# sts.moveMarker([-121.036,38.885],id='7dddf464-e54f-483a-8cc9-9fa224d8e334')
# sts.editMarkerDescription('testDescription2',id='7dddf464-e54f-483a-8cc9-9fa224d8e334')
# sts.editMarkerDescription('testDescription3',title='a')
# with open('test.txt','w') as testLog:
#     testLog.write('current map title: '+str(sts.getMapTitle()))
#     testLog.write('\n\n'+json.dumps(sts.mapData,indent=3))
    # testLog.write('Name of PVTGT:'+sts.getMapTitle('PVTGT'))
    # testLog.write('\n***\nGroup memberships:\n'+str(sts.getGroupAccountTitles()))
    # testLog.write('\n***\nAll group map lists:\n'+json.dumps(sts.getAllMapLists(),indent=3))
    # testLog.write('\n***\nAll map lists including personal:\n'+json.dumps(sts.getAllMapLists(includePersonal=True),indent=3))
    # # sts.getAccountData(fromFileName='acct_since_0-mai.json')
    # testLog.write('\n***\naccountData:\n'+json.dumps(sts.accountData,indent=3))
    # testLog.write('\n***\nSAR Training maps:\n'+json.dumps(sts.getMapList('SAR Training'),indent=3))
    # testLog.write('\n***\nNCSSAR maps:\n'+json.dumps(sts.getMapList('NCSSAR'),indent=3))
    # testLog.write('\n***\nSAR Training maps:\n'+json.dumps(sts.getMapList('SAR Training',titlesOnly=True),indent=3))
    # testLog.write('\n***\ngroupAccounts:\n'+json.dumps(sts.groupAccounts,indent=3))
    # testLog.write('\n***\npersonalAccounts:\n'+json.dumps(sts.personalAccounts,indent=3))
# print('\nTest MAI Incident maps:\n'+json.dumps(sts.getMapList('Test MAI Incident'),indent=3))


# sts.openMap('44H1C')
# sts.openMap('J80')

# attempt to write to non-writable map
# sts.openMap('N3U63') # non-writable map, from SDL 10/26/23
# sts.addFolder('tmgFolder')
# sts.addMarker(39,-120,'tmgMarker')
# sts.addLine([[39,-120],[39.1,-120.1]],'tmgLine')
# sts.addPolygon([[39,-120],[39.1,-120.1],[39,-120.1]],'tmgPolygon')
# sts.addLineAssignment([[39.2,-120.2],[39.1,-120.1]],'tmgLineAssignment')
# sts.addAreaAssignment([[39.3,-120.3],[39.4,-120.4],[39,-120.5]],'tmgAreaAssignment')
# sts.addAppTrack([[39.6,-120.6],[39.7,-120.7]],'tmgAppTrack')

# sts.editFeature(className='Folder',title='Clues',properties={'title':'tmgCluesFolder'})
# exact case:
# sts.editFeature(className='Marker',title='Z',properties={'title':'tmgZ'})
# sts.editFeature(className='Shape',title='line1',properties={'title':'tmgLine1'})
# sts.editFeature(className='Shape',title='poly1',properties={'title':'tmgPoly1'})
# sts.editFeature(className='Assignment',letter='AreaAssign1',properties={'title':'tmgAreaAssign1'})
# sts.editFeature(className='Assignment',letter='LineAssign1',properties={'title':'tmgLineAssign1'})

# sts.caseSensitiveComparisons=True

# mismatched case:
# sts.editFeature(className='Marker',title='z',properties={'title':'tmgZ'})
# sts.editFeature(className='Shape',title='lIne1',properties={'title':'tmgLine1'})
# sts.editFeature(className='Shape',title='pOly1',properties={'title':'tmgPoly1'})
# sts.editFeature(className='Assignment',letter='ArEaAssign1',properties={'title':'tmgAreaAssign1'})
# sts.editFeature(className='Assignment',letter='LiNeAssign1',properties={'title':'tmgLineAssign1'})


# # geometry operations tests
# # start by deleting all objects / with a blank map,
# # then import geomTest.json

# sts.cut('AC 103','b0') # cut area assignment using line
# sts.cut('a1','b1') # cut polygon using line; preserve folder
# sts.cut('a2','b2') # cut line using line
# sts.cut('a3','b3') # cut line using line (multiple intersections)

# sts.expand('a4','b4') # expand polygon using polygon (partial crossing)
# sts.cut('AD 111','b00') # cut line using line (preserve attrinutes)
# sts.cut('a5','b5') # cut polygon using polygon (preserve attributes)
# sts.cut('a6','b6') # cut line using polygon
# sts.expand('a7','b7') # expand polygon using polygon (complete crossing)
# sts.cut('a8','b8') # cut polygon using line
# sts.expand('a9','b9') # expand polygon (partial crossing)

# # arguments are features
# a10=sts.getFeatures(title='a10')[0]
# b10=sts.getFeatures(title='b10')[0]
# sts.cut(a10,b10)

# # arguments are id strings
# a11id=sts.getFeatures(title='a11')[0]['id']
# b11id=sts.getFeatures(title='b11')[0]['id']
# sts.expand(a11id,b11id)

# sts.cut('a12','b12')
# sts.expand('a13','b13')
# sts.crop('a14','b14') # crop line using polygon
# sts.crop('a15','b15') # crop line using area assignment
# sts.crop('a16','b16') # crop polygon (multiple intersections)

# # objects don't intersect - make sure we return gracefully
# sts.expand('a11','a13')
# sts.cut('a11','a6')
# sts.crop('a14','b15')

# # objects don't exist = make sure we return gracefully
# sts.cut('foo','bar')
# sts.expand('foo','bar')
# sts.crop('foo','bar') 

# sts.cut('a1','bar')
# sts.expand('a1','bar')
# sts.crop('a1','bar')

# print(str(sts.getBounds(sts.getFeatures('Assignment'))))

# QA of .buffer2 and .intersection2 would be a bit more complicated
#  since they operate on shapely geometries, rather than caltopo features.
#  That means they would be much less likely to be called externally
#  (maybe they should actually be internal methods?) and probably don't need QA
#  before release of 2.0.0.

# sts.buffer2('a17',0.001)
# sts.intersection2('a18','b18')

# time.sleep(20) # to show that sync is still going

# print('\n\nadding folder')
# fid=sts.addFolder('MyFolder')
# print('\n\nadding marker: stuff')
# stuffID=sts.addMarker(39,-120,'stuff')
# time.sleep(15)
# sts.editMarkerDescription('abc',stuffID)

# print('\n\nadding marker: myStuff')
# myStuffID=sts.addMarker(39.01,-120.01,'myStuff',folderId=fid)
# print('\n\ngetting markers')
# r=sts.getFeatures('Marker')
# print('\n\nr:'+str(r))
# print('\n\nmoving the marker after a pause:'+myStuffID)
# time.sleep(30)
# print('\n\nmoving marker: myStuff')
# sts.moveMarker(39.02,-120.02,existingId=myStuffID)
# sts.addMarker(39.02,-120.02,'myStuff',existingId=myStuffID)
# print('\n\ndeleting "stuff" after a pause:')
# time.sleep(15)
# print('\n\ndeleting marker: stuff')
# sts.delMarker(stuffID)
# print('\n\ndone')

# j={}
# id='64acc33f-464d-47d0-9b5c-37f2aee81044'
# sts.editAreaAssignmentNumber('123',existingId=id)
# j['id']=id
# j['properties']={}
# j['properties']['number']='111'
# sts.sendRequest('post','assignment',j,id=id,returnJson='ID')