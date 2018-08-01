from django.shortcuts import render
from xmlrpc.client import ServerProxy, getparser, ProtocolError
import httplib2
from .models import did
from .models import customer
from .models import account
from .models import vendor
from .models import histDid
from .models import yoothUser
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


def checkLogin(request):

    email=request.POST['email']
    password=request.POST['password']

    usersTable=yoothUser.objects.all()
    test=False
    result:''
    userNow:{}
    for user in usersTable:
        if(user.email==email and check_password(password,user.password)==True):
            userNow=user
            test=True
            break
    if(test==True):
        request.session['User']=userNow.username
        return render(request, 'accueil.html', {'name':request.session['User']})
    else:
        result='loginFailed'
        return render(request, 'login.html', {'result': result})

def logout(request):

    request.session.clear()
    return render(request, 'login.html')


def signUp(request):
    username = request.POST['username']
    email = request.POST['email']
    password = make_password(request.POST['password'])
    result:''

    yoothTable=yoothUser.objects.all()
    test=False
    for user in yoothTable:
        if(user.email==email):
            result='Email already exist'
            test=True
            break
        if(user.username==username):
            result='Username already exist'
            test=True
            break

    if(test==False):
        yoothuser = yoothUser(username=username, email=email, password=password)
        yoothuser.publish()
        result = 'ok'

    return render(request, 'login.html',{'result':result})

def didList(request):

    if('User' not in request.session):
        return render(request, 'login.html')
    else:
        didstabe = did.objects.all()
        listOfDids = []

        for item in didstabe:
            row = {}

            if(histDid.objects.all().count() != 0):
                last = histDid.objects.get(did=str(item.did))
                if (last.delegated_to != item.delegated_to and last.delegated_to != None and last.delegated_to != ''):
                    i_Last_customer = int(last.delegated_to)
                    lastCustomerInfo = customer.objects.get(i_customer=i_Last_customer)
                    row['last_customer'] = lastCustomerInfo.name
            else:
                row['last_customer'] =''

            row['did'] = item.did
            row['incoming_did'] = item.incoming_did
            row['i_did'] = item.i_did
            row['description'] = item.description
            row['i_connection'] = item.i_connection
            row['i_account'] = item.i_account

            if (item.delegated_to != None and item.delegated_to != ''):
                i_customer = int(item.delegated_to)
                customerInfo = customer.objects.get(i_customer=i_customer)
                row['delegated_to'] = customerInfo.name
            else:
                row['delegated_to'] = item.delegated_to

            if (item.i_account != None and item.i_account != ''):
                i_account = int(item.i_account)
                AccountInfo = account.objects.get(i_account=i_account)
                row['status'] = AccountInfo.blocked
            else:
                row['status'] = -1

            if (item.i_vendor != None and item.i_vendor != ''):
                i_vendor = int(item.i_vendor)
                VendorInfo = vendor.objects.get(i_vendor=i_vendor)
                row['i_vendor'] = VendorInfo.name
            else:
                row['i_vendor'] = item.i_vendor

            listOfDids.append(row)

        return render(request, 'didList.html', {'dids': listOfDids,'name':request.session['User']})






def SDAList(request):
    if('User' not in request.session):
        return render(request, 'login.html')
    else:
        didsSDAtabe = did.objects.all()
        listOfSDA = []

        for item in didsSDAtabe:

            if (item.did != None and item.incoming_did != None and str(item.did) != str(item.incoming_did)):

                row = {}

                if (histDid.objects.all().count() != 0):
                    last = histDid.objects.get(did=str(item.did))
                    if (
                            last.delegated_to != item.delegated_to and last.delegated_to != None and last.delegated_to != ''):
                        i_Last_customer = int(last.delegated_to)
                        lastCustomerInfo = customer.objects.get(i_customer=i_Last_customer)
                        row['last_customer'] = lastCustomerInfo.name
                else:
                    row['last_customer'] =''

                row['did'] = item.did
                row['incoming_did'] = item.incoming_did
                row['i_did'] = item.i_did
                row['description'] = item.description
                row['i_connection'] = item.i_connection
                row['i_account'] = item.i_account

                if (item.delegated_to != None and item.delegated_to != ''):
                    i_customer = int(item.delegated_to)
                    customerInfo = customer.objects.get(i_customer=i_customer)
                    row['delegated_to'] = customerInfo.name
                else:
                    row['delegated_to'] = item.delegated_to

                if (item.i_account != None and item.i_account != ''):
                    i_account = int(item.i_account)
                    AccountInfo = account.objects.get(i_account=i_account)
                    row['status'] = AccountInfo.blocked
                else:
                    row['status'] = -1

                if (item.i_vendor != None and item.i_vendor != ''):
                    i_vendor = int(item.i_vendor)
                    VendorInfo = vendor.objects.get(i_vendor=i_vendor)
                    row['i_vendor'] = VendorInfo.name
                else:
                    row['i_vendor'] = item.i_vendor

                listOfSDA.append(row)

        return render(request, 'SDAList.html', {'SDAList': listOfSDA,'name':request.session['User']})





