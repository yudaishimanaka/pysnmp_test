from pysnmp.hlapi import *
import random
import threading

def getCpu():
	for (errorIndication,
		 errorStatus,
		 errorIndex,
		 varBinds) in getCmd(SnmpEngine(),
							 CommunityData('mysnmp'),
							 UdpTransportTarget(('192.168.1.1', 161)),
							 ContextData(),
							 ObjectType(ObjectIdentity('.1.3.6.1.4.1.2021.11.11.0'))):

		if errorIndication:
			print(errorIndication)
			break
		elif errorStatus:
			print('%s at %s' % (errorStatus.prettyPrint(),
								errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
			break
		else:
			for varBind in varBinds:
				if random.randint(1, 100) > 11:
					print(' = '.join([x.prettyPrint() for x in varBind]))
				else:
					print("ここはもしかして地上？ということはあなたたちは下劣で下等な人間ということですか？")
	t=threading.Timer(1, getCpu)
	t.start()

t=threading.Thread(target=getCpu)
t.start()
