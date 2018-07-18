from django.shortcuts import render
from xmlrpc.client import ServerProxy, getparser, ProtocolError
import httplib2


def didList(request):


    class HTTPSDigestAuthTransport:
        def request(self, host, handler, request_body, verbose=0):

            h = httplib2.Http()
            if verbose:
                h.debuglevel = 1
            h.add_credentials('ssp-root', '123456go')
            h.disable_ssl_certificate_validation = True

            resp, content = h.request("https://sva.yooth-it.com/xmlapi/xmlapi" + handler, "POST", body=request_body,
                                      headers={'content-type': 'text/xml'})

            if resp.status != 200:
                raise ProtocolError("https://sva.yooth-it.com/xmlapi/xmlapi" + handler,
                                    resp.status, resp.reason, None)

            p, u = getparser(0)
            p.feed(content)

            return u.close()

    transport = HTTPSDigestAuthTransport()
    client = ServerProxy("https://ssp-root:123456go@sva.yooth-it.com/xmlapi/xmlapi", transport)
    res = client.getDIDsList({'i_wholesaler': 338})

    listdidwithCustomers=[]
    listcustid=[]
    listcustidName=[{'id':int,'name':str}]
    result=res['dids']

    for item in result:
        if ('delegated_to' in item and item['delegated_to'] != ''):
            i_customer = int(item['delegated_to'])
            if(i_customer not in listcustid):
                listcustid.append(i_customer)
    for i in listcustid:
        transport = HTTPSDigestAuthTransport()
        client = ServerProxy("https://ssp-root:123456go@sva.yooth-it.com/xmlapi/xmlapi", transport)
        ress = client.getCustomerInfo({'i_customer': i})
        custRes = ress['customer']
        listcustidName.append({'id':i,'name':custRes['name']})


    for j in listcustidName:
        print(j)
    print('*****************finish*****************')



    for r in result:
        if('delegated_to' in r and r['delegated_to']!=''):
            i_customer=int(r['delegated_to'])

            for p in listcustidName:
                    if(p['id']==i_customer):
                        r['delegated_to']=p['name']
                        listdidwithCustomers.append(r)
                        break

        else:
            listdidwithCustomers.append(r)






    #print('Result: ' + res['result'])
    #print(res['dids'][5])

    return render(request, 'didList.html', {'dids':listdidwithCustomers})



def SDAList(request):


    class HTTPSDigestAuthTransport:
        def request(self, host, handler, request_body, verbose=0):

            h = httplib2.Http()
            if verbose:
                h.debuglevel = 1
            h.add_credentials('ssp-root', '123456go')
            h.disable_ssl_certificate_validation = True

            resp, content = h.request("https://sva.yooth-it.com/xmlapi/xmlapi" + handler, "POST", body=request_body,
                                      headers={'content-type': 'text/xml'})

            if resp.status != 200:
                raise ProtocolError("https://sva.yooth-it.com/xmlapi/xmlapi" + handler,
                                    resp.status, resp.reason, None)

            p, u = getparser(0)
            p.feed(content)

            return u.close()

    transport = HTTPSDigestAuthTransport()
    client = ServerProxy("https://ssp-root:123456go@sva.yooth-it.com/xmlapi/xmlapi", transport)
    res = client.getDIDsList({'i_wholesaler': 338})
    result=res['dids']
    listSDA=[]
    for r in result:
        if(r['did']!=r['incoming_did']):
            listSDA.append(r)

    return render(request, 'SDAList.html', {'SDAList':listSDA})


def getinfoCustomer(request,name):

    class HTTPSDigestAuthTransport:
        def request(self, host, handler, request_body, verbose=0):

            h = httplib2.Http()
            if verbose:
                h.debuglevel = 1
            h.add_credentials('ssp-root', '123456go')
            h.disable_ssl_certificate_validation = True

            resp, content = h.request("https://sva.yooth-it.com/xmlapi/xmlapi" + handler, "POST", body=request_body,
                                      headers={'content-type': 'text/xml'})

            if resp.status != 200:
                raise ProtocolError("https://sva.yooth-it.com/xmlapi/xmlapi" + handler,
                                    resp.status, resp.reason, None)

            p, u = getparser(0)
            p.feed(content)

            return u.close()

    customerName=name
    transport = HTTPSDigestAuthTransport()
    client = ServerProxy("https://ssp-root:123456go@sva.yooth-it.com/xmlapi/xmlapi", transport)
    ress = client.getCustomerInfo({'name': customerName})
    customer = ress['customer']
    print(customer)


    return render(request, 'infoCustomer.html', {'customer':customer })

def getAccountInfo(request,i_account):

    class HTTPSDigestAuthTransport:
        def request(self, host, handler, request_body, verbose=0):

            h = httplib2.Http()
            if verbose:
                h.debuglevel = 1
            h.add_credentials('ssp-root', '123456go')
            h.disable_ssl_certificate_validation = True

            resp, content = h.request("https://sva.yooth-it.com/xmlapi/xmlapi" + handler, "POST", body=request_body,
                                      headers={'content-type': 'text/xml'})

            if resp.status != 200:
                raise ProtocolError("https://sva.yooth-it.com/xmlapi/xmlapi" + handler,
                                    resp.status, resp.reason, None)

            p, u = getparser(0)
            p.feed(content)

            return u.close()
    id_account=i_account
    transport = HTTPSDigestAuthTransport()
    client = ServerProxy("https://ssp-root:123456go@sva.yooth-it.com/xmlapi/xmlapi", transport)
    resss = client.getAccountInfo({'i_account': id_account })
    print(resss)

    return render(request, 'InfoAccount.html', {'Account': resss})