def CustomersList(request):

    if ('User' not in request.session):
        return render(request, 'login.html')
    else:
        didstabe = customer.objects.all()
        listOfCustomer = []

        for item in didstabe:
            row = {}
            row['name'] = item.name
            row['description'] = item.description
            row['balance'] = item.balance
            row['credit_limit'] = item.credit_limit
            row['state'] = item.state
            row['email'] = item.email
            row['company_name'] = item.company_name
            row['phone'] = item.phone
            row['payment_method'] = item.payment_method
            listOfCustomer.append(row)

        return render(request, 'CustomersList.html', {'CustomersList': listOfCustomer,'name':request.session['User']})



def AccountsList(request):

    if ('User' not in request.session):
        return render(request, 'login.html')
    else:
        didstabe = account.objects.all()
        listOfAccount = []

        for item in didstabe:
            row = {}
            row['i_account'] = item.i_account
            row['balance'] = item.balance
            row['username'] = item.username
            row['created_by'] = item.created_by
            row['blocked'] = item.blocked
            row['company_name'] = item.company_name
            row['description'] = item.description
            row['payment_currency'] = item.payment_currency
            row['credit_limit'] = item.credit_limit
            listOfAccount.append(row)

        return render(request, 'AccountsList.html', {'AccountsList': listOfAccount,'name':request.session['User']})


def VendorsList(request):

    if ('User' not in request.session):
        return render(request, 'login.html')
    else:
        didstabe = vendor.objects.all()
        listOfVendor = []

        for item in didstabe:
            row = {}
            row['i_vendor'] = item.i_vendor
            row['name'] = item.name
            row['web_login'] = item.web_login
            row['email'] = item.email
            row['balance'] = item.balance
            row['first_name'] = item.first_name
            row['last_name'] = item.last_name
            row['street_addr'] = item.street_addr
            row['credit_limit'] = item.credit_limit
            listOfVendor.append(row)

        return render(request, 'VendorsList.html', {'VendorsList': listOfVendor,'name':request.session['User']})


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


def accueil (request):
    if('User' in request.session):
        return render(request, 'accueil.html',{'name':request.session['User']})
    else:
        return render(request, 'login.html')





