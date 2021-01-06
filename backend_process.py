from SolarSystemDataBase import SolarSystemRepository
from termcolor import colored 
import logger_config
from logger_config import *


#---Configuring log filename---
log_file=os.path.splitext(os.path.basename(__file__))[0]+".log"
log = logger_config.configure_logger('default', ""+DIR+""+LOG_DIR+"/"+log_file+"")

def processRequest(req):
    result = req.get("queryResult")
    user_asked = result.get("queryText")
    log.info(colored("User Asked : "+str(user_asked), 'green'))
    parameters = result.get("parameters")
    log.info(colored("Parameters: "+str(parameters),'green'))
    intent = result.get('intent').get('displayName')
    
    if (intent == 'UserAsksMass'):
        # if parameters['body-mass'] == 'mass':
        # api_result = SolarSystemAPI(param1).get_body_mass()
        conditions = {"englishName":parameters['space-object'].capitalize()}
        api_result = SolarSystemRepository().read(conditions)
        data = f"Mass of the {api_result['englishName']} is {api_result['mass']['massValue']} x 10^{api_result['mass']['massExponent']}kg."
        return {
                "fulfillmentText":data
                }
    elif (intent=='UserAsksVolume'):
        print("inside user asks volume")
        conditions = {"englishName":parameters['space-object'].capitalize()}
        # if parameters['body-volume'] == 'volume':
        # api_result = SolarSystemAPI(param1).get_body_volume()
        conditions = {"englishName":parameters['space-object'].capitalize()}
        api_result = SolarSystemRepository().read(conditions)
        data = f"Volume of the {api_result['englishName']} is {api_result['vol']['volValue']} x 10^{api_result['vol']['volExponent']} km\u00b3."

        return {
                "fulfillmentText":data
                }

    elif (intent == 'UserAsksMoonsCount'):
        print("inside user asks moons count")
        param1 = parameters['space-object']
        param2 = parameters['body-count'][0]
        # if param2 == 'moons':
            # api_result = SolarSystemAPI(param1).get_moons_count()
        conditions = {"englishName":param1.capitalize()}
        api_result = SolarSystemRepository().read(conditions)

        if api_result['isPlanet']:
            list_of_moons = api_result['moons']
            if list_of_moons == None:
                return {
                "fulfillmentText":(f"{api_result['englishName']} planet has no moon")\
                }
            else:               
                moon_names_list = []
                for moon in list_of_moons:
                    moon_names_list.append(moon.get('moon'))                
                if len(moon_names_list) == 1:
                    return {"fulfillmentText": (f"{api_result['englishName']} has only one moon which is {', '.join(moon_names_list)}.")}
                else:
                    return {"fulfillmentText":(f"{api_result['englishName']} has {len(moon_names_list)} moons which are {', '.join(moon_names_list)}.")}                

        else:
            return {"fulfillmentText":(f"{api_result['englishName']} is not a planet")}

    elif (intent == "UserAsksDensity"):
        print("inside UserAsksDensity")
        # if parameters['body-density'] == 'density':
        conditions = {"englishName":parameters['space-object'].capitalize()}
        api_result = SolarSystemRepository().read(conditions)
        data = f"Density of {api_result['englishName']} is {api_result['density']} g/cm\u00b3."
        return {
                "fulfillmentText":data
                }

    elif (intent=='UserAsksGravity'):
        # print("Inside gravity")
        # if parameters['body-gravity'] == 'gravity':
        conditions = {"englishName":parameters['space-object'].capitalize()}
        api_result = SolarSystemRepository().read(conditions)
        # print(api_result)
        data = f"Gravity of {api_result['englishName']} is {api_result['density']} m/s\u00b2"
        return {
                "fulfillmentText":data
                }
    elif (intent == 'UserAsksAxialTilt'):
        print("Inside axial tilt")   
        conditions = {"englishName":parameters['space-object'].capitalize()}
        api_result = SolarSystemRepository().read(conditions)
        data = f"Axial tilt of the {api_result['englishName']} is {api_result['axialTilt']} degrees."
        return {
            "fulfillmentText":data
        }
        
    elif (intent == 'UserAsksEscapeVelocity'):
        print("inside escape velocity")
        conditions = {"englishName":parameters['space-object'].capitalize()}
        api_result = SolarSystemRepository().read(conditions)  
        data = f"Escape velocity of {api_result['englishName']} is {api_result['escape']} m/s"
        return {
            "fulfillmentText":data
        }
    else:
        log.error(colored("Some error here", 'red'))                
