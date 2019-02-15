.. include:: global.rst.inc

Quickstart
============

Create a key
------------

First of all, to use SmartMonkey Services you will need a user (`create a new user`_) and an `API Key`_.

Optimize a route
----------------

The following example shows how to optimize a route with two stops. Let's see the whole code and then
dive into the example line by line::

    # Declare vehicles and services
    vehicles = [
        {
            "id": "Tesla 1",
            "start": {
                "lat": 41.40,
                "lng": 2.15,
            },
        }
    ]

    services = [
        {
            "id": "Provide Candy",
            "location": {"lat": 41.45, "lng": 2.14},
        },
        {
            "id": "Provide Marshmallows",
            "location": {"lat": 41.35, "lng": 2.14},
        },
    ]
    # Import Smartmonkey Client
    from smartmonkey import Client

    # Create a route optimization
    api_client = Client(key=MY_API_CLIENT_KEY)
    result = api_client.optimize(vehicles, services)


As you can see, the first thing we do is declare the vehicles and services that
we are going to use in this optimization. Both are declared with a parameter *id*
and a parameter *start*, in vehicles and *location* in services that are objects
of the type { 'lat': <float>, 'lng': <float>}::

    # Declare vehicles and services
    vehicles = [
        {
            "id": "Tesla 1",
            "start": {
                "lat": 41.40,
                "lng": 2.15,
            },
        }
    ]

    services = [
        {
            "id": "Provide Candy",
            "location": {"lat": 41.45, "lng": 2.14},
        },
        {
            "id": "Provide Marshmallows",
            "location": {"lat": 41.35, "lng": 2.14},
        },
    ]

Services and Vehicles are both lists of dictionaries. By now we will just
use a few parameters, but you can use a large set of restrictions, to know more
just `visit our documentation`_.

Then we will just create a new Client with our API Key::

    # Import Smartmonkey Client
    from smartmonkey import Client

    # Create a route optimization
    api_client = Client(key=MY_API_CLIENT_KEY)

And do the optimization call which will store the result in a local variable::

    result = api_client.optimize(vehicles, services)

The expected result for this optimization is::

    # Result
    result = {
        "job_id": "5c66890851028d00209bcb03",
        "status": "success",
        "processing_time": 181,
        "solution": {  
            "routes": [  
                {  
                    "vehicle_id": "Tesla 1",
                    "steps": [  
                        {  
                            "type":"start",
                            "dep_time":0,
                        },
                        {  
                            "id":"Provide Marshmallows",
                            "type":"stop",
                            "arr_time":547,
                            "dep_time":547,
                            "distance":7770
                        },
                        {  
                            "id":"Provide Candy",
                            "type":"stop",
                            "arr_time":1606,
                            "dep_time":1606,
                            "distance":15261
                        },
                        {  
                            "type":"end",
                            "arr_time":1606
                        }
                    ],
                    "geometry":"o~t{Fi~bL}AfCsA`CCR?XAz@@vABdABlAHbADRFRx@bCjAxBpA`CtBlDxAnCl@vAf@`BX|@T~@d@bCFv@LhALnA@\\Bt@?|A?~@@`G?hG@vCmBtAg@\\wCtBEDKF`BvArBhBjAr@LHNBVF~@@\\ALAl@Qb@[nAqAz@s@VUz@_@\\CN@PFJFRNnBjBt@p@v@hA|@vAd@fAz@tBtAbDFVBP@N?T?^FVJNPLNPBL`@h@\\ZTRf@^NFRLb@R~@f@h@Vj@TNBVDb@Pb@LfAZt@R~@T`@J`@HpDt@PBP@b@Dr@FdAH^?vA@xBCb@ExASpAKjBWnRyEbDy@lAYHCrFiApO}DtGaBtJmCnDw@nBm@PG~DeApGkB~JeFpCmB|A}@`@Md@K^E`@BHJJHPHP@TCRKPSDMDOBMAs@GWPc@X_@^YzA_AlFqD`IcFh@[bC}Ah@]tE}Cl@_@jImFd@_@LIf@_@tKgHxFwDr@zA~@bBr@bA|@rAv@nAnBrBtEzEe@j@_AfA_BeBa@c@_@a@a@c@sBwBvA{Bw@oA}@sAs@cA_AcBs@{AO[sFnDgHtEqBrAu@d@mBnAaGxDsLvHeR|LeDvBe@TS@QFONMPGVAJAP{EhCgDzBsJzEsMnDgHnBmJpC_HxA_EbAsIvBeK`CkBb@yL|CuDv@{Df@aBP]BeB@w@?oACeAIiAMQESCiAUe@KoBa@MCc@Ki@Mg@Ma@K}@YMEQGUKSGMEQGMEOG]QoBaA[QOMSOOMQS[c@KQOa@aGuNq@cAgAcBaEmD_@SWCU@]Di@VgD~Cc@Z]NMD_@@w@EYKOCOKeAm@KI@_Ig@\\wCtBEDKFyAdAOJcBlAaBlAeC|Ay@n@q@h@m@b@cBfA_BjAyB~AuCnBO[Yk@S]KWu@aB]u@qC_Gs@sAgAcCGM}BcA]Ok@IiAAeA?]Mm@s@wCcDSSU]Og@M}@EoAUcBg@gBS[Ya@a@YaB{@WVaBNcEr@{Dt@U@]KWOWWo@aAi@WQA_@Hi@VSPi@v@i@n@QGyAiBeAy@s@_@qAa@uZsKeA_@{IqD{C}As@]wMyEq@WwJuDs@WsJeD}FoBi@We@QaAo@eBgA{A{@e@[}@q@u@s@}@aA[a@o@y@{A}By@aBo@_BIWa@gASq@MuAEy@BWDa@Le@PWNYPYDM~AmAVSLMLKDO@QAQGMIKKCK?KDGFEJ}@l@{DiAe@Ky@WaCq@e@MaEmAy@Q_AUBUEUGKIEK?IBIH]CSE[EcDs@u@HuB~Ay@HWG]QUO[CWRMb@L`@TJ`@@j@Kp@Ef@MfAa@r@?f@b@Pd@Rd@HtAS~@[t@Sv@Dv@H\\Ph@r@`ATp@L~@FfACf@O\\UP]?eAI_CM[GSM]g@[Q{@E{DCyBIm@Co@Mc@LGj@Vh@J`@Ab@?r@^Rr@Ax@j@x@tAp@r@`@b@DjAI|BUd@]Ru@@yADaACs@F]TKdAa@n@i@r@Wb@A\\DZVZjA`Ad@Pb@Dp@X\\d@?h@e@b@s@B_@Yk@]]?Oh@@l@?d@Bh@O|@]d@M\\Cd@Tf@b@\\d@Nn@DT@PFXLVVHX@TCTIRKLSFw@@W@UNMLQXUh@Yd@SRo@l@M`@Gd@EhA?T?XMjAYvA"
                }
            ],
            "missing":[]
        }
    }

If you want to check how the result looks like you can go to the `requests page`_.