def getAllData():

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


        resDids = client.getDIDsList({'i_wholesaler': 338})
        resultDids = resDids['dids']
        # Saving dids list
        for item in resultDids:
            i_ivr = None
            i_acc = None
            i_vendor = None
            i_connex = None
            i_did_deleg = None
            delegTo = None
            desc: ''
            if ('i_ivr_application' in item and item['i_ivr_application'] != None):
                i_ivr = item['i_ivr_application']
            if ('i_account' in item and item['i_account'] != None):
                i_acc = item['i_account']
            if ('i_vendor' in item and item['i_vendor'] != None):
                i_vendor = item['i_vendor']
            if ('i_connection' in item and item['i_connection'] != None):
                i_connex = item['i_connection']
            if ('i_did_delegation' in item and item['i_did_delegation'] != None):
                i_did_deleg = item['i_did_delegation']
            if ('delegated_to' in item and item['delegated_to'] != None):
                delegTo = item['delegated_to']
            if ('description' in item and item['description'] != None):
                desc = item['description']

            didtable = did(i_did=item['i_did'], did=item['did'], incoming_did=item['incoming_did'],
                           i_ivr_application=i_ivr,
                           i_account=i_acc, i_vendor=i_vendor, i_connection=i_connex, i_did_delegation=i_did_deleg,
                           delegated_to=delegTo, description=desc, created_date=timezone.now())
            didtable.publish()
            print('ROW SAVED')
        print('******TABLE DID SAVED*****')
        # Saving Customers
        resCust = client.listCustomers({'i_wholesaler': 338})
        resultCust = resCust['customers']

        for item in resultCust:

            resCustInfo = client.getCustomerInfo({'i_customer': item['i_customer']})
            itemInfo = resCustInfo['customer']
            balance = None
            first_name = ''
            last_name = ''
            name = ''
            company_name = ''
            street_addr = ''
            state = ''
            postal_code = ''
            city = ''
            country = ''
            contact = ''
            phone = ''
            fax = ''
            email = ''
            mail_from = ''
            payment_currency = ''
            payment_method = None
            i_tariff = None
            credit_limit = None
            min_payment_amount = None
            api_access = None
            api_mgmt = None
            i_commission_agent = None
            tariffs_mgmt = None
            vouchers_mgmt = None
            accounts_mgmt = None
            customers_mgmt = None
            system_mgmt = None
            did_pool_enabled = None
            ivr_apps_enabled = None
            debit_credit_cards_enabled = None
            description = ''
            i_lang = ''
            i_export_type = None
            max_calls_per_second = None

            if ('balance' in itemInfo):
                balance = itemInfo['balance']
            if ('first_name' in itemInfo):
                first_name = itemInfo['first_name']
            if ('last_name' in itemInfo):
                last_name = itemInfo['last_name']
            if ('name' in itemInfo):
                name = itemInfo['name']
            if ('company_name' in itemInfo):
                company_name = itemInfo['company_name']
            if ('street_addr' in itemInfo):
                street_addr = itemInfo['street_addr']
            if ('state' in itemInfo):
                state = itemInfo['state']
            if ('postal_code' in itemInfo):
                postal_code = itemInfo['postal_code']
            if ('city' in itemInfo):
                city = itemInfo['city']
            if ('country' in itemInfo):
                country = itemInfo['country']
            if ('contact' in itemInfo):
                contact = itemInfo['contact']
            if ('phone' in itemInfo):
                phone = itemInfo['phone']
            if ('fax' in itemInfo):
                fax = itemInfo['fax']
            if ('email' in itemInfo):
                email = itemInfo['email']
            if ('mail_from' in itemInfo):
                mail_from = itemInfo['mail_from']
            if ('payment_currency' in itemInfo):
                payment_currency = itemInfo['payment_currency']
            if ('payment_method' in itemInfo):
                payment_method = itemInfo['payment_method']
            if ('i_tariff' in itemInfo):
                i_tariff = itemInfo['i_tariff']
            if ('credit_limit' in itemInfo):
                credit_limit = itemInfo['credit_limit']
            if ('min_payment_amount' in itemInfo):
                min_payment_amount = itemInfo['min_payment_amount']
            if ('api_access' in itemInfo):
                api_access = itemInfo['api_access']
            if ('api_mgmt' in itemInfo):
                api_mgmt = itemInfo['api_mgmt']
            if ('i_commission_agent' in itemInfo):
                i_commission_agent = itemInfo['i_commission_agent']
            if ('tariffs_mgmt' in itemInfo):
                tariffs_mgmt = itemInfo['tariffs_mgmt']
            if ('vouchers_mgmt' in itemInfo):
                vouchers_mgmt = itemInfo['vouchers_mgmt']
            if ('accounts_mgmt' in itemInfo):
                accounts_mgmt = itemInfo['accounts_mgmt']
            if ('system_mgmt' in itemInfo):
                system_mgmt = itemInfo['system_mgmt']
            if ('customers_mgmt' in itemInfo):
                customers_mgmt = itemInfo['customers_mgmt']
            if ('did_pool_enabled' in itemInfo):
                did_pool_enabled = itemInfo['did_pool_enabled']
            if ('ivr_apps_enabled' in itemInfo):
                ivr_apps_enabled = itemInfo['ivr_apps_enabled']
            if ('debit_credit_cards_enabled' in itemInfo):
                debit_credit_cards_enabled = itemInfo['debit_credit_cards_enabled']
            if ('description' in itemInfo):
                description = itemInfo['description']
            if ('i_lang' in itemInfo):
                i_lang = itemInfo['i_lang']
            if ('i_export_type' in itemInfo):
                i_export_type = itemInfo['i_export_type']
            if ('max_calls_per_second' in itemInfo):
                max_calls_per_second = itemInfo['max_calls_per_second']

            cutomerstable = customer(i_customer=item['i_customer'], balance=balance, first_name=first_name,
                                     last_name=last_name, name=name,
                                     company_name=company_name, street_addr=street_addr, state=state,
                                     postal_code=postal_code, city=city, country=country, contact=contact,
                                     phone=phone, fax=fax, email=email, mail_from=mail_from,
                                     payment_currency=payment_currency, payment_method=payment_method,
                                     i_tariff=i_tariff, credit_limit=credit_limit,
                                     min_payment_amount=min_payment_amount, api_access=api_access, api_mgmt=api_mgmt,
                                     i_commission_agent=i_commission_agent, tariffs_mgmt=tariffs_mgmt,
                                     vouchers_mgmt=vouchers_mgmt, accounts_mgmt=accounts_mgmt,
                                     customers_mgmt=customers_mgmt, system_mgmt=system_mgmt,
                                     did_pool_enabled=did_pool_enabled, ivr_apps_enabled=ivr_apps_enabled,
                                     debit_credit_cards_enabled=debit_credit_cards_enabled, description=description,
                                     i_lang=i_lang, i_export_type=i_export_type,
                                     max_calls_per_second=max_calls_per_second, created_date=timezone.now())
            cutomerstable.publish()
            print('ROW SAVED')

        print('*****TABLE CUTOMERS SAVED****')

        #Saving list account
        resAccount = client.listAccounts()
        resultAccount = resAccount['accounts']

        for item in resultAccount:

            resAccountInfo = client.getAccountInfo({'i_account': item['i_account']})
            itemInfo = resAccountInfo
            balance = None
            username: ''
            first_name = ''
            last_name = ''
            created_by = ''
            company_name = ''
            street_addr = ''
            state = ''
            postal_code = ''
            city = ''
            country = ''
            contact = ''
            phone = ''
            fax = ''
            email = ''
            payment_currency = ''
            blocked = None
            payment_method = None
            credit_limit = None
            min_payment_amount = None
            i_commission_agent = None
            description = ''
            i_lang = ''
            i_export_type = None
            max_calls_per_second = None
            on_payment_action = None
            preferred_codec = None

            if ('balance' in itemInfo):
                balance = itemInfo['balance']
            if ('first_name' in itemInfo):
                first_name = itemInfo['first_name']
            if ('last_name' in itemInfo):
                last_name = itemInfo['last_name']
            if ('username' in itemInfo):
                username = itemInfo['username']
            if ('company_name' in itemInfo):
                company_name = itemInfo['company_name']
            if ('street_addr' in itemInfo):
                street_addr = itemInfo['street_addr']
            if ('state' in itemInfo):
                state = itemInfo['state']
            if ('postal_code' in itemInfo):
                postal_code = itemInfo['postal_code']
            if ('city' in itemInfo):
                city = itemInfo['city']
            if ('country' in itemInfo):
                country = itemInfo['country']
            if ('contact' in itemInfo):
                contact = itemInfo['contact']
            if ('phone' in itemInfo):
                phone = itemInfo['phone']
            if ('fax' in itemInfo):
                fax = itemInfo['fax']
            if ('email' in itemInfo):
                email = itemInfo['email']
            if ('payment_currency' in itemInfo):
                payment_currency = itemInfo['payment_currency']
            if ('blocked' in itemInfo):
                blocked = itemInfo['blocked']
            if ('payment_method' in itemInfo):
                payment_method = itemInfo['payment_method']
            if ('credit_limit' in itemInfo):
                credit_limit = itemInfo['credit_limit']
            if ('min_payment_amount' in itemInfo):
                min_payment_amount = itemInfo['min_payment_amount']
            if ('api_access' in itemInfo):
                api_access = itemInfo['api_access']
            if ('api_mgmt' in itemInfo):
                api_mgmt = itemInfo['api_mgmt']
            if ('i_commission_agent' in itemInfo):
                i_commission_agent = itemInfo['i_commission_agent']
            if ('description' in itemInfo):
                description = itemInfo['description']
            if ('i_lang' in itemInfo):
                i_lang = itemInfo['i_lang']
            if ('i_export_type' in itemInfo):
                i_export_type = itemInfo['i_export_type']
            if ('max_calls_per_second' in itemInfo):
                max_calls_per_second = itemInfo['max_calls_per_second']
            if ('on_payment_action' in itemInfo):
                on_payment_action = itemInfo['on_payment_action']
            if ('preferred_codec' in itemInfo):
                preferred_codec = itemInfo['preferred_codec']

            accountstable = account(i_account=item['i_account'], balance=balance, username=username,
                                    first_name=first_name, last_name=last_name, created_by=created_by,
                                    company_name=company_name, street_addr=street_addr, state=state,
                                    postal_code=postal_code, city=city, country=country, contact=contact,
                                    phone=phone, fax=fax, email=email, payment_currency=payment_currency,
                                    blocked=blocked,
                                    payment_method=payment_method, credit_limit=credit_limit,
                                    min_payment_amount=min_payment_amount,
                                    i_commission_agent=i_commission_agent, description=description, i_lang=i_lang,
                                    i_export_type=i_export_type,
                                    max_calls_per_second=max_calls_per_second, on_payment_action=on_payment_action,
                                    preferred_codec=preferred_codec, created_date=timezone.now())
            accountstable.publish()
            print('ROW SAVED')

        print('*****TABLE ACCOUNT SAVED*****')

        #Saving vendor list
        resVendor = client.getVendorsList()
        resultVendor = resVendor['vendors']
        print(resultVendor)
        for itemInfoV in resultVendor:

            balance = None
            credit_limit = None
            base_currency = ''
            name: ''
            web_login = ''
            first_name = ''
            last_name = ''
            company_name = ''
            street_addr = ''
            state = ''
            postal_code = ''
            city = ''
            country = ''
            contact = ''
            phone = ''
            fax = ''
            email = ''
            i_lang = ''
            i_export_type = None

            if ('balance' in itemInfoV):
                balance = itemInfoV['balance']
            if ('credit_limit' in itemInfoV):
                credit_limit = itemInfoV['credit_limit']
            if ('base_currency' in itemInfoV):
                base_currency = itemInfoV['base_currency']
            if ('first_name' in itemInfoV):
                first_name = itemInfoV['first_name']
            if ('last_name' in itemInfoV):
                last_name = itemInfoV['last_name']
            if ('name' in itemInfoV):
                name = itemInfoV['name']
            if ('web_login' in itemInfoV):
                web_login = itemInfoV['web_login']
            if ('company_name' in itemInfoV):
                company_name = itemInfoV['company_name']
            if ('street_addr' in itemInfoV):
                street_addr = itemInfoV['street_addr']
            if ('state' in itemInfoV):
                state = itemInfoV['state']
            if ('postal_code' in itemInfoV):
                postal_code = itemInfoV['postal_code']
            if ('city' in itemInfoV):
                city = itemInfoV['city']
            if ('country' in itemInfoV):
                country = itemInfoV['country']
            if ('contact' in itemInfoV):
                contact = itemInfoV['contact']
            if ('phone' in itemInfoV):
                phone = itemInfoV['phone']
            if ('fax' in itemInfoV):
                fax = itemInfoV['fax']
            if ('email' in itemInfoV):
                email = itemInfoV['email']
            if ('i_lang' in itemInfoV):
                i_lang = itemInfoV['i_lang']
            if ('i_export_type' in itemInfoV):
                i_export_type = itemInfoV['i_export_type']

            accountstable = vendor(i_vendor=int(itemInfoV['i_vendor']), balance=balance, credit_limit=credit_limit,
                                   base_currency=base_currency, name=name,
                                   first_name=first_name, last_name=last_name, web_login=web_login,
                                   company_name=company_name, street_addr=street_addr, state=state,
                                   postal_code=postal_code, city=city, country=country, contact=contact,
                                   phone=phone, fax=fax, email=email, i_lang=i_lang, i_export_type=i_export_type,
                                   created_date=timezone.now())
            accountstable.publish()
            print('ROW SAVED')

        print('*****TABLE VENDOR SAVED*****')

        return True


def syncronisation(request):

    if ('User' not in request.session):
        return render(request, 'login.html')
    else:
        vendor.objects.all().delete()
        account.objects.all().delete()
        customer.objects.all().delete()

        if (histDid.objects.all().count() == 0):

            if (did.objects.all().count() != 0):
                copyTable = did.objects.all()
                for item in copyTable:
                    hisTable = histDid(i_did=item.i_did, did=item.did, delegated_to=item.delegated_to)
                    hisTable.publish()
                    print('ROW COPIED')
                print('*******TABLE COPIED********')
                did.objects.all().delete()
                getAllData()
        else:
            verifDid()
            did.objects.all().delete()
            getAllData()
        return render(request, 'accueil.html',{'name':request.session['User']})


def verifDid():
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
    resDids = client.getDIDsList({'i_wholesaler': 338})
    resultDids = resDids['dids']

    for item in resultDids:
        if('delegated_to' in item and item['delegated_to'] != None and item['delegated_to'] != ''):
            if(did.objects.filter(i_did=int(item['i_did'])).exists()==True):
                filterRow=did.objects.get(i_did=int(item['i_did']))
                if(filterRow.delegated_to != int(item['delegated_to'])):
                    filterRowInHist=histDid.objects.get(i_did=filterRow.i_did)
                    filterRowInHist.delegated_to=filterRow.delegated_to
                    filterRowInHist.publish()
    return True



def login(request):
    return render(request,'login.html